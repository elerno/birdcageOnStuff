from math import sqrt

def todos(noDeElementos, inicio = 1):
	"""Construye una serie de n_meros naturales con noDeElementos n_mero de elementos. El segundo argumento (opcional) es en que n_mero empezar."""
	parciales = range(inicio, (noDeElementos + 1))	return parciales

def pares(noDeElementos, inicio = 2):
	"""Construye una serie de n_umeros pares con noDeElementos n_mero de elementos. Si inicio no es par, empieza en el siguiente n_mero par."""
	if inicio % 2 != 0:
		inicio = inicio + 1
	parciales	= []	par		= inicio	contador	= 0
	while contador < noDeElementos:		parciales.append(par)		par = par + 2		contador = contador + 1	return parciales

def nones(noDeElementos, inicio = 1):
	"""Construye una serie de n_umeros nones con noDeElementos n_mero de elementos. Si inicio no es non, empieza en el siguiente n_mero par."""
	if inicio % 2 == 0:
		inicio = inicio + 1
	parciales	= []	non		= 1	contador	= 0
	while contador < noDeElementos:		parciales.append(non)		non = non + 2		contador = contador + 1	return parcialesdef fibonacci(noDeElementos=1, primerNo = 1, segundoNo = 1):	"""Construye una serie de n_umeros de fibonacci con noDeElementos n_mero de elementos. Si se quiere que se repita el primer elemento, primerNo debe ser igual a 0. Es posible comenzar desde cualquier par de n_meros"""	parciales	= []	a		= primerNo	b		= segundoNo	contador	= 0		while contador < noDeElementos:		parciales.append(b)		a, b = b, a + b		contador = contador + 1	return parciales
def primos(noDeElementos, inicio = 2):
	parciales	= []	candidato	= inicio	contador	= 0	while contador < noDeElementos:		probarHasta = int(sqrt(candidato)) + 1		for x in range (2, probarHasta):			if candidato % x == 0:				candidato = candidato + 1				break		else:			parciales.append(candidato)			candidato = candidato + 1			contador = contador + 1	return parciales


def lineares(hastaNo, noDeElementos):

	pasos		= noDeElementos - 1
	unPaso		= float(hastaNo) / pasos
	lineares	= [0]

	for x in range(pasos):
		nuevoValor = lineares[-1] + unPaso
		lineares.append(nuevoValor)
	return lineares


def logaritmicos(hastaNo, noDeElementos):

	pasos	= noDeElementos - 1
	poder	= 1.0 / pasos
	unPaso	= pow(hastaNo, poder)

	logaritmicos = [1]

	for x in range(pasos):
		nuevoValor = logaritmicos[-1] * unPaso
		logaritmicos.append(nuevoValor)
	return logaritmicos


def serieAIntervalos(lista):
		intervalos = []
		a = lista[0]
		for x in lista:
			nuevoIntervalo = x - a
			intervalos.append(nuevoIntervalo)
			a = x
		intervalos.pop(0)
		return intervalos


def intervalosASerie(intervalos, comienzo):

	serie	= [comienzo]

	for x in intervalos:
		elemento = x + serie[-1]
		serie.append(elemento)
	return serie
