import time

import INTRODUCCION
import prueba_distorsion_espectral2 as prueba

#Variables que contienen las opciones de Csound y los _tomos para construir la orquesta y partitura.
opcionesCsound		= 'csound -o %sBirdCageExtrapolation.wav -W -N -Z -d temp.orc temp.sco' %(time.strftime('%d-%m_%H.%M'))

encabezadoDeOrquesta	= """
sr = 44100	; sample rate
kr = 44100	; control rate
ksmps = 1		; sr/kr
nchnls = 1	; # of channels"""

instrumento1		= """

    instr 1

idur			= abs(p3)
iamp			= p4
ifreq			= p5
imindurenv		= idur - .007

ir		tival
i1	= -1
	tigoto nuevoenv
i1	= 0
kampenv		linseg 0, .002, iamp, imindurenv, iamp, .005, 0

nuevoenv:
if ir == 0 kgoto sonido
kmidenv		linseg 0.001, idur * 0.3, iamp * 0.5, idur * 0.70, 0.001
kampenv = kampenv - kmidenv

sonido:
asig		oscili kampenv, ifreq, 1, i1
    out asig
    endin
"""

instrumento2	= """

    instr 2

idur			= abs(p3)	; in seconds
iamp			= p4		; 0-32767
ifreq1			= p5		; in hz
ifreq2			= p6		; in hz
imindurenv		= idur - .007

kampenv		linseg 0, .002, iamp, imindurenv, iamp, .005, 0
kfreqgliss	expseg ifreq1, idur * 0.2 , ifreq1, idur * .7, ifreq2, idur * .1, ifreq2
asig		oscili kampenv, kfreqgliss, 1
    out asig
    endin
"""

instrumento3		= """

    instr 3

idur			= abs(p3)
iamp			= p4
ifreq			= p5
imindurenv		= idur - .04

kampenv		linseg 0, .02, iamp, imindurenv, iamp, .02, 0
akenv		oscili kampenv, ifreq, 1

anoise		noise 1, 0
afilter		butterbp anoise, ifreq, 1
abalance	balance afilter, akenv
    out abalance
    endin
"""

definicionesDeFunciones	= """
f1 0 16384 10 1

"""

def formatearLineasPartitura():
	#partituraEnLista = INTRODUCCION.compilacion()
	partituraEnLista = prueba.pruebaEspectra()
	partituraEnCuerda = ''

	for x in partituraEnLista:
		partituraEnCuerda = partituraEnCuerda + x + '\n'
	return partituraEnCuerda

def hacerOrquesta():
	orquesta = """%s%s%s%s""" %(encabezadoDeOrquesta, instrumento1, instrumento2, instrumento3)
	return orquesta



def hacerPartitura():
	partitura = """%s%s""" %(definicionesDeFunciones, formatearLineasPartitura())
	return partitura
