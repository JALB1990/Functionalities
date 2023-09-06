#!/usr/bin/python
# -*- coding: latin-1 -*-
import pathlib
import pdfrw
import pandas
import os
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
	

now = datetime.now()
start_date = now.strftime("%m/%d/%Y")
end_date = now + timedelta(1)
end_date = end_date.strftime("%m/%d/%Y")

data = pandas.read_csv('C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/PS_Template_pricingMatrix.csv', encoding="latin-1",engine='python', skiprows=1)
data = data.astype({"Precio con IVA ": float})
data.replace('-',0)
data.replace('%',"")
data.replace('$',"")

#data2 = pandas.read_csv('C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/MatrizDePrecios.csv', encoding="latin-1",engine='python', skiprows=1)
amzpcc = pandas.read_csv('C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/AMZPCC.csv',encoding="latin-1",engine='python')
info = ['OPERATION','DEALER','EFFECTIVE','EXPIRATION','COVERAGE_TYPE','PRODUCT_CODE','CERTIFICATE_DURATION','COVERAGE_DURATION','OFFSET_TO_START','LOW_PRICE','HIGH_PRICE','GROSS_AMT','COMMISSIONS_PERCENT','MARKETING_PERCENT','ADMIN_EXPENSE','PROFIT_EXPENSE','LOSS_COST_PERCENT','LIABILITY_LIMIT','DEDUCTIBLE','LIABILITY_LIMIT_PERCENT','IS_CLAIM_ALLOWED','USE_COVERAGE_START_DATE','DEDUCTIBLE_PERCENT','DEDUCTIBLE_BASED_ON','AGENT_CODE','MARKUP_DISTRIBUTION_PERCENT','COV_LIABILITY_LIMIT','COV_LIABILITY_LIMIT_PERCENT','REPAIR_DISCOUNT_PCT','REPLACEMENT_DISCOUNT_PCT','METHOD_OF_REPAIR','OFFSET_TO_START_DAYS','OFFSET_METHOD','RECOVER_DEVICE','IS_REINSURED','DEF_REINS_STATUS','GROSS_AMOUNT_PERCENT','RENEWAL_NUMBER','COV_CLAIM_LIMIT','TAX_TYPE_XCD','REGION_DESCRIPTION','COMMISSIONS_PERCENT_SOURCE_XCD','MARKETING_PERCENT_SOURCE_XCD','ADMIN_EXPENSE_SOURCE_XCD','PROFIT_PERCENT_SOURCE_XCD','LOSS_COST_PERCENT_SOURCE_XCD','FULFILLMENT_PROVIDER_XCD','LINE_NUMBER']
df = pandas.DataFrame(columns = info)
#df.fillna(0)

r = -1
for index, row in data.iterrows():
 r = r+1
 r1 = -1
 pro_cod_conv = data.iloc[r,1]
 comision = float(data.iloc[r,11])
 marketing = float(data.iloc[r,12])
 admin = float(data.iloc[r,13])
 profit  = float(data.iloc[r,14])
 reserva = float(data.iloc[r,15])
 if str(data.iloc[r,0]) == 'Extended':
  dealer_code = 'EA12'
 if str(data.iloc[r,0]) == 'Accidental':
  dealer_code = 'SD02'
 for index, row in amzpcc.iterrows():
  r1 = r1 + 1
  if pro_cod_conv == amzpcc.iloc[r1,2]:
   pro_cod =(amzpcc.iloc[r1,1])
   total_per = comision + marketing + admin + profit + reserva
 total = float("%.4f" %total_per)
 if total > 100.0000:
  while total > 100.0000:
   if profit == 0.0000:
    admin = float("%.4f" %admin) - 0.0001
    total_per = comision + marketing + float("%.4f" %admin) + profit + reserva
    total = float("%.4f" %total_per)
   if profit > 0.0000:
    profit = float("%.4f" %profit) - 0.0001
    total_per = comision + marketing + admin + float("%.4f" %profit) + reserva
    total = float("%.4f" %total_per)
 if total < 100.0000:
  while total < 100.0000:
   profit = float("%.4f" %profit) + 0.0001
   total_per = float(comision) + float(marketing) + float(admin) + float("%.4f" %profit) + float(reserva)
   total = float("%.4f" %total_per)
 df = df.append({'OPERATION': 'A',
   'DEALER': dealer_code,
   'EFFECTIVE': start_date,
   'EXPIRATION': end_date,
   'COVERAGE_TYPE': data.iloc[r,0],
   'PRODUCT_CODE': pro_cod,
   'CERTIFICATE_DURATION': data.iloc[r,3],
   'COVERAGE_DURATION': data.iloc[r,4],
   'OFFSET_TO_START': data.iloc[r,5],
   'LOW_PRICE': data.iloc[r,6],
   'HIGH_PRICE': data.iloc[r,7],
   'GROSS_AMT': str("%.2f" %data.iloc[r,8]),
   'COMMISSIONS_PERCENT': str("%.4f" %comision),
   'MARKETING_PERCENT': str("%.4f" %marketing),
   'ADMIN_EXPENSE': str("%.4f" %admin),
   'PROFIT_EXPENSE': str("%.4f" %profit),
   'LOSS_COST_PERCENT': str("%.4f" %reserva),
   'LIABILITY_LIMIT': '0',
   'DEDUCTIBLE': data.iloc[r,23],
   'LIABILITY_LIMIT_PERCENT': '100',
   'IS_CLAIM_ALLOWED': 'Y',
   'USE_COVERAGE_START_DATE': 'N',
   'DEDUCTIBLE_PERCENT': data.iloc[r,17],
   'DEDUCTIBLE_BASED_ON': 'FIXED',
   'AGENT_CODE': '',
   'MARKUP_DISTRIBUTION_PERCENT': '0',
   'COV_LIABILITY_LIMIT': '0',
   'COV_LIABILITY_LIMIT_PERCENT': '0',
   'REPAIR_DISCOUNT_PCT': '0',
   'REPLACEMENT_DISCOUNT_PCT': '0',
   'METHOD_OF_REPAIR': '',
   'OFFSET_TO_START_DAYS': '0',
   'OFFSET_METHOD': 'FIXED',
   'RECOVER_DEVICE': 'Y',
   'IS_REINSURED': 'N',
   'DEF_REINS_STATUS': '',
   'GROSS_AMOUNT_PERCENT': '',
   'RENEWAL_NUMBER': '',
   'COV_CLAIM_LIMIT': '',
   'TAX_TYPE_XCD': '',
   'REGION_DESCRIPTION': '',
   'COMMISSIONS_PERCENT_SOURCE_XCD': '',
   'MARKETING_PERCENT_SOURCE_XCD': '',
   'ADMIN_EXPENSE_SOURCE_XCD': '',
   'PROFIT_PERCENT_SOURCE_XCD': '',
   'LOSS_COST_PERCENT_SOURCE_XCD': '',
   'FULFILLMENT_PROVIDER_XCD': ''
   }, ignore_index=True)
 
 print(r)

df.to_csv('C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/File Name.csv', index = False)

