def fibonacci_function(n,seperator=''):
    maximum_fibonacci = 999
    n = int(n)
    if n > maximum_fibonacci:
        n = maximum_fibonacci
    elif n == 0:
        return "enter valid input"

    fibonacci = ['0']
    o1 = 0
    o2 = 1
    store = 0
    for i in range(n-1):
        o1 = o2
        o2 = store
        store = o1 + o2
        fibonacci.append(str(store))
    #print(fibonacci)
    
    if seperator != " " or seperator != "":
        seperator = seperator + " "
    return f"{seperator}".join(fibonacci)
