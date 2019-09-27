# Implementation of Numerical Methods to compute the area under a curve (integral) for given discrete points.
# Use trapezium() if data has EQUAL intervals
# Use generalTrapezium() if data has UNION intervals.

import numpy as np

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