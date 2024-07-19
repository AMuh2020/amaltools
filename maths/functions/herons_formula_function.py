
def heron_formula(a,b,c):
    #https://www.britannica.com/science/Herons-formula
    #Idea create a way for user to choose rounding
    a = float(a)
    b = float(b)
    c = float(c)
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return round(area, 3)