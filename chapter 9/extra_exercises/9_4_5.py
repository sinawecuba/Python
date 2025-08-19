# 9-4. Number Served (extended Restaurant class)
class Restaurant:
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # default value

    def describe_restaurant(self):
        """Print a summary of the restaurant."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, additional_customers):
        """Increment the number of customers served."""
        if additional_customers > 0:
            self.number_served += additional_customers
        else:
            print("Increment must be positive.")


# Instance for Exercise 9-4
restaurant = Restaurant("Pasta Palace", "Italian")
print(f"Number served: {restaurant.number_served}")
restaurant.number_served = 50
print(f"Number served after direct change: {restaurant.number_served}")
restaurant.set_number_served(75)
print(f"Number served after set_number_served(): {restaurant.number_served}")
restaurant.increment_number_served(25)
print(f"Number served after increment_number_served(): {restaurant.number_served}")


# 9-5. Login Attempts (extended User class)
class User:
    """A simple attempt to model a user."""
    def __init__(self, first_name, last_name, **additional_info):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.additional_info = additional_info
        self.login_attempts = 0  # default value

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}")
        for key, value in self.additional_info.items():
            print(f"{key.title()}: {value}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}!\n")

    def increment_login_attempts(self):
        """Increment the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0


# Instance for Exercise 9-5
user = User("Alice", "Johnson", age=30, location="New York")
print(f"Login attempts initially: {user.login_attempts}")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts after incrementing: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts after resetting: {user.login_attempts}")
