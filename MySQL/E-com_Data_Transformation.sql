USE ecommerce_db;

SELECT * FROM Ecom_cleaned;


-- Transforming Data

CREATE VIEW vw_Ecom_transformed AS
SELECT 
    *,
    
    -- 1. Revenue Calculation
    (Sales * (1 - Discount / 100)) AS Revenue,
    
    -- 2. Profit Calculation
    ((Sales * (1 - Discount / 100)) - Cost) AS Profit,
    
    -- 3. Profit Margin Calculation
    CASE 
        WHEN (Sales * (1 - Discount / 100)) = 0 THEN 0
        ELSE (((Sales * (1 - Discount / 100)) - Cost) / (Sales * (1 - Discount / 100))) * 100
    END AS Profit_Margin,
    
    -- 4. Date Extract Transformations
    YEAR(Order_Date) AS Year,
    MONTH(Order_Date) AS Month,
    MONTHNAME(Order_Date) AS Month_Name,
    QUARTER(Order_Date) AS Quarter,
    
    -- 5. Discount Category
    CASE 
        WHEN Discount = 0 THEN 'No Discount'
        WHEN Discount <= 10 THEN 'Low Discount'
        WHEN Discount <= 25 THEN 'Medium Discount'
        ELSE 'High Discount'
    END AS Discount_Category

FROM Ecom_cleaned;


-- Retreving Transformed Data

SELECT * FROM vw_Ecom_transformed;

SELECT * FROM vw_Ecom_transformed
WHERE Profit < 0;

