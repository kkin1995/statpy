# Implementations of Numerical Methods for solving Ordinary Differential Equations
# Currently implemented:
# 1. Euler's Method
# 2. Modified Euler's Method - Taking an average of the slope.

import numpy as np

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
