# This script:
# 1. calculates total number of cart abandonments
# 2. calculates average number of items in abandoned carts
# 3. calculates average total value of abandoned carts
# 4. identifies the cart with the highest total value abandoned
# 5. counts abandonments per user

import pandas as pd

# Load data into a pandas DataFrame
df = pd.read_csv("cart_abandonment.csv", parse_dates=["abandonment_time"])

# Calculate total number of cart abandonments
total_abandonments = len(df)
print("# Total number of cart abandonments:")
print(total_abandonments)

# Calculate average number of items in abandoned carts
avg_items_in_cart = df["items_in_cart"].mean()
print(f"\n# Average number of items in abandoned carts: {avg_items_in_cart:.2f}")

# Calculate average total value of abandoned carts
avg_cart_value = df["total_value"].mean()
print(f"\n# Average total value of abandoned carts: ${avg_cart_value:.2f}")

# Identify the cart with the highest total value abandoned
max_value_cart = df.loc[df["total_value"].idxmax()]
print("\n# Cart with the highest total value abandoned:")
print(f"User ID: {max_value_cart['user_id']}, Cart ID: {max_value_cart['cart_id']}, "
      f"Total Value: ${max_value_cart['total_value']:.2f}, Items: {max_value_cart['items_in_cart']}")

# Count abandonments per user
abandonments_per_user = df["user_id"].value_counts()
print("\n# Number of abandonments per user:")
print(abandonments_per_user)
