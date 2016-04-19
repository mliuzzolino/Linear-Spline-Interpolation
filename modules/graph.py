import numpy as np
import matplotlib.pyplot as plt

def plot(X, Y, linear_spline, x_interpolate=None, y_interpolate=None):
	
	plt.ion()
	plt.clf()
	
	# Plot data points and linear spline interpolating polynomials
	plt.plot(X, Y, 'ro')
	linear_spline.plot()

	# Define graph parameters
	min_x = min(X) - np.abs(max(X)*0.25)
	max_x = max(X)*1.25
	min_y = min(Y) - np.abs(max(Y)*0.25)
	max_y = max(Y)*1.25
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.title('Linear Spline Interpolation')

	# Plot interpolated values
	if x_interpolate is not None:

		# Plot interpolation values
		plt.plot(x_interpolate, y_interpolate, 'ko')
		
		# Plot horizontal black dashed line that indicates the interpolated point on the graph
		plt.plot(np.linspace(min_x, x_interpolate, 50), np.ones(50)*y_interpolate, 'k--')
		# Plot vertical black dashed line that indicates the interpolated point on the graph
		plt.plot(np.ones(50)*x_interpolate, np.linspace(min_y, y_interpolate, 50), 'k--')

		# Define text position parameters
		x_text_position = x_interpolate + 0.2
		y_text_position = y_interpolate + 0.2
		plt.text(x_text_position, y_text_position, '({:.3f}, {:.3f})'.format(x_interpolate, y_interpolate), fontsize=13.75)
		
	
	plt.axis([min_x, max_x, min_y, max_y])