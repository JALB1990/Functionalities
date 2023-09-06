import requests
import json
import pandas as pd
import numpy as np
import em_ch
import Constants as keys

url = keys.url_report
headers = keys.headers

#contact_input = str(input()).lower()

def report_email(contact_input):
 response_email = requests.post(url, headers=headers,json={
 "id": 100127,
 "filters": [{
    "name": "Email",
    "values": [
        contact_input
    ]
    }]
 })
 data_100127 = response_email.json()
 return data_100127

def report_employee(contact_input):
 response_employee = requests.post(url, headers=headers,json={
 "id": 100127,
 "filters": [{
    "name": "Employee ID",
    "values": [
        contact_input
    ]
    }]
 })
 data_100127 = response_employee.json()
 return data_100127

def transform_data(data_100127):
 list_rows_100127 = data_100127["rows"]
 list_cols_100127 = data_100127["columnNames"]
 df_100127 = pd.DataFrame(list_rows_100127, columns = list_cols_100127)
 return df_100127

def check(contact_input):
 if em_ch.check(contact_input) == True:
  data = report_email(contact_input)
  df = transform_data(data)
  if df.empty:
   return False
  else:
   contact_id = str(df.iloc[0,0]).lower()
   return(contact_id)
 elif em_ch.check(contact_input) == False:
  data = report_employee(contact_input)
  df = transform_data(data)
  if df.empty:
   return False
  else:
   contact_id = int(df.iloc[0,0])
   return(contact_id)
  


'''
response_email = requests.post(url, headers=headers,json={
"id": 100127,
"filters": [{
   "name": "Email",
   "values": [
       'A123'
   ]
   }]
})
data_100127 = response_email.json()
list_rows_100127 = data_100127["rows"]
list_cols_100127 = data_100127["columnNames"]
df_100127 = pd.DataFrame(list_rows_100127, columns = list_cols_100127)
df_100127.iloc[0,0]
'''