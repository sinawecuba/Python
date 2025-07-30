# 2-3. Personal Message
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")

print("\n" + "-"*40 + "\n")  # separator

# 2-4. Name Cases
name = "eric"
print(name.lower())   # lowercase
print(name.upper())   # UPPERCASE
print(name.title())   # Title Case

print("\n" + "-"*40 + "\n")

# 2-5. Famous Quote
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

print("\n" + "-"*40 + "\n")

# 2-6. Famous Quote 2
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)

print("\n" + "-"*40 + "\n")

# 2-7. Stripping Names
name = "\t\n Eric \n\t"
print("Original with whitespace:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())

print("\n" + "-"*40 + "\n")

# 2-8. File Extensions
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))  # removes the .txt extension
