# -------------------------------
# 10-6: Addition with Exception Handling
# -------------------------------
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = int(num1) + int(num2)
    print(f"The sum is {result}.")
except ValueError:
    print("Oops! Please enter valid numbers.")

# -------------------------------
# 10-7: Addition Calculator with Loop
# -------------------------------
print("\nAddition Calculator (type 'q' to quit)")
while True:
    num1 = input("Enter the first number: ")
    if num1.lower() == 'q':
        break
    num2 = input("Enter the second number: ")
    if num2.lower() == 'q':
        break
    try:
        result = int(num1) + int(num2)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    else:
        print(f"The sum is {result}.")

# -------------------------------
# 10-8 & 10-9: Cats and Dogs Files
# -------------------------------
for filename in ['cats.txt', 'dogs.txt']:
    try:
        with open(filename) as file:
            print(f"\nContents of {filename}:")
            print(file.read())
    except FileNotFoundError:
        # 10-8 prints a message
        # print(f"Sorry, {filename} does not exist.") 
        # 10-9 fails silently instead
        pass

# -------------------------------
# 10-10: Common Words in Text
# -------------------------------
def count_word_in_file(filename, word):
    """Count occurrences of a word in a text file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return 0
    else:
        # Count all occurrences (case-insensitive)
        return contents.lower().count(word.lower())

# Example usage (replace with your Project Gutenberg files)
files_to_check = ['book1.txt', 'book2.txt']
for file in files_to_check:
    count = count_word_in_file(file, 'the')
    print(f"The word 'the' appears {count} times in {file}.")
