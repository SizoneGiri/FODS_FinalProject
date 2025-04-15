import numpy as np
import matplotlib.pyplot as plt
from Users import User

# Define the Admin class, which inherits from the User class
class Admin(User):
    def __init__(self, username, name, id, role, age):
        # Call the User class constructor
        super().__init__(username, name, id, role, age)

    # Define the admin menu
    def admin_menu(self):
        # Loop until the user chooses to logout
        while True:
            # Display the admin menu options
            print("1. Add New User")
            print("2. View All Students")
            print("3. Generate Grade Details")
            print("4. Delete User")
            print("5. Edit Student")
            print("6. Change Password")
            print("7. Logout")

            # Get the user's choice
            choice = input("Enter your choice: ")

            # Handle the user's choice
            if choice == "1":
                # Add a new user
                self.add_user()
            elif choice == "2":
                # View all students
                self.view_all_students()
            elif choice == "3":
                # Generate grade details
                self.generate_grade_report()
            elif choice == "4":
                # Delete a user
                self.delete_user()
            elif choice == "5":
                self.edit_student()

            elif choice == "6":
                # Change password
                self.change_password()
            elif choice == "7":
                # Logout
                print("Logging out...\n")
                break
            else:
                # Invalid choice
                print("Invalid choice. Please try again.")

    # Define the add user method
    def add_user(self):
        # Get the user's input
        username = input("Enter username: ")
        name = input("Enter full name: ")
        role = input("Enter role (student/admin): ").lower()
        id = input("Enter ID: ")
        age = input("Enter age: ")
        password = input("Enter password: ")

        # Write to users.txt
        try:
            with open("users.txt", "a") as user_file:
                user_file.write(f"{username},{name},{role},{id},{age}\n")
        except:
            print("Error writing to users.txt")

        # Write to passwords.txt
        try:
            with open("passwords.txt", "a") as pass_file:
                pass_file.write(f"{username},{password}\n")
        except:
            print("Error writing to passwords.txt")

        # Print a success message
        print(f"User '{username}' added successfully!")

    # Define the view all students method
    def view_all_students(self):
        # Print the header
        print("\n**** All Students ****")

        # Try to open users.txt
        try:
            with open("users.txt", "r") as file:
                # Initialize a flag to indicate if any students were found
                found = False

                # Loop through each line in the file
                for line in file:
                    # Split the line into its components
                    data = line.strip().split(",")

                    # Check if the user is a student
                    if data[2].lower() == "student":
                        # Print the student's information
                        print(f"\nUsername: {data[0]}")
                        print(f"Name: {data[1]}")
                        print(f"ID: {data[3]}")
                        print(f"Age: {data[4]}")

                        # Set the found flag to True
                        found = True

                # If no students were found, print a message
                if not found:
                    print("No students found.")
        except FileNotFoundError:
            # If the file does not exist, print an error message
            print("users.txt not found.")

    # Define the generate grade report method
    def generate_grade_report(self):
        # Print the header
        print("\n**** Grade Summary Report ****")

        # Define the subjects
        subjects = ["English", "FODS", "IT", "FOM", "CSN"]

        # Initialize variables to keep track of the total marks and the top student
        subject_totals = [0] * len(subjects)
        student_count = 0
        top_student = ""
        top_total = -1

        # Try to open grades.txt
        try:
            with open("grades.txt", "r") as file:
                # Loop through each line in the file
                for line in file:
                    # Split the line into its components
                    data = line.strip().split(",")

                    # Get the student's username and marks
                    username = data[0]
                    marks = list(map(int, data[1:]))

                    # Check if the marks are valid
                    if len(marks) != len(subjects):
                        continue

                    # Increment the student count
                    student_count += 1

                    # Add the marks to the subject totals
                    for i in range(len(subjects)):
                        subject_totals[i] += marks[i]

                    # Calculate the student's total marks
                    total = sum(marks)

                    # Check if the student is the top student
                    if total > top_total:
                        top_total = total
                        top_student = username

            # If no students were found, print a message
            if student_count == 0:
                print("No valid grade data found.")
                return

            # Calculate the subject averages
            subject_averages = [total / student_count for total in subject_totals]

            # Print the report
            print(f"\nTotal students: {student_count}")
            print(f"Top performer: {top_student} with {top_total} total marks\n")
            print("Subject Averages:")
            for subject, avg in zip(subjects, subject_averages):
                print(f"{subject}: {avg:.2f}")

            # Plot the subject averages
            self.plot_subject_averages(subjects, subject_averages)

        except FileNotFoundError:
            # If the file does not exist, print an error message
            print("grades.txt not found.")

    # Define the plot subject averages method
    def plot_subject_averages(self, subjects, averages):
        # Create a figure and axis
        plt.figure(figsize=(8, 5))
        plt.bar(subjects, averages, color="lightgreen")

        # Set the y-axis limits
        plt.ylim(0, 100)

        # Set the title and labels
        plt.title("Class Subject Averages")
        plt.xlabel("Subjects")
        plt.ylabel("Average Marks")

        # Add a grid
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        # Show the plot
        plt.tight_layout()
        plt.show()

    # The delete user method
    def delete_user(self):
        # Print the header
        print("\n--- Delete User ---")

        # Get the username to delete
        username_to_delete = input("Enter the username to delete: ")

        # Try to open users.txt
        try:
            with open("users.txt", "r") as f:
                # Read the lines into a list
                lines = f.readlines()

            # Open users.txt in write mode
            with open("users.txt", "w") as f:
                # Loop through each line
                for line in lines:
                    # Check if the line starts with the username to delete
                    if not line.startswith(username_to_delete + ","):
                        # Write the line to the file
                        f.write(line)

        except FileNotFoundError:
            # If the file does not exist, print an error message
            print("users.txt not found.")

        # Try to open passwords.txt
        try:
            with open("passwords.txt", "r") as f:
                # Read the lines into a list
                lines = f.readlines()

            # Open passwords.txt in write mode
            with open("passwords.txt", "w") as f:
                # Loop through each line
                for line in lines:
                    # Check if the line starts with the username to delete
                    if not line.startswith(username_to_delete + ","):
                        # Write the line to the file
                        f.write(line)

        except FileNotFoundError:
            # If the file does not exist, print an error message
            print("passwords.txt not found.")

        # Print a success message
        print(f"User '{username_to_delete}' has been deleted from all records (if existed).")

    # Define the change password method
    def change_password(self):
        # Print the header
        print("\n**** Change Password ****")

        # Get the current password
        current_password = input("Enter your current password: ").strip()

        # Try to open passwords.txt
        try:
            with open("passwords.txt", "r") as file:
                # Read the lines into a list
                lines = file.readlines()

            # Initialize a flag to indicate if the password was found
            valid = False

            # Loop through each line
            for line in lines:
                # Check if the line matches the current password
                if line.strip() == f"{self.username},{current_password}":
                    # Set the valid flag to True
                    valid = True
                    break

            # If the password was not found, print an error message
            if not valid:
                print("Incorrect current password.")
                return

            # Get the new password
            new_password = input("Enter new password: ").strip()
            confirm_password = input("Confirm new password: ").strip()

            # Check if the new password matches the confirm password
            if new_password != confirm_password:
                print("Passwords do not match.")
                return

            # Open passwords.txt in write mode
            with open("passwords.txt", "w") as file:
                # Loop through each line
                for line in lines:
                    # Check if the line starts with the username
                    if line.startswith(self.username + ","):
                        # Write the new password to the file
                        file.write(f"{self.username},{new_password}\n")
                    else:
                        # Write the line to the file
                        file.write(line)

            # Print a success message
            print("Password updated successfully.")

        except FileNotFoundError:
            # If the file does not exist, print an error message
            print("passwords.txt not found.")


    def edit_student(self):
     print("\n**** Edit Student Info ****")
     target_username = input("Enter the username of the student to edit: ")

     updated_lines = []
     found = False

     try:
        with open("users.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == target_username:
                    found = True
                    print(f"\nCurrent Info:")
                    print(f"Username: {data[0]}")
                    print(f"Name: {data[1]}")
                    print(f"Role: {data[2]}")
                    print(f"ID: {data[3]}")
                    print(f"Age: {data[4]}")

                    print("\nEnter new values (press Enter to keep current):")
                    new_name = input("New Name: ").strip() or data[1]
                    new_role = input("New Role (student/admin): ").strip() or data[2]
                    new_id = input("New ID: ").strip() or data[3]
                    new_age = input("New Age: ").strip() or data[4]

                    updated_line = f"{data[0]},{new_name},{new_role},{new_id},{new_age}\n"
                    updated_lines.append(updated_line)
                else:
                    updated_lines.append(line)

        if found:
            with open("users.txt", "w") as file:
                file.writelines(updated_lines)
            print(f"Student '{target_username}' info updated successfully.")
        else:
            print(f"No student found with username: {target_username}")

     except FileNotFoundError:
        print("users.txt not found.")