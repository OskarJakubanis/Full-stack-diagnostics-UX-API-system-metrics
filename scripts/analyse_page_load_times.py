# This script:
# 1. calculates average page load times per page URL
# 2. identifies the slowest page based on average load time
# 3. counts how many times each page was loaded
# 4. calculates overall average load time across all pages

import pandas as pd

# Load data into a pandas DataFrame
df = pd.read_csv("page_load_times.csv", parse_dates=["timestamp"])

# Calculate average load time per page URL
avg_load_time_per_page = df.groupby("page_url")["load_time_ms"].mean()
print("# Average load time per page (ms):")
print(avg_load_time_per_page)

# Identify the slowest page by average load time
slowest_page = avg_load_time_per_page.idxmax()
slowest_page_time = avg_load_time_per_page.max()
print("\n# Slowest page:")
print(f"{slowest_page} with average load time {slowest_page_time:.2f} ms")

# Count total requests per page URL
requests_per_page = df["page_url"].value_counts()
print("\n# Total requests per page:")
print(requests_per_page)

# Calculate overall average load time across all pages
overall_avg_load_time = df["load_time_ms"].mean()
print(f"\n# Overall average load time across all pages: {overall_avg_load_time:.2f} ms")
