import requests
import json
import pandas as pd
import numpy as np
import em_ch
import Constants as keys

url = keys.url_report
headers = keys.headers

def report_incident(ref_number):
 response_incident = requests.post(url, headers=headers,json={
 "id": 100025,
 "filters": [{
    "name": "Name",
    "values": [
        ref_number
    ]
    }]
 })
 data_100025 = response_incident.json()
 return data_100025

def transform_data(data_100025):
 list_rows_100025 = data_100025["rows"]
 list_cols_100025 = data_100025["columnNames"]
 df_100025 = pd.DataFrame(list_rows_100025, columns = list_cols_100025)
 return df_100025

def check(ref_number):
 data = report_incident(ref_number)
 df = transform_data(data)
 if df.empty:
  return False
 else:
  status = str(df.iloc[0,7]).lower()
  return(status)