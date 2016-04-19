import numpy as np
import matplotlib.pyplot as plt

def plot(X, Y, linear_spline, x_interpolate=None, y_interpolate=None):
	plt.ion()
	plt.clf()
	plt.plot(X, Y, 'ro')
	linear_spline.plot()

	if x_interpolate is not None:
		plt.plot(x_interpolate, y_interpolate, 'ko')
		plt.plot(np.linspace(min(X)-1, x_interpolate, 50), np.ones(50)*y_interpolate, 'k--')
		plt.plot(np.ones(50)*x_interpolate, np.linspace(min(Y)-1, y_interpolate, 50), 'k--')

		x_text_position = x_interpolate + 0.2
		y_text_position = y_interpolate + 0.2
		plt.text(x_text_position, y_text_position, '({:.3f}, {:.3f})'.format(x_interpolate, y_interpolate), fontsize=13.75)
		plt.xlabel('x')
		plt.ylabel('f(x)')
		plt.title('Linear Spline Interpolation')

	plt.axis([min(X)-1, max(X)+1, min(Y)-1, max(Y)+1])