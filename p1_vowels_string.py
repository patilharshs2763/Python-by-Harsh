# Write a Python program for  extracting the vowels from the string and display its count.
string = input("Enter a string: ")
vowel_count = 0
string = string.lower()

vowels = ['a', 'e', 'i', 'o', 'u']
for char in string:
    if char in vowels:
        vowel_count += 1
print(f"Number of vowels in the string: {vowel_count}")
