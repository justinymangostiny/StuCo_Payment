import sqlite3

def update_user_balance(user_id, change_amount):
    connection = None
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()

        # Retrieve the current balance for the user
        cursor.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()

        if result is None:
            print(f"No user found with ID '{user_id}'.")
            return

        current_balance = result[0]

        # Calculate the new balance
        new_balance = current_balance + change_amount

        # Update the user's balance in the database
        cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, user_id))

        # Commit the changes
        connection.commit()
        print(f"User ID '{user_id}': Balance updated successfully to {new_balance:.2f}.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if connection:
            connection.close()

def main():
    # Get user input from the terminal
    user_id = int(input("Enter the ID: "))
    balance_change = input("Enter the amount to change (e.g., +300 or -300): ")

    # Convert the input to a float
    change_amount = float(balance_change)
    If change_amount >=0
    # Update the user's balance
    update_user_balance(user_id, change_amount)

if __name__ == "__main__":
    main()
