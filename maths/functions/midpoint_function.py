import matplotlib
import matplotlib.pyplot as plt
#https://stackoverflow.com/questions/27147300/matplotlib-tcl-asyncdelete-async-handler-deleted-by-the-wrong-thread
matplotlib.use('Agg')
from io import StringIO
def midpoint(point1,point2):
    
    point1 = [float(point1[0]),float(point1[1])]
    point2 = [float(point2[0]),float(point2[1])]

    #Math for midpoint
    midpoint = [(point1[0]+point2[0])/2,(point1[1]+point2[1])/2]
    if midpoint[0].is_integer():
        midpoint[0] = int(midpoint[0])

    if midpoint[1].is_integer():
        midpoint[1] = int(midpoint[1])

    x_values = [point1[0],point2[0]]
    y_values = [point1[1],point2[1]]
    fig = plt.figure()
    plt.plot(x_values,y_values)
    plt.annotate(f"({point1[0]},{point1[1]})", (point1[0],point1[1]))
    plt.annotate(f"({point2[0]},{point2[1]})", (point2[0],point2[1]))
    plt.annotate(f"({midpoint[0]},{midpoint[1]})", (midpoint[0],midpoint[1]))
    plt.grid()
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)
    graph_data = imgdata.getvalue()
    plt.close("all")
    return midpoint, graph_data