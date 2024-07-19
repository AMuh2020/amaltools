from sympy import sympify, latex, integrate, Symbol, SympifyError
import re

# Function to evaluate a mathematical formula
def clean(formula):
    # Allow digits, arithmetic operators, parentheses, sin, cos, tan, pi, e, sqrt, log, ln, abs
    # cleaned_formula = re.sub(r"[^0-9a-z+\-*/()^sincostanπe pi sqrt log ln abs.]", "", formula)
    # cleaned_formula = re.sub(r"[^0-9a-z+\-*/()^sincostancotseccsctanhasinhcoshcothsechcschasinacosatanacotacscacseceπiexploglnabs.!γsqrtrootpij ]", "", formula)
    return sympify(formula)
    

def definiteIntegration(formula, lower, upper):
    # Evaluate the formula
    print(formula)
    ans = clean(formula)
    x = Symbol('x')
    ans = integrate(ans, (x, lower, upper))
    exact_ans = latex(ans)
    float_ans = ans.evalf()
    return {'numerical':float_ans, 'exact':exact_ans}

def indefiniteIntegration(formula):
    # Evaluate the formula

    # print for debugging
    print(formula)

    # remove all characters that are not allowed
    ans = clean(formula)

    # print for debugging
    x = Symbol('x')
    ans = integrate(ans, x)
    print(ans)
    ans_final = latex(ans)
    return {'expression': ans_final,'type': 'indefinite'}

# Test the function
# ans = indefiniteIntegration("e^x")
# print(ans)
