import pandas as pd

#Load dataset
df=pd.read_csv(r"C:\Users\pr359\OneDrive\Desktop\Smart-Influencer-ROI-Analyzer\01.Data\raw_data.csv.xls")

#Show basic info
print(df.info)

#Remove duplicates
df.drop_duplicates(inplace=True)

#Handle missing values
df.fillna(0,inplace=True)

#Standardrize column names
df.columns=df.columns.str.strip().str.replace(" ","_")

#arraning platform

df["Platform"]=df["Platform"].str.lower().str.strip()

df["Platform"]=df["Platform"].replace({
    "tik tok":"TikTok",
    "youtube":"YouTube",
    "fb":"Facebook",
    "facebook":"Facebook",
    "instagram":"Instagram",
    "yt":"Youtube",
    "ig":"Instagram",
    "insta":"Instagram",
    "linkedin":"Linkedin",
    "tikTok":"TikTok",
    "tiktok":"Tiktok",
    "you tube":"YouTube"
})
# add only starting 1200 rows
df=df.head(1200)

# Arranging all columns Datatype
# 1. Clean column names
# -------------------------------
df.columns = df.columns.str.strip().str.lower()

# -------------------------------
# 2. Function: Convert K, M, L → numbers
# -------------------------------
def convert_values(x):
    if isinstance(x, str):
        x = x.strip().upper()
        x = x.replace(',', '').replace('₹', '')

        try:
            if x.endswith('K'):
                return float(x[:-1]) * 1_000
            elif x.endswith('M'):
                return float(x[:-1]) * 1_000_000
            elif x.endswith('L'):
                return float(x[:-1]) * 100_000
            else:
                return float(x)
        except:
            return None
    return x

# -------------------------------
# 3. Convert numeric columns
# -------------------------------
numeric_cols = [
    'followers', 'likes', 'comments', 'shares',
    'impressions', 'clicks', 'conversions',
    'campaign cost', 'revenue'
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].apply(convert_values)
        df[col] = pd.to_numeric(df[col], errors='coerce')

# -------------------------------
# 4. Convert date column
# -------------------------------
if 'Campaign_Date' in df.columns:
    df['Campaign_Date'] = pd.to_datetime(df['campaign date'], errors='coerce', dayfirst=True)

# -------------------------------
# 5. Convert text columns (optional)
# -------------------------------
text_cols = ['influencer name', 'platform', 'content type']

for col in text_cols:
    if col in df.columns:
        df[col] = df[col].astype(str)

# -------------------------------
# 6. Shuffle data (no grouping)
# -------------------------------
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Arranging the Campaign_Date format
# 1. Clean column names properly
# -------------------------------
df.columns = df.columns.str.strip().str.lower().str.replace('_', ' ')

# -------------------------------
# 2. Check actual column names
# -------------------------------
print(df.columns)

# -------------------------------
# 3. Automatically detect campaign date column
# -------------------------------
date_col = None
for col in df.columns:
    if 'campaign' in col and 'date' in col:
        date_col = col
        break

print("Detected column:", date_col)

# -------------------------------
# 4. Apply date conversion safely
# -------------------------------
if date_col:
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce', dayfirst=True)
    df[date_col] = df[date_col].dt.strftime('%Y-%m-%d')
else:
    print("⚠️ Campaign date column not found!")


# To fill the blank campaign_date column


# 1. Clean column names
# -------------------------------
df.columns = df.columns.str.strip().str.lower().str.replace('_', ' ')

# -------------------------------
# 2. Convert to datetime
# -------------------------------
df['campaign date'] = pd.to_datetime(df['campaign date'], errors='coerce', dayfirst=True)

# -------------------------------
# 3. Fill missing values
# -------------------------------
df['campaign date'] = df['campaign date'].fillna(method='ffill')  # previous value
df['campaign date'] = df['campaign date'].fillna(method='bfill')  # next value (if starting me blank ho)

# -------------------------------
# 4. Convert to same format
# -------------------------------
df['campaign date'] = df['campaign date'].dt.strftime('%Y-%m-%d')


# Arrange the datatype of campaign cost
# 1. Clean column names
# -------------------------------
df.columns = df.columns.str.strip().str.lower().str.replace('_', ' ')

# -------------------------------
# 2. Function for conversion
# -------------------------------
def convert_cost(x):
    if isinstance(x, str):
        x = x.strip().upper()
        x = x.replace(',', '').replace('₹', '')

        try:
            if x.endswith('K'):
                return float(x[:-1]) * 1_000
            elif x.endswith('M'):
                return float(x[:-1]) * 1_000_000
            elif x.endswith('L'):
                return float(x[:-1]) * 100_000
            else:
                return float(x)
        except:
            return None
    return x

# -------------------------------
# 3. Apply on campaign cost
# -------------------------------
if 'campaign cost' in df.columns:
    df['campaign cost'] = df['campaign cost'].apply(convert_cost)
    df['campaign cost'] = pd.to_numeric(df['campaign cost'], errors='coerce')

# -------------------------------
# 4. Check datatype
# -------------------------------
print(df['campaign cost'].dtype)

# Fill the blank campaign cost using median
# 1. Clean column names
# -------------------------------
df.columns = df.columns.str.strip().str.lower().str.replace('_', ' ')

# -------------------------------
# 2. Convert campaign cost to numeric
# -------------------------------
df['campaign cost'] = pd.to_numeric(df['campaign cost'], errors='coerce')

# -------------------------------
# 3. Fill missing values with MEDIAN
# -------------------------------
median_value = df['campaign cost'].median()

df['campaign cost'] = df['campaign cost'].fillna(median_value)

# -------------------------------
# 4. Check
# -------------------------------
print(df['campaign cost'].isna().sum())  # should be 0


#Save cleaned data
df.to_csv("01.Data/cleaned_data.csv",index=False)



print("✅ Data Cleaning Completed!")