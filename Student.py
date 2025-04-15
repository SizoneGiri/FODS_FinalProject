import numpy as np
import matplotlib.pyplot as plt
from Users import User

# Define the Student class, which inherits from the User class
class Student(User):
    def __init__(self, username, name, id, role, age):
        # Call the User class constructor
        super().__init__(username, name, id, role, age)

    # Define the display method
    def display(self):
        # Print the student's information
        print("\n**** Your Profile ****")
        print(f"Username: {self.username}")
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Age: {self.age}")
        print(f"Role: {self.role}")

    # Define the student menu method
    def student_menu(self):
        # Loop until the user chooses to logout
        while True:
            # Print the menu options
            print(f"\nWelcome, {self.name} (Student)")
            print("1. View Profile")
            print("2. View Grades")
            print("3. View ECA Activities")
            print("4. Logout")

            # Get the user's choice
            choice = input("Enter your choice: ")

            # Handle the user's choice
            if choice == "1":
                # Display the student's profile
                self.display()
            elif choice == "2":
                # View the student's grades
                self.view_grades()
            elif choice == "3":
                # View the student's ECA activities
                self.eca_menu()
            elif choice == "4":
                # Logout
                print("Logging out...\n")
                break
            else:
                # Invalid choice
                print("Invalid choice. Please try again.")

    # Define the view grades method
    def view_grades(self):
        # Define the subjects
        subjects = ["English", "FODS", "IT", "FOM", "CSN"]

        # Try to open grades.txt
        try:
            with open("grades.txt", "r") as file:
                # Loop through each line
                for line in file:
                    # Split the line into its components
                    data = line.strip().split(",")

                    # Check if the line matches the student's username
                    if data[0] == self.username:
                        # Get the student's marks
                        marks = list(map(int, data[1:]))

                        # Print the student's grades
                        print("\n--- Your Grades ---")
                        for subject, mark in zip(subjects, marks):
                            print(f"{subject}: {mark}")

                        # Calculate the student's average grade
                        average = sum(marks) / len(marks)
                        print(f"\nAverage Grade: {average:.2f}")

                        # Plot the student's grades
                        self.show_grade_chart(subjects, marks)
                        return
                # If the student's grades were not found, print a message
                print("Grades not found.")
        except FileNotFoundError:
            # If the file does not exist, print an error message
            print("grades.txt not found.")

    # Define the show grade chart method
    def show_grade_chart(self, subjects, marks):
        # Create a figure and axis
        plt.figure(figsize=(8, 5))
        plt.bar(subjects, marks, color='blue')

        # Set the y-axis limits
        plt.ylim(0, 100)

        # Set the title and labels
        plt.title(f"{self.name}'s Grades")
        plt.xlabel("Subjects")
        plt.ylabel("Marks")

        # Add a grid
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Show the plot
        plt.tight_layout()
        plt.show()

    # Define the view ECA activities method
    def view_eca(self):
        # Try to open eca.txt
        try:
            with open("eca.txt", "r") as file:
                # Loop through each line
                for line in file:
                    # Split the line into its components
                    data = line.strip().split(",")

                    # Check if the line matches the student's username
                    if data[0] == self.username:
                        # Get the student's ECA activities
                        activities = data[1].split(';')

                        # Print the student's ECA activities
                        print("\n--- Your ECA Activities ---")
                        for activity in activities:
                            print(f"- {activity.strip()}")
                        return
                # If the student's ECA activities were not found, print a message
                print("No ECA activities found for your account.")
        except FileNotFoundError:
            # If the file does not exist, print an error message
            print("eca.txt not found.")

    # Define the ECA menu method
    def eca_menu(self):
        # Loop until the user chooses to go back to the main menu
        while True:
            # Print the menu options
            print("\n**** ECA Activities Menu ****")
            print("1. View ECA Activities")
            print("2. Add New Activity")
            print("3. Remove an Activity")
            print("4. Replace All Activities")
            print("5. Back to Main Menu")

            # Get the user's choice
            choice = input("Enter your choice: ")

            # Handle the user's choice
            if choice == "1":
                # View the student's ECA activities
                self.view_eca()
            elif choice == "2":
                # Add a new ECA activity
                self.add_eca()
            elif choice == "3":
                # Remove an ECA activity
                self.remove_eca()
            elif choice == "4":
                # Replace all ECA activities
                self.replace_eca()
            elif choice == "5":
                # Go back to the main menu
                break
            else:
                # Invalid choice
                print("Invalid choice. Please try again.")

    # Define the add ECA activity method
    def add_eca(self):
        # Get the new ECA activity
        new_activity = input("Enter the activity to add: ").strip()

        # Check if the activity is empty
        if not new_activity:
            print("Activity cannot be empty.")
            return

        # Try to open eca.txt
        try:
            with open("eca.txt", "r") as file:
                # Read the lines into a list
                lines = file.readlines()

            # Initialize a flag to indicate if the activity was found
            found = False

            # Loop through each line
            for line in lines:
                # Check if the line matches the student's username
                if line.startswith(self.username + ","):
                    # Split the line into its components
                    parts = line.strip().split(",")
                    activities = parts[1].split(";") if len(parts) > 1 else []

                    # Check if the activity is already in the list
                    if new_activity in [a.strip() for a in activities]:
                        print("Activity already exists in your list.")
                        return

                    # Add the activity to the list
                    activities.append(new_activity)

                    # Update the line
                    lines[lines.index(line)] = self.username + "," + ";".join(activities) + "\n"

                    # Set the found flag to True
                    found = True

            # If the activity was not found, add a new line
            if not found:
                lines.append(self.username + "," + new_activity + "\n")

            # Open eca.txt in write mode
            with open("eca.txt", "w") as file:
                # Write the lines to the file
                file.writelines(lines)

            # Print a success message
            print(f"Activity '{new_activity}' added successfully!")
        except FileNotFoundError:
            # If the file does not exist, create it and add the activity
            with open("eca.txt", "w") as file:
                file.write(self.username + "," + new_activity + "\n")
            print(f"Activity '{new_activity}' added successfully!")

    # Define the remove ECA activity method
    def remove_eca(self):
        # Get the activity to remove
        activity_to_remove = input("Enter the activity to remove: ").strip()

        # Check if the activity is empty
        if not activity_to_remove:
            print("Activity name cannot be empty.")
            return

        # Try to open eca.txt
        try:
            with open("eca.txt", "r") as file:
                # Read the lines into a list
                lines = file.readlines()

            # Initialize a flag to indicate if the activity was found
            found = False

            # Loop through each line
            for line in lines:
                # Check if the line matches the student's username
                if line.startswith(self.username + ","):
                    # Split the line into its components
                    parts = line.strip().split(",")
                    activities = parts[1].split(";")

                    # Check if the activity is in the list
                    if activity_to_remove in [a.strip() for a in activities]:
                        # Remove the activity from the list
                        activities.remove(activity_to_remove)

                        # Update the line
                        lines[lines.index(line)] = self.username + "," + ";".join(activities) + "\n"

                        # Set the found flag to True
                        found = True

            # If the activity was not found, print a message
            if not found:
                print(f"'{activity_to_remove}' not found in your list.")
                return

            # Open eca.txt in write mode
            with open("eca.txt", "w") as file:
                # Write the lines to the file
                file.writelines(lines)

            # Print a success message
            print(f"Activity '{activity_to_remove}' removed successfully.")
        except FileNotFoundError:
            # If the file does not exist, print an error message
            print("eca.txt not found.")

    # Define the replace all ECA activities method
    def replace_eca(self):
        # Get the new ECA activities
        new_activities = input("Enter all new activities (separated by semicolons): ").strip()

        # Check if the activities are empty
        if not new_activities:
            print("Activity list cannot be empty.")
            return

        # Split the activities into a list
        activity_list = [a.strip() for a in new_activities.split(";") if a.strip()]

        # Check if the list is empty
        if not activity_list:
            print("Please enter at least one valid activity.")
            return

        # Try to open eca.txt
        try:
            with open("eca.txt", "r") as file:
                # Read the lines into a list
                lines = file.readlines()

            # Initialize a flag to indicate if the student's ECA activities were found
            found = False

            # Loop through each line
            for line in lines:
                # Check if the line matches the student's username
                if line.startswith(self.username + ","):
                    # Update the line
                    lines[lines.index(line)] = self.username + "," + ";".join(activity_list) + "\n"

                    # Set the found flag to True
                    found = True

            # If the student's ECA activities were not found, add a new line
            if not found:
                lines.append(self.username + "," + ";".join(activity_list) + "\n")

            # Open eca.txt in write mode
            with open("eca.txt", "w") as file:
                # Write the lines to the file
                file.writelines(lines)

            # Print a success message
            print("Your ECA activities have been successfully updated.")
        except FileNotFoundError:
            # If the file does not exist, create it and add the activities
            with open("eca.txt", "w") as file:
                file.write(self.username + "," + ";".join(activity_list) + "\n")
            print("Your ECA activities have been successfully saved.")