# Implementation of Numerical Methods to compute the area under a curve (integral) for given discrete points.
# Use trapezium() if data has EQUAL intervals
# Use generalTrapezium() if data has UNION intervals.

import numpy as np
import matplotlib.pyplot as plt

def trapezium(x,y):
	'''
	Calculates the approximate area under the curve for EQUAL intervals
	Takes x and y as (lists) arguments and returns the approximate area as a numerical value
	'''
	n = len(x)
	a = x[0]
	b = x[-1]
	h = (b-a)/(n-1)
	sumOfMiddleY = 0
	for i in range(1,n-1):
		sumOfMiddleY += y[i]
	area = (h/2)*(y[0] + y[-1] + 2*sumOfMiddleY)

	return area

def generalTrapezium(x,y):
	'''
	Calculates the area under the curve for UNEQUAL intervals
	Takes x and y as (lists) arguments and returns the approximate area as a numerical value
	'''
	n = len(x)
	area1 = 0
	for i in range(n-1):
		area1 += ((y[i] + y[i+1])/2) * (x[i+1] - x[i])

	return area1

# Implementations of Numerical Methods for solving Ordinary Differential Equations
# Currently implemented:
# 1. Euler's Method
# 2. Modified Euler's Method - Taking an average of the slope.

def fprime(x,y):
	'''
	Explicitly define the first order ODE function
	'''
	return

def euler(n,x0,xf,y0):
	'''
	Takes the following arguments:
	n: number of iterations
	x0: initial condition for x
	xf: Upper limit
	y0: Inital condition for y
	'''
	h = (xf-x0)/(n-1)
	x = []
	y = []
	while x0 <= xf:
		y0 += h*fprime(x0,y0)
		x0 += h
		x.append(x0)
		y.append(y0)
	return x,y

def modifiedEuler(n,x0,xf,y0):
	h = (xf - x0)/(n-1)
	x = []
	y = []
	x01 = x0
	y01 = y0
	while x0 <= xf:
		y01 += h*fprime(x01,y01)
		x01 += h
		y0 += (h/2)*(fprime(x0,y0) + fprime(x01,y01))
		x0 += h
		x.append(x0)
		y.append(y0)
	return x, y



class RK4:
    """
    Performs a single step of the Runge - Kutta 4th Order Method
    Parameters:
    step_size: 0.001 (default)
    Returns: An Instance of the RK4 Class
    """
    def __init__(self, step_size = 0.001):
        self.step_size = step_size

    def step(self, y):
        """
        Single Step of RK4. Must also define F(y) - Equation of the first derivative.
        Parameters:
        y: Integer. Pass in each value of the independent variable y
        """
        dy1 = self.step_size * F(y)
        dy2 = self.step_size * F(y + (dy1 / 2))
        dy3 = self.step_size * F(y + (dy2 / 2))
        dy4 = self.step_size * F(y + dy3)
        dy = (dy1 + 2*dy2 + 2*dy3 + dy4) / 6
        y = y + dy
        return y

if __name__ == "__main__":
    def F(x):
        return -2*x # dy/dx = -2x

    step_size = 0.01
    x = np.arange(start = 0, stop = 5, step = step_size)
    N = len(x)
    y = np.zeros(N)
    y[0] = 3 # Inital Condition
    rk4_instance = RK4(step_size)
    for i in range(1,N):
        y[i] = rk4_instance.step(y[i-1])
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()