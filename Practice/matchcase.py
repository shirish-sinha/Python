num = int(input("Enter a number: "))
print("You can check: Prime(P), Odd(O), Even(E)")
operation = input("Enter the operation(P, O or E): ").lower()
prime = True
match operation:
    case "e":
        match num % 2:
                case 0:
                  print("Even")
                case _:
                  print("Not Even")
    case "o":
          match num % 2:
               case 1:
                    print("Odd")
               case _:
                    print("Not Odd")
    case "p":
          for i in range(2, num):
               match num % i:
                    case 0:
                         prime = False
                    case _:
                         continue
          match prime:
               case True:
                    print("Prime")
               case _:
                    print("Not Prime")
    case _:
          print("You did not choose a valid operation")