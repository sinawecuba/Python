motorcycles = ['honda', 'yamaha', 'suzuki']       # Create a list of motorcycles
print(motorcycles)                                # Output the original list
motorcycles[0] = 'ducati'                         # Replace the first item with 'ducati'
print(motorcycles)                                # Output the updated list

motorcycles = ['honda', 'yamaha', 'suzuki']       # Reset the list to original
print(motorcycles)                                # Print current list
motorcycles.append('ducati')                      # Add 'ducati' to the end of the list
print(motorcycles)                                # Print updated list

motorcycles = []                                  # Start with an empty list
motorcycles.append('honda')                       # Add 'honda' to the list
motorcycles.append('yamaha')                      # Add 'yamaha' to the list
motorcycles.append('suzuki')                      # Add 'suzuki' to the list
print(motorcycles)                                # Print the final list

motorcycles = ['honda', 'yamaha', 'suzuki']       # Start with a fresh list
motorcycles.insert(0, 'ducati')                   # Insert 'ducati' at the beginning
print(motorcycles)                                # Print updated list

motorcycles = ['honda', 'yamaha', 'suzuki']       # Create a list again
print(motorcycles)                                # Show original list
del motorcycles[0]                                # Delete the first item
print(motorcycles)                                # Show updated list

motorcycles = ['honda', 'yamaha', 'suzuki']       # Reset the list
print(motorcycles)                                # Show list
del motorcycles[1]                                # Delete the second item
print(motorcycles)                                # Show updated list

motorcycles = ['honda', 'yamaha', 'suzuki']       # Create a list again
print(motorcycles)                                # Show original list
popped_motorcycle = motorcycles.pop()             # Remove and store the last item
print(motorcycles)                                # Show updated list
print(popped_motorcycle)                          # Show the item that was removed

motorcycles = ['honda', 'yamaha', 'suzuki']       # Create a new list
last_owned = motorcycles.pop()                    # Pop the last item into a variable
print(f"The last motorcycle I owned was a {last_owned.title()}.")  # Print a message

motorcycles = ['honda', 'yamaha', 'suzuki']       # Create another list
first_owned = motorcycles.pop(0)                  # Pop the first item
print(f"The first motorcycle I owned was a {first_owned.title()}.")  # Show message

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']  # Create a list with 4 items
print(motorcycles)                                     # Show the list
too_expensive = 'ducati'                               # Set a variable for item to remove
motorcycles.remove(too_expensive)                      # Remove 'ducati' by value
print(motorcycles)                                     # Show updated list
print(f"\nA {too_expensive.title()} is too expensive for me.")  # Print message


