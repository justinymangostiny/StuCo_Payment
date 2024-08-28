
import sqlite3

def add_user_to_database(user_id, user_name):
    connection = None
    try:
        # Connect to the SQLite database (or create it if it doesn't exist)
        connection = sqlite3.connect('example.db')

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # SQL command to create the 'users' table if it does not exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            balance REAL DEFAULT 0.0
        )
        """)

        # Insert user into the table with a default balance of 0.0
        cursor.execute("INSERT INTO users (id, name, balance) VALUES (?, ?, 0.0)", (user_id, user_name))

        # Commit the changes
        connection.commit()
        print(f"User '{user_name}' with ID '{user_id}' added successfully.")

    except sqlite3.IntegrityError:
        print(f"Error: A user with ID '{user_id}' already exists.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if connection:
            connection.close()

def main():
    # Get user input from the terminal
    user_id = int(input("Enter the ID: "))
    user_name = input("Enter the name: ")

    # Add the user to the database
    add_user_to_database(user_id, user_name)

if __name__ == "__main__":
    main()
