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
print(cars.loc[cars["Model"] == "Camaro Z28", "cyl"].values[0])

# (d) Show cylinders and gear type for 3 specific car models
print("\nCylinders and gear type for Mazda RX4 Wag, Ford Pantera L, and Honda Civic:")
display(cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']])