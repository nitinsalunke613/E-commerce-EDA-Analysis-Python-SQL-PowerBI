import os
import matplotlib.pyplot as plt
import seaborn as sns


def create_visualization(df,output_path):

    os.makedirs(output_path,exist_ok = True)


    # Category Revenue

    category_revenue = (
        df.groupby("Category")["Revenue"].sum()
        .sort_values(ascending = False)
    )

    plt.figure(figsize = (8,5))
    category_revenue.plot(kind = "bar")
    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,"revenue_by_category.png"))
    plt.close()


    # Region Revenue

    region_revenue = (
        df.groupby("Region")["Revenue"].sum()
        .sort_values(ascending = False)
    )

    plt.figure(figsize = (8,5))
    region_revenue.plot(kind = "bar")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,"revenue_by_region.png"))
    plt.close()


    # Monthly Revenue

    monthly_Revenue = (
        df.groupby("Month_Name")["Revenue"].sum()
    )

    plt.figure(figsize = (10,5))
    monthly_Revenue.plot(kind = "line", marker = "o")
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,"monthly_revenue.png"))
    plt.close()


    # Order Status

    plt.figure(figsize = (7,5))
    sns.countplot(data = df, x = "Order_Status")
    plt.title("Order_Status_distribution")
    plt.xlabel("Order_Status")
    plt.ylabel("Number of Orders")
    plt.xticks(rotation = 30)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,"order_status.png"))
    plt.close()


    # Payment

    payment_count = (
     df["Payment_Mode"].value_counts()  
    )
    
    plt.figure(figsize = (7,5))
    payment_count.plot(kind = "bar")
    plt.title("Payment Mode Usage")
    plt.xlabel("Payment Mode")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,"payment_mode.png"))
    plt.close()


    # Profit by Category

    category_profit = (
        df.groupby("Category")["Profit"].sum()
        .sort_values(ascending = False)
    )

    plt.figure(figsize = (8,5))
    category_profit.plot(kind = "bar")
    plt.title("Profit by Category")
    plt.xlabel("Category")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,"profit_by_category.png"))
    plt.close()


    # Discount vs Profit

    plt.figure(figsize = (8,5))
    sns.scatterplot(data = df, x = "Discount", y = "Profit")
    plt.title("Discount vs Profit")
    plt.xlabel("Discount")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path,"discount_vs_profit.png"))
    plt.close()

