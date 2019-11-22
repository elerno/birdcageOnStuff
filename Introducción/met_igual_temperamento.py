import math as m
import decimal as d

def alturasTemperadas(noDeAltura, modulo=12, referencia=53):
	step = m.pow(m.e, m.log(2) / modulo)
	altura = referencia * m.pow(step, noDeAltura)
	return altura

def octIgualTempNPasos(pasos, desdeFreq=20, hastaFreq=20000):
	alturas		= []
	contador	= 0

	while 1:
		altura = alturasTemperadas(contador, pasos, desdeFreq)
		if altura < hastaFreq:
			alturas.append(altura)
		else:
			break
		contador = contador + 1
	return alturas

def dictModuloNPasos(modulo, desdeFreq=20, hastaFreq=20000):
	todasAlturas	= octIgualTempNPasos(modulo, desdeFreq, hastaFreq)
	contador	= 0
	moduloStr	= str(modulo)
	divisorRem	= d.Decimal(1)
	dicccionario	= {'modulo': modulo}

	for x in moduloStr:
		divisorRem = divisorRem * d.Decimal('0.1')


	for x in todasAlturas:
		compLlave = divmod(contador, modulo)
		llave = str(d.Decimal(str(compLlave[0])) + (d.Decimal(str(compLlave[1])) * divisorRem))
		dicccionario[llave] = x
		contador = contador + 1
	return dicccionario
