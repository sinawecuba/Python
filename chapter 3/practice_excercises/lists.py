# 3-1. Names
names = ["Alice", "Brian", "Cindy", "Derek"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print("\n" + "-"*40 + "\n")

# 3-2. Greetings
for name in names:
    print(f"Hello {name}, hope you're having a great day!")

print("\n" + "-"*40 + "\n")

# 3-3. Your Own List
transportation = ["Honda motorcycle", "Tesla car", "Kawasaki bike", "BMW scooter"]
for vehicle in transportation:
    print(f"I would like to own a {vehicle}.")
