# UC Davis & Google Cloud Data Hack
The Amazing A's present... a beautiful project that we hope you enjoy :two_hearts:!

> Our deck containing the results can be found [here](https://docs.google.com/presentation/d/1GHAn7mJwcziCJKoNjoPT1itJP-0fwEBp_LWq4GeAeYE/edit?usp=sharing).

> Our ***Data Studio report*** can be found [here](https://datastudio.google.com/reporting/bc6d3174-ddf1-4f4e-b446-8191fefdce91)

## The Social Issue
Over the last several decades, homelessness in the United States has been steadily increasing and is a social issue that affects one in every 200 Americans. To many Americans, interactions with homeless individuals is an everyday occurance, and to some it is an issue that directly affects our loved ones. So we wanted to ask the question, how can analytics improve the way we support individuals struggling with homelessness and step into a tomorrow where the fear of homelessness is mitigated.

## Our Insights
The premise and background research of this analysis pointed to the fact that our the public fews local investment in mitigating homelessness in their community directly affects how national funding is disrupted. A negative public sentiment on the issue can lead to national funding going unused, redirectly to less beneficial projects, and even discourage future funding to the area. 

*Luckily*, public sentiment can be analyzed using machine learning techniques with the help of the **Google Cloud Platform (GCP)**. By taking the video/audio of already readily available local government open meetings where members of the communities get to express their opinions on housing or homeless funding proposals, text can be transcripted and natural language processing techniques can be applied to calculate the average public sentiment on the issue. Having this information on the 400+ CoCs in the US can help HUD better optimize the distribution of funding to aid the low income and homeless communities. 

Currently, the HOD takes into account hundreds of different factors to make its prediction of future homelessness levels in America. Using the 2019 HUD prediction model as a jumping off point, utilizing other machine learning techniques provide a strongly fit model that tells the story of predicted homeless population growth being correlated with the current number of available shelter options for low income or disabled individuals. This means that America is stuck in a very dangerous cycle of not funding shelter facilities which leads to more systemic homelessness. 

## Public Sentiment
The Department of Housing and Urban Development (HUD) is the US government agency that is responsible for providing homelessness related aid and coordinating national level effort to help mitigate the effects of homelessness on individuals. Currently, HUD utilizes a machine learning approach to predict future homeless population level in what they call Continuum of Care Areas (CoCs) which is unique way to divide up counties and cities within the US based historic population density of homeless need. 

However, one of the main ways HUD financially supports in need communities is by financially funding homeless shelter facilities. The proposed location of these facilities more often than not stir up public controversy from local business owners and residents. The development of these facilities often require the approval at the CIty Council level. It is at this level where public sentiment can have a significant, potentially negative, impact on the usage of HUD and local government funding toward homelessness. 

To best promote social good and reduce the habitual social injustice against homeless people, both predicted total homeless population and public sentiment need to be taken into grant distribution decisions. This is not to say that areas without positive sentiment on the issue should not be provided funding, but understanding public sentiment can help better determine the type of aid that can be provide to best serve the homeless community.

We decided to measure public sentiment by analysis City COuncil public addresses. For the purpose of this presentation, we focused on three CoC areas as displayed above; Sacramento County CoC, Bakersfield/Kern County CoC, and Orange/ Santa Ana County CoC. From these visualization and our analysis we can pull out some impactful insights to promote social justice for the homeless community.



## Our GCP Journey
In order to accomplish this analysis we used a 6 GCP tools. Each tool provide the advantages of cloud storage, analytics and AI/ML which helped accomplish this Data Hack in the 24 hour time limit.

These were the GCP tools used:
- **Cloud Storage**
- **Big Query**
- **Speech-to-Text**
- **Natural Language**
- **Tables**
- **Data Studio**

## Taking the Next Steps
The fight for social change is just that, a fight. A fight to make tomorrow a better today. The struggles that low-income and homeless communities face are not new, but they are getting worse every day. In today’s world of data science, AI, and machine learning, together we can help better serve these underserved communities by taking steps towards a utilizing the data we have at hand. 

From our analysis we have two main suggested next steps to take the ideas and insights discussed in this presentation to the next step in helping the cause. First, finding the optimal weighted balance of distributing aid based on predicted population growth and public sentiment. This will require local, state, and national government agencies to work together to make sure the financial aid that is meant to help the homeless community, makes the greatest impact possible. Second, conducting a more specific and wide public sentiment analysis. This can be done by analysizing more CoCs and looking at sentiment on more granular topic within the umbrella issue of low income housing and homeless community support.

These are obtainable a necessary next step to help those that need it the most. 

After all, not having a home does not make you any less human :yellow_heart: 

## Sources
-  [Housing Finance](https://www.housingfinance.com/news/study-more-americans-are-homeless_o)
- [Front Steps](https://www.frontsteps.org/u-s-homelessness-facts/#:~:text=U.S.%20Homelessness%20Facts%20%2D%20Front%20Steps&text=The%20National%20Alliance%20to%20End,disabled%20and%20unable%20to%20work)
- [End Homelessness](https://endhomelessness.org/resource/changes-in-the-hud-definition-of-homeless/#:~:text=Changes%20in%20the%20HUD%20Definition%20of%20%E2%80%9CHomeless%E2%80%9D,-January%2018%2C%202012&text=The%20new%20definition%20includes%20four,institution%20where%20they%20temporarily%20resided)

