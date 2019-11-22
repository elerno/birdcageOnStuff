import automata as aut
from espectro_distorsionado import espectroDistorsionado
from series_numericas import *

def data1(ancho, alto, celViva):
	
	tamagno = (ancho, alto)

	# Crea el automata, su organizador y un automata de control.
	automata 			= aut.crearAutomata(tamagno, celViva)
	orgAutomata 		= aut.organizadorAutomata(automata)
	automataDeControl 	= aut.crearAutomata(tamagno, celViva)

	noQueHaVivido		= 1
	contador			= 1
	maxPoblacion		= 377
	poblacionMax		= 0
	parar				= 0
	historiaAutomata	= ['iter0', celViva]

	#una iteracion para inicializar el automata
	orgAutomata.iterateAutomaton()

	
	while 1:
		if parar:
			break
		historiaAutomata.append('iter' + str(contador))
		for x in range(ancho):
			if parar:
				break			for y in range(alto):
				if parar:
					break
				onOff = automata.get((x, y))
				if onOff:
					if automataDeControl.get((x, y)) == 0:
						historiaAutomata.append((x, y))
						noQueHaVivido += 1
					automataDeControl.set((x, y), 1)
					if noQueHaVivido == maxPoblacion:
						parar = 1
						break
		poblacion = orgAutomata.iterateAutomaton()
		if poblacion > poblacionMax:
			poblacionMax = poblacion
		
		contador += 1
	return historiaAutomata


def data2(ancho, alto, celViva, hist1Automata):
	
	tamagno = (ancho, alto)

	# Crea el automata, su organizador y un automata de control.
	automata 			= aut.crearAutomata(tamagno, celViva)
	orgAutomata 		= aut.organizadorAutomata(automata)

	indicesCoords	= coordAIndice(hist1Automata)

	contador			= 1
	maxPoblacion		= 377
	historiaAutomata	= ['iter0', celViva]
	parar				= 0

	#una iteracion para inicializar el automata
	orgAutomata.iterateAutomaton()
	
	while 1:
		if parar:
			break
		historiaAutomata.append('iter' + str(contador))
		for x in range(ancho):			if parar:
				break
			for y in range(alto):
				onOff = automata.get((x, y))
				if onOff:
					if indicesCoords.has_key(str((x, y))):
						historiaAutomata.append((x, y))
						del indicesCoords[str((x, y))]
						if not len(indicesCoords):
							parar = 1
							break
		orgAutomata.iterateAutomaton()
		contador += 1
		if contador > 1000:
			break
	historiaAutomata.pop(0)
	return historiaAutomata


def coordAIndice(dataAutomata):

	coordsAutomata	= []
	coordsIndice	= []
	indice		= 0

	for x in dataAutomata:
		if isinstance(x, tuple):
			coordsAutomata.append(x)

	for x in coordsAutomata:
		newTuple = (str(x), indice)
		coordsIndice.append(newTuple)
		indice += 1

	indiceCoordDict = dict(coordsIndice)
	return indiceCoordDict

def coordAVoz(dataAutomata):

	coordsAutomata	= []
	coordsIndice	= []
	contVoces	= 1

	for x in dataAutomata:
		if isinstance(x, tuple):
			coordsAutomata.append(x)

	for x in coordsAutomata:
		voz = contVoces * .001
		newTuple = (str(x), voz)
		coordsIndice.append(newTuple)
		contVoces += 1

	vozCoordDict = dict(coordsIndice)
	return vozCoordDict
		
	
