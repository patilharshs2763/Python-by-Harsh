x=int(input("Enter a numner:"))
match x:
    case 0:
        print("You entered 0")
    case 1:
        print("You entered 1")
    case 2:
        print("You entered 2")
    case 3:
        print("You entered 3")
    case 4:
        print("You entered 4")
    case _:
        print(x)
