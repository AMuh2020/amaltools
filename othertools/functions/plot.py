import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io
import base64

matplotlib.use('Agg')

def plot_graph(data, plot_type="line", grid_lines=False,title=""):
    print("here")
    # reads the csv fil into a pandas dataframe
    df = pd.read_csv(data)
    
    if df.shape[1] < 2:
        raise ValueError("Data must have at least two columns")

    fig, ax = plt.subplots()
    print(df.iloc[:, 0],"/n",df.iloc[:, 1])

    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    
    if plot_type == "line":
        # plot line graph with x and y axis
        ax.plot(x, y)
        
    elif plot_type == "scatter":
        # plot scatter graph with x and y axis
        ax.scatter(x, y)
        m, b = np.polyfit(x, y, 1)
        ax.plot(x, m*x + b, color='red')
    elif plot_type == "bar":
        # plot bar graph with x and y axis
        
        ax.bar(x, y)
    elif plot_type == "hist":
        ax.hist(y)  # Histogram only needs one variable
    else:
        raise ValueError(f"Invalid plot type: {plot_type}. Must be one of 'line', 'scatter', 'bar', or 'hist'")
    ax.set(xlabel=df.columns[0], ylabel=df.columns[1])
    ax.set_title(title)

    if grid_lines:
        ax.grid()

    # ax.set_xlim(left=0)
    # ax.set_ylim(bottom=0)
    # # return the image as bytes to be displayed on the frontend
    # buf = io.BytesIO()
    # fig.savefig(buf, format='png')
    # buf.seek(0)
    # string = base64.b64encode(buf.read()).decode('utf-8')
    # # print(string)
    # return string

    # save the image to a file
    fig.savefig('tempGraph/plot.png')
    return 'tempGraph/plot.png'

    
    
    # add other graph types
# plot_graph(open('data.csv','rb'), plot_type="scatter", grid_lines=False,title="test vs test2")