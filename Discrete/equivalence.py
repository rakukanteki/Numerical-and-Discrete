import sympy

p, q = sympy.symbols("p, q")

exp1 = ~(p & q)
exp2 = ~p | ~q

equivalent = sympy.simplify_logic(exp1) ==  sympy.simplify_logic(exp1)

if equivalent:
    print("The expressions are logically equivalent..")
else:
    print("The expressions are not logically equivalent..")
    
