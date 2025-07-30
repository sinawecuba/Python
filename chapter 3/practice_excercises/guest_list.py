# 3-4: Guest List
guests = ['Nelson Mandela', 'Albert Einstein', 'Oprah Winfrey']
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my place.")

print("\n")

# 3-5: Changing Guest List
print(f"Unfortunately, {guests[1]} can't make it to dinner.\n")
guests[1] = 'Barack Obama'  # Replace Einstein with Obama

for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner!")

print("\n")

# 3-6: More Guests
print("Great news! I found a bigger dinner table!\n")

guests.insert(0, 'Maya Angelou')                 # Add to beginning
guests.insert(len(guests)//2, 'Leonardo da Vinci')  # Add to middle
guests.append('Malala Yousafzai')                # Add to end

for guest in guests:
    print(f"Dear {guest}, you are warmly invited to dinner!")

print("\n")

# 3-7: Shrinking Guest List
print("Bad news: I can only invite two people to dinner.\n")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

print("\n")

for guest in guests:
    print(f"{guest}, you’re still invited to dinner!")

# Remove the remaining guests
del guests[0]
del guests[0]

# Confirm the list is empty
print("\nFinal guest list:", guests)  # Should print an empty list
