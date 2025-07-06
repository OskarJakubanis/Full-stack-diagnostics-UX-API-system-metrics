# This script:
# 1. Performs sentiment analysis on user feedback to classify it as positive, negative, or neutral
# 2. Compares sentiment vs. numerical rating and summarizes discrepancies
# 3. Count how many entries have mismatched sentiment labels

import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load dataset from user_feedback.csv
df_feedback = pd.read_csv("user_feedback.csv", parse_dates=["timestamp"])

# Calculate the average rating rounded to 2 decimal places for better readability
print("Average rating:", round(df_feedback["rating"].mean(), 2))

# Define a function to classify text sentiment based on polarity score
def text_to_sentiment(text):
    if pd.isna(text):
        return "missing"

# Calculate sentiment polarity using TextBlob (range: -1 to 1)
    sentiment_polarity = TextBlob(text).sentiment.polarity

 # Classify as positive, negative, or neutral based on polarity threshold
    if sentiment_polarity > 0.1:
        return "positive"
    elif sentiment_polarity < -0.1:
        return "negative"
    else:
        return "neutral"
      
# Apply the sentiment function to each feedback text and store results in a new column
df_feedback["sentiment"] = df_feedback["feedback_text"].apply(text_to_sentiment)

# Classify as positive, negative, or neutral based on rating - mission no 1 done!
def rating_to_sentiment(rating):
    if rating <= 2:
        return "negative"
    elif rating == 3:
        return "neutral"
    else:
        return "positive"

# Apply the sentiment function to each numerical rating and store results in a new column
df_feedback["rating_sentiment"] = df_feedback["rating"].apply(rating_to_sentiment)

# Create column comparing text and rating-based sentiment (True = match, False = mismatch) - mission no 2 done!
df_feedback["sentiment_match"] = df_feedback["sentiment"] == df_feedback["rating_sentiment"]

# Count how many entries have mismatched sentiment labels - mission no 3 done!
mismatch_count = (~df_feedback["sentiment_match"]).sum()
total_count = len(df_feedback)
