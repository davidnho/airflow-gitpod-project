DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(50),
    quantity INT,
    price NUMERIC(10,2),
    sale_date DATE
);

INSERT INTO sales (product_name, quantity, price, sale_date) VALUES
('Coffee', 10, 2.50, '2025-08-01'),
('Tea', 5, 1.50, '2025-08-02'),
('Cake', 2, 15.00, '2025-08-02'),
('Sandwich', 4, 5.00, '2025-08-03');
