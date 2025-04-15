# Import Classes module

from Admin import Admin
from Student import Student

# Define the login function
def login():
    # Loop until the user logs in successfully
    while True:
        # Get the username and password
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Try to open passwords.txt
        try:
            with open('passwords.txt', 'r') as auth:
                # Loop through each line
                for line in auth:
                    # Check if the line matches the username and password
                    if line.strip() == f"{username},{password}":
                        # Print a success message
                        print("Login successful")
                        return username
        except FileNotFoundError:
            # If the file does not exist, print an error message
            print("Password file not found.")

        # Print an error message
        print("Incorrect username or password.")

# Define the get info function
def get_info(username):
    # Try to open users.txt
    try:
        with open('users.txt', 'r') as info:
            # Loop through each line
            for line in info:
                # Split the line into its components
                data = line.strip().split(',')

                # Check if the line matches the username
                if data[0] == username:
                    # Return the user's information
                    return username, data[1], data[2], data[3], data[4]
    except FileNotFoundError:
        # If the file does not exist, print an error message
        print("User file not found.")

    # Return None if the user was not found
    return None

# Define the main function
def main():
    # Loop until the user chooses to quit
    while True:
        # Get the username
        username = login()

        # Get the user's information
        user_info = get_info(username)

        # Check if the user was found
        if user_info:
            # Get the user's attributes
            username, name, role, id, age = user_info

            # Check the user's role
            if role == "admin":
                # Create an Admin object
                admin = Admin(username, name, id, role, age)

                # Call the admin menu method
                admin.admin_menu()
            elif role == "student":
                # Create a Student object
                student = Student(username, name, id, role, age)

                # Call the student menu method
                student.student_menu()
            else:
                # Print an error message
                print("Unknown role.")
        else:
            # Print an error message
            print("User not found in database.")

        # Ask the user if they want to log in again
        again = input("Do you want to log in again? (yes/no): ").lower()

        # Check the user's response
        if again != "yes":
            # Print a goodbye message
            print("Goodbye!")
            break

# Call the main function
main()