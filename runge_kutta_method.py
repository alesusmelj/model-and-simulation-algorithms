import numpy as np
import pandas as pd

# ============= Config =============

# Define the function
def f(x, y):
    return x*(np.sqrt(y))

# Define 
def y_real(x):
    return ((x**2 + 7) / 4)**2 

# Initial conditions of the model
t0 = 1
y0 = 4
h = 0.2
n = 3

# ==================================

# Define initial variables for the function
summary = []
t = np.zeros(n+1)
y = np.zeros(n+1)

t[0], y[0] = t0, y0

for i in range(n):
    t[i+1] = t[i] + h

for i in range(n):

    # Calculates the k values
    k1 = f(t[i], y[i])
    k2 = f(t[i] + h/2, y[i] + (h/2)*k1)
    k3 = f(t[i] + h/2, y[i] + (h/2)*k2)
    k4 = f(t[i] + h, y[i] + h*k3)

    y_next = y[i] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    y[i+1] = y_next
    y_real_var = y_real(t[i])

    error = np.abs((y_real_var - y[i])/y_real_var)*100

    summary.append([t[i], y[i], k1, k2, k3, k4, y_next, y_real_var, error])

# Prints the results
df_summary = pd.DataFrame(summary, columns=['t_n', 'y_n', 'k1', 'k2', 'k3', 'k4', 'y_n+1', 'y_real', 'err%'])
pd.set_option('display.float_format', '{:.8f}'.format)

print()
print(df_summary)
