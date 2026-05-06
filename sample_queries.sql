SELECT transaction_id, customer_name, amount 
FROM sales_data
WHERE amount > 500 AND status = 'Completed'
ORDER BY amount DESC;


SELECT 
    SUM(amount) AS total_revenue, 
    AVG(amount) AS average_sale,
    COUNT(transaction_id) AS total_transactions
FROM sales_data;


SELECT category, COUNT(*) AS units_sold
FROM inventory
GROUP BY category
HAVING units_sold > 10;

SELECT name, email 
FROM customers
WHERE email LIKE '%@gmail.com' 
OR phone_number IS NULL;


SELECT orders.order_date, customers.name, orders.total_price
FROM orders
JOIN customers ON orders.customer_id = customers.id;
