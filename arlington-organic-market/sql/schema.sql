CREATE DATABASE IF NOT EXISTS organic_market; USE organic_market;
CREATE TABLE vendor(vendor_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(120) NOT NULL,email VARCHAR(160) UNIQUE);
CREATE TABLE item(item_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(160) NOT NULL,price DECIMAL(10,2) NOT NULL CHECK(price>=0),stock_qty INT NOT NULL DEFAULT 0 CHECK(stock_qty>=0),vendor_id INT NOT NULL,FOREIGN KEY(vendor_id) REFERENCES vendor(vendor_id));
CREATE TABLE customer(customer_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(120) NOT NULL,email VARCHAR(160) UNIQUE);
CREATE TABLE customer_order(order_id INT AUTO_INCREMENT PRIMARY KEY,customer_id INT NOT NULL,ordered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY(customer_id) REFERENCES customer(customer_id));
CREATE TABLE order_line(order_id INT,item_id INT,quantity INT NOT NULL CHECK(quantity>0),unit_price DECIMAL(10,2) NOT NULL,PRIMARY KEY(order_id,item_id),FOREIGN KEY(order_id) REFERENCES customer_order(order_id),FOREIGN KEY(item_id) REFERENCES item(item_id));
CREATE VIEW sales_by_item AS SELECT i.item_id,i.name,SUM(ol.quantity) units,SUM(ol.quantity*ol.unit_price) revenue FROM item i JOIN order_line ol ON i.item_id=ol.item_id GROUP BY i.item_id,i.name;
