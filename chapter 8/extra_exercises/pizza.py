# 1. Import the module
import pizza_functions
pizza_functions.make_pizza(16, 'pepperoni')

# 2. Import the function directly
from pizza_functions import make_pizza
make_pizza(12, 'mushrooms', 'green peppers')

# 3. Import with alias
from pizza_functions import make_pizza as mp
mp(10, 'cheese', 'tomato')

# 4. Import module as alias
import pizza_functions as pf
pf.make_pizza(14, 'sausage', 'olives')

# 5. Import everything (not recommended for large modules)
from pizza_functions import *
make_pizza(18, 'bacon', 'onion')
