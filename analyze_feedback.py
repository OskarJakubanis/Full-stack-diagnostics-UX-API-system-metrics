import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Wczytanie
df_feedback = pd.read_csv("user_feedback.csv", parse_dates=["timestamp"])

# Średnia ocena
print("Średnia ocena:", df_feedback["rating"].mean())

# Wordcloud z feedbacków z oceną ≤ 2
low_scores = df_feedback[df_feedback["rating"] <= 2]["feedback_text"].str.cat(sep=" ")
wordcloud = WordCloud(background_color='white', width=800, height=400).generate(low_scores)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Najczęstsze słowa w negatywnych opiniach")
plt.tight_layout()
plt.savefig("feedback_wordcloud.png")
