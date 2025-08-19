car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # False

color = 'blue'

print("\nIs color == 'blue'? I predict True.")
print(color == 'blue')  # True

print("\nIs color != 'red'? I predict True.")
print(color != 'red')  # True

print("\nIs color == 'green'? I predict False.")
print(color == 'green')  # False

age = 20

print("\nIs age > 18? I predict True.")
print(age > 18)  # True

print("\nIs age < 18? I predict False.")
print(age < 18)  # False

print("\nIs age == 20? I predict True.")
print(age == 20)  # True

print("\nIs age != 20? I predict False.")
print(age != 20)  # False

print("\nIs age == 25? I predict False.")
print(age == 25)  # False


# Equality and inequality with strings
fruit = 'Apple'
print("\nIs fruit == 'Apple'? I predict True.")
print(fruit == 'Apple')  # True

print("\nIs fruit != 'Banana'? I predict True.")
print(fruit != 'Banana')  # True

print("\nIs fruit == 'apple'? I predict False.")
print(fruit == 'apple')  # False

# Tests using the lower() method
print("\nIs fruit.lower() == 'apple'? I predict True.")
print(fruit.lower() == 'apple')  # True

print("\nIs fruit.lower() == 'banana'? I predict False.")
print(fruit.lower() == 'banana')  # False

# Numerical tests
number = 42
print("\nIs number == 42? I predict True.")
print(number == 42)  # True

print("\nIs number != 100? I predict True.")
print(number != 100)  # True

print("\nIs number > 10? I predict True.")
print(number > 10)  # True

print("\nIs number < 10? I predict False.")
print(number < 10)  # False

print("\nIs number >= 42? I predict True.")
print(number >= 42)  # True

print("\nIs number <= 41? I predict False.")
print(number <= 41)  # False

# Tests using and / or
print("\nIs number > 10 and number < 50? I predict True.")
print(number > 10 and number < 50)  # True

print("\nIs number > 10 and number < 40? I predict False.")
print(number > 10 and number < 40)  # False

print("\nIs number == 42 or number == 0? I predict True.")
print(number == 42 or number == 0)  # True

print("\nIs number == 100 or number == 0? I predict False.")
print(number == 100 or number == 0)  # False

# Test whether item is in a list
items = ['apple', 'banana', 'cherry']

print("\nIs 'banana' in items? I predict True.")
print('banana' in items)  # True

print("\nIs 'grape' in items? I predict False.")
print('grape' in items)  # False

# Test whether item is not in a list
print("\nIs 'grape' not in items? I predict True.")
print('grape' not in items)  # True

print("\nIs 'apple' not in items? I predict False.")
print('apple' not in items)  # False
