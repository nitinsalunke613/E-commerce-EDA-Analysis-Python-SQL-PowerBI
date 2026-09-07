import os
from src.data_loader import load_data
from src.data_cleaning import clean_data, save_cleaned_data
from src.data_transformation import transform_data
from src.analysis import generate_analysis, save_business_insights
from src.visualization import create_visualization
from src.report import create_report
from src.config import ANALYSIS_PATH, GRAPH_PATH, REPORT_PATH


def main():
    print("Loading Data.....")
    df = load_data()

    print("Cleaning Data.....")
    df = clean_data(df)
    save_cleaned_data(df)

    print("Transforming Data.....")
    df = transform_data(df)

    print("Generating Analysis.....")
    analysis = generate_analysis(df)

    print("Saving Business Insights.....")
    os.makedirs(os.path.dirname(ANALYSIS_PATH), exist_ok=True)
    save_business_insights(analysis, ANALYSIS_PATH)

    print("Creating Visualizations.....")
    create_visualization(df, GRAPH_PATH)

    print("Creating PDF Report.....")
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    create_report(analysis, REPORT_PATH)

    print("\nE-Commerce EDA Completed Successfully")


if __name__ == "__main__":
    main()

