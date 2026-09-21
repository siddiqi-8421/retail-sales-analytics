-- Monthly revenue trend
SELECT order_month, SUM(sales) AS total_sales
FROM orders
GROUP BY order_month
ORDER BY order_month;

-- Top 10 products by profit
SELECT product_name, SUM(profit) AS total_profit
FROM orders
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 10;

-- Average shipping delay by region
SELECT region, AVG(shipping_delay_days) AS avg_delay
FROM orders
GROUP BY region;