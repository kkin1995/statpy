import numpy as np
import matplotlib.pyplot as plt

def interpolate(x,y,x0):
    """ 
    Takes in 3 inputs, two lists for x and y and 1 integer value for interpolation.
    Returns two values. One is the value given for interpolation and the other is the interpolated value.

    Uses the method of Linear Interpolation.

    """

    i = 0
    start = time.time()
    while x[i]<=x0:
        i=i+1

    slope = (y[i] - y[i-1])/(x[i] - x[i-1])
    y0 = (slope*(x0 - x[i-1])) + y[i-1]

    end = time.time()

    print("Previous Data Point = ",x[i-1])
    print("Next Data Point = ",x[i])
    print("Time taken to interpolate 1 point", end - start)
    return x0,y0

def interpolate_list(x,y,x0):
    """
    Works the same as interpolate() but will take a list of points for interpolation.

    Uses the method of Linear Interpolation.

    """
    j = 0
    plt.plot(x,y)
    lengthUnknowns = len(x0)
    y0 = []
    slope = []
    print(x,y)
    for i in range(lengthUnknowns):
        while x[j] <= x0[i]:
            j = j+1
        print(j)
        print(x[j],y[j])
        s = (y[j] - y[j-1])/(x[j] - x[j-1])
        slope.append(s)
        y0.append((slope[i]*(x[j] - x[j-1])) + y[j-1])
        print(slope)
        print(x0,y0)
        plt.plot(x0[i],y0[i],"r*") 
    plt.show()
    return x0,y0

def lagrangeInterpolate(x,y,x0):
    """
    Uses the method of Lagrange Interpolation. Takes in 3 inputs. 
    x: input as a list
    y: input as a list
    x0: point to be interpolated

    Returns the interpolated value y0 and the value x0
    """
    k = len(x)
    ya = []
    for j in range(k):
        L = 1
        for m in range(k):
            if j != m:
                L = L * ((x0 - x[m])/(x[j] - x[m]))
        ya.append(y[j] * L)
    y0 = sum(ya)
    return x0,y0

def lagrangeInterpolateList(x,y,x0):
    """
    Uses the method of Lagrange Interpolation. Takes in 3 inputs.
    x: input as a list
    y: input as a list
    x0: points to be interpolated as a lists

    """
    k = len(x)
    y0 = []
    for i in range(len(x0)):
        ya = []
        for j in range(k):
            L = 1
            for m in range(k):
                if j != m:
                    L = L * ((x0[i] - x[m])/(x[j] - x[m]))
            ya.append(y[j] * L)
        y0.append(sum(ya))
    return x0,y0

