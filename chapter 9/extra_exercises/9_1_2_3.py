# 9-1. Restaurant
class Restaurant:
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a summary of the restaurant."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

# Instance for Exercise 9-1
restaurant = Restaurant("Pasta Palace", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2. Three Restaurants
restaurant1 = Restaurant("Burger Barn", "American")
restaurant2 = Restaurant("Sushi Spot", "Japanese")
restaurant3 = Restaurant("Curry Corner", "Indian")

for r in [restaurant1, restaurant2, restaurant3]:
    r.describe_restaurant()
    print()


# 9-3. Users
class User:
    """A simple attempt to model a user."""
    def __init__(self, first_name, last_name, **additional_info):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.additional_info = additional_info

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}")
        for key, value in self.additional_info.items():
            print(f"{key.title()}: {value}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}!\n")

# Instances for Exercise 9-3
user1 = User("Alice", "Johnson", age=30, location="New York")
user2 = User("Bob", "Smith", age=25, location="Los Angeles")
user3 = User("Charlie", "Brown", age=40, location="Chicago")

for user in [user1, user2, user3]:
    user.describe_user()
    user.greet_user()
