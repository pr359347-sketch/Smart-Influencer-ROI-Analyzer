#This file perform final cleaning of finaldataset where I clean column names fix fake detection remove infinite values etc
# final_cleaning.py

import pandas as pd
import numpy as np

# STEP 1: Load dataset
df = pd.read_csv(r"C:\Users\pr359\OneDrive\Desktop\Smart-Influencer-ROI-Analyzer\01.Data\final_dataset.csv")

# STEP 2: Clean column names (IMPORTANT for SQL + Power BI)
df.columns = df.columns.str.strip().str.upper().str.replace(" ", "_")

# STEP 3: Remove infinite values
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# STEP 4: Handle missing values
df.dropna(inplace=True)

# STEP 5: Fix INFLUENCER_SCORE (avoid inf issue)
if 'INFLUENCER_SCORE' in df.columns:
    df['INFLUENCER_SCORE'] = df['INFLUENCER_SCORE'].replace([np.inf, -np.inf], 0)

# STEP 6: Fix FAKE DETECTION / INFLUENCER_TYPE (important)
if 'INFLUENCER_TYPE' in df.columns:
    # Recalculate based on engagement rate (better logic)
    if 'ENGAGEMENT_RATE' in df.columns:
        df['INFLUENCER_TYPE'] = df['ENGAGEMENT_RATE'].apply(
            lambda x: 1 if x > 0.05 else 0
        )

# STEP 7: Ensure numeric columns are correct
numeric_cols = ['FOLLOWERS', 'ENGAGEMENT_RATE', 'ROI', 'CAMPAIGN_COST']

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# STEP 8: Final null cleanup (after conversion)
df.dropna(inplace=True)

# STEP 9: Remove duplicates
df.drop_duplicates(inplace=True)

# STEP 10: Reset index
df.reset_index(drop=True, inplace=True)

# STEP 11: Save final clean dataset
df.to_csv("01.Data/final_dataset_cleaned.csv", index=False)

print("✅ CLEAN DATASET READY: final_dataset_cleaned.csv")
print(df.info())
print(df.describe())
print("✅😀Succesfully cleaned the final dataset and generate new finaldataset!")