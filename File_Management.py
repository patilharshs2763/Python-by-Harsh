# Writing to a file
# with open("file1.txt", "w") as file:
    # file.write("Hello Python")

# Opening and reading a file
with open("file1.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a file
with open("file1.txt", "a") as f:
    f.write("\nNothing!")

# Renaming a file
# os.rename("old_file.txt", "new_file.txt")

# Removing a file
# os.remove("file_to_remove.txt")
