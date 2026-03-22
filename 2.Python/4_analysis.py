# This file perform analysis of top 5 influencer by ROI and Engagement and their platform-wise performance and detection of fake infulencer
import pandas as pd

#Load final dataset

df=pd.read_csv(r"C:\Users\pr359\OneDrive\Desktop\Smart-Influencer-ROI-Analyzer\01.Data\final_dataset.csv")

#TOP 5 influencer by ROI

top_roi=df.sort_values(by="ROI",ascending=False).head(5)
print("\n🔥 Top 5 Influencer by ROI:")
print(top_roi[["INFLUENCER NAME","ROI"]])

#TOP 5 by Engagement

top_engagement=df.sort_values(by="ENGAGEMENT_RATE",ascending=False).head(5)
print("\n🔥 Top 5 Influencer by Engagement:")
print(top_engagement[["INFLUENCER_SCORE","ENGAGEMENT_RATE"]])

#Platform-wise performance
platform_perf=df.groupby("PLATFORM")[["ROI","ENGAGEMENT_RATE"]].mean()
print("\n📊 Platfrom Performance:")
print(platform_perf)

#Fake Influencer detection
fake=df[(df["FOLLOWERS"]>100000) & (df["ENGAGEMENT_RATE"]<1)]
print("\n🚨 Potential Fake Influencer:")
print(fake[["INFLUENCER NAME","FOLLOWERS","ENGAGEMENT_RATE"]])

print("\n✅ Analysis Completed!")

