from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

class Linear_Spline(object):

	def __init__(self, X, Y):
		self.X_indata = X
		self.Y_indata = Y
		self.n = len(X)

		self.generate_lagrange_polynomials()


	def generate_lagrange_polynomials(self):

		self.lagrange_polynomials = []
		self.lagrange_resolution = 0.01

		for index_i in xrange(0, self.n-1):
			# Generate X values for Lagrange Polynomial over current interval
			X_Lagrange_Polynomial = np.arange(self.X_indata[index_i], self.X_indata[index_i+1], self.lagrange_resolution)

			# Instantiate Y array for Lagrange Polynomial values over current interval
			Y_Lagrange_Polynomial = np.zeros(len(X_Lagrange_Polynomial))

			# Calculate current interval's linear Lagrange Function
			for x_index, x in enumerate(X_Lagrange_Polynomial):
				first_point_term = self.Y_indata[index_i] * (x - self.X_indata[index_i+1]) / (self.X_indata[index_i] - self.X_indata[index_i+1])
				second_point_term = self.Y_indata[index_i+1] * (x - self.X_indata[index_i]) / (self.X_indata[index_i+1] - self.X_indata[index_i])

				Y_Lagrange_Polynomial[x_index] = first_point_term + second_point_term

			self.lagrange_polynomials.append((X_Lagrange_Polynomial, Y_Lagrange_Polynomial))


	def plot(self, intervals=None):

		for index, lagrange_function in enumerate(self.lagrange_polynomials):
			
			if intervals is None:
				x = lagrange_function[0]
				y = lagrange_function[1]
				plt.plot(x, y, 'b--')

			else:
				if index in intervals:
					x = lagrange_function[0]
					y = lagrange_function[1]
					plt.plot(x, y, 'b--')


	def interpolate(self, interpolate_x):
		for index, lagrange_function in enumerate(self.lagrange_polynomials):
			X = lagrange_function[0]

			if interpolate_x >= min(X) and interpolate_x <= max(X):
				Y = lagrange_function[1]

				for x_index, x in enumerate(X):
				
					if np.abs(interpolate_x - x) < self.lagrange_resolution*1e-1:
						self.interpolated_value = Y[x_index]
						return Y[x_index]
					
				return False
