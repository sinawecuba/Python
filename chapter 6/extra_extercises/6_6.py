# Dictionary of favorite languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

# List of people who should take the poll
people_to_poll = ['jen', 'john', 'sarah', 'maria', 'edward', 'david']

# Loop through the list
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, please take our favorite languages poll!")
