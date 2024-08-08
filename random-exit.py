#!/usr/bin/env python3

"""Returns a random integer for sys.exit"""

import sys
import random

value=random.randint(0,3)
print("Returning: " + str(value))
sys.exit(value)
