stc = input("Enter a sentence: ").split()
checked = ""
for i in range(len(stc)):
    if stc[i] not in checked:
        count = 1
        checked += stc[i] + ": "
        for j in range(i+1, len(stc)):
            if stc[j] == stc[i]:
                count += 1
            else:
                continue
        checked += str(count) + " " + "\n"
        if count == 2:
            checked += "Repeated" + "\n"
        elif 3 <= count <= 4:
            checked += "Frequently Repeated" + "\n"
        elif count > 4:
            checked += "Highly Repeated" + "\n"
        
print(checked)