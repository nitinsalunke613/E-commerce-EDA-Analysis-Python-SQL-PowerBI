import pandas as pd


def transform_data(df):
    df = df.copy()

    df["Revenue"] = df["Sales"] * (1 - df["Discount"] / 100)
    df["Profit"] = df["Revenue"] - df["Cost"]
    df["Profit Margin"] = (df["Profit"] / df["Revenue"].replace(0, 1)) * 100

    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
    df["Year"] = df["Order_Date"].dt.year
    df["Month"] = df["Order_Date"].dt.month
    df["Month_Name"] = df["Order_Date"].dt.month_name()
    df["Quarter"] = df["Order_Date"].dt.quarter

    df["Discount_Category"] = df["Discount"].apply(classify_discount)

    return df


def classify_discount(discount):
    if discount == 0:
        return "No Discount"
    elif discount <= 10:
        return "Low Discount"
    elif discount <= 25:
        return "Medium Discount"
    else:
        return "High Discount"

