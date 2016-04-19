from __future__ import division
import numpy as np
import pandas as pd
import sys, os


def introduction():
	print('\n'*2)
	print('\t|-----------------------------------------------------|')
	print("\t| Welcome to the Linear Spline Interpolation Script.  |")
	print("\t| Given N data inputs, this script will generate      |")
	print("\t| an N-1 linear Lagrange Polynomials, which are       |")
	print("\t| utilized to find interpolated values.               |")
	print("\t|                                                     |")
	print("\t| Press q at anytime to quit the program.             |")
	print('\t|-----------------------------------------------------|')
	print('\n'*2)


def user_x_input(X):
	quit_answers = ['q', 'Q', 'quit', 'QUIT', 'Quit', 'exit', 'Exit', 'EXIT']
	while True:
		user_x = raw_input("\n\tEnter value in [{:.2f}, {:.2f}): ".format(min(X), max(X)))

		# Check for user quit
		if user_x in quit_answers:
			print("\n\tExiting program...")
			sys.exit()

		# Ensure numeric value was entered
		try:
			user_x = float(user_x)
		except:
			continue

		# Ensure user entered value is within X domain
		if user_x < min(X) or user_x > max(X):
			print("\n\tERROR: Value outside of [{:.2f}, {:.2f})".format(min(X), max(X)))
			continue
		else:
			return user_x



def prompt_user(default=True, prompt=None):
	yes_answers = ['y', 'Y', 'yes', 'YES', 'Yes']
	no_answers =  ['n', 'N', 'no',  'NO',  'No']
	quit_answers = ['q', 'Q', 'quit', 'QUIT', 'Quit', 'exit', 'EXIT', 'Exit']

	while True:
		if default:
			user_choice = raw_input("\n\tWould you like to log the interpolated values (y/n)? ")
		else:
			user_choice = raw_input(prompt)

		if user_choice in yes_answers:
			if default:
				outfile_path = get_outfile_name()
			else:
				outfile_path = None
			return True, outfile_path

		elif user_choice in no_answers:
			return False, False

		elif user_choice in quit_answers:
			print("\n\tExiting program...\n\n")
			sys.exit()
		else:
			print("\n\tERROR: Invalid entry.\n")
			continue


def check_file_exists(filename):

	outfiles = check_existing_files('output', 'csv')

	if filename in outfiles:
		return True
	else:
		return False


def get_outfile_name():

	filename = raw_input("\n\tEnter filename for output data:\n\t>> ")
	while True:

		# Check if entered filename was only a space. Invalid. Reprompt user.
		if len(filename.strip()) == 0:
			print("\tERROR: You did not enter a filename.\n")
			filename = raw_input("\n\tEnter another filename for output data:\n\t>> ")
			continue

		# Check if file already exists. 
		elif check_file_exists(filename):
			print("\n\tWarning: File already exists.")
			# Ask if user wants to overwrite the file.
			overwrite, _ = prompt_user(False, '\tOverwrite existing file (y/n)? ')
			
			# If user wants to overwrite...
			if overwrite:
				file_path = './data/output/' + filename + '.csv'

			# Else, user wants to save existing file and pick another name
			elif not overwrite:
				filename = raw_input("\n\tEnter another filename for output data file: ")
				continue

		# Else, everything is fine.
		else:
			file_path = './data/output/' + filename.strip() + '.csv'

		# Confirm with user
		print("\n\tThe data will be stored as {}.csv".format(filename))
		filename_ok, _ = prompt_user(False, "\tContinue (y/n)? ")
		if filename_ok:
			break
		else:
			filename = raw_input("\n\tEnter another filename for output data file: ")

	# Final confirm of filename and save location
	print("\n\tOutfile location: {}\n".format(file_path))
	print('\t' + '='*50)

	# Create outfile
	with open(file_path, 'w') as outfile:
		outfile.write("x, y\n")
	
	return file_path
		

def get_user_input(L):

	# Set bounds within which user can choose values
	min_x, max_x = min(L.X), max(L.X)

	while True:
		user_input = raw_input("\n\tEnter value x within [{}, {}]:\n\t>> ".format(min_x, max_x))
		
		if user_input == 'q':
			print("\n\tExiting program...\n\n")
			sys.exit()

		# Ensure user enters appropriate numeric value; e.g., No letters or "weird" input values
		try:
			x_inter = float("{:.3f}".format(float(user_input)))
			
		except:
			print("\n\tERROR: Invalid entry.\n")
			continue

		if x_inter < min_x or x_inter > max_x:
			print("\n\tERROR: Entry outside of [{}, {}]".format(min_x, max_x))
			continue
		else:
			break

	return x_inter


def check_existing_files(folder, suffix=None):

	file_dir = "./data/" + folder + "/"
	if suffix is None:
		term_command = "ls " + file_dir + "*"
	elif suffix is 'csv':
		term_command = "ls " + file_dir + "*.csv"

	raw_files = os.popen(term_command)

	# Determine infiles already processed
	files = []
	for index, file_ in enumerate(raw_files):
		if suffix is None:
			files.append(file_[len(file_dir):].strip())
		else:
			files.append(file_[len(file_dir):-5].strip())

	return files


def data_logger(inter_x, inter_y, outfile_name):
	with open(outfile_name, 'a') as outfile:
		line = "{:.3f},{:.3f}\n".format(inter_x, inter_y)
		outfile.write(line)


def get_data():

	# Obtain list of input files
	infiles = check_existing_files('input')

	# List input files
	print("\tSelect input data file:")
	print('\t-----------------------')
	for index, infile in enumerate(infiles):
		print("\t{}. {}".format(index+1, infile))

	
	while True:
		# Get user choice
		user_choice = raw_input("\t>> ")
	
		# Checks for program quit
		if user_choice == 'q':
			print("\tExiting program...\n\n")
			sys.exit()

		# Checks for alphanumeric misentries
		try:
			user_choice = int(user_choice)
		except:
			print("\n\tERROR: Enter numeric, integer value corresponding to list above.")
			continue

		# Checks for integer to be within the correct file index range
		if int(user_choice) <= 0 or int(user_choice) > index+1:
			print("\n\tERROR: Incorrect entry range.")
			continue

		# Success!
		else:
			break

	# Declare infile path
	infile_name = infiles[user_choice-1]
	data_path = './data/input/' + infile_name

	# Create test dataframe from csv infile to check for headres
	df_test = pd.read_csv(data_path)
	
	try:
		int(df_test.columns[0])
		header = False
	except:
		header = True

	if header:
		df = df_test
	
	elif not header:
		df = pd.read_csv(data_path, header=None)
	
	# Rename columns for easy access
	df.columns = ['x', 'y']

	# Extra X and Y from dataframe
	X = df['x']
	Y = df['y']

	return X, Y
