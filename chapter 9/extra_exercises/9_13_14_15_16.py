import random

# -------------------------------
# 9-13: Dice
# -------------------------------
class Die:
    """A simple die with a configurable number of sides."""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of sides."""
        return random.randint(1, self.sides)

# Roll a 6-sided die 10 times
six_sided = Die()
print("6-sided die rolls:")
for _ in range(10):
    print(six_sided.roll_die(), end=' ')
print("\n")

# Roll a 10-sided die 10 times
ten_sided = Die(10)
print("10-sided die rolls:")
for _ in range(10):
    print(ten_sided.roll_die(), end=' ')
print("\n")

# Roll a 20-sided die 10 times
twenty_sided = Die(20)
print("20-sided die rolls:")
for _ in range(10):
    print(twenty_sided.roll_die(), end=' ')
print("\n")

# -------------------------------
# 9-14: Lottery
# -------------------------------
lottery_numbers = list(range(10)) + ['A', 'B', 'C', 'D', 'E']
winning_ticket = random.sample(lottery_numbers, 4)
print(f"Winning lottery numbers/letters: {winning_ticket}")

# -------------------------------
# 9-15: Lottery Analysis
# -------------------------------
my_ticket = random.sample(lottery_numbers, 4)
attempts = 0

while True:
    attempts += 1
    draw = random.sample(lottery_numbers, 4)
    if draw == my_ticket:
        break

print(f"My ticket {my_ticket} won after {attempts} attempts!")

# -------------------------------
# 9-16: Python Module of the Week
# -------------------------------
# Visit https://pymotw.com/ to explore standard library modules.
# Example: random module used above. You can explore others like math, os, datetime, etc.
