# Task 3: Sentiment Analysis
# Author: Pratiksha Singh

import pandas as pd
from textblob import TextBlob

# Step 1: Load the dataset
df = pd.read_csv("bbc_headlines.csv")

# Step 2: Function to analyze sentiment
def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Step 3: Apply sentiment analysis
df["Sentiment"] = df["Headline"].apply(get_sentiment)

# Step 4: Count sentiment values
sentiment_count = df["Sentiment"].value_counts()

# Step 5: Display results
print("Sentiment Distribution:\n")
print(sentiment_count)

# Step 6: Save output
df.to_csv("headline_sentiment_analysis.csv", index=False)
