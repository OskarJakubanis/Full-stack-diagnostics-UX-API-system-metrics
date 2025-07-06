# This script:
# 1. counts errors per endpoint
# 2. computes average response times
# 3. calculates total requests and total errors with error rate percentage
# 4. identifies the slowest service based on average response time
# 5. counts errors per service

import pandas as pd

# Load data into a pandas DataFrame
df_logs = pd.read_csv("api_logs.csv", parse_dates=["timestamp"])

# Define common error codes to identify and analyze failed API requests.
error_codes = [400, 401, 403, 404, 429, 500, 503]

# Filter logs to keep only entries with the error codes listed above
errors = df_logs[df_logs["status_code"].isin(error_codes)]

# Count how many errors occurred on each endpoint to see their frequency
errors_by_endpoint = errors["endpoint"].value_counts()

# Show number of errors per endpoint — mission 1 done!
print("Errors per endpoint:\n", errors_by_endpoint)

# Calculate the average response time for each service to check performance
avg_response = df_logs.groupby("service_name")["response_time_ms"].mean()

# Show average response time per service — mission 2 done!
print("\nAverage response time (ms):\n", avg_response)

# Total number of requests
total_requests = len(df_logs)

# Total number of errors
total_errors = len(errors)

# Error rate percentage
error_rate = round((total_errors / total_requests) * 100, 2)

# Print total requests, errors and error rate — mission 3 done!
print(f"\nTotal requests: {total_requests}")
print(f"Total errors: {total_errors} ({error_rate}%)")

# Identify slowest service by average response time
slowest_service = df_logs.groupby('service_name')['response_time_ms'].mean().idxmax()

# Print slowest service — mission 4 done!
print(f"Slowest service (avg response time): {slowest_service}")

# Number of errors grouped by service
errors_by_service = errors.groupby('service_name').size()

# Print errors by service — mission 5 done!
print("Errors by service:\n", errors_by_service)
