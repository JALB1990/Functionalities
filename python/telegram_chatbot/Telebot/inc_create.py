#TST2 Super user U1VQRVJVU0VSQURNSU46U1VTcGFzczEwNzJUU1RA
#TST2 Yo SkFMQUdVTkFCQVJCOlBhc3N3b3JkMQ==
#220879
from django.http import JsonResponse
from django.http import HttpRequest
import requests
import json
import pandas as pd
import numpy as np
import sqlite3 as sql
import Constants as keys

url = keys.url_inc
headers = keys.headers

def inc_create(contact_id,thread):
 incident = requests.post(url, headers=headers,json={
 "primaryContact":
    {
    "id": int(contact_id)
    },
 "subject": "Test Subject",
 "threads":
 {
 "channel":
  {
  "id":6 #1 = Inbound-Email, 2 = Outreach-Email, 3 = Phone, 4 = Fax, 5 = Post, 6 = text/Service web
  },  
 "entryType":
  {
  "id":2 # 1 = Private Note, 2 = Response
  },
 "text": thread,
 }
 })
 data = incident.json()
 df = pd.DataFrame.from_dict(data,orient='index')
 ref_number = df.iloc[1,0]
 return ref_number

'''
incident = requests.get(url, headers=headers,json={
"lookupName":"211207-000011"
})
try:
 cantidad = int(input("Dígame una cantidad en pesetas: "))
except:
 print("eso no es un numero")

###
incident = requests.post(url, headers=headers,json={
"primaryContact":
   {
   "id": 220879
   },
"subject": "Test Subject",
"threads":
{
"channel":
 {
 "id":6 #1 = Inbound-Email, 2 = Outreach-Email, 3 = Phone, 4 = Fax, 5 = Post, 6 = text/Service web
 },  
"entryType":
 {
 "id":2 # 1 = Private Note, 2 = Response
 },
"text": 'test',
}
})
if incident
data = incident.json()
df = pd.DataFrame.from_dict(data,orient='index')
ref_number = df.iloc[1,0]


'''
