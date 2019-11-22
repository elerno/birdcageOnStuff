from random import uniform

from escalado import escaladoANuevoTotal
def amplitudEspectralUniforme(espectro, dinamica):
	"""Genera una serie de amplitudes espectrales, con distribuci_n uniforme, cuya suma sea igual a din_mica. Los valores de din_mica van de 1=ppp a 8=fff"""
	ampsEspectrales	= []

	for x in espectro:        
		unaAmp = uniform(0.1, 1)		ampsEspectrales.append(unaAmp)	ampsEspectralesEscaladas = escaladoANuevoTotal(ampsEspectrales, dinamica)	return ampsEspectralesEscaladas
