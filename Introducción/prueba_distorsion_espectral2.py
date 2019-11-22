import DataAutomata
from series_numericas import *
from dict_nomenclatura import diccionarioDeDinamicas
from espectro_distorsionado import espectroDistorsionado
from notasEspectrales import notaIprueba
from met_igual_temperamento import dictModuloNPasos as modulo
from control_amplitud_espectral import amplitudEspectralUniforme

hist1Automata	= DataAutomata.data1(26, 20, (13,9))
indicesCoords	= DataAutomata.coordAIndice(hist1Automata)
pppAfff		= diccionarioDeDinamicas()
m47		= modulo(47,53,15000)


def aislarIters(historia, itersList):

	celulasIter 	= []

	for noIter in itersList:
		startAppend	= 0
		for x in historia:
			if startAppend == 1 and isinstance(x, str):
				break
			if isinstance(x, str) and x.endswith(str(noIter)):
				celulasIter.append(x)
				startAppend = 1
			if startAppend == 1 and isinstance(x, tuple):
				celulasIter.append(x)

	return celulasIter


def noParciales(historia, numero=377):

	celulas		= []
	contador	= 0

	for x in historia:
		if isinstance(x, tuple):
			celulas.append(x)
			contador += 1
		else:
			celulas.append(x)
		if contador == numero:
			break
	return celulas

def densidadEntradas(historia):

	densidadEntradas	= []
	counter			= 0

	historia.reverse()
	for x in historia:
		if isinstance(x, tuple):
			counter += 1
		else:
			densidadEntradas.append(counter)
			counter = 0
	historia.reverse()
	densidadEntradas.reverse()
	return densidadEntradas

def hacerComzosYfins(historia, ultComzo):

	comzosYfins			= []
	comzos				= []
	densidadPorEntrada	= densidadEntradas(historia)
	evenOdd			= 1
	counter 		= 0

	for x in historia:
		if isinstance(x, str):
			counter += 2

	comzosPlanos = logaritmicos(ultComzo, counter)

	for x in comzosPlanos:
		if evenOdd % 2.0 != 0:
			densidad = densidadPorEntrada.pop(0)
			if densidad !=0:
				comzosYfins.extend([x] * densidad)
			evenOdd = 2
		else:
			comzosYfins.extend([-x])
			evenOdd = 1
	for x in comzosYfins:
		if x > 0:
			comzos.append(x)

	return comzosYfins, comzos
		

def hacerComzosAglo(historia, ultComzo):

	comzos			= []
	densidadPorEntrada	= densidadEntradas(historia)
	counter 		= 0

	for x in historia:
		if isinstance(x, str):
			counter += 1

	comzosPlanos = logaritmicos(ultComzo, counter)

	for x, y in zip(comzosPlanos, densidadPorEntrada):
		comzos.append([x] * y)

	return comzos


def hacerDurs(comzosYfins):

	durs		= []
	densidad 	= []
	comzos		= []
	finales		= []
	contador	= 0
	nuevoComzo	= [comzosYfins[0]]

	for x in comzosYfins:

		if x > 0:
			contador += 1
			if x != nuevoComzo:
				comzos.append(x)
				nuevoComzo = x
		else:
			densidad.append(contador)
			finales.append(x)
			contador = 0

	for x, y, z in zip(densidad, comzos, finales):
		unaDur = abs(z) - y
		durs.extend([unaDur] * x)
	return durs


def hacerDursAglo(durTotal, comzos):

	durs		= []
	durTotalYOffset	= durTotal + comzos[0][0]

	for x in comzos:
		dursEntrada = []
		for y in x:
			dur = durTotalYOffset - y
			dursEntrada.append(dur)
		durs.append(dursEntrada)
	return durs


def automataAfreq(fund, historia, tipoDeEspect, facDeDistor):

	parcialesDelEspectro	= [todos, pares, nones, fibonacci, primos]
	espectroElegido		= parcialesDelEspectro.pop(tipoDeEspect)
	todosParciales		= espectroElegido(2000)

	indices	  = []
	parciales = []

	for x in historia:
		if isinstance(x, tuple):
			indice = indicesCoords[str(x)]
			indices.append(indice)
	for x in indices:
		parcial = todosParciales[x]
		parciales.append(parcial)
		
	alturas = espectroDistorsionado(fund, parciales, facDeDistor)
	return alturas

def componerLista(frecs, durs):

	frecsComp	= []

	for x in durs:
		sublista = []
		for y in range(len(x)):
			sublista.append(frecs.pop(0))
		frecsComp.append(sublista)
	return frecsComp


def pruebaEspectra(noParciales=377,din='fff',pitch='1.23',tipoDeEspect=0,durTot=18):

	score			= []
	historia		= todos(377)
	comzos			= range(0, 300, 3)
	durs			= 2
	ampMax			= pppAfff[din]
	distor			= range(1, 101)

	for x, y in zip(comzos, distor):
		y = y*.01
		print y
		frecs = espectroDistorsionado(m47[pitch], historia, y)
		espectro = notaIprueba(x, 2, ampMax, frecs)
		print 'esp', frecs
		score.extend(espectro)
	return score


def compilacion():

	intro = pruebaEspectra()
	return intro

if __name__ == "__main__":
	print hist1Automata
