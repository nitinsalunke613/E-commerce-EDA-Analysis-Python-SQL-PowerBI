USE ecommerce_db;

SELECT * FROM Ecom_cleaned;
SELECT * FROM vw_Ecom_Transformed;


-- Analysis on Cleaned Data

DELIMITER //

CREATE PROCEDURE get_business_insights()

BEGIN

	SELECT
    
		COUNT(*) AS Total_Orders,
        SUM(Sales) AS Total_Sales,
        SUM(Revenue) AS Total_Revenue,
        SUM(Cost) AS Total_Cost,
        SUM(Profit) AS Total_Profit,
        ROUND(SUM(Revenue) / COUNT(*), 2) AS Average_Order_Value,
        
        (
			SELECT Category FROM vw_Ecom_Transformed
			GROUP BY Category
			ORDER BY SUM(Revenue) DESC
			LIMIT 1
		) AS Best_Category,
        
        (
			SELECT City FROM vw_Ecom_Transformed
            GROUP BY City
            ORDER BY SUM(Revenue) DESC 
            LIMIT 1
        ) AS Best_City,
        
        (
			SELECT Payment_Mode FROM vw_Ecom_Transformed
            GROUP BY Payment_Mode
            ORDER BY COUNT(*) DESC 
            LIMIT 1
        ) AS Most_Used_Payment_Mode,
        
        (
			SELECT Order_Status FROM vw_Ecom_Transformed
            GROUP BY Order_Status
            ORDER BY COUNT(*) DESC
            LIMIT 1
        ) AS Most_Common_Order_Status,
        
        (
			SELECT Customer_Name FROM vw_Ecom_Transformed
            GROUP BY Customer_Name
            ORDER BY SUM(Revenue) DESC
            LIMIT 1
        ) AS Top_Customer
        
	FROM vw_Ecom_Transformed;

END //

DELIMITER ;
        

CALL get_business_insights();
