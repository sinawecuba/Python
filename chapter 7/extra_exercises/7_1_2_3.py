# 7-1. Rental Car
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.\n")

# 7-2. Restaurant Seating
group_size = int(input("How many people are in your dinner group? "))
if group_size > 8:
    print("Sorry, you'll have to wait for a table.\n")
else:
    print("Your table is ready!\n")

# 7-3. Multiples of Ten
number = int(input("Enter a number: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10.\n")
else:
    print(f"{number} is not a multiple of 10.\n")
