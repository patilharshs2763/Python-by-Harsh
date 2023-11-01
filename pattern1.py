n = 5

# Upper Triangle
for rows in range(1, n + 1):
    # Print spaces
    print(" " * (n - rows), end="")
    
    # Print first star
    print("*", end="")
    
    # Print spaces between stars
    print(" " * ((rows - 1) * 2), end="")
    
    # Print second star
    if rows != 1:
        print("*", end="")
    
    # Move to the next line
    print()

# Lower Triangle
for rows in range(n - 1, 0, -1):
    # Print spaces
    print(" " * (n - rows), end="")
    
    # Print first star
    print("*", end="")
    
    # Print spaces between stars
    print(" " * ((rows - 1) * 2), end="")
    
    # Print second star
    if rows != 1:
        print("*", end="")
    
    # Move to the next line
    print()
