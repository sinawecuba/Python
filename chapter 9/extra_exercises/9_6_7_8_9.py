# 9-6. Ice Cream Stand (inherits from Restaurant)
class IceCreamStand(Restaurant):
    """Represent an ice cream stand, a special kind of restaurant."""
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """Display a list of available ice cream flavors."""
        print(f"{self.restaurant_name} offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Instance for 9-6
ice_cream_stand = IceCreamStand("Cool Cones")
ice_cream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint"]
ice_cream_stand.display_flavors()


# 9-7 & 9-8. Admin and Privileges classes
class Privileges:
    """Represent privileges for an admin user."""
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges of the admin."""
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Represent an admin user."""
    def __init__(self, first_name, last_name, **additional_info):
        super().__init__(first_name, last_name, **additional_info)
        self.privileges = Privileges()


# Instance for 9-7/9-8
admin_user = Admin("Bob", "Smith")
admin_user.describe_user()
admin_user.privileges.show_privileges()


# 9-9. Battery Upgrade (extends ElectricCar/Battery classes)
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery to 65 kWh if it isn't already."""
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already upgraded.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# Instance for 9-9
my_leaf = ElectricCar("Nissan", "Leaf", 2024)
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
