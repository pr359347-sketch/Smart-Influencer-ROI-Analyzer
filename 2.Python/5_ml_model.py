
# This file perform  use of ML models  for influencer datset
# Regression + Classification Model (Clean Version)

import pandas as pd

# ML libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# =========================
# 1. LOAD DATA
# =========================
df = pd.read_csv(r"C:\Users\pr359\OneDrive\Desktop\Smart-Influencer-ROI-Analyzer\01.Data\final_dataset.csv")


# =========================
# 2. DATA CLEANING (IMPORTANT)
# =========================

# Convert columns to numeric (handles ######, text etc.)
cols = ['FOLLOWERS','LIKES','COMMENTS','SHARES','CAMPAIGN COST','ROI']

for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Remove all NaN values
df = df.dropna()


# =========================
# 3. REGRESSION MODEL
# =========================

# Features
X = df[['FOLLOWERS','LIKES','COMMENTS','SHARES','CAMPAIGN COST']]

# Target
y = df['ROI']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
reg_model = LinearRegression()

# Train
reg_model.fit(X_train, y_train)

# Predict
y_pred = reg_model.predict(X_test)

# Score
print("R2 Score:", r2_score(y_test, y_pred))


# =========================
# 4. CLASSIFICATION MODEL
# =========================

# Create labels based on ROI
df['INFLUENCER_TYPE'] = df['ROI'].apply(
    lambda x: "Good" if x > 20 else ("Average" if x > 10 else "Bad")
)

# Encode labels
le = LabelEncoder()
df['INFLUENCER_TYPE'] = le.fit_transform(df['INFLUENCER_TYPE'])

# Features (same except ROI)
X = df[['FOLLOWERS','LIKES','COMMENTS','SHARES','CAMPAIGN COST']]

# Target
y = df['INFLUENCER_TYPE']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
clf_model = DecisionTreeClassifier()

# Train
clf_model.fit(X_train, y_train)

# Predict
y_pred = clf_model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

import joblib
joblib.dump(clf_model,"influencer_model.pkl")

#save final dataset
df.to_csv(r"C:\Users\pr359\OneDrive\Desktop\Smart-Influencer-ROI-Analyzer\01.Data\final_dataset.csv",index=False)

print("\n✅ Ml Model (Linear Regression and Classification succesfully Completed!)")
