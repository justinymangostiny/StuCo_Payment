import sqlite3


def setup_database():
    """
    Creates the 'users' table and inserts sample data into it.
    This function is used for setting up the database.
    """
    connection = None
    try:
        # Connect to the SQLite database (creates the file if it doesn't exist)
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()

        # Create the 'users' table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY ,
            name TEXT NOT NULL,
            balance REAL
        )
        """)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if connection:
            connection.close()


def get_user_info(user_id):
    """
    Retrieve user information based on the given user ID.

    Args:
    user_id (int): The ID of the user whose information is to be retrieved.

    Returns:
    tuple: A tuple containing user information (id, name, balance), or None if the user is not found.
    """
    connection = None
    user_info = None

    try:
        # Connect to the SQLite database
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()

        # Query to fetch user information based on the provided ID
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user_info = cursor.fetchone()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if connection:
            connection.close()

    return user_info


def main():
    # Set up the database and sample data
    setup_database()

    try:
        # Get the user ID from the terminal
        user_id = int(input("Enter user ID: "))

        # Fetch user information
        user_info = get_user_info(user_id)

        # Display user information
        if user_info:
            print(f"User ID: {user_info[0]}")
            print(f"Name: {user_info[1]}")
            print(f"Balance: {user_info[2]:.2f}元")
        else:
            print("User not found.")

    except ValueError:
        print("Invalid input. Please enter a valid integer for the user ID.")

if __name__ == "__main__":
    main()
