age=int(input("Enter your age:"))
if age > 0:
    print("Welcome")
    if age >= 18:
        print("\tVoting Successful!")
    else:
        print("\tSorry,You can't vote!!")
print("Thank you!")