# Problem 1
import pandas as pd   # load the pandas library

# Read the CSV file and save it into a DataFrame called 'cars'
cars = pd.read_csv('cars.csv')
display(cars)

# (a) Show the first 5 rows of the dataset
print("First 5 rows of cars:")
display(cars.head())

# (b) Show the last 5 rows of the dataset
print("\nLast 5 rows of cars:")
display(cars.tail())