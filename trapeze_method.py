import numpy as np
import pandas as pd

# ============= Config =============

# Define the function to integrate
def f(x):
    return np.exp(x**4) 

# Define the number of trapezoids
n = 5

# Define the integration limits
a = 0
b = 1

# ==================================

data = []

# Initialize method variables
area = 0
array_x_i = []
array_f_x_i = []

# Calculate the width of each trapezoid (Delta X)
dx = (b - a) / n

# Calculate initial F(a) and F(b)
f_a = f(a)
f_b = f(b)

# Calculates the position of each trapezoid (Xi)
for i in range(n):
  if i == 0:
    array_x_i.append(0)
  else:
    array_x_i.append(a + (i * dx))

# Evaluates each iteration in the function
for i in range(n):
    if i == 0:
        array_f_x_i.append(0)
    else:
        array_f_x_i.append(f(a+(i*dx)))

# Create a table with the results
for i in range(n):
  data.append([array_x_i[i], array_f_x_i[i]])

# Calculates the area under the curve
area = (dx/2) * (f_a + (2 * sum(array_f_x_i)) + f_b)

# Prints the results
tabla_iteraciones = pd.DataFrame(data, columns=['Xi', 'f(a + i*dx)'])

print()
print('Sum F(a + i*dx)', sum(array_f_x_i))
print("Approximate area under the curve (Trapezoidal Rule):", area)
print()
print(tabla_iteraciones)
