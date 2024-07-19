import matplotlib
import matplotlib.pyplot as plt
#https://stackoverflow.com/questions/27147300/matplotlib-tcl-asyncdelete-async-handler-deleted-by-the-wrong-thread
matplotlib.use('Agg')
from io import StringIO
def line_equation(point1,point2):
    #x,y
    point1 = [float(point1[0]), float(point1[1])]
    point2 = [float(point2[0]), float(point2[1])]
    #add a default round_by value
    round_by = 2
    try:
        m = (point2[1]-point1[1])/(point2[0]-point1[0])
    except ZeroDivisionError:
        print("cant divide by 0")
        return "cant divide by 0", None
    c = point1[1]-(m*point1[0])
    #list is used for m and c to perserve accurate value, accurate value and rounded value are bundled together
    #aesthstic
    if m.is_integer():
        #original, int
        m = [m,int(m)]
    else:
        if round_by > 0:
            #print("round")
            m = [m,round(m,round_by)]
    
    if c.is_integer():
        c = [c,int(c)]
    else:    
        if round_by > 0:
            #print("round")
            c = [c,round(c,round_by)]
    
    if c[0] >= 0:
        equation = f"y={m[1]}x+{c[1]}"
    else:
        equation = f"y={m[1]}x-{-c[1]}"
    
    #print(equation)

    max_x_value = int(round(max([point1[0],point2[0]]) + 2,1))
    min_x_value = int(round(min([point1[0],point2[0]]) - 2,1))
    #step = int((max_x_value-min_x_value) /10)

    #Is all this even needed??
    x_values = [point1[0],point2[0]]
    y_values = [round(m[0]*i+c[0], 3) for i in x_values]
    
    #USED
    #https://www.youtube.com/watch?v=H0OU9rD9Jjk
    #https://matplotlib.org/3.5.3/api/index.html
    fig = plt.figure()
    plt.plot(x_values,y_values)
    plt.title(equation)
    #limits the graph to minimum y value line
    min_y_value = int(round(min([point1[1],point2[1]]) - 2,1))
    if min_y_value > 0:
        plt.ylim(ymin=0)
    if min_x_value > 0:
        plt.xlim(xmin=0)

    #plt.axvline(x=0, c="black", label="x=0")
    #plt.axhline(y=0, c="black", label="y=0")

    #labels the X and Y axis
    plt.xlabel('x')
    plt.ylabel('y')
    #puts the coordinates of the points inputted
    plt.annotate(f"({point1[0]},{point1[1]})", (point1[0],point1[1]))
    plt.annotate(f"({point2[0]},{point2[1]})", (point2[0],point2[1]))
    plt.grid()
    
    
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    data = imgdata.getvalue()
    plt.close()
    return equation, data

#wait what about y=c case or x=value case?
