#!/usr/bin/python
# -*- coding: latin-1 -*-
import pathlib
import pdfrw
import pandas
import os
import time
import datetime
#from datetime import datetime, datetime.timedelta #(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
from dateutil.relativedelta import relativedelta
import smtplib
from email.message import EmailMessage

now = datetime.datetime.now()
#hoy = now.strftime("%d/%m/%Y")
end_date = now + datetime.timedelta(1)
#end_date = end_date.strftime("%d/%m/%Y")

data = pandas.read_csv('C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/Reporte de Elita con status Extendidos.csv', encoding="latin-1",engine='python')
#todos recipientes son iguales
recipents = 'bernardo.perez@assurant.com,jose.laguna@assurant.com' #bo.mexico@eficasiacentrodecontacto.mx>, gestor.mexico@eficasiacentrodecontacto.mx, enrique.velazquez@eficasiacentrodecontacto.mx, rodrigo.luviano@eficasiacentrodecontacto.mx,jorge.rivera@assurant.com


r = -1
for index, row in data.iterrows():
 r = r+1
 r1 = -1
 start_date = time.strptime(data.iloc[r,2], "%d/%m/%Y")
 start_date = datetime.datetime(*start_date[:6])
 if str(data.iloc[r,4]) == 'A':
 #1
  if str(data.iloc[r,43]) == 'Pending acceptance from SP':
   if (now - start_date) >= datetime.timedelta(days=2):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 2 días favor de contactar a TFM para a solicitud de pantallas.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #2
  if str(data.iloc[r,43]) == 'Customer documentation not completed':
   if (now - start_date) >= datetime.timedelta(days=90):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 90 días favor de contactar al cliente para saber si quiere continuar con su reclamo.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #3
  if str(data.iloc[r,43]) == 'Customer documentation completed':
   if (now - start_date) >= datetime.timedelta(days=1):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\n El claim ha excedido el SLA de 1 día favor de pasar al siguiente paso del proceso.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #4
  if str(data.iloc[r,43]) == 'En trasporte':
   if (now - start_date) >= datetime.timedelta(days=3):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 3 días favor de validar la guía o la visia al CSA.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #5
  if str(data.iloc[r,43]) == 'Diagnostico requerido':
   if (now - start_date) >= datetime.timedelta(days=2):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 2 días favor de solicitar el reporte técnico al CSA.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #6
  if str(data.iloc[r,43]) == 'Irreparable':
   if (now - start_date) >= datetime.timedelta(hours=24):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 1 día favor de pasar al siguiente paso del proceso.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #7
  if str(data.iloc[r,43]) == 'Deducible informado al cliente':
   if (now - start_date) >= datetime.timedelta(days=4):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 4 días favor de contactar al cliente para saber si quiere pagar su deducible.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #8
  if str(data.iloc[r,43]) == 'Deducible pagado':
   if (now - start_date) >= datetime.timedelta(hours=24):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 1 día favor de pasar al siguiente paso del proceso.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #9
  if str(data.iloc[r,43]) == 'Deducible Recibido':
   if (now - start_date) >= datetime.timedelta(hours=24):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 1 día favor de pasar contactar a mariana.rodriguez@assurant.com para la validación.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #10
  if str(data.iloc[r,43]) == 'Reparado':
   if (now - start_date) >= datetime.timedelta(days=3):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 3 días favor de validar la guía.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #11
  if str(data.iloc[r,43]) == 'Reemplazo aprobado':
   if (now - start_date) >= datetime.timedelta(days=3):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 7 días favor de contactar al cliente para saber si ya tiene su equipo.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #12
  if str(data.iloc[r,43]) == 'Reemplazo enviado':
   if (now - start_date) >= datetime.timedelta(days=3):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 3 días favor de validar la guía.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit() 
 #13
  if str(data.iloc[r,43]) == 'Cliente desiste del seguro':
   if (now - start_date) >= datetime.timedelta(days=1):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nFavor de cerrar el claim.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #14
  if str(data.iloc[r,43]) == 'Claim Denied':
   if (now - start_date) >= datetime.timedelta(days=1):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nFavor de cerrar el claim.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #15
  if str(data.iloc[r,43]) == 'Cliente no contactado en llamada 1':
   if (now - start_date) >= datetime.timedelta(days=1):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nFavor de contactar al cliente.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #16
  if str(data.iloc[r,43]) == 'Cliente no contactado en llamada 2':
   if (now - start_date) >= datetime.timedelta(days=1):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nFavor de contactar al cliente.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #17
  if str(data.iloc[r,43]) == 'Cliente no contactado en llamada 3':
   if (now - start_date) >= datetime.timedelta(days=1):
    print("hola")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nFavor de cerrar el claim. '
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()

