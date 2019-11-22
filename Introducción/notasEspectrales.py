from series_numericas import *from espectro_distorsionado import espectroDistorsionadofrom control_amplitud_espectral import amplitudEspectralUniformedef espectroI1(comzos, durs, ampMax, fund, noDeArms, tipoDeEspect, facDeDistor):
	""" M_todo para un espectro distorsionado usando el instrumento 1."""
	parcialesDelEspectro	= [todos, pares, nones, fibonacci, primos]
	espectroElegido		= parcialesDelEspectro.pop(tipoDeEspect)
	parciales		= espectroElegido(noDeArms)	espectroDist		= espectroDistorsionado(fund, parciales, facDeDistor)
	amplitudesCSD	= amplitudEspectralUniforme(espectroDist, ampMax)	parcialesCSD	= []

	print len(comzos),len(durs),len(amplitudesCSD), len(espectroDist)							for w, x, y, z in zip(comzos, durs, amplitudesCSD, espectroDist):		noteCSD = ("i1 %s %s %s %s" %(w, x, y, z))		parcialesCSD.append(noteCSD)	return parcialesCSD


def notaI1(instrFracts, comzos, durs, ampMax, frecs):
	""" M_todo para una porcion de espectro distorsionado usando el instrumento 1."""

	amplitudesCSD	= amplitudEspectralUniforme(comzos, ampMax)	parcialesCSD	= []						for v, w, x, y, z in zip(instrFracts, comzos, durs, amplitudesCSD, frecs):		noteCSD = ("i%s %s %s %s %s" %(1 + v, w, x, y, z))		parcialesCSD.append(noteCSD)	return parcialesCSD


def notaI2(instrFracts, comzos, durs, amps, frecs):
	""" M_todo para un espectro distorsionado usando el instrumento 1."""

	parcialesCSD = []			for v, w, x, y, z in zip(instrFracts, comzos, durs, amps, frecs):		noteCSD = ("i%s %s %s %s %s" %(1 + (v * .001), w, x, y, z))		parcialesCSD.append(noteCSD)	return parcialesCSD


def notaI3(instrFracts, comzos, durs, amps, frecs, frecs2):
	""" M_todo para un espectro distorsionado usando el instrumento 1."""

	parcialesCSD = []			for u, v, w, x, y, z in zip(instrFracts, comzos, durs, amps, frecs,
								frecs2):		noteCSD = ("i%s %s %s %s %s %s" %(2 + (u * .001), v , w, x, y, z))		parcialesCSD.append(noteCSD)	return parcialesCSD


def notaIprueba(comzos, durs, ampMax, frecs):
	""" M_todo para una porcion de espectro distorsionado usando el instrumento 1."""

	amplitudesCSD	= amplitudEspectralUniforme(range(377), ampMax)	parcialesCSD	= []						for  y, z in zip(amplitudesCSD, frecs):		noteCSD = ("i1 %s %s %s %s" %(comzos, 2, y, z))		parcialesCSD.append(noteCSD)	return parcialesCSD

