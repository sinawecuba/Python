# 7-8. Deli
sandwich_orders = ['tuna', 'pastrami', 'ham', 'pastrami', 'turkey', 'pastrami']
finished_sandwiches = []

# 7-9. No Pastrami
print("The deli has run out of pastrami!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Make sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# List all finished sandwiches
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

print("\n")

# 7-10. Dream Vacation
responses = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")
    responses[name] = vacation
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Show poll results
print("\n--- Poll Results ---")
for name, vacation in responses.items():
    print(f"{name.title()} would like to visit {vacation.title()}.")
