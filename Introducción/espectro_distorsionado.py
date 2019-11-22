def espectroDistorsionado(fundamental, parciales, factorDeDistorsion):	"""Genera un espectro arm_nico distorsionado iterando la funci_n s = f*(p elevado a la d), donde "f" es la fundamental, "p" el parcial y "d" el factor de distorsi_n"""	espectro = []		for x in parciales:		parcialDistorsionado = pow(x, factorDeDistorsion)		frecuenciaDeUnParcial = fundamental * parcialDistorsionado		if  frecuenciaDeUnParcial < 20000 :
			frecuenciaDeUnParcial = round(frecuenciaDeUnParcial, 3)
			espectro.append(frecuenciaDeUnParcial)		else:
			print 'Umbral audible rebasado en espectroDistorsionado'			break	return espectro
