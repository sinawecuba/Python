# 3-8. Seeing the World

places = ['Japan', 'Iceland', 'Egypt', 'New Zealand', 'Brazil']
print("Original list:")
print(places)

print("\nAlphabetical order (temporary):")
print(sorted(places))  # Sorted alphabetically

print("\nOriginal list after sorted():")
print(places)

print("\nReverse alphabetical order (temporary):")
print(sorted(places, reverse=True))

print("\nOriginal list still unchanged:")
print(places)

print("\nList reversed with reverse():")
places.reverse()
print(places)

print("\nReversed back to original order:")
places.reverse()
print(places)

print("\nList sorted permanently (alphabetical):")
places.sort()
print(places)

print("\nList sorted permanently (reverse alphabetical):")
places.sort(reverse=True)
print(places)


# 3-9. Dinner Guests (from earlier guest list program)
guests = ['Maya Angelou', 'Barack Obama']
print(f"\nI am inviting {len(guests)} people to dinner.")


# 3-10. Every Function
languages = ['Zulu', 'Spanish', 'Mandarin', 'Swahili', 'French']

print("\nOriginal list of languages:")
print(languages)

# Accessing elements
print("\nFirst language:", languages[0])
print("Last language:", languages[-1])

# Adding items
languages.append('German')  # Add to end
languages.insert(2, 'Arabic')  # Add at index 2

print("\nList after adding two languages:")
print(languages)

# Removing items
del languages[1]  # Remove by index
popped_lang = languages.pop()  # Remove last
languages.remove('Arabic')  # Remove by value

print("\nList after deletions:")
print(languages)
print("Popped language:", popped_lang)

# Sorting
print("\nTemporarily sorted list:")
print(sorted(languages))

print("Original list after sorted():")
print(languages)

languages.sort()
print("\nPermanently sorted list:")
print(languages)

languages.reverse()
print("List reversed:")
print(languages)

# Length of the list
print(f"\nNumber of languages in list: {len(languages)}")
