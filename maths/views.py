from django.shortcuts import render
from .functions import calculator_function, integral_function, line_equation_function, herons_formula_function, midpoint_function, fibonacciFunction,suvat_function,quadratic_function, simultaneous_function, derivative_function
# Potential bottle neck is image generation/storing.... FIXED SERIALIZING MAKES THINGS MUCH EASIER
def straight_line(request):
    # library_reference = {
    #     "name": "matplotlib",
    #     "link": "",
    # }
    if request.method == "POST":
        point1 = [request.POST["x1"],request.POST["y1"]]
        point2 = [request.POST["x2"],request.POST["y2"]]
        equation, graph = line_equation_function.line_equation(point1,point2)
        print(equation)
        return render(request, "maths/y=mx+c.html",{"equation":equation,"graph":graph,"point1":point1,"point2":point2})
    else:
        return render(request, "maths/y=mx+c.html")
        #Make a default where x1=0 y1=0 x2=2 y2=5 (giving y=2x+1)

def herons_formula_view(request):
    if request.method == "POST":
        a = request.POST["a"]
        b = request.POST["b"]
        c = request.POST["c"]
        result = herons_formula_function.heron_formula(a,b,c)
        return render(request, "maths/herons_formula.html",{"result":result,"a":a,"b":b,"c":c})
    else:
        return render(request, "maths/herons_formula.html")

def mid_point_view(request):
    library_reference = {
        "name": "matplotlib",
        "link": "https://matplotlib.org/",
    }
    if request.method == "POST":
        point1 = [request.POST["x1"],request.POST["y1"]]
        point2 = [request.POST["x2"],request.POST["y2"]]
        midpoint, graph = midpoint_function.midpoint(point1,point2)
        
        return render(request, "maths/midpoint.html",{"midpoint":midpoint,"graph":graph,"point1":point1,"point2":point2,"library_reference":library_reference})
    else:
        return render(request, "maths/midpoint.html",{"library_reference":library_reference})

def fibonacci_sequence(request):
    if request.method == 'POST':
        n_terms = request.POST['number_of_terms']
        seperator = request.POST['seperator']
        print(seperator)
        fibonacci_seq = fibonacciFunction.fibonacci_function(n_terms,seperator)
        return render(request,'maths/fibonacci_sequence.html', {"fibonacci_sequence":fibonacci_seq,"input":n_terms})
    else:
        return render(request, 'maths/fibonacci_sequence.html')

def suvat(request):
    if request.method == 'POST':

        try:
            s = request.POST['s']
        except:
            s = None
        
        try:
            u = request.POST['u']
        except:
            u = None
        
        try:
            v = request.POST['v']
        except:
            v = None
        
        try:
            a = request.POST['a']
        except:
            a = None
        
        try:
            t = request.POST['t']
        except:
            t = None
        
        solve_for = request.POST['solve_for']
        remove = request.POST['remove']
        answer = suvat_function.suvat(s,u,v,a,t,solve_for,remove)
        return render(request,'maths/suvat_2point0.html',{"answer":answer,"s_in":s,"u_in":u,"v_in":v,"a_in":a,"t_in":t})
    else:
        return render(request,'maths/suvat_2point0.html')
    

def quadratic(request):
    if request.method == "POST":
        a = request.POST["a"]
        b = request.POST["b"]
        c = request.POST["c"]
        result = quadratic_function.quadratic(a,b,c)
        print(result)
        x1, x2, err_msg = result
        return render(request, "maths/quadratic.html",{"result":result,"x1":x1,"x2":x2,"a":a,"b":b,"c":c,"err_msg":err_msg})
    else:
        return render(request, "maths/quadratic.html")

def simultaneous(request):
    if request.method == "POST":
        a1 = request.POST["a1"]
        b1 = request.POST["b1"]
        c1 = request.POST["c1"]
        a2 = request.POST["a2"]
        b2 = request.POST["b2"]
        c2 = request.POST["c2"]
        x,y = simultaneous_function.simultaneous_equation(a1, b1, c1, a2, b2, c2)
        return render(request, "maths/simultaneous.html",{"x":x,"y":y,"a1":a1,"b1":b1,"c1":c1,"a2":a2,"b2":b2,"c2":c2})
    else:
        return render(request, "maths/simultaneous.html")

def calculator(request):
    library_reference = {
        "name": "sympy",
        "link": "https://www.sympy.org/en/index.html",
    }
    if request.method == "POST":
        expression = request.POST["expression"]
        try:
            result = calculator_function.calculate(expression)
        except:
            return render(request, "maths/calculator.html",{"expression":expression,"library_reference":library_reference, "error_msg":"Invalid expression. Please try again."})
        return render(request, "maths/calculator.html",{"result":result,"expression":expression,"library_reference":library_reference})
    else:
        return render(request, "maths/calculator.html",{"library_reference":library_reference})

def integralCalculator(request):
    library_reference = {
        "name": "sympy",
        "link": "https://www.sympy.org/en/index.html",
    }
    if request.method == "POST":
        expression = request.POST["expression"]
        type_integration = request.POST["integralType"]

        # error handling
        try:
            if type_integration == "indefinite":
                result = integral_function.indefiniteIntegration(expression)
                print(result)
            elif type_integration == "definite":
                result = integral_function.definiteIntegration(expression, request.POST["lower_bound"], request.POST["upper_bound"])
                print(result)
        except:
            return render(request, "maths/integral_calculator.html",{"expression":expression,"type_integration":type_integration,
                                                                 "lower_bound":request.POST["lower_bound"],"upper_bound":request.POST["upper_bound"],
                                                                 "library_reference":library_reference, "error_msg":"Invalid expression. Please try again."})

        return render(request, "maths/integral_calculator.html",{"result":result,"expression":expression,"type_integration":type_integration,
                                                                 "lower_bound":request.POST["lower_bound"],"upper_bound":request.POST["upper_bound"],
                                                                 "library_reference":library_reference})
    else:
        return render(request, "maths/integral_calculator.html",{"library_reference":library_reference})

def derivativeCalculator(request):
    library_reference = {
        "name": "sympy",
        "link": "https://www.sympy.org/en/index.html",
    }
    if request.method == "POST":
        expression = request.POST["expression"]
        try:
            result = derivative_function.differentiation(expression)
        except:
            return render(request, "maths/derivative_calculator.html",{"expression":expression,"library_reference":library_reference, "error_msg":"Invalid expression. Please try again."})
        print(result)
        return render(request, "maths/derivative_calculator.html",{"result":result,"expression":expression,"library_reference":library_reference})
    else:
        return render(request, "maths/derivative_calculator.html",{"library_reference":library_reference})