first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
course = input("Enter course: ").strip()
age = input("Enter age: ").strip()

full_name = first_name + " " + last_name

print(full_name.title())
print(full_name.upper())
print(full_name.lower())
print(len(full_name))
print(full_name[0])
print(full_name[-1])
print(city, course)
print(f"Age: {age}")
print("Python" in course)
print(course.replace("Python", "Java"))
print(len(course.split()))
