import json
import os

# -------------------------------
# 10-11 & 10-12: Favorite Number
# -------------------------------
filename = 'favorite_number.json'

def get_favorite_number():
    """Prompt for favorite number and store it in a file."""
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
    print(f"I'll remember that your favorite number is {number}.")

def show_favorite_number():
    """Read favorite number from file and display it."""
    if os.path.exists(filename):
        with open(filename) as f:
            number = json.load(f)
        print(f"I know your favorite number! It's {number}.")
    else:
        get_favorite_number()

show_favorite_number()

# -------------------------------
# 10-13: User Dictionary
# -------------------------------
user_file = 'user_info.json'

def collect_user_info():
    """Collect multiple pieces of info and store in JSON."""
    user_info = {}
    user_info['username'] = input("Enter your username: ")
    user_info['age'] = input("Enter your age: ")
    user_info['city'] = input("Enter your city: ")
    with open(user_file, 'w') as f:
        json.dump(user_info, f)
    print("User information saved.")

def show_user_info():
    """Read and display user info from file."""
    if os.path.exists(user_file):
        with open(user_file) as f:
            info = json.load(f)
        print(f"Welcome back, {info['username']}! Age: {info['age']}, City: {info['city']}")
    else:
        collect_user_info()

show_user_info()

# -------------------------------
# 10-14: Verify User
# -------------------------------
def verify_user():
    """Check if current user matches stored username."""
    if os.path.exists(user_file):
        with open(user_file) as f:
            info = json.load(f)
        response = input(f"Are you {info['username']}? (yes/no) ").lower()
        if response != 'yes':
            collect_user_info()
        else:
            print(f"Welcome back, {info['username']}!")
    else:
        collect_user_info()

verify_user()
