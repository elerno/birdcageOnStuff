import DataAutomata
from series_numericas import *
from dict_nomenclatura import diccionarioDeDinamicas
from espectro_distorsionado import espectroDistorsionado
from notasEspectrales import notaI1, notaI2, notaI3
from met_igual_temperamento import dictModuloNPasos as modulo
from control_amplitud_espectral import amplitudEspectralUniforme

hist1Automata	= DataAutomata.data1(26, 20, (13,9))
hist2Automata	= DataAutomata.data2(26, 20, (11,11), hist1Automata)
indicesCoords	= DataAutomata.coordAIndice(hist1Automata)
instFractCoords	= DataAutomata.coordAVoz(hist1Automata)
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


def automataAInstFract(historia):

	instFracts	  = []

	for x in historia:
		if isinstance(x, tuple):
			instFract = instFractCoords[str(x)]
			instFracts.append(instFract)
	return instFracts


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
				comzosYfins.extend([x])
			evenOdd = 2
		else:
			comzosYfins.extend([-x])
			evenOdd = 1
	for x in comzosYfins:
		if x > 0:
			comzos.append(x)

	return comzosYfins, comzos
		

def hacerComzosAglo(historia, ultComzo, offset = 0, retrograda=0):

	comzos			= []
	densidadPorEntrada	= densidadEntradas(historia)
	counter 		= 0

	for x in historia:
		if isinstance(x, str):
			counter += 1

	comzosPlanos = logaritmicos(ultComzo , counter)
	if retrograda == 1:
		intervalos = serieAIntervalos(comzosPlanos)
		intervalos.reverse()
		comzosPlanosRetr = intervalosASerie(intervalos, comzosPlanos[0])
		comzosPlanos = comzosPlanosRetr

	for x, y in zip(comzosPlanos, densidadPorEntrada):
		x += offset - 1
		comzos.append([x] * y)

	return comzos


def hacerComzosAgloLin(historia, ultComzo, offset = 0, retrograda=0):

	comzos				= []
	densidadPorEntrada	= densidadEntradas(historia)
	counter 			= 0

	for x in historia:
		if isinstance(x, str):
			counter += 1

	comzosPlanos = lineares(ultComzo , counter)
	if retrograda == 1:
		intervalos = serieAIntervalos(comzosPlanos)
		intervalos.reverse()
		comzosPlanosRetr = intervalosASerie(intervalos, comzosPlanos[0])
		comzosPlanos = comzosPlanosRetr

	for x, y in zip(comzosPlanos, densidadPorEntrada):
		x += offset
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

	for x in comzos:
		dursEntrada = []
		for y in x:
			dur = durTotal - y
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


def elemento1(iteraciones=[2,3,5,5], din='mp', pitch='0.28', tipoDeEspect=2,
				facDeDistor=[.03,.05,.02],  durTot=18):

	score			= []
	historia		= aislarIters(hist1Automata, iteraciones)

	iters		= []
	for x in iteraciones:
		unaIter = aislarIters(hist1Automata, [x])
		iters.append(unaIter)

	comzosYfins, comzos	= hacerComzosYfins(historia, durTot)
	durs			= hacerDurs(comzosYfins)
	ampMax			= pppAfff[din]

	for x, y in zip(range(2), facDeDistor[:2]):

		unaIter		= iters[x]
		instrFracts	= automataAInstFract(unaIter)
		nComzos		= [comzos[x]] * len(instrFracts)
		nDurs		= [durs[x]] * len(instrFracts)
		frecs		= automataAfreq(m47[pitch], unaIter, tipoDeEspect, y)

		espectro = notaI1(instrFracts, nComzos, nDurs, ampMax, frecs)
		score.extend(espectro)

	tie = 1
	for x in range(2,4):
		unaIter		= iters[x]
		instrFracts	= automataAInstFract(unaIter)
		if tie == 1:
			nComzos = [comzos[x]] * len(instrFracts)
			nDurs = [(29-nComzos[0]) * -1] * len(instrFracts)
		else:
			nComzos = [18] * len(instrFracts)
			nDurs = [29] * len(instrFracts)
		frecs = automataAfreq(m47[pitch], unaIter, tipoDeEspect,
								facDeDistor[-1])
		espectro = notaI1(instrFracts, nComzos, nDurs, ampMax, frecs)
		score.extend(espectro)
		tie = 0
	return score


def elemento2(offset=11, celulas=377, din='mf', ultComzo=18, durTotal=36,
				pitch='1.09', tipoDeEspect=1, facDeDistor=.013):

	score		= []
	historia	= hist1Automata
	instrFracts	= automataAInstFract(historia)
	comzos		= hacerComzosAglo(historia, ultComzo, offset, retrograda=1)
	durs		= hacerDursAglo(durTotal + offset, comzos)
	instrFractsComp	= componerLista(instrFracts, durs)
	ampMax		= pppAfff[din]
	amps		= amplitudEspectralUniforme(range(celulas), ampMax)
	ampsComp	= componerLista(amps, durs)
	frecs		= automataAfreq(m47[pitch], historia, tipoDeEspect,
								facDeDistor)
	frecsComp	= componerLista(frecs, durs)

	for v, w, x, y, z in zip(instrFractsComp, comzos, durs, ampsComp,
								frecsComp):
		espectro = notaI2(v, w, x, y, z)
		score.extend(espectro)
	return score


def elemento3(offset=29, celulas=377, din='ff', ultComzo=17.5, durTotal=18,
				pitch='0.00', tipoDeEspect=0, facDeDistor=.007):

	score		= []
	historia	= hist2Automata
	instrFracts	= automataAInstFract(historia)
	comzos		= hacerComzosAgloLin(historia, ultComzo, offset, retrograda=1)
	durs		= hacerDursAglo(durTotal + offset, comzos)
	instrFractsComp	= componerLista(instrFracts, durs)
	ampMax		= pppAfff[din]
	amps		= amplitudEspectralUniforme(range(celulas), ampMax)
	ampsComp	= componerLista(amps, durs)
	frecs		= automataAfreq(m47[pitch], historia, tipoDeEspect,
								facDeDistor)
	frecsComp	= componerLista(frecs, durs)
	frecs2		= automataAfreq(m47[pitch], historia, tipoDeEspect, .07)
	frecsComp2	= componerLista(frecs2, durs)

	for u, v, w, x, y, z in zip(instrFractsComp, comzos, durs, ampsComp,
								frecsComp, frecsComp2):
		espectro = notaI3(u, v, w, x, y, z)
		score.extend(espectro)
	return score


def compilacion():

	intro = elemento1()
	intro.extend(elemento2())
	intro.extend(elemento3())
	return intro

if __name__ == "__main__":
	elemento2()
