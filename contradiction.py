# Importing Libraries
import sympy
from itertools import product
# itertools.product:
# To generate all possible combinations of truth values for given symbols.
from sympy.logic.boolalg import truth_table
# A function in SymPy to generate truth tables.
from sympy.abc import x, y
# A module in SymPy providing predefined symbols like x and y.

p, q = sympy.symbols("p q")

# Logical Expression
exp = ~(p | ~p)
table = truth_table(exp, [p, q])

contradiction = True
# Checking
for t in table:
    # Printing truth table
    print("{0} -> {1}".format(*t))
    if t[1]:
        contradiction = False
        break


if contradiction:
    print("The statement is Contradiction")
else:
    print("The statement is not Contradiction")