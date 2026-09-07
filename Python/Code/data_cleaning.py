import pandas as pd
from src.config import PROCESSED_DATA_PATH

def clean_data(df):
    df = df.copy()


    # Remove Duplicates

    df = df.drop_duplicates()


    # Clean Text columns

    text_columns = [
        "Customer_Name",
        "Gender",
        "City",
        "State",
        "Region",
        "Category",
        "Sub_Category",
        "Product",
        "Payment_Mode",
        "Order_Status"
    ]


    # Remove Whitespace from text values safely

    for column in text_columns:
        df[column] = df[column].astype(str).str.strip()


    # Date Conversion

    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"],
        errors="coerce"
    )


    # Numeric Conversion

    numeric_columns = [
        "Age",
        "Quantity",
        "Sales",
        "Discount",
        "Cost"
    ]
    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


    # Missing Values

    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Quantity"] = df["Quantity"].fillna(1)
    df["Discount"] = df["Discount"].fillna(0)
    df["Sales"] = df["Sales"].fillna(df["Sales"].median())
    df["Cost"] = df["Cost"].fillna(df["Cost"].median())


    # Remove Invalid Data

    df = df[df["Age"] > 0]
    df = df[df["Quantity"] > 0]
    df = df[df["Sales"] >= 0]
    df = df[df["Cost"] >= 0]
    df = df.dropna(subset=["Order_Date"])


    # Reset Index

    df = df.reset_index(drop=True)
    return df


def save_cleaned_data(df):
    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )

