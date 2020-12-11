import numpy as np
import matplotlib.pyplot as plt

def LinearRegression1(X,Y,lr,epochs):
	''' Performs Single Variable Linear Regression. Required Arguments are the inderpendent and dependent variables, the learning rate and the
		number of epochs.
		Returns the slope, intercept, the loss, the number of iterations and the predicted independent variables.
	'''
	m = 0
	c = 0
	n = float(len(X))
	Loss = []
	Iterations = []
	
	# Gradient Descent
	for i in range(epochs):
		Iterations.append(i)
		Y_pred = m*X + c
		Error = (1/n)*sum((Y-Y_pred)**2)
		Loss.append(Error)
		nabla_m = (-2/n)*sum(X*(Y-Y_pred))
		nabla_c = (-2/n)*sum(Y-Y_pred)
		m -= nabla_m*lr
		c -= nabla_c*lr
	return m, c, Loss, Iterations, Y_pred