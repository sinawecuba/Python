# 6-10. Favorite Numbers
favorite_numbers = {
    'Alice': [7, 42],
    'Bob': [3, 9, 27],
    'Cathy': [11]
}

for person, numbers in favorite_numbers.items():
    numbers_str = ", ".join(str(num) for num in numbers)
    print(f"{person}'s favorite numbers are: {numbers_str}")

print("\n" + "="*40 + "\n")

# 6-11. Cities
cities = {
    'Paris': {'country': 'France', 'population': 2148327, 'fact': 'Known as the City of Light'},
    'Tokyo': {'country': 'Japan', 'population': 13929286, 'fact': 'Largest metropolitan area in the world'},
    'Cape Town': {'country': 'South Africa', 'population': 433688, 'fact': 'Famous for Table Mountain'}
}

for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f"\tCountry: {info['country']}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact']}")

print("\n" + "="*40 + "\n")

# 6-12. Extensions (Extended People)
person1 = {'first_name': 'John', 'last_name': 'Doe', 'age': 28, 'city': 'New York',
           'occupation': 'Engineer', 'hobbies': ['cycling', 'painting']}
person2 = {'first_name': 'Jane', 'last_name': 'Smith', 'age': 34, 'city': 'London',
           'occupation': 'Doctor', 'hobbies': ['reading', 'swimming']}
person3 = {'first_name': 'Ali', 'last_name': 'Khan', 'age': 22, 'city': 'Cape Town',
           'occupation': 'Student', 'hobbies': ['gaming', 'soccer']}

people = [person1, person2, person3]

for person in people:
    print(f"{person['first_name']} {person['last_name']}, Age: {person['age']}, City: {person['city']}")
    print(f"\tOccupation: {person['occupation']}")
    print(f"\tHobbies: {', '.join(person['hobbies'])}")
