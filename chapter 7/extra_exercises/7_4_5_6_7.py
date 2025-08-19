# 7-4. Pizza Toppings
print("Enter the pizza toppings you want. Type 'quit' to finish.")
while True:
    topping = input("Enter a topping: ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza.")

print("\n")

# 7-5. Movie Tickets
print("Movie ticket prices based on age.")
while True:
    age_input = input("Enter your age (or 'quit' to exit): ")
    if age_input.lower() == 'quit':
        break
    age = int(age_input)
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"Your ticket costs ${price}.\n")

# 7-6. Three Exits (examples using pizza toppings)
# Conditional in while loop
topping = ''
while topping != 'quit':
    topping = input("Enter a topping (conditional test to stop): ")
    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")

# Active variable to control loop
active = True
while active:
    topping = input("Enter a topping (active variable to stop): ")
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")

# Break statement to exit loop
while True:
    topping = input("Enter a topping (break to exit): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza.")

# 7-7. Infinity (commented out to avoid crashing the program)
# while True:
#     print("This loop will run forever. Press CTRL-C to stop.")
