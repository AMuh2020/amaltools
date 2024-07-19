import re
from sympy import sympify, N, latex

# Function to evaluate a mathematical formula
def clean(formula):
    # Allow digits, arithmetic operators, parentheses, sin, cos, tan, pi, e, sqrt, log, ln, abs
    cleaned_formula = re.sub(r"[^0-9a-z+\-*/()^sincostanπe pi sqrt log ln abs.]", "", formula)
    return sympify(cleaned_formula)

def calculate(formula):
    # Evaluate the formula
    ans = clean(formula)
    print(ans, type(ans))

    # evaluate the answer
    numerical_ans = ans.evalf()

    # Convert the answer to a string
    ans_str = str(numerical_ans)
    # Remove trailing zeros and the decimal point if it is the last character
    ans_str = ans_str.rstrip('0').rstrip('.') if '.' in ans_str else ans_str
    
    print(ans_str, type(ans_str))
    ans = latex(ans)
    # print(ans_str, type(ans_str))
    return {'numerical':ans_str, 'exact':ans}

# test the function
# ans = calculate("x^2 + 2*x + 1")
# print(ans)
