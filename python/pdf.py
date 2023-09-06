#!/usr/bin/python
# -*- coding: latin-1 -*-
import pathlib
import pdfrw
import pandas
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
	

#garantia extendida
now = datetime.now()
data = pandas.read_csv('C:/Users/KX0690/Desktop/PDF/SD0420200812.csv', delimiter="¦", encoding="latin-1",engine='python',skiprows=1,header=None, dtype={13:str, 21:str})
data.fillna(" ", inplace = True) 
amzpcc = pandas.read_csv('C:/Users/KX0690/Desktop/PDF/OFFRDSPC.csv',encoding="latin-1",engine='python')
data[26]=data[26].apply(lambda x: '{0:0>8}'.format(x))
data[26]=data[26]

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = []
    for page in template_pdf.pages[:3]:
     annotations.extend(page.Annots or [])
     for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
                    annotation.update(pdfrw.PdfDict(Ff=1))
    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)





r = -1
for index, row in data.iterrows():
 r1 = -1
 suma_asegurada = float(data.iloc[r,3])
 prima_neta = float(data.iloc[r,6])
 iva = float(data.iloc[r,6]*0.16)
 prima_total = float(data.iloc[r,6])*1.16
 phone = str(data.iloc[r,22])
 rfc = str(data.iloc[r,13])
 marca = str(data.iloc[r,29])
 modelo = str(data.iloc[r,30])
 if (pandas.isnull(data.iloc[0,22]) == True):
  phone = str(data.iloc[r,21])
  if (pandas.isnull(data.iloc[r,13]) == True):
   phone = str(data.iloc[r,21])
  if (pandas.isnull(data.iloc[r,29]) == True):
   phone = str(data.iloc[r,21])
  if (pandas.isnull(data.iloc[r,30]) == True):
   phone = str(data.iloc[r,21])
 now = datetime.now()
 fec_com=data.iloc[r,26],
 d,m,y = str(fec_com)[2:4],str(fec_com)[4:6],str(fec_com)[6:10]
 fec_fin_str = d+m+y
 fec_fin_con = datetime.strptime(fec_fin_str, '%d%m%Y')
 pro_cod = data.iloc[r,27]
 for index, row in amzpcc.iterrows():
  r1 = r1 + 1
  if pro_cod == amzpcc.iloc[r1,1]:
   print(pro_cod,amzpcc.iloc[r1,1],amzpcc.iloc[r1,3],amzpcc.iloc[r1,4])
   tip_pro=(amzpcc.iloc[r1,3])
   mnm = (amzpcc.iloc[r1,4])
   meses = relativedelta(months=mnm)
   fec_fin = fec_fin_con + meses
   y1,m1,d1=str(fec_fin)[:4],str(fec_fin)[5:7],str(fec_fin)[8:10]
  #else: tip_pro = "Sin Product Code Conversion"
   if tip_pro == "Consolas":
     num_eve = "2 Eventos"
     break
   elif tip_pro != "Consolas": 
    num_eve = "1 Evento en los primeros 12 meses"
    break
 data_dict = {
   'Número de Póliza': str(data.iloc[r,12]),
   'Nombre del Contratante': "Assurant Servicios de México S.A de C.V.",
   'RFC': "ASM031117DR4",
   'Domicilio Actual del Contratante Calle y Número': "Av. Insurgentes Sur 2453-301 Col. Tizapán C.P. 01090 Ciudad de México, México",
   'Nombre del Asegurado': str(data.iloc[r,14]),
   'RFC_2': str(data.iloc[r,13]),
   'Domicilio Actual del Asegurado Calle y Número': str(data.iloc[r,16])+" "+str(data.iloc[r,18])+" "+str(data.iloc[r,20])+" "+str(data.iloc[r,19]),
   'Día': d,
   'Mes': m,
   'Año': y,
   'Día_2': d,
   'Mes_2': m,
   'Año_2': y,
   'Día_3': d1,
   'Mes_3': m1,
   'Año_3': y1,
   'Moneda': str(data.iloc[r,25]),
   'Tipo': tip_pro,
   'Marca y Modelo': str(data.iloc[r,2]),
   'Número de Serie': str(data.iloc[r,31]),
   'Identidad Internacional del Equipo Móvil IMEI': str(data.iloc[r,31]),
   'Número de Teléfono DN': str(data.iloc[r,21]),
   'Coberturas Contratadas': "Daño Accidental",
   'por evento': str("%.2f" %suma_asegurada),
   'durante toda la vigencia': num_eve,   
   'Deducible': "30% Sobre Suma Asegurada Máxima",   
   'Prima Neta': str("%.2f" %prima_neta),
   'Gastos de expedición': "0.00",
   'Prima Antes de Impuestos': str("%.2f" %prima_neta),
   'IVA': str("%.2f" %iva),
   'Prima Total': ("%.2f" %prima_total),
   'Dia2': d,
   'Mes2': m,
   'Año2': y,
   'undefined': "Firma",
   #'quedaron registradas ante la Comisión Nacional de Seguros y Fianzas a partir del día': "29",
   #'con el número': "CNSF-S0067-0298-2020",
   #'de_3': "junio de 2020",
   #'Número RECAS': "CONDUSEF-004431-01"
 }
 r=r+1
 INVOICE_TEMPLATE_PATH = 'C:/Users/KX0690/Desktop/PDF/OfficeDepot.pdf'
 INVOICE_OUTPUT_PATH = os.path.join('C:/Users/KX0690/Desktop/PDF/salida/' + str(r) + str(now.strftime("%d%m%Y %H%M%S%f")) + '.pdf')
 write_fillable_pdf(INVOICE_TEMPLATE_PATH,INVOICE_OUTPUT_PATH,data_dict)

 
 
 