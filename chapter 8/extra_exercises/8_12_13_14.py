# 8-12. Sandwiches
def make_sandwich(*items):
    """Print a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

# Call the function three times with different numbers of items
make_sandwich('ham', 'cheese', 'lettuce')
make_sandwich('turkey', 'tomato')
make_sandwich('peanut butter', 'jelly', 'banana', 'honey')


# 8-13. User Profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Example profile
my_profile = build_profile(
    'Sinawe', 'Cuba',
    location='South Africa',
    profession='Developer',
    hobbies=['reading', 'coding', 'gaming']
)

print("\nUser Profile:")
for key, value in my_profile.items():
    print(f"{key}: {value}")


# 8-14. Cars
def make_car(manufacturer, model, **options):
    """Return a dictionary representing a car with arbitrary info."""
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    for key, value in options.items():
        car_info[key] = value
    return car_info

# Example car
my_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print("\nCar Information:")
for key, value in my_car.items():
    print(f"{key}: {value}")
