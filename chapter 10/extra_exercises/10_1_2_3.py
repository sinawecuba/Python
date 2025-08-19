# -------------------------------
# 10-1: Learning Python
# -------------------------------

# Read the entire file and print
filename = 'learning_python.txt'

try:
    with open(filename, 'r') as file:
        contents = file.read()
        print("Reading entire file at once:")
        print(contents)
except FileNotFoundError:
    print(f"Error: The file {filename} does not exist.")

# Read the file line by line into a list and loop over it
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        print("\nReading line by line from the list:")
        for line in lines:
            print(line.strip())
except FileNotFoundError:
    print(f"Error: The file {filename} does not exist.")

# -------------------------------
# 10-2: Learning C
# -------------------------------

try:
    with open(filename, 'r') as file:
        print("\nReplacing 'Python' with 'C':")
        for line in file:
            print(line.replace('Python', 'C').strip())
except FileNotFoundError:
    print(f"Error: The file {filename} does not exist.")

# -------------------------------
# 10-3: Simpler Code
# -------------------------------

# Looping directly over splitlines() without a temporary variable
try:
    with open(filename, 'r') as file:
        print("\nUsing splitlines() directly:")
        contents = file.read()
        for line in contents.splitlines():
            print(line)
except FileNotFoundError:
    print(f"Error: The file {filename} does not exist.")
