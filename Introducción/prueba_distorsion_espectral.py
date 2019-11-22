from metodos_de_notas import espectroI1
from metodos_desviacion_controlada import gaussControlado

def unaNota():
	#espectroI1(start, totalDuration, fundamental, noDeArmonicos, tipoDeEspectro, factorDeDistorsion)

	inicios			= range(1, 1000, 2)
	iniciosGauss		= gaussControlado(inicios)
	distorsion		= range(1, 37)
	score			= []

	for x in distorsion:
		x = x * .01
		espectro = espectroI1(iniciosGauss.pop(0), 2, 53, 377, 0, x)
		score.extend(espectro)
	return score
