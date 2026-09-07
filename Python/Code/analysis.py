import pandas as pd


def generate_analysis(df):
    analysis = {}

    analysis["Total Orders"] = len(df)
    analysis["Total Sales"] = df["Sales"].sum()
    analysis["Total Revenue"] = df["Revenue"].sum()
    analysis["Total Cost"] = df["Cost"].sum()
    analysis["Total Profit"] = df["Profit"].sum()
    analysis["Average Order Value"] = round(df["Revenue"].sum() / len(df), 2)

    category_sales = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
    analysis["Best Category"] = category_sales.index[0] if not category_sales.empty else "N/A"

    city_sales = df.groupby("City")["Revenue"].sum().sort_values(ascending=False)
    analysis["Best City"] = city_sales.index[0] if not city_sales.empty else "N/A"

    analysis["Most Used Payment Mode"] = df["Payment_Mode"].mode()[0]
    
    status_count = df["Order_Status"].value_counts()
    analysis["Most Common Order Status"] = status_count.index[0]

    customer_sales = df.groupby("Customer_Name")["Revenue"].sum().sort_values(ascending=False)
    analysis["Top Customer"] = customer_sales.index[0] if not customer_sales.empty else "N/A"

    return analysis


def save_business_insights(analysis, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        for key, value in analysis.items():
            if isinstance(value, float):
                value = round(value, 2)
            file.write(f"{key}: {value}\n")

