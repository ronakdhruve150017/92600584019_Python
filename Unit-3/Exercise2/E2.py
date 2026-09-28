# 1. Import complete module
import mymodule2
print("Addition:", mymodule2.add(10, 5))

# 2. Import specific function
from mymodule2 import sub
print("Subtraction:", sub(10, 5))

# 3. Import module with alias
import mymodule2 as m
print("Value of X:", m.x)
