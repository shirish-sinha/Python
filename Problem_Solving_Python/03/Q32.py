password = input("Enter your password: ")
attempts_left = 5
for i in range(5):
    attempt = input("Re-Enter your password: ")
    matching_positions = 0
    correct = True
    if len(password) == len(attempt):
        for j in range(len(attempt)):
            if attempt[j] == password[j]:
                matching_positions += 1
            else:
                correct = False
    elif len(attempt) < len(password):
        correct = False
        for j in range(len(attempt)):
            if attempt[j] == password[j]:
                matching_positions += 1
    elif len(password) < len(attempt):
        correct = False
        for j in range(len(password)):
            if attempt[j] == password[j]:
                matching_positions += 1
        
    print(f"Matching Positions: {matching_positions}")
    if correct:
        print("Correct")
        break
    else:
        print("Incorrect")