# my fucntion_has to be in a separate file named ryan_function
def greet(name):
    return f"Hello,", name

# another function has to be in file named ryan_function
def add():
    a = int(input(f"Please input an integer: "))
    b = int(input(f"Please input another integer: "))
    return a + b

import datetime
print(datetime.datetime.now())

import requests
response = requests.get('https://www.youtube.com/')
print(response.status_code) #200 is succesfull response code

import pandas as pd
df = pd.DataFrame({
    'Name' : ['Michael', "Nikola", "Lebron"],
    'Number' : [323, 15, 23]
})
print(df)

import numpy as np
array = np.array([1,2,3,4])
print(array)

import matplotlib.pyplot as plt

plt.plot([1,2,3],[4,5,6])
plt.show()

# import csv

# with open('data.csv', mode='r') as file:   # This data.csv file does not exist
    # csv_reader = csv.reader(file)
    # for row in csv_reader:
        # print(row)

'''import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv") # File data.csv does not exist
                 
start_year = 2000
end_year = 2024
filtered_df = df[(df["Year"] >= start_year) & (df["Year"] <= end_year)]
ax = filtered_df.plot(kind="bar", x="Module", y="Year")
plt.ylim(start_year, end_year)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha="right")
plt.show()'''



