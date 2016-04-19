from modules.linear_spline import Linear_Spline
import modules.utilities as utility
import modules.graph as graph
import numpy as np
import matplotlib.pyplot as plt
import sys



def main(X, Y, log_data=False, outfile_path=None):

	# Generate linear spline for X, Y
	linear_spline = Linear_Spline(X, Y)

	# Plot the spline with data points
	graph.plot(X, Y, linear_spline)

	while True:

		# Obtain x value from user at which to find interpolated value
		x_interpolate = utility.user_x_input(X)
		
		# Calculates interpolated value
		if linear_spline.interpolate(x_interpolate):
			#x_interpolate = linear_spline.interpolated_values[0]
			y_interpolate = linear_spline.interpolated_value
			print("\tInterpolated y at x = {:.3f}: {:.3f}".format(x_interpolate, y_interpolate))
		
		# Resolution error.
		else:
			print("\tERROR interpolating.")
			continue

		# Log data if enabled
		if log_data:
			utility.data_logger(x_interpolate, y_interpolate, outfile_path)

		# Plot the graph
		graph.plot(X, Y, linear_spline, x_interpolate, y_interpolate)

	# Turn off interactive plot and hold last plot until user quits
	plt.ioff()
	plt.show()

	

if __name__ == '__main__':

	# Print introduction
	utility.introduction()

	# Obtains data
	X, Y = utility.get_data()
	
	# Check if user wants to log data, obtain outfile name, and initiate main function
	log_data, outfile_path = utility.prompt_user()
	if not log_data:
		main(X, Y)
	else:
		main(X, Y, True, outfile_path)