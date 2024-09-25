import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
def f(x):
	return (np.cos(x) - x)
 
def g(x):
	return (np.cos(x))
 
def fixed_point_iteration(x0, tol=1e-5, max_iter=100):
	x = x0
	iteraciones = []
	iter_values = [x0]
	for i in range(max_iter):
		x_new = g(x)
		
		error = (abs(x_new - x) / x_new) * 100
		iter_values.append(x_new)
		iteraciones.append((x_new, error))

		if abs(x_new - x) < tol:
			break
		x = x_new
	return x_new, iter_values, iteraciones

# ================================ MAIN ================================

x0 = 0.5 # Valor inicial
root, iter_values, iteraciones = fixed_point_iteration(x0)

## TABLA DE RESULTADOS

tabla_iteraciones = pd.DataFrame(iteraciones, columns=['Xn', 'err %'])
tabla_iteraciones.index = tabla_iteraciones.index + 1
pd.set_option('display.float_format', '{:.8f}'.format)

print()
print(tabla_iteraciones)
 
## Graficar la función original y el proceso de iteración
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y_vals = np.cos(x_vals)
 
plt.plot(x_vals, y_vals, label='$f(x) = \cos(x)$')
plt.scatter(iter_values, [f(x) for x in iter_values], color='red', zorder=5)
plt.plot(iter_values, [f(x) for x in iter_values], color='red', linestyle='--', zorder=5)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Método del Punto Fijo para $f(x) = \cos(x)$')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend()
plt.show()
 
print(f"La raíz aproximada es: {root}")