import sqlite3

def display_all_data():
    """
    Connects to the SQLite database, retrieves all data from the 'users' table,
    and prints each record.
    """
    connection = None
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()

        # Query to fetch all rows from the 'users' table
        cursor.execute("SELECT * FROM users")

        # Fetch all rows from the result of the query
        rows = cursor.fetchall()

        # Print each row
        print("All data in the 'users' table:")
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if connection:
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    display_all_data()
