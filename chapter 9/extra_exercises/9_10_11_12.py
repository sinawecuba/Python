# -------------------------------
# Module: user_module.py
# Contains User class
# -------------------------------

class User:
    """A simple user class."""
    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.info = kwargs

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        for key, value in self.info.items():
            print(f"{key}: {value}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")


# -------------------------------
# Module: admin_module.py
# Contains Admin and Privileges classes
# -------------------------------

class Privileges:
    """Stores a list of admin privileges."""
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = ["can add post", "can delete post", "can ban user"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """Represents an admin user."""
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.privileges = Privileges()


# -------------------------------
# Example usage: exercises 9-10 to 9-12
# -------------------------------

# 9-10: Imported Restaurant example
# (assuming Restaurant class is in restaurant_module.py)
# from restaurant_module import Restaurant
# my_restaurant = Restaurant("Sunshine Diner", "American")
# my_restaurant.describe_restaurant()

# 9-11: Imported Admin from admin_module.py
# from admin_module import Admin
admin_user = Admin("Alice", "Johnson")
admin_user.privileges.show_privileges()

# 9-12: Multiple modules
# from user_module import User
# from admin_module import Admin, Privileges
admin2 = Admin("Bob", "Smith")
admin2.privileges.show_privileges()
