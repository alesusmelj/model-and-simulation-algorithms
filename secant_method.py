import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
def secant_method(f, x0, x1, tol=1e-8, max_iter=100):
	"""
	Implementación del método de la secante para encontrar la raíz de una función.
	
	Parámetros:
	f : función
		La función de la cual queremos encontrar la raíz.
	x0, x1 : float
		Las aproximaciones iniciales.
	tol : float
		La tolerancia para la convergencia.
	max_iter : int
		El número máximo de iteraciones.
	
	Retorna:
	float
		La aproximación de la raíz.
	"""
	iteraciones = []

	for i in range(max_iter):
		if abs(f(x1) - f(x0)) < tol:
			print("La diferencia entre f(x1) y f(x0) es muy pequeña, puede que no converja.")
			return None, iteraciones
		
		x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
		
		if i==0 or i==1:
			error = '-'
		else:
			error = (abs(x2 - x1) / x2) * 100
	
		iteraciones.append((x0,f(x0), error))
		
		if abs(x2 - x1) < tol:
			return x2, iteraciones
		
		x0, x1 = x1, x2
	print("Número máximo de iteraciones alcanzado.")
	return None, iteraciones
 
# ================================ MAIN ================================

f = lambda x: (x**3 - x - 2)
x0 = 1 
x1 = 2
raiz, iteraciones = secant_method(f, x0, x1)
 
if raiz is not None:
	print()
	print(f"La raíz aproximada es: {raiz}")
else:
	print("No se encontró una raíz.")
	
## Tabla de resultados

tabla_iteraciones = pd.DataFrame(iteraciones, columns=['x0', 'f(x0)', 'err %'])
pd.set_option('display.float_format', '{:.8f}'.format)

print()
print(tabla_iteraciones)
 
## Graficar la función y la raíz encontrada

x = np.linspace(-3, 3, 400)
y = f(x)
 
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='$f(x) = x^2 - 4$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.scatter(raiz, f(raiz), color='red', zorder=5)
plt.title('Método de la Secante')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
