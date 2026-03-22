# This file perform visualisation of ROI distribution
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\pr359\OneDrive\Desktop\Smart-Influencer-ROI-Analyzer\01.Data\final_dataset.csv")

#ROI distribution
plt.hist(df["ROI"])
plt.title("ROI DISTRIBUTION")
plt.xlabel("ROI")
plt.ylabel("FREQUENCY")
plt.show()

print("\n✅ Visualization Completed!")
