# 8-3. T-Shirt
def make_shirt(size, message):
    """Print a summary of the shirt size and message."""
    print(f"The shirt is size {size} and has the message: '{message}'.")

# Call using positional arguments
make_shirt('M', 'Python is awesome!')

# Call using keyword arguments
make_shirt(size='L', message='Code every day!')

print("\n")

# 8-4. Large Shirts with defaults
def make_shirt_default(size='L', message='I love Python'):
    """Print a summary of the shirt size and message, with defaults."""
    print(f"The shirt is size {size} and has the message: '{message}'.")

# Default large shirt
make_shirt_default()

# Medium shirt with default message
make_shirt_default(size='M')

# Any size with a custom message
make_shirt_default(size='S', message='Hello World!')

print("\n")

# 8-5. Cities
def describe_city(city, country='Iceland'):
    """Print a statement about a city and its country."""
    print(f"{city} is in {country}.")

# Call for three different cities
describe_city('Reykjavik')          # Default country
describe_city('Paris', 'France')    # Specified country
describe_city('Tokyo', 'Japan')     # Specified country
