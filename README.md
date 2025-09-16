# Problem 1
In Problem 1, you will be guided through the fundamental steps for working with data in Pandas. You will load a CSV file into a DataFrame and display the first five and last five rows. This step checks whether the data is loaded correctly and gives a quick snapshot of the dataset. It serves as the starting point of the experiment and ensures that you know how to view data using Pandas.

	#Problem 1

	#load the pandas library
 
	import pandas as pd   


	# Read the CSV file and save it into a DataFrame called 'cars'
 
	cars = pd.read_csv('cars.csv')


	# (a) Show the first 5 rows of the dataset
 
	print("First 5 rows of cars:")
 
	display(cars.head())
 

	# (b) Show the last 5 rows of the dataset
 
	print("\nLast 5 rows of cars:")
 
	display(cars.tail())

# Problem 2
Problem 2 teaches students how to use subsetting, slicing, and indexing in Pandas. They will extract specific rows and columns from the dataset to answer questions like finding details about different car models. This problem demonstrates how Pandas can be used to focus on important information for closer study. It helps students understand how to filter and analyze data efficiently.

	# Problem 2
 
	import pandas as pd   # load the pandas library


	# Read the CSV file and save it into a DataFrame called 'cars'
 
	cars = pd.read_csv('cars.csv')


	# (a) Show the first 5 rows with every other column (1st, 3rd, 5th, etc.)
 
	print("First Five Rows with Odd-Numbered Columns:")
 
	display(cars.iloc[:5, 1::2])
 

	# (b) Show the row where the car model is 'Mazda RX4'
 
	print("\nRow that contains the model 'Mazda RX4':")
 
	display(cars.loc[cars['Model'] == 'Mazda RX4'])


	# (c) Show how many cylinders the 'Camaro Z28' has
 
	print("\nNumber of cylinders for Camaro Z28:")
 
	print(cars.loc[df["Model"] == "Camaro Z28", "cyl"].values[0])


	# (d) Show cylinders and gear type for 3 specific car models
 
	print("\nCylinders and gear type for Mazda RX4 Wag, Ford Pantera L, and Honda Civic:")
 
	display(cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']])
