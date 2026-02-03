import pandas as pd

# Load CSV file
file_path = "data/Customers_with_Errors.csv"
df = pd.read_csv(file_path)

print("Original Data:")
print(df.head())

valid_professions = [
    "Engineer", "Doctor", "Artist", "Lawyer",
    "Healthcare", "Homemaker", "Executive", "Entertainment"
]

# Normalize profession column (handle NaN, spaces, case)
df["Profession"] = (
    df["Profession"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Detect invalid professions
df["Profession_Status"] = df["Profession"].apply(
    lambda x: "Valid" if x in valid_professions else "Invalid"
)

# Count invalid entries
invalid_count = (df["Profession_Status"] == "Invalid").sum()
print(f"Invalid professions found: {invalid_count}")

# Replace invalid values
df.loc[df["Profession_Status"] == "Invalid", "Profession"] = "Unknown"

# Save cleaned file
df.to_csv("data/Cleaned_Customers.csv", index=False)

print("✅ Data cleaning completed successfully")
