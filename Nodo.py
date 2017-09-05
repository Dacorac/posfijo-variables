class Nodo():
	
	def __init__(self, valor, izq = None, der = None):
		self.valor = valor
		self.izq = izq
		self.der = der

class Tabla():
	variables = {}

def evaluar(arbol):
	if arbol.valor == '+':
		return int(evaluar(arbol.izq)) + int(evaluar(arbol.der))

	if arbol.valor == '-':
		return int(evaluar(arbol.izq)) - int(evaluar(arbol.der))
	
	if arbol.valor == '/':
		return int(evaluar(arbol.izq)) / int(evaluar(arbol.der))

	if arbol.valor == '*':
		return int(evaluar(arbol.izq)) * int(evaluar(arbol.der))

	if arbol.valor == '=':
		valor = evaluar(arbol.izq)
		Tabla.variables[arbol.der.valor] = valor
		return valor
	
	if Tabla.variables.has_key(arbol.valor) == True:
		return Tabla.variables[arbol.valor]
	elif Tabla.variables.has_key(arbol.valor) == False:
		return int(arbol.valor)
			
			


