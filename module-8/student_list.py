
import json


def print_students(class_list):
    """Print each student's information."""
    for student in class_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , "
            f"Email = {student['Email']}"
        )


# Load the student data from the JSON file.
with open("student.json", "r", encoding="utf-8") as file:
    class_list = json.load(file)


# Display the original student list.
print("Original Student List:")
print_students(class_list)
# Add a new student to the class list.
class_list.append({
    "F_Name": "Joshua",
    "L_Name": "Herrick",
    "Student_ID": 90001,
    "Email": "TheJammyDM@greatexpanse.com"
})


# Display the updated student list.
print("\nUpdated Student List:")
print_students(class_list)

# Save the updated student list to the JSON file.
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(class_list, file, indent=4)

print("\nThe student.json file has been updated.")