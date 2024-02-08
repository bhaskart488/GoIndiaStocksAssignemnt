# Go India Stocks Assignment

#### Link to Google Colab: https://colab.research.google.com/drive/1FmSxAUCPUySZbzXMqAiqhf8RNNYpPoUv?usp=sharing

#### Link to Google Sheet: https://docs.google.com/spreadsheets/d/1bAuXtPfp6BVluhVyEa7BMEfqIuHkTobS2sfbMKTpiCk/edit?usp=sharing

#### Link to Resume: https://drive.google.com/file/d/1lUi__mHkTT67oii5unbci6IUpsGL7Lad/view?usp=sharing

Of late there has been a sudden interest in the term “Green Hydrogen”. As an investor you spend a major
part of your time to find such trends and invest in it earlier than everyone else understands it. So you are
required to write a python program to figure out the buzz around green hydrogen and what all are the
stocks that could benefit due sudden popularity of green hydrogen

## Data Sources used for Analysis:
1. Web Scrape the following websitehttps://www.cnbc.com/search/?query=green%20hydrogen&qsearchterm=green%20hydrogen in order to get headline of the news on this page
2. Use google news rss feed to get all news headline having “green hydrogen” as keyword https://news.google.com/rss/search?q=green%20hydrogen&hl=en-IN&gl=IN&ceid=IN:en
  
## Analysis:
1. Store the result in a pandas dataframe also include News date
2. Use pandas.DataFrame.apply to add an extra column in this table called sentiment score. For sentiment analysis use a pre-trained sentiment analysis model on huggingface.
3. Use appropriate hugging face NER (Named Entity Recognition) model to identify all organization name in news headline
   
## Final Deliverables:
Code has to be written in Google Collab
1. csv table containing news Date, headline and source
2. Using google sheet python api transfer this csv table to a google sheet with access right to “Anyone with the Link”. Write the code for this in google collab only.
3. Graph which shows Week wise trend of average sentiment score for all the news in that particular week
4. Word cloud map with organization name identified in the News headline
   
