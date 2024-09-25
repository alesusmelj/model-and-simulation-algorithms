import numpy as np
import pandas as pd

# ============= Config =============

## Define the function
def f(x):
  return np.exp(x**2) 

## Define the number of rectangles
n = 5 

## Define the limits of integration
a = 0 
b = 1

# ==================================

data = []

# Calculate the width of each rectangle (Delta X)
dx = (b - a) / n

# Initialize method variables
area = 0
array_x_i = []
array_middle_x_i = []
array_f_x_i = []

# Calculates the position of each rectangle (Xi)
for i in range(n + 1):
  if i == 0:
    array_x_i.append(0)
  else:
    array_x_i.append(a + (i * dx))

# Calculates each rectangle middle point
for i in range(n + 1):
  if i == 0:
    array_middle_x_i.append(0)
  else:
    array_middle_x_i.append((array_x_i[i - 1] + array_x_i[i]) / 2)

# Evaluates each middle point in the function
for i in range(n + 1):
  if i == 0:
    array_f_x_i.append(0)
  else:
    array_f_x_i.append(f(array_middle_x_i[i]))

# Create a table with the results
for i in range(n + 1):
  data.append([array_x_i[i], array_middle_x_i[i], array_f_x_i[i]])

# Calculates the area under the curve
area = sum(array_f_x_i) * dx

# Prints the results
tabla_iteraciones = pd.DataFrame(data, columns=['Xi', 'Middle_Xi', 'f(Middle_Xi)'])

print()
print('Sum F(Middle_Xi)', sum(array_f_x_i))
print("Approximate area under the curve:", area)
print()
print(tabla_iteraciones)

