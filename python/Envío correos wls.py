#!/usr/bin/python
# -*- coding: latin-1 -*-
import pathlib
import pandas
import os
import time
import datetime
import smtplib
from email.message import EmailMessage

start_time = time.time()
data = pandas.read_csv('C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/Email.csv', encoding="latin-1",engine='python')
f= open("C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/Tiempo.txt","w+")
file_text = open("C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/Texto Email.txt","r")
text_msg = file_text.read()
r = -1
for index, row in data.iterrows():
 r = r+1
 now = datetime.datetime.now()
 hora=now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-4]
 recipent=str(data.iloc[r,0])
 title = 'Fin Soporte Internet Explorer 2021 - Compatibilidad WLS - Seguimiento a Pruebas'
 #text = 'Buen día por medio de la presente,\n\nEl navegador Internet Explorer dejará de ofrecer soporte en agosto del año 2021.\nPor lo que se necesita verificar que las aplicaciones listadas a continuación, puedan trabajar en su totalidad dentro de los exploradores Edge y Chrome\n\nEn caso de que exista alguna incidencia, será necesario levantar el ticket con los detalles para informarlo al equipo de internacional.\nFavor de compartir esta información y solicitud con todos los usuarios necesarios que ocupen estos sistemas:\n\n*WLS2\n*CRMIconnect\n*MR Connect\n\nCualquier duda o aclaración favor de contactar a jose.laguna@assurant.com\n\n***************************************\nSistemas Corporativos, Assurant México'
 text = text_msg
 msg = EmailMessage()
 msg['Subject'] = title
 msg['From'] = 'sistemas.corporativos@assurant.com'
 msg['To'] = recipent
 msg.set_content(text)
 s = smtplib.SMTP(host='10.80.192.32', port=25)
 s.send_message(msg)
 s.quit()
 print(str(data.iloc[r,0]))
 f.write("Email: "+recipent+" Hora de envío: "+hora+"\n\n")

f.close()

tiempo_total = "--- %s seconds ---" % (time.time() - start_time)
print(tiempo_total)
f = open("C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/Tiempo.txt")
contenido = f.read()
f.close()
title = 'Duración Ejecucion envío de Correo'
text = 'Tiempo total de ejecución: ' + tiempo_total + '\n\n' + contenido
msg = EmailMessage()
msg['Subject'] = title
msg['From'] = 'sistemas.corporativos@assurant.com'
msg['To'] = 'jose.laguna@assurant.com'
msg.set_content(text)
s = smtplib.SMTP(host='10.80.192.32', port=25)
s.send_message(msg)
s.quit()