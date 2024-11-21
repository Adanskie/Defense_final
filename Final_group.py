import os


# Function to create or register an account
def register_account():
    print("Register a new account")
    username = input("Enter your username: ")

    # Check if username already exists in file
    with open('accounts.txt', 'r') as file:
        accounts = file.readlines()
        for account in accounts:
            stored_username = account.split(',')[0].strip()
            if stored_username == username:
                print("Username already exists. Please choose a different one.")
                return

    password = input("Enter your password: ")

    # Save the new account in the file
    with open('accounts.txt', 'a') as file:
        file.write(f"{username}, {password}\n")

    print("Account created successfully!")


# Function to login with an existing account
def login_account():
    print("Login to your account")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the credentials are correct by reading the file
    with open('accounts.txt', 'r') as file:
        accounts = file.readlines()
        for account in accounts:
            stored_username, stored_password = account.strip().split(', ')
            if stored_username == username and stored_password == password:
                print("Login successful!")
                return True

    print("Invalid username or password. Please try again.")
    return False


# Function to delete a specific account
def delete_account():
    username_to_delete = input("Enter the username of the account you want to delete: ")

    # Read all accounts
    with open('accounts.txt', 'r') as file:
        accounts = file.readlines()

    # Check if the account exists and remove it
    account_found = False
    with open('accounts.txt', 'w') as file:
        for account in accounts:
            stored_username = account.split(',')[0].strip()
            if stored_username == username_to_delete:
                print(f"Account with username '{username_to_delete}' deleted successfully.")
                account_found = True  # Found and deleted the account
            else:
                file.write(account)  # Write back all other accounts

    if not account_found:
        print(f"No account found with the username '{username_to_delete}'.")


# Main function to run the account system
def account_system():
    # Create the file if it doesn't exist
    if not os.path.exists('accounts.txt'):
        open('accounts.txt', 'w').close()

    while True:
        print("\nWelcome to the account system!")
        print("1. Register a new account")
        print("2. Login")
        print("3. Delete an account")
        print("4. Exit")
        choice = input("Please select an option (1/2/3/4): ")

        if choice == '1':
            register_account()
        elif choice == '2':
            if login_account():
                break  # Exit the loop once the login is successful
        elif choice == '3':
            delete_account()  # Call the function to delete an account
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the account system
account_system()
