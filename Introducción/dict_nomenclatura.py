def diccionarioDeDinamicas(fff=32000):
	ff		= fff * 0.5
	f		= ff  * 0.5
	mf		= f * 0.5
	mp		= mf * 0.5
	p		= mp * 0.5
	pp		= p * 0.5
	ppp		= pp * 0.5
	dinamicas	= {'ppp': ppp, 'pp': pp, 'p': p, 'mp': mp, 'mf': mf, 'f': f, 'ff': ff, 'fff': fff}
	return dinamicas
