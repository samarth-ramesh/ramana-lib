import sqlite3
import csv
import django
django.setup()

from rlib.models import Book  # Replace 'myapp' with the actual name of your Django app

# Function to insert data into the SQLite database using Django model
def insert_book(data):
    book = Book(**data)
    book.save()

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')  # Replace with your actual database file
cursor = conn.cursor()


# Commit changes to the database
conn.commit()

# Load data from CSV file
csv_file_path = 'rlib.csv'  # Replace with the actual path to your CSV file

with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file, fieldnames=['BookTitle', 'Description', 'Author', 'Category', 'Volume', 'Language', 'OldShelfCode', 'OldAccNo', 'Publisher', 'YearOfPublication', 'NewShelfCode', 'Checked', 'BookId', 'ISBN', 'Status'])
    header = next(csv_reader)  # Get header row

    for row in csv_reader:
        print(row)
        # Only insert data for columns that exist in the defined field names
        filtered_row = {str(key): str(row[key]) for key in header if (key in row) and (key is not None)}
        insert_book(filtered_row)

# Commit changes and close the connection
conn.commit()
conn.close()
