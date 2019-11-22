# GOD en la aplicaci_on del aut_mata.
import BCAutomaton.GOD as apiAutomata
import random
import sys
import operator

def crearAutomata(tamagno = (80,20), comienzo = (0,0)):
	"""Crea un automata celular de birdcage. Argumentos estandar: tamagno = (80,20), comienzo = (0,0). Un tuple vacio como segundo argumento genera un automata sin celulas vivas"""

	# Instancia la clase que genera al aut_mata

	generador = apiAutomata.Generator()

	# Data necesaria para construir el aut_mata
	(ancho, alto) = tamagno
	topologia = ("GridTopology", 0)
	vecindad = ("VonNeumannNeighborhood", )
	regla = ("ReductionRule", (operator.xor, 0))
	tipoDeAutomata = ("SynchronousAutomaton_2D", )

	# Genera el automata, y configura el estado inicial.
	automata = generador.generateAutomaton(tamagno, topologia, vecindad, regla, tipoDeAutomata)
	automata.set(comienzo, 1)
	
	return automata

def organizadorAutomata(automata):
	"""Crea un organizador para elautomata celular de birdcage. Toma como argumento un automata."""

	organizador = apiAutomata.Organizer(automata)
	
	return organizador
