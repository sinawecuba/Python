# 6-7. People
person1 = {'first_name': 'John', 'last_name': 'Doe', 'age': 28, 'city': 'New York'}
person2 = {'first_name': 'Jane', 'last_name': 'Smith', 'age': 34, 'city': 'London'}
person3 = {'first_name': 'Ali', 'last_name': 'Khan', 'age': 22, 'city': 'Cape Town'}

people = [person1, person2, person3]

for person in people:
    print(f"{person['first_name']} {person['last_name']}, Age: {person['age']}, City: {person['city']}")

print("\n" + "="*40 + "\n")

# 6-8. Pets
pet1 = {'type': 'dog', 'owner': 'Alice'}
pet2 = {'type': 'cat', 'owner': 'Bob'}
pet3 = {'type': 'parrot', 'owner': 'Cathy'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"{pet['owner']}'s pet is a {pet['type']}.")

print("\n" + "="*40 + "\n")

# 6-9. Favorite Places
favorite_places = {
    'Alice': ['Paris', 'Tokyo'],
    'Bob': ['New York'],
    'Cathy': ['Sydney', 'Rio de Janeiro', 'London']
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"\t- {place}")
