# Student Marks and Grade Calculator

def calculate_total(marks1, marks2, marks3):
    total = marks1 + marks2 + marks3
    return total


def calculate_percentage(total, maximum_marks):
    percentage = (total / maximum_marks) * 100
    return percentage


def calculate_grade(percentage):
    if percentage >= 80:
        return "A Grade"
    elif percentage >= 70:
        return "B Grade"
    elif percentage >= 60:
        return "C Grade"
    elif percentage >= 50:
        return "D Grade"
    else:
        return "Fail"


def display_result(name, total, percentage, grade):
    print("\nSTUDENT RESULT\n")
    print("Student Name:", name)
    print("Total Marks:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)


# Main Program

student_name = input("Enter student name: ")

subject1 = float(input("Enter marks in Python: "))
subject2 = float(input("Enter marks in Mathematics: "))
subject3 = float(input("Enter marks in Computer Science: "))

total_marks = calculate_total(subject1, subject2, subject3)

percentage = calculate_percentage(total_marks, 300)

grade = calculate_grade(percentage)

display_result(student_name, total_marks, percentage, grade)
