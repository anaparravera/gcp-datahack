from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

def save_results(response, coc):
    """
    Save results to local text file

    Args:
      response from transcribing long audio file from Cloud Storage using 
    asynchronous speech recognition
    """
    # create local file to save results to
    filename = "transcripts/transcript_" + coc + ".txt"
    f = open(filename, "w+")

    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        # print(format(alternative.transcript))
        # save to local file
        f.write(format(alternative.transcript))
    f.close()  # close the file

def sample_long_running_recognize(storage_uri, coc=None):
    """
    Transcribe long audio file from Cloud Storage using asynchronous speech
    recognition

    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
    """

    client = speech_v1.SpeechClient()

    if coc=='Sacramento':
        storage_uri = 'gs://avo-bucket-datahack/SacramentoCityCouncil082719.flac'
        # storage_uri = 'gs://avo-bucket-datahack/SacramentoCityCouncil082719_s.flac'
    elif coc=='Orange':
        storage_uri = 'gs://avo-bucket-datahack/VirtualTownHall_OrangeCounty_04302020.flac'
    elif coc=='Bakersfield':
        storage_uri = 'gs://avo-bucket-datahack/kerncounty_citycouncil.flac'

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 44100

    # The language of the supplied audio
    language_code = "en-US"

    # Encoding of audio data sent
    config = {
        "sample_rate_hertz": sample_rate_hertz,
        "language_code": language_code,
        # "encoding": encoding,
        "encoding": 'FLAC',
        "audio_channel_count": 2,
    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    print("Transcribing Town Hall audio for {}. Waiting for operation to complete...".format(coc))
    response = operation.result()
    # Save results to temp local file
    save_results(response, coc)



def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--storage_uri",
        type=str,
        default="gs://cloud-samples-data/speech/brooklyn_bridge.raw",
    )
    args = parser.parse_args()
    
    coc_areas = ["Sacramento","Bakersfield","Orange"]
    for coc in coc_areas:
        sample_long_running_recognize(args.storage_uri, coc)
    print()


if __name__ == "__main__":
    main()
