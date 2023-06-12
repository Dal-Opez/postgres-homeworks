-- SQL-команды для создания таблиц
CREATE TABLE IF NOT EXISTS customers_data
(
	customer_id char(5) PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS employees_data
(
	employee_id int2 PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar(50),
	birth_date char(10),
	notes text NOT NULL
);

CREATE TABLE IF NOT EXISTS orders_data
(
	order_id int2 PRIMARY KEY,
	customer_id char(5) REFERENCES customers_data(customer_id),
	employee_id int2 REFERENCES employees_data(employee_id),
	order_date char(10) NOT NULL,
	ship_city varchar(20) NOT NULL
);