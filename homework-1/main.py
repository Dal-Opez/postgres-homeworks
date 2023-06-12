"""Скрипт для заполнения данными таблиц в БД Postgres."""
import os
import csv

BASE_PATH = os.path.abspath("north_data")
CUSTOMERS_FILE_PATH = os.path.join(BASE_PATH, "customers_data.csv")
EMPLOYEES_FILE_PATH = os.path.join(BASE_PATH, "employees_data.csv")
ORDERS_FILE_PATH = os.path.join(BASE_PATH, "orders_data.csv")


def main():
    import psycopg2

    customers_list = []
    with open(CUSTOMERS_FILE_PATH, "r", encoding="windows-1251") as csv_file:
        reader = csv.DictReader(csv_file)
        correct_columns = ["customer_id", "company_name", "contact_name"]
        if reader.fieldnames == correct_columns:
            for customer in reader:
                customers_list.append((customer["customer_id"], customer["company_name"], customer["contact_name"]))

    employees_list = []
    with open(EMPLOYEES_FILE_PATH, "r", encoding="windows-1251") as csv_file:
        reader = csv.DictReader(csv_file)
        correct_columns = ["employee_id", "first_name", "last_name", "title", "birth_date", "notes"]
        if reader.fieldnames == correct_columns:
            for employee in reader:
                employees_list.append((employee["employee_id"], employee["first_name"], employee["last_name"],
                                       employee["title"], employee["birth_date"], employee["notes"]))

    orders_list = []
    with open(ORDERS_FILE_PATH, "r", encoding="windows-1251") as csv_file:
        reader = csv.DictReader(csv_file)
        correct_columns = ["order_id", "customer_id", "employee_id", "order_date", "ship_city"]
        if reader.fieldnames == correct_columns:
            for order in reader:
                orders_list.append((order["order_id"], order["customer_id"], order["employee_id"], order["order_date"],
                                    order["ship_city"]))
    conn = psycopg2.connect(
        host="localhost",
        database="homework_1",
        user="postgres",
        password="12345"
    )
    with conn.cursor() as cur:
        cur.executemany("INSERT INTO customers_data VALUES (%s, %s, %s)", customers_list)
        cur.executemany("INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)", employees_list)
        cur.executemany("INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)", orders_list)
        conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
