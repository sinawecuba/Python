# -------------------------------
# 10-4: Guest
# -------------------------------

guest_file = 'guest.txt'

name = input("What is your name? ")
with open(guest_file, 'w') as file:
    file.write(name + '\n')
print(f"Hello, {name}! Your name has been recorded in {guest_file}.")

# -------------------------------
# 10-5: Guest Book
# -------------------------------

guest_book_file = 'guest_book.txt'

print("\nEnter 'q' to quit the guest book.")
while True:
    guest_name = input("Enter your name: ")
    if guest_name.lower() == 'q':
        break
    with open(guest_book_file, 'a') as file:
        file.write(guest_name + '\n')
    print(f"Thank you, {guest_name}, for signing the guest book!")

print(f"All entries have been saved in {guest_book_file}.")
