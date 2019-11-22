## Contains classes that collect numeric utilities.
from math import sqrt

class Series(object):
	""" Contains methods to generate the following numeric series: even,
	odd, fibo (fibonacci), and prime.
	"""
	def __init__(self, harmonic):
		""" The initialization parameter should be 0 or 1. When zero is
		chosen, the methods construct series with as many elements as
		desired. If the value is one, the series are limited to a number
		of elements, depending on the series. The criterium fot the
		limit is: 20 (minimum audible frequency) elevated to the last
		value of the series has to be less than 20,000 (maximum audible
		frequency).
		harmonic	---> 0 for any series, 1 for spectral-purpose series
		"""
		if not harmonic or harmonic ==1:
			self.harmonic = harmonic
		else:
			print 'Initialization parameter must be 0 or 1'

	def even(self, noOfElmnts):		""" Constructs an even-number series of noOfElements.
		noOfElements	---> the desired elements in the series
		"""		evenLst    = []
		even        = 2
		# If series is intended for a harmonic series, limit the value
		#to the audible range (controlled by the self.harmonic).
		if self.harmonic == 1 and noOfElmnts > 500:			noOfElmnts = 500

		for x in xrange(noOfElmnts):			evenLst.append(even)			even = even + 2		return evenLst	def odd(self, noOfElmnts):		""" Constructs an odd-number series of noOfElements.
		noOfElements	---> the desired elements in the series
		"""		oddLst    = []		odd         = 1		counter     = 0
		# If series is intended for a harmonic series, limit the value
		#to the audible range (controlled by the self.harmonic).
		if self.harmonic == 1 and noOfElmnts > 499:			noOfElmnts = 499				for x in xrange(noOfElmnts):			oddLst.append(odd)			odd = odd+2		return oddLst
	def fibo(self, noOfElmnts):		""" Constructs a fibonacci-number series of noOfElements.
		noOfElements	---> the desired elements in the series		"""		fiboLst    = []		a           = 0		b           = 1
		# If series is intended for a harmonic series, limit the value
		#to the audible range (controlled by the self.harmonic), and do
		#not repeat 1 at the beginning of the series (i.e. don't double
		#the fundamental.
		if self.harmonic == 1 and noOfElmnts > 14:			noOfElmnts = 14
			a = 1				for x in xrange(noOfElmnts):			fiboLst.append(b)			a, b = b, a+b		return fiboLst	def prime(self, noOfElmnts):
		""" Constructs a prime-number series of noOfElements.
		noOfElmnts	---> the desired elements in the series
		"""		primeLst    = []		candidate   = 2		counter     = 0
		# If series is intended for a harmonic series, limit the value
		#to the audible range (controlled by the self.harmonic).
		if self.harmonic == 1 and noOfElmnts > 168:			noOfElmnts = 168		while counter < noOfElmnts:			maxTest = int(sqrt(candidate)) + 1			for x in range(2, maxTest):				if candidate % x == 0:					candidate += 1					break			else:				primeLst.append(candidate)				candidate += 1				counter += 1		return primeLst


	def geometr(self, strt, noOfElmnts):
		""" Constructs a list of geometrical values, where the starting
		point is the power.
		strt		---> a number from which to begin.
		noOfElmnts	---> noOfElmnts	---> the desired elements in the
						series
		return		--> a geometrical list
		"""
		geoLst	= [1]

		for x in xrange(noOfElmnts - 1):
			lastVal = geoLst[-1]
			newVal = lastVal * strt
			geoLst.append(newVal)
		return geoLst


	def logar(self, hastaNo, noDeElementos, reverse=0):
		"""
		"""
		pasos	= noDeElementos - 1
		poder	= 1.0 / pasos
		unPaso	= pow(hastaNo, poder)

		logaritmicos = [1]

		for x in range(pasos):
			nuevoValor = logaritmicos[-1] * unPaso
			logaritmicos.append(nuevoValor)

		if reverse == 1:
			intrvls = self.serToIntrvl(logaritmicos)
			intrvls.reverse()
			retrgrdSeries = self.intrvlsToSer(intrvls, logaritmicos[0])
			logaritmicos = retrgrdSeries
		return logaritmicos


	def serToIntrvl(self, lst):
		""" Converts a list of points into a list of intervals.
		"""
		intrvls = []

		a = lst[0]
		for x in lst:
			newIntrvl = x - a
			intrvls.append(newIntrvl)
			a = x
		intrvls.pop(0)
		return intrvls


	def intrvlsToSer(self, intrvls, strt):

		newLst	= [strt]

		for x in intrvls:
			elmnt = x + newLst[-1]
			newLst.append(elmnt)
		return newLst

########

class Scaling(object):
	""" Contains methods for scaling values or lists.
	"""
	def lstToTotl(self, aList, newTotl):
		"""Scales the values in aList so they add up to a new total.
		aList	---> the list to scale
		newTotl	---> the sum of all elements of the scaled list
		return	--> a scaled list
		"""
		oldTotl	= 0.0
		newLst		= []

		for x in aList:
			oldTotl += x

		if oldTotl:
			scaleFactor = newTotl / oldTotl
		else:
			scaleFactor = newTotl

		for x in aList:
			newVal = x * scaleFactor
			newLst.append(newVal)
		return newLst


	def valToRng(self, val, oldMin, oldMax, newMin, newMax):		"""Scales a value within a range to it's equivalent in a new range.
		val		---> the value to be scaled.
		oldMin	---> the minimum of the old range
		oldMax	---> the maximum of the old range
		newMin	---> the minimum of the new range
		newMax	---> the maximum of the new range
		return 	--> a scaled value
		"""		oldRng = (oldMax*1.0) - oldMin		newRng = newMax - newMin		ratio = newRng/oldRng		scaledVal	= ((val - oldMin) * ratio + newMin)		return scaledVal
########

class Interpol(object):
	""" Contains methods for interpolation.
	"""
	def gradlLstsLin(self, original, target):
		""" Returns a list where the first value comes from the original
		list, the last one from the target, and in-between values that 			incrementally approach the target. The interpolation is linear.
		"""
		newLst		= []
		noOfStps	= len(target)
		counter		= 0

		for x in xrange(noOfStps):
			if len(original) != len(target):
				print 'Interpol: lists must be the same size'
				break
			dist = target[counter] - original[counter]
			oneStp = float(dist) / noOfStps
			partlInrpl = original[counter] + (oneStp * (counter + 1))
			newLst.append(partlInrpl)
			counter += 1
		return newLst
			
