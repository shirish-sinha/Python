# Problem 29

print("1: Search Book")
print("2: Issue Book")
print("3: Return Book")
print("4: View Issued Books")
print("5: Exit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Search Book Selected")
    case 2:
        print("Issue Book Selected")
    case 3:
        print("Return Book Selected")
    case 4:
        print("View Issued Books Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")