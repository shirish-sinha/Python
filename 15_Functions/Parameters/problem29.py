def calculate_result(marks, passing_marks=35):
    if marks >= passing_marks:
        return "Pass"
    return "Fail"


print(calculate_result(40))
print(calculate_result(30))
print(calculate_result(30, 25))
