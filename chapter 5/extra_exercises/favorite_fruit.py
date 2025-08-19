# ----- 5-3: Alien Colors #1 -----

# Version that passes the if test
alien_color = 'green'
if alien_color == 'green':
    print("5-3 PASS: Player just earned 5 points!")

# Version that fails the if test (no output expected)
alien_color = 'red'
if alien_color == 'green':
    print("5-3 FAIL: Player just earned 5 points!")  # This won't print


# ----- 5-4: Alien Colors #2 -----

# Version where if block runs
alien_color = 'green'
if alien_color == 'green':
    print("5-4 IF: Player just earned 5 points for shooting the alien.")
else:
    print("5-4 ELSE: Player just earned 10 points.")

# Version where else block runs
alien_color = 'yellow'
if alien_color == 'green':
    print("5-4 IF: Player just earned 5 points for shooting the alien.")
else:
    print("5-4 ELSE: Player just earned 10 points.")


# ----- 5-5: Alien Colors #3 -----

# Version for green alien
alien_color = 'green'
if alien_color == 'green':
    print("5-5 GREEN: Player earned 5 points.")
elif alien_color == 'yellow':
    print("5-5 GREEN: Player earned 10 points.")
else:
    print("5-5 GREEN: Player earned 15 points.")

# Version for yellow alien
alien_color = 'yellow'
if alien_color == 'green':
    print("5-5 YELLOW: Player earned 5 points.")
elif alien_color == 'yellow':
    print("5-5 YELLOW: Player earned 10 points.")
else:
    print("5-5 YELLOW: Player earned 15 points.")

# Version for red alien
alien_color = 'red'
if alien_color == 'green':
    print("5-5 RED: Player earned 5 points.")
elif alien_color == 'yellow':
    print("5-5 RED: Player earned 10 points.")
else:
    print("5-5 RED: Player earned 15 points.")
