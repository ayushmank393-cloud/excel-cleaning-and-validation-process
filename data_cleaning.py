import pandas as pd

# ---------------- Load Data ----------------
file_path = "data/Customers_with_Errors.csv"
df = pd.read_csv(file_path)

print("\n🔹 Original Data Preview:")
print(df.head())

# ---------------- Valid Professions ----------------
valid_professions = [
    "Engineer", "Doctor", "Artist", "Lawyer",
    "Healthcare", "Homemaker", "Executive", "Entertainment"
]

# Common typo corrections
profession_corrections = {
    "Enginer": "Engineer",
    "Docter": "Doctor",
    "Artst": "Artist",
    "Lawer": "Lawyer"
}

# ---------------- Clean Profession Column ----------------
# Handle missing values
df["Profession"] = df["Profession"].fillna("Unknown")

# Normalize text
df["Profession"] = (
    df["Profession"]
    .str.strip()
    .str.title()
)

# Fix common typos
df["Profession"] = df["Profession"].replace(profession_corrections)

# ---------------- Validation ----------------
df["Profession_Status"] = df["Profession"].apply(
    lambda x: "Valid" if x in valid_professions else "Invalid"
)

invalid_before = (df["Profession_Status"] == "Invalid").sum()

# Replace invalid values
df.loc[df["Profession_Status"] == "Invalid", "Profession"] = "Unknown"

invalid_after = (df["Profession"] == "Unknown").sum()

# ---------------- Remove Duplicates ----------------
duplicates_removed = df.duplicated().sum()
df = df.drop_duplicates()

# ---------------- Save Cleaned Data ----------------
output_path = "data/Cleaned_Customers.csv"
df.to_csv(output_path, index=False)

# ---------------- Summary ----------------
print("\n✅ DATA CLEANING SUMMARY")
print(f"Invalid professions corrected : {invalid_before}")
print(f"Final 'Unknown' professions   : {invalid_after}")
print(f"Duplicate records removed     : {duplicates_removed}")
print(f"Cleaned file saved to         : {output_path}")
