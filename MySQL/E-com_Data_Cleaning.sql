USE ecommerce_db;

DESC Sales;

ALTER TABLE Sales RENAME TO Ecom_raw;


-- Creating table to store cleaned dataset

CREATE TABLE Ecom_cleaned AS
SELECT * FROM Ecom_raw;


-- Droping Duplicates

CREATE TEMPORARY TABLE temp_cleaned AS
SELECT DISTINCT * FROM Ecom_cleaned;

TRUNCATE TABLE Ecom_cleaned;

INSERT INTO Ecom_cleaned
SELECT * FROM temp_cleaned;

SELECT * FROM Ecom_cleaned;


-- Removing white spaces from text columns

SET SQL_SAFE_UPDATES = 0;

UPDATE Ecom_cleaned 
SET
	Customer_Name = TRIM(Customer_Name),
	Gender = TRIM(Gender),
	City = TRIM(City),
    State = TRIM(State),
    Region = TRIM(Region),
    Category = TRIM(Category),
    Sub_Category = TRIM(Sub_Category),
    Product = TRIM(Product),
    Payment_Mode = TRIM(Payment_Mode),
    Order_Status = TRIM(Order_Status);
    
    
-- Date Conversion

ALTER TABLE Ecom_cleaned
ADD COLUMN Date_Converted DATETIME;

UPDATE Ecom_cleaned 
SET Date_Converted = STR_TO_DATE(Order_Date, '%Y-%m-%d %H:%i:%s');

ALTER TABLE Ecom_cleaned 
DROP COLUMN Order_Date;

ALTER TABLE Ecom_cleaned
RENAME COLUMN Date_Converted TO Order_Date;


-- Numeric Conversion

ALTER TABLE Ecom_cleaned
	MODIFY COLUMN Age INT,
    MODIFY COLUMN Quantity INT, 
    MODIFY COLUMN Sales INT,
    MODIFY COLUMN Discount INT, 
    MODIFY COLUMN Cost INT;
    

-- Missing Values

UPDATE Ecom_cleaned
CROSS JOIN (
    SELECT 
        AVG(Age) AS avg_age, 
        AVG(Sales) AS avg_sales, 
        AVG(Cost) AS avg_cost 
    FROM Ecom_cleaned
) AS stats
SET 
    Age = COALESCE(Age, stats.avg_age),
    Quantity = COALESCE(Quantity, 1),
    Discount = COALESCE(Discount, 0),
    Sales = COALESCE(Sales, stats.avg_sales),
    Cost = COALESCE(Cost, stats.avg_cost);
    

-- Remove Invalid Data

DELETE FROM Ecom_cleaned
WHERE Age <= 0
   OR Quantity <= 0
   OR Sales < 0
   OR Cost < 0
   OR Order_Date IS NULL;
   
SET SQL_SAFE_UPDATES = 1;

