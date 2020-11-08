from cryptography.fernet import Fernet

def GENERAR_KEY ():

    KEY = Fernet.generate_key()
    
    with open("../DefaultKey/Config/password.key","wb") as file:
        
        file.write(KEY)


def CARGAR_KEY ():

    return open("../DefaultKey/Config/password.key","rb").read()

def ENCRIPTADO_DE_ARCHIVOS (DATO,LLAVE):
	
	f = Fernet(LLAVE)
	
	with open (DATO ,"rb") as file :
		ARCHIVO_A_ENCRIPTAR = file.read()
	DATOS_ENCRIPTADOS = f.encrypt(ARCHIVO_A_ENCRIPTAR)
	with open (DATO, "wb") as file:
		file.write(DATOS_ENCRIPTADOS)

GENERAR_KEY()

LLAVE = CARGAR_KEY()
DATO = b"../DefaultKey/Config/password.enc"
ENCRIPTADO_DE_ARCHIVOS(DATO,LLAVE)

CORREO = b"../DefaultKey/Config/dato.enc"
ENCRIPTADO_DE_ARCHIVOS(CORREO,LLAVE)
