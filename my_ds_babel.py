import sqlite3
import csv

def create_table(cursor, table_name):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            "Volcano Name" varchar(100),
            "Country" varchar(100),
            "Type" varchar(100),
            "Latitude (dd)" real,
            "Longitude (dd)" real,
            "Elevation (m)" real
        )
    ''')


def insert_data(cursor, table_name, data):
    cursor.executemany(
        f"INSERT INTO {table_name} (\"Volcano Name\", \"Country\", \"Type\", \"Latitude (dd)\", \"Longitude (dd)\", \"Elevation (m)\") VALUES (?, ?, ?, ?, ?, ?)",
        data
    )


def csv_to_sql(csv_content, database, table_name):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    create_table(cursor, table_name)

    csv_data = csv_content.getvalue()
    reader = csv.DictReader(csv_data.splitlines())

    data_to_insert = [
        (i['Volcano Name'], i['Country'], i['Type'], i['Latitude (dd)'], i['Longitude (dd)'], i['Elevation (m)']) for i
        in reader]

    insert_data(cursor, table_name, data_to_insert)

    conn.commit()
    conn.close()
