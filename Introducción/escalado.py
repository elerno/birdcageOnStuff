def escaladoANuevoTotal(lista, totalNuevo):
	"""Escala los valores de una lista para que su suma sea igual al nuevoTotal."""
	TotalIniciallista	= 0.0
	nuevaLista		= []

	for x in lista:
		TotalIniciallista = TotalIniciallista + x
	factorDeEscalado = totalNuevo / TotalIniciallista
	for x in lista:
		nuevoValor = x * factorDeEscalado
		nuevoValor = round(nuevoValor, 3)
		nuevaLista.append(nuevoValor)
	return nuevaLista

def dilatadoDeLista(lista, factor):
	"""Multiplica cada elemento de una lista por un factor."""
	nuevaLista = []

	for x in lista:
		nuevoValor = factor * x
		nuevaLista.append(nuevoValor)
	return nuevaLista

def multiplicarParaMap(x, y):
	return x + y
