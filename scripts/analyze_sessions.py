# This script:
# 1. Calculates session durations in minutes
# 2. Counts the most frequent drop-off pages in user sessions
# 3. Computes average session duration

import pandas as pd

# Loading data into a pandas DataFrame to make calculations easier
df_sessions = pd.read_csv("session_tracking.csv", parse_dates=["start_time", "end_time"])

# Calculating session duration in minutes by subtracting start from end times - mission no 1 done!
df_sessions["duration_min"] = (df_sessions["end_time"] - df_sessions["start_time"]).dt.total_seconds() / 60

# Counting how many times each drop-off page occurs to identify where users leave most often - mission no 2 done!
drop_offs = df_sessions["drop_off_page"].value_counts()
print("Most common drop-offs:\n", drop_offs)

# Calculating the average session duration across all sessions - mission no 3 done!
print("\nAverage session duration:", df_sessions["duration_min"].mean(), "minutes")
