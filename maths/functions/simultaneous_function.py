def simultaneous_equation(a1, b1, c1, a2, b2, c2):
    a1 = int(a1)
    b1 = int(b1)
    c1 = int(c1)
    a2 = int(a2)
    b2 = int(b2)
    c2 = int(c2)

    # a1x + b1y = c1
    # a2x + b2y = c2
    # 2x + y = 1
    # 3x + 4y = 5
    # x = -1/5
    # y = -7/5

    x_yequals = -a1/b1 
    constant_yequals = c1/b1

    constant_left_side = b2 * constant_yequals
    constant_right_side = c2 - constant_left_side
    x_second_equation = b2 * x_yequals + a2
    x = constant_right_side / x_second_equation
    
    y = c1 - (a1*x)
    return x, y

# print(simultaneous_equation(2, 1, 1, 3, 4, 5))