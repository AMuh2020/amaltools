
def quadratic(a,b,c,round_to=3,output_form=1):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return "Enter numbers"
    
    discriminat = b**2 - 4*a*c
    print(discriminat)
    if discriminat < 0:
        return "","", "no real roots"
    
    ans1 = (-b + (discriminat**0.5))/(2*a)
    ans2 = (-b - (discriminat**0.5))/(2*a)
    print(ans1,ans2)
    ans1 = round(ans1, round_to)
    ans2 = round(ans2, round_to)
    #create other forms, mixed etc
    #return f"x={ans1}", f"x={ans2}"
    if output_form == 1:
        return ans1,ans2, None
    elif output_form == 2:
        return f"x={ans1}", f"x={ans2}", f"(-{b} + sqrt({discriminat}))/{2*a}"
