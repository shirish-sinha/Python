# Problem 4

color = input("Enter signal: ").lower().strip()

match color:
    case("red"):
        print("Stop")
    case("green"):
        print("Go")
    case("yellow"):
        print("Wait")
    case _:
        print("Invalid Signal")