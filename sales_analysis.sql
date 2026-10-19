-- 1. View the first 10 rows
SELECT *
FROM superstore
LIMIT 10;


-- 2. Count the rows
SELECT COUNT(*)
FROM superstore;


-- 3. Calculate total sales, profit, and orders
SELECT
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders
FROM superstore;


-- 4. Sales and profit by category
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 5. Rank categories by total profit
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC;

-- 6. Analyse sales and profit by region
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;

-- 7. Calculate profit margin by region
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(
        SUM(Profit) * 100.0 / SUM(Sales),
        2
    ) AS Profit_Margin_Percent
FROM superstore
GROUP BY Region
ORDER BY Profit_Margin_Percent DESC;

-- 8. Identify unprofitable product sub-categories
SELECT
    "Sub-Category",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY "Sub-Category"
HAVING SUM(Profit) < 0
ORDER BY Total_Profit ASC;

-- 9. Analyse average profit at each discount level
SELECT
    Discount,
    COUNT(*) AS Number_of_Records,
    ROUND(AVG(Sales), 2) AS Average_Sales,
    ROUND(AVG(Profit), 2) AS Average_Profit
FROM superstore
GROUP BY Discount
ORDER BY Discount;

-- 10. Analyse monthly sales and profit
SELECT
    substr("Order Date", -4, 4) || '-' ||
    printf('%02d',
        CAST(substr("Order Date", 1,
        instr("Order Date", '/') - 1) AS INTEGER)
    ) AS Sales_Month,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Sales_Month
ORDER BY Sales_Month;


-- 11. Analyse yearly sales and profit
SELECT
    substr("Order Date", -4, 4) AS Sales_Year,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Sales_Year
ORDER BY Sales_Year;


-- 12. Find the top 10 products by sales
SELECT
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 10;


-- 13. Find the 10 least profitable products
SELECT
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY "Product Name"
ORDER BY Total_Profit ASC
LIMIT 10;


-- 14. Calculate profit margin for each product
SELECT
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(
        SUM(Profit) * 100.0 / SUM(Sales), 2
    ) AS Profit_Margin_Percent
FROM superstore
GROUP BY "Product Name"
HAVING SUM(Sales) > 0
ORDER BY Profit_Margin_Percent ASC
LIMIT 10;
