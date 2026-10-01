# Travel & Tourism Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
df = pd.read_csv("Travel-And-Tourism.csv")

# Basic cleaning and feature engineering
for c in ["Booking_Date", "Travel_Date", "Return_Date"]:
    df[c] = pd.to_datetime(df[c], errors="coerce")
num_cols = ["Customer_Age","Number_of_Travellers","Number_of_Adults","Number_of_Children","Hotel_Rating","Number_of_Rooms","Number_of_Nights","Discount_Amount","Customer_Rating","Total_Trip_Cost"]
for c in num_cols: df[c] = pd.to_numeric(df[c], errors="coerce")
df["Lead_Time_Days"] = (df["Travel_Date"] - df["Booking_Date"]).dt.days
df["Trip_Duration_Days"] = (df["Return_Date"] - df["Travel_Date"]).dt.days
df["Revenue_After_Discount"] = df["Total_Trip_Cost"] - df["Discount_Amount"]
df["Cost_Per_Traveller"] = df["Total_Trip_Cost"] / df["Number_of_Travellers"]
df["Cost_Per_Night"] = df["Total_Trip_Cost"] / df["Number_of_Nights"]
df["Booking_Year"] = df["Booking_Date"].dt.year

# EDA checks
print(df.shape)
print(df.info())
print(df.isna().sum().sort_values(ascending=False).head(15))
print("Duplicate rows:", df.duplicated().sum())
print(df.describe(include="all").T)

# KPI table
kpis = pd.Series({
    "Bookings": len(df),
    "Completed bookings": (df.Booking_Status == "Completed").sum(),
    "Cancellation rate": (df.Booking_Status == "Cancelled").mean(),
    "Completed revenue": df.loc[df.Booking_Status == "Completed", "Total_Trip_Cost"].sum(),
    "Avg completed trip value": df.loc[df.Booking_Status == "Completed", "Total_Trip_Cost"].mean(),
    "Avg completed customer rating": df.loc[df.Booking_Status == "Completed", "Customer_Rating"].mean()
})
print(kpis)

# Categorical summaries
for col in ["Booking_Status", "Destination_City", "Payment_Method", "Transportation_Type", "Meal_Plan"]:
    print("\\n", col)
    print(df[col].value_counts().head(15))

# Visualizations
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
sns.countplot(data=df, x="Booking_Status", order=df.Booking_Status.value_counts().index, ax=axes[0,0])
axes[0,0].set_title("Booking status distribution")
sns.histplot(df["Total_Trip_Cost"], bins=35, ax=axes[0,1])
axes[0,1].set_title("Trip cost distribution")
sns.histplot(df.loc[df.Customer_Rating > 0, "Customer_Rating"], bins=10, ax=axes[0,2])
axes[0,2].set_title("Customer rating distribution")
(df.groupby("Destination_City")["Total_Trip_Cost"].sum().nlargest(10).sort_values()).plot.barh(ax=axes[1,0])
axes[1,0].set_title("Top destinations by gross value")
df.groupby("Booking_Status")["Total_Trip_Cost"].sum().plot.bar(ax=axes[1,1])
axes[1,1].set_title("Gross value by booking status")
monthly = df[df.Booking_Status == "Completed"].set_index("Booking_Date").resample("MS")["Total_Trip_Cost"].sum()
monthly.plot(ax=axes[1,2], marker="o")
axes[1,2].set_title("Completed revenue trend")
plt.tight_layout()
plt.show()

# Business cuts
cancel_reasons = df[df.Booking_Status == "Cancelled"].groupby("Cancellation_Reason").agg(Cancellations=("Booking_ID","count"), At_Risk_Value=("Total_Trip_Cost","sum")).sort_values("Cancellations", ascending=False)
print(cancel_reasons)
destination = df.groupby(["Destination_City","Destination_Country"]).agg(Bookings=("Booking_ID","count"), Gross_Value=("Total_Trip_Cost","sum"), Avg_Rating=("Customer_Rating", lambda s: s[s > 0].mean()), Cancellation_Rate=("Booking_Status", lambda s: (s == "Cancelled").mean())).sort_values("Gross_Value", ascending=False)
print(destination.head(15))
