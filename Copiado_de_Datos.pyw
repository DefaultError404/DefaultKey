import subprocess
import getpass
import os.path as path
import shutil
import os
import subprocess

def borrarPantalla():
	
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")

USER_NAME = getpass.getuser()
RUTA_DE_INICIO_WINDOWS = 'C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'.format(USER_NAME)
RUTA_LINUX = '/usr/local/bin/'
TEMP = '../DefaultKey/temp/'
def SISTEMA_OPERATIVO_CON_PYTHON():

	if path.exists(RUTA_DE_INICIO_WINDOWS+'DefaultKey.pyw') == True:

		pass
	
	else:

		shutil.copy("DefaultKey.lnk", RUTA_DE_INICIO_WINDOWS)
                

def SISTEMA_OPERATIVO_SIN_PYTHON():

	if path.exists(RUTA_DE_INICIO_WINDOWS+'DefaultKeyPython.lnk') == True:

		pass
	
	else:
		shutil.copy("DefaultKeyPython.lnk", RUTA_DE_INICIO_WINDOWS)


def ELECCION():

	while True:
		print("El sistema es Windows o Linux <W o L>")
		print("")
		SISTEMA = input (">> ")
		if SISTEMA.upper() == "W" or SISTEMA.upper() == "WINDOWS":
			
			print("El sitema tiene instalado python <sí o no>")
			print("")
			RESPUESTA=input(">> ")
			
			if RESPUESTA.upper()=="N" or RESPUESTA.upper()=="NO":
				
				SISTEMA_OPERATIVO_SIN_PYTHON()
				break
			
			elif RESPUESTA.upper()=="S" or RESPUESTA.upper()=="SI":
				
				SISTEMA_OPERATIVO_CON_PYTHON()
				break
			else:
				print("Opcion no existente")
				
		elif SISTEMA.upper() == "L" or SISTEMA.upper() == "LINUX":

			ORIGEN = '../DefaultKey'
			shutil.copytree(ORIGEN,'temp')
			shutil.copytree(TEMP,RUTA_LINUX+"DefaultKey")
			shutil.rmtree(TEMP)
			os.system("chmod 777 /usr/local/bin/DefaultKey -R")
			break

		else:
			print("Opcion Inexistente")

                        
if __name__ == '__main__':

	ELECCION()
