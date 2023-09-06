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
hoy = now.strftime("%Y%m%d")
end_date = now + datetime.timedelta(1)
#end_date = end_date.strftime("%d/%m/%Y")

data = pandas.read_csv('C:/Users/um9137/Documents/Automation Anywhere Files/Automation Anywhere/My Tasks/01. Automatizaciones 2020/11. Estatus Extendidos/1. Entrada/REx.csv', encoding="latin-1",engine='python')
#data = pandas.read_csv('C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/REx.csv', encoding="latin-1",engine='python')
data2 = pandas.DataFrame(columns=["Reclamo","Estatus","Fecha de Adición","Fecha Actual","Días Transcurridos"])
#todos recipientes son iguales
recipents = #'bo.mexico@eficasiacentrodecontacto.mx', 'gestor.mexico@eficasiacentrodecontacto.mx', 'enrique.velazquez@eficasiacentrodecontacto.mx', 'rodrigo.luviano@eficasiacentrodecontacto.mx','jorge.rivera@assurant.com'
holidays = ['2020-01-01','2020-02-05','2020-03-16','2020-05-01','2020-09-16','2020-11-16','2020-12-25']


r = -1
for index, row in data.iterrows():
 r = r+1
 r1 = -1
 start_date = time.strptime(data.iloc[r,2], "%d/%m/%Y")
 start_date = datetime.datetime(*start_date[:6])
 ts = pandas.Timestamp(start_date)
 ts2 = pandas.Timestamp(now)
 h= (pandas.bdate_range(start=ts,end=ts2,freq='C',holidays=holidays)).size
 data2=data2.append({'Reclamo': data.iloc[r,0],'Estatus': data.iloc[r,43],'Fecha de Adición': data.iloc[r,2],'Fecha Actual': now.strftime("%d/%m/%Y"),'Días Transcurridos': h},ignore_index=True)
 if str(data.iloc[r,4]) == 'A' or str(data.iloc[r,4]) == 'P':
 #1
  if str(data.iloc[r,43].strip()) == 'Pending acceptance from SP':
   if h >= 2:
    print("1")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 2 días favor de contactar a TFM para a solicitud de pantallas.'
    msg = EmailMessage()
    msg.set_charset('latin-1')
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
 #2
  if str(data.iloc[r,43].strip()) == 'Customer documentation not completed':
   if h >= 90:
    print("2")
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
  if str(data.iloc[r,43].strip()) == 'Customer documentation completed':
   if h >= 1:
    print("3")
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
  if str(data.iloc[r,43].strip()) == 'En trasporte':
   if h >= 3:
    print("4")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 3 días favor de validar la guía o la visita al CSA.'
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
  if str(data.iloc[r,43].strip()) == 'Diagnostico requerido':
   if h >= 2:
    print("5")
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
  if str(data.iloc[r,43].strip()) == 'Irreparable':
   if (now - start_date) >= datetime.timedelta(hours=24):
    print("6")
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
  if str(data.iloc[r,43].strip()) == 'Deducible informado al cliente':
   if h >= 4:
    print("7")
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
  if str(data.iloc[r,43].strip()) == 'Deducible pagado':
   if (now - start_date) >= datetime.timedelta(hours=24):
    print("8")
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
  if str(data.iloc[r,43].strip()) == 'Deducible Recibido':
   if (now - start_date) >= datetime.timedelta(hours=24):
    print("9")
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
  if str(data.iloc[r,43].strip().strip()) == 'Reparado':
   if h >= 3:
    print("10")
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
  if str(data.iloc[r,43].strip()) == 'Reemplazo aprobado':
   if h >= 3:
    print("11")
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
  if str(data.iloc[r,43].strip()) == 'Reemplazo enviado':
   if h >= 3:
    print("12")
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
  if str(data.iloc[r,43].strip()) == 'Cliente desiste del seguro':
   if h >= 1:
    print("13")
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
  if str(data.iloc[r,43].strip()) == 'Claim Denied':
   if h >= 1:
    print("14")
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
  if str(data.iloc[r,43].strip()) == 'Cliente no contactado en llamada 1':
   if h >= 1:
    print("15")
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
  if str(data.iloc[r,43].strip()) == 'Cliente no contactado en llamada 2':
   if h >= 1:
    print("16")
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
  if str(data.iloc[r,43].strip()) == 'Cliente no contactado en llamada 3':
   if h >= 1:
    print("17")
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
 #18
  if str(data.iloc[r,43].strip()) == 'En espera de documentación':
   if h >= 90:
    print("18")
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
 #19
  if (str(data.iloc[r,43].strip()) == '') is True:
   if h >= 90:
    print("19")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim no tiene estatus extendido asociado, favor de agregarlo.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()


r1 = -1
for index, row in data.iterrows():
 r1 = r1+1
 if str(data.iloc[r1,4]) == 'A' or str(data.iloc[r1,4]) == 'P':
 #Monto
  if (int(data.iloc[r1,9]) == 0) is True:    
   print("Monto")
   title = 'Claim ' + str(data.iloc[r1,0])+ ' | '+ str(data.iloc[r1,17])
   text = 'Hola a todos:\n\nEl claim tiene monto 0, favor de agregar un monto correcto.'
   msg = EmailMessage()
   msg['Subject'] = title
   msg['From'] = 'rpa.estatusextendidos@assurant.com'
   msg['To'] = recipents
   msg.set_content(text)
   # Send the message via our own SMTP server.
   s = smtplib.SMTP(host='10.80.192.32', port=25)
   s.send_message(msg)
   s.quit()
	
data2.sort_values(by='Días Transcurridos', ascending=False, na_position='first')
#data2.to_csv("C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/Resumen_"+hoy+ ".csv", sep=',',index=False, encoding="latin-1")
data2.to_csv("C:/Users/um9137/Documents/Automation Anywhere Files/Automation Anywhere/My Tasks/01. Automatizaciones 2020/11. Estatus Extendidos/2. Salida/Resumen_"+hoy+ ".csv", sep=',',index=False, encoding="latin-1")
