# Dictionary of rivers and the countries they run through
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()  # blank line

# Print just the names of the rivers
for river in rivers.keys():
    print(river.title())

print()  # blank line

# Print just the countries
for country in rivers.values():
    print(country.title())
