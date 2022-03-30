from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import PyQt5

def enviarCorreo(lista):
    try:
        msg = MIMEMultipart()
        message = lista[4]
        password = lista[1]  # "variable_password"
        msg['From'] = lista[0]  # "variable_address"
        msg['To'] = lista[3]  # "destinatario-gmail"
        msg['Subject'] = lista[2]
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        # create server
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print("successfully sent email to %s:" % (msg['To']))
        PyQt5.QtWidgets.QMessageBox.about(None, "Mensaje enviado", "El mensaje se envio exitosamente")
    except:
        print ('Algo Salio Mal, Intentelo Nuevamente')
        PyQt5.QtWidgets.QMessageBox.about(None, "Mensaje No enviado", "Verifique su username y password")
        pass