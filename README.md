# 🛒 E-commerce Exploratory Data Analysis (EDA) — Multi-Tool Implementation

A comprehensive end-to-end data analysis project exploring e-commerce performance data using **Python**, **MySQL**, and **Power BI**. This repository demonstrates three distinct technical approaches to data cleaning, SQL query execution, statistical analysis, and executive visual reporting on the exact same dataset.

---

## 📊 1. Executive Dashboard (Power BI)

Interactive reporting and KPI visualizations built using Power BI Desktop, DAX measures, and custom Figma dashboard canvas templates.

![Power BI Dashboard Overview](PowerBI/Screenshots/E-commerce%20EDA%20Project%20Report.png)

---

## 🐍 2. Python Exploratory Data Analysis (`/Python`)

Python scripts and notebooks utilizing **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn** for deep statistical analysis, data cleaning, and automated chart generation.

| Monthly Revenue Trend | Discount vs. Profit Analysis |
| :---: | :---: |
| ![Monthly Revenue](Python/Graphs/monthly_revenue.png) | ![Discount vs Profit](Python/Graphs/discount_vs_profit.png) |

| Profit by Category | Order Status Distribution |
| :---: | :---: |
| ![Profit by Category](Python/Graphs/profit_by_category.png) | ![Order Status](Python/Graphs/order_status.png) |

| Revenue by Category | Revenue by Region |
| :---: | :---: |
| ![Revenue by Category](Python/Graphs/revenue_by_category.png) | ![Revenue by Region](Python/Graphs/revenue_by_region.png) |

---

## 🗄️ 3. Relational Database & SQL Analytics (`/MySQL`)

Structured MySQL scripts handling table schema setup, data cleaning, transformations, and complex metric queries using SQL commands, views and stored procedures.

![MySQL Query Analysis](MySQL/Screenshots/Ecom_Analysis_MySQL.png)

---

## 📂 Repository Structure

```text
├── data/                       # Raw CSV / Excel datasets
├── Python/                     # Python scripts & visualization code
│   ├── Graphs/                 # Generated EDA charts (.png)
│   ├── main.py                 # Primary execution script
│   └── requirements.txt        # Python dependencies
├── MySQL/                      # Sequential SQL scripts
│   ├── E-com_Data_Loader.sql
│   ├── E-com_Data_Cleaning.sql
│   ├── E-com_Data_Transformation.sql
│   └── E-com_Data_Analysis.sql
├── PowerBI/                    # Power BI report (.pbix, .pdf) & layouts
└── screenshots/                # Key project screenshots for documentation
