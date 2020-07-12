# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json

def get_single_sentiment(coc):
    """
    Get sentiment from transcript file using Natural Language

    Args:
      unofficial coc area name
    """
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    filename = "transcripts/transcript_" + coc + ".txt"
    f = open(filename, "r")
    transcript = f.read()
    f.close()

    document = types.Document(
        content=transcript,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('COC: {}'.format(coc))
    # print('Text: {}'.format(transcript))
    print('Sentiment: {}, Magnitude: {}'.format(sentiment.score, sentiment.magnitude))
    return sentiment.score

def get_sentiments(coc_areas):
    """
    Save results to local json file

    Args:
      unofficial coc area names
    """
    # create dictionary to store coc areas and their sentiment
    sentiments = {}
    for coc in coc_areas:
        sentiments[coc] = get_single_sentiment(coc)
    # print(sentiments)

    # save to local json file
    with open('sentiments.json', 'w+') as fp:
        json.dump(sentiments, fp, indent=4)



def main():
    print("Calculating sentiments...")
    coc_areas = ["Sacramento","Bakersfield","Orange"]
    get_sentiments(coc_areas)


if __name__ == "__main__":
    main()
