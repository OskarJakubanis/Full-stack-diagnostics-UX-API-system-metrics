# This script:
# 1. counts total clicks per page
# 2. counts total clicks per element clicked
# 3. counts unique users
# 4. finds the most clicked element overall
# 5. counts clicks per user_id

import pandas as pd

# Load data into a pandas DataFrame
df = pd.read_csv("clickstream.csv", parse_dates=["timestamp"])

# Count total clicks per page
clicks_per_page = df["page"].value_counts()
print("# Total clicks per page:")
print(clicks_per_page)

# Count total clicks per element clicked
clicks_per_element = df["element_clicked"].value_counts()
print("\n# Total clicks per element clicked:")
print(clicks_per_element)

# Count unique users
unique_users = df["user_id"].nunique()
print(f"\n# Number of unique users: {unique_users}")

# Find the most clicked element overall
most_clicked_element = clicks_per_element.idxmax()
most_clicked_count = clicks_per_element.max()
print(f"\n# Most clicked element: '{most_clicked_element}' with {most_clicked_count} clicks")

# Count clicks per user_id
clicks_per_user = df["user_id"].value_counts()
print("\n# Total clicks per user_id:")
print(clicks_per_user)
