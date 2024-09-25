import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ============= Config =============

# Define the function
def f(x):
    return (x**3 - 3*x -4)

# Define derivated f
def f_derivated(x):
    return (3*(x**2) - 3)

# Initial conditions of the model
x0 = 2
n = 5
x0_real = 2.19582334

# ==================================

# Define initial variables for the function
summary = []
x_values = []
x_values.append(x0)
summary.append([x0, 0, 0, 0])

# Calculates Xn+1 value
for i in range(n):
    x_next = x_values[i] - (f(x_values[i]) / f_derivated(x_values[i]))
    x_values.append(x_next)
    error = (((x0_real - x_next)/x0_real)*-1)*100

    summary.append([x_next, f(x0), f_derivated(x0), error])

# Prints the results
df_summary = pd.DataFrame(summary, columns=['Xn', 'f(Xn)', 'f\'(Xn)', 'err%'])
pd.set_option('display.float_format', '{:.8f}'.format)

print()
print(df_summary)