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
import numpy as np


now = datetime.datetime.now()
hoy = now.strftime("%Y%m%d")
end_date = now + datetime.timedelta(1)
#end_date = end_date.strftime("%d/%m/%Y")

data = pandas.read_csv('C:/Users/um9137/Documents/Automation Anywhere Files/Automation Anywhere/My Tasks/01. Automatizaciones 2020/11. Estatus Extendidos/1. Entrada/REx.csv', encoding="latin-1",engine='python')
#data = pandas.read_csv('C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/REx.csv', encoding="latin-1",engine='python')
data = data.replace(np.nan, '', regex=True)
data2 = pandas.DataFrame(columns=["Reclamo","Estatus","Fecha de Adición","Fecha Actual","Días Transcurridos"])
#f= open('C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/Resumen_'+hoy+ ".txt","w+")
f= open('C:/Users/um9137/Documents/Automation Anywhere Files/Automation Anywhere/My Tasks/01. Automatizaciones 2020/11. Estatus Extendidos/1. Entrada/Resumen_'+hoy+ ".txt","w+")
#todos recipientes son iguales
recipents = 'jose.laguna@assurant','bernardo.perez@assurant.com'#'bo.mexico@eficasiacentrodecontacto.mx', 'gestor.mexico@eficasiacentrodecontacto.mx', 'enrique.velazquez@eficasiacentrodecontacto.mx', 'rodrigo.luviano@eficasiacentrodecontacto.mx','jorge.rivera@assurant.com'
holidays = ['2020-01-01','2020-02-05','2020-03-16','2020-05-01','2020-09-16','2020-11-16','2020-12-25']

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
c10 = 0
c11 = 0
c12 = 0
c13 = 0
c14 = 0
c15 = 0
c16 = 0
c17 = 0
c18 = 0
c19 = 0
c20 = 0


r = -1
for index, row in data.iterrows():
 r = r+1
 r1 = -1
 creation_date = time.strptime(data.iloc[r,2], "%m/%d/%Y")
 creation_date = datetime.datetime(*creation_date[:6])
 if (str(data.iloc[r,42].strip()) == '') == True:
  lestatus_date = creation_date
  
 else:
  lestatus_date = time.strptime(data.iloc[r,42], "%m/%d/%Y %H:%M")
  lestatus_date = datetime.datetime(*lestatus_date[:6])
 
 ts = pandas.Timestamp(creation_date)
 ts2 = pandas.Timestamp(now)
 ts3 = pandas.Timestamp(lestatus_date)
 h= (pandas.bdate_range(start=ts,end=ts3,freq='C',holidays=holidays)).size
 h1= (pandas.bdate_range(start=ts,end=ts2,freq='C',holidays=holidays)).size
 data2=data2.append({'Reclamo': data.iloc[r,0],'Estatus': data.iloc[r,43],'Fecha de Adición': data.iloc[r,2],'Fecha Actual': now.strftime("%d/%m/%Y"),'Días Transcurridos': h},ignore_index=True)
 if str(data.iloc[r,4]) == 'A' or str(data.iloc[r,4]) == 'P':
 #1
  if str(data.iloc[r,43].strip()) == 'Pending acceptance from SP':
   if h >= 2:
    print(str(data.iloc[r,0])+" Pending acceptance from SP")
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
    c1 += 1	
 #2
  if str(data.iloc[r,43].strip()) == 'Customer documentation not completed':
   if h >= 90:
    print(str(data.iloc[r,0])+" Customer documentation not completed")
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
    c2 += 1
 #3
  if str(data.iloc[r,43].strip()) == 'Customer documentation completed':
   if h >= 1:
    print(str(data.iloc[r,0])+" Customer documentation completed")
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
    c3 += 1
 #4
  if str(data.iloc[r,43].strip()) == 'En trasporte' or str(data.iloc[r,43].strip()) == 'In Transportation':
   if h >= 3:
    print(str(data.iloc[r,0])+" En trasporte")
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
    c4 += 1
 #5
  if str(data.iloc[r,43].strip()) == 'Diagnostico requerido' or str(data.iloc[r,43].strip()) == 'Diagnostic Required':
   if h >= 2:
    print(str(data.iloc[r,0])+" Diagnostico requerido")
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
    c5 += 1
 #6
  if str(data.iloc[r,43].strip()) == 'Irreparable' or str(data.iloc[r,43].strip()) == 'Irrepairable':
   if (now - creation_date) >= datetime.timedelta(hours=24):
    print(str(data.iloc[r,0])+" Irreparable")
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
    c6 += 1
 #7
  if str(data.iloc[r,43].strip()) == 'Deducible informado al cliente' or str(data.iloc[r,43].strip()) == 'Deductible Informed to the Client':
   if h >= 90:
    print(str(data.iloc[r,0])+" Deducible informado al cliente")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim ha excedido el SLA de 90 días favor de contactar al cliente para saber si quiere pagar su deducible.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
    c7 += 1
 #8
  if str(data.iloc[r,43].strip()) == 'Deducible pagado' or str(data.iloc[r,43].strip()) == 'Deductible paid':
   if (now - creation_date) >= datetime.timedelta(hours=24):
    print(str(data.iloc[r,0])+" Deducible pagado")
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
    c8 += 1
 #9
  if str(data.iloc[r,43].strip()) == 'Deducible Recibido' or str(data.iloc[r,43].strip()) == 'Deductible Received':
   if (now - creation_date) >= datetime.timedelta(hours=24):
    print(str(data.iloc[r,0])+" Deducible Recibido")
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
    c9 += 1
 #10
  if str(data.iloc[r,43].strip().strip()) == 'Reparado' or str(data.iloc[r,43].strip().strip()) == 'Equipment Repaired':
   if h >= 3:
    print(str(data.iloc[r,0])+" Reparado")
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
    c10 += 1
 #11
  if str(data.iloc[r,43].strip()) == 'Reemplazo aprobado' or str(data.iloc[r,43].strip()) == 'Replacement Approved':
   if h >= 7:
    print(str(data.iloc[r,0])+" Reemplazo aprobado")
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
    c11 += 1
 #12
  if str(data.iloc[r,43].strip()) == 'Reemplazo enviado' or str(data.iloc[r,43].strip()) == 'Replacement Sent':
   if h >= 3:
    print(str(data.iloc[r,0])+" Reemplazo enviado")
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
    c12 += 1
 #13
  if str(data.iloc[r,43].strip()) == 'Cliente desiste del seguro':
   if h >= 1:
    print(str(data.iloc[r,0])+" Cliente desiste del seguro")
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
    c13 += 1
 #14
  if str(data.iloc[r,43].strip()) == 'Claim Denied':
   if h >= 1:
    print(str(data.iloc[r,0])+" Claim Denied")
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
    c14 += 1
 #15
  if str(data.iloc[r,43].strip()) == 'Cliente no contactado en llamada 1':
   if h >= 1:
    print(str(data.iloc[r,0])+" Cliente no contactado en llamada 1")
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
    c15 += 1
 #16
  if str(data.iloc[r,43].strip()) == 'Cliente no contactado en llamada 2':
   if h >= 1:
    print(str(data.iloc[r,0])+" Cliente no contactado en llamada 2")
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
    c16 += 1
 #17
  if str(data.iloc[r,43].strip()) == 'Cliente no contactado en llamada 3':
   if h >= 1:
    print(str(data.iloc[r,0])+" Cliente no contactado en llamada 3")
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
    c17 += 1
 #18
  if str(data.iloc[r,43].strip()) == 'En espera de documentación' or str(data.iloc[r,43].strip()) == 'Waiting documentation':
   if h >= 90:
    print(str(data.iloc[r,0])+" En espera de documentación")
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
    c18 += 1
 #19
  if (str(data.iloc[r,43].strip()) == '') is True:
   if str(data.iloc[r,4]) == 'P' and h1 >= 90:
    print(str(data.iloc[r,0])+" En blanco")
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
    c19 += 1
   if str(data.iloc[r,4]) == 'A':
    print(str(data.iloc[r,0])+" En blanco")
    title = 'Claim ' + str(data.iloc[r,0])+ ' | '+ str(data.iloc[r,17])
    text = 'Hola a todos:\n\nEl claim no tiene estatus extendido asociado y está Activo, favor de agregarlo.'
    msg = EmailMessage()
    msg['Subject'] = title
    msg['From'] = 'rpa.estatusextendidos@assurant.com'
    msg['To'] = recipents
    msg.set_content(text)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(host='10.80.192.32', port=25)
    s.send_message(msg)
    s.quit()
    c19 += 1


r1 = -1
for index, row in data.iterrows():
 r1 = r1+1
 if str(data.iloc[r1,4]) == 'A' or str(data.iloc[r1,4]) == 'P':
 #Monto
  if (int(data.iloc[r1,9]) == 0) is True:    
   print(str(data.iloc[r,0])+" Monto")
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
   c20 += 1

if c1 != 0:
 print(str(c1)+ " Casos de: Pending acceptance from SP")
 f.write(str(c1)+ " Casos de: Pending acceptance from SP\r")
if c2 != 0:
 print(str(c2)+ " Casos de: Customer documentation not completed")
 f.write(str(c2)+ " Casos de: Customer documentation not completed\r")
if c3 != 0:
 print(str(c3)+ " Casos de: Customer documentation completed")
 f.write(str(c3)+ " Casos de: Customer documentation completed\r")
if c4 != 0:
 print(str(c4)+ " Casos de: En trasporte")
 f.write(str(c4)+ " Casos de: En trasporte\r")
if c5 != 0:
 print(str(c5)+ " Casos de: Diagnostico requerido")
 f.write(str(c5)+ " Casos de: Diagnostico requerido\r")
if c6 != 0:
 print(str(c6)+ " Casos de: Irreparable")
 f.write(str(c6)+ " Casos de: Irreparable\r")
if c7 != 0:
 print(str(c7)+ " Casos de: Deducible informado al cliente")
 f.write(str(c7)+ " Casos de: Deducible informado al cliente\r")
if c8 != 0:
 print(str(c8)+ " Casos de: Deducible pagado")
 f.write(str(c8)+ " Casos de: Deducible pagado\r")
if c9 != 0:
 print(str(c9)+ " Deducible Recibido")
 f.write(str(c9)+ " Deducible Recibido\r")
if c10 != 0:
 print(str(c10)+ " Casos de: Reparado")
 f.write(str(c10)+ " Casos de: Reparado\r")
if c11 != 0:
 print(str(c11)+ " Casos de: Reemplazo aprobado")
 f.write(str(c11)+ " Casos de: Reemplazo aprobado\r")
if c12 != 0:
 print(str(c12)+ " Casos de: Reemplazo enviado")
 f.write(str(c12)+ " Casos de: Reemplazo enviado\r")
if c13 != 0:
 print(str(c13)+ " Casos de: Cliente desiste del seguro")
 f.write(str(c13)+ " Casos de: Cliente desiste del seguro\r")
if c14 != 0:
 print(str(c14)+ " Casos de: Claim Denied")
 f.write(str(c14)+ " Casos de: Claim Denied\r")
if c15 != 0:
 print(str(c15)+ " Casos de: Cliente no contactado en llamada 1")
 f.write(str(c15)+ " Casos de: Cliente no contactado en llamada 1\r")
if c16 != 0:
 print(str(c16)+ " Casos de: Cliente no contactado en llamada 2")
 f.write(str(c16)+ " Casos de: Cliente no contactado en llamada 2\r")
if c17 != 0:
 print(str(c17)+ " Casos de: Cliente no contactado en llamada 3")
 f.write(str(c17)+ " Casos de: Cliente no contactado en llamada 3\r")
if c18 != 0:
 print(str(c18)+ " Casos de: En espera de documentación")
 f.write(str(c18)+ " Casos de: En espera de documentación\r")
if c19 != 0:
 print(str(c19)+ " Casos de: Estatus Extendido en Blanco")
 f.write(str(c19)+ " Casos de: Estatus Extendido en Blanco\r")
if c20 != 0:
 print(str(c20)+ " Casos de: Sin Monto")
 f.write(str(c20)+ " Casos de: Sin Monto\r")

f.close() 
	
data2.sort_values(by='Días Transcurridos', ascending=False, na_position='first')
#data2.to_csv("C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/Resumen_"+hoy+ ".csv", sep=',',index=False, encoding="latin-1")
data2.to_csv("C:/Users/um9137/Documents/Automation Anywhere Files/Automation Anywhere/My Tasks/01. Automatizaciones 2020/11. Estatus Extendidos/2. Salida/Resumen_"+hoy+ ".csv", sep=',',index=False, encoding="latin-1")
