subjects = {"AI", "Python", "Web"}

print("My subjects are:")
print(subjects)

subjects.add("Database")
print("After adding a subject:")
print(subjects)

subjects.remove("Web")
print("After removing a subject:")
print(subjects)

print("Total subjects:", len(subjects))