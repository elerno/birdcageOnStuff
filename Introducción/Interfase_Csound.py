import csnd

## Importa los modulos definidos por el usuario.
import compilador_data_Csound as data

class ComunicacionConCsound:
	"""Contiene los metodos de comunicaci_n con Csound."""
	

	def __init__(self, opciones = data.opcionesCsound, orquesta = data.hacerOrquesta(), partitura =
			data.hacerPartitura()):
		"""Al ser instanciada (mediante el m_todo __init__), inicializa Csound con las opciones de l_nea de comando, la orquesta y la partitura."""
		self.csound = csnd.CppSound()
		self.csound.setPythonMessageCallback()
		self.csound.setCommand(opciones)
		self.csound.setOrchestra(orquesta)
		self.csound.setScore(partitura)

	def rendir(self):
		"""Rinde la partitura, produciendo un archivo de audio."""
		self.csound.exportForPerformance()
		self.csound.perform()
		self.csound.removeScore()

if __name__ == "__main__":
	instancia = ComunicacionConCsound()
	instancia.rendir()
