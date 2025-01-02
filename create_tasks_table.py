import sqlite3

# Connect to the database
connection = sqlite3.connect('car_wash.db')

# Create a cursor object
cursor = connection.cursor()

# SQL command to create the table
create_table_query = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    service_type TEXT NOT NULL,
    date TEXT NOT NULL,
    status TEXT DEFAULT 'Pending'
);
"""

# Execute the query
cursor.execute(create_table_query)

# Commit the changes to the database
connection.commit()

# Provide feedback
print("Table 'tasks' created successfully.")

# Close the connection
connection.close()
