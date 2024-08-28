import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create the 'users' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance REAL
)
""")

# Retrieve all data from the 'users' table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Delete Alice's record
cursor.execute("DELETE FROM users WHERE name = 'Alice'")

# Commit the changes and close the connection
connection.commit()
connection.close()

if __name__ == "__main__":
    display_all_data()