# ----- 5-8: Hello Admin -----

usernames = ['admin', 'jaden', 'kyle', 'sarah', 'tina']

print("5-8: Hello Admin")
for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

print("\n")

# ----- 5-9: No Users -----

usernames = []  # Empty list to simulate no users

print("5-9: No Users")
if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

print("\n")

# ----- 5-10: Checking Usernames (Case Insensitive) -----

current_users = ['John', 'Alice', 'Mike', 'admin', 'Tina']
new_users = ['mike', 'TINA', 'George', 'Lily', 'Admin']

# Convert current_users to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

print("5-10: Checking Usernames")
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a new one.")
    else:
        print(f"The username '{new_user}' is available.")

print("\n")

# ----- 5-11: Ordinal Numbers -----

numbers = list(range(1, 10))

print("5-11: Ordinal Numbers")
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
