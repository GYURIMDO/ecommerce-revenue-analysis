import pandas as pd

# Load the dataset
df = pd.read_csv("data/superstore_cleaned.csv")

# Convert dates to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Extract Year from Order Date (to enable global filtering)
df["Year"] = df["Order Date"].dt.year

# Create a "Delayed" column (1 = Delayed, 0 = On-Time)
df["Delayed"] = (df["Ship Date"] > df["Order Date"] + pd.Timedelta(days=5)).astype(int)

# Group by Year, Region, and Ship Mode to allow filtering
ship_mode_delay_table = df.groupby(["Year", "Region", "Ship Mode"]).agg(
    Total_Orders=("Order ID", "count"), 
    Delayed=("Delayed", "sum")
).reset_index()

# Calculate the delay percentage for each Ship Mode
ship_mode_delay_table["Delay Percentage"] = ship_mode_delay_table["Delayed"] / ship_mode_delay_table["Total_Orders"]

# Save the cleaned table for Tableau
ship_mode_delay_table.to_csv("data/ship_mode_delay_table.csv", index=False)

print("✅ Ship Mode Delay table created successfully!")
print(ship_mode_delay_table)
