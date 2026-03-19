# This file performs matrices,calculate Engagement Rate, calculate ROI, Calculate Influencer Score
import pandas as pd

#Load cleaned data
df=pd.read_csv(r"C:\Users\pr359\OneDrive\Desktop\Smart-Influencer-ROI-Analyzer\01.Data\cleaned_data.csv")

#Engagement Rate
df["Engagement_Rate"]=(df["likes"]+df["comments"]+df["shares"]/df["followers"])*100

#ROI
df["ROI"]=(df["revenue"]-df["campaign cost"]/df["campaign cost"])*100

#Conversion Rate
if "clicks" in df.columns and "conversions" in df.columns:
    df["Conversion_Rate"]=(df["conversions"]/df["clicks"])*100
else:
    df["Conversion_Rate"]=0

#Influencer Score
df["Influencer_score"]=(df["Engagement_Rate"]*0.4+df["ROI"]*0.6)

df.columns=df.columns.str.upper()

#Save final dataset
df.to_csv("01.Data/final_dataset.csv",index=False)

print("✅ Feature Engineering Completed!")
