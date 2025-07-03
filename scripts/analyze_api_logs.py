# This script:
# 1. counts errors per endpoint, 
# 2. computes average response times,
# 3. plots HTTP status code distribution with errors highlighted in red.

import pandas as pd
import matplotlib.pyplot as plt

# Loading data into a pandas DataFrame to make calculations easier
df_logs = pd.read_csv("api_logs.csv", parse_dates=["timestamp"])

# Defining common error codes to identify and analyze failed API requests.
error_codes = [400, 401, 403, 404, 429, 500, 503]

# Filtering logs to keep only entries with the error codes listed above
errors = df_logs[df_logs["status_code"].isin(error_codes)]

# Counting how many errors occurred on each endpoint to see their frequency
errors_by_endpoint = errors["endpoint"].value_counts()

# Show number of errors per endpoint — mission 1 done!
print("Errors per endpoint:\n", errors_by_endpoint)

# Calculating the average response time for each service to check performance
avg_response = df_logs.groupby("service_name")["response_time_ms"].mean()

# Show average response time per service — mission 2 done!
print("\nAverage response time (ms):\n", avg_response)

# Count how many times each distinct status code appears in the data
status_counts = df_logs["status_code"].value_counts().sort_index()

# Define colors for the bar chart visualization: red for error codes, blue for the rest
colors = ['red' if code in error_codes else 'skyblue' for code in status_counts.index]

# Create bar plot of status code distribution with error codes highlighted - mission 3 done!
plt.figure(figsize=(8,4))
plt.bar(status_counts.index.astype(str), status_counts.values, color=colors)
plt.title("HTTP Status Code Distribution with Errors Highlighted")
plt.xlabel("Status code")
plt.ylabel("Number of occurrences")
plt.tight_layout()
plt.savefig("api_status_code_analysis.png")
plt.show()
