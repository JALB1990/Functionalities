from django.http import JsonResponse
from django.http import HttpRequest
import requests
import json
import pandas as pd
import numpy as np
import sqlite3 as sql

url = "https://quadgraphics.custhelp.com/services/rest/connect/v1.3/analyticsReportResults"
headers = {'Authorization':'Basic U1VQRVJVU0VSQURNSU46U1VTcGFzczEwNzJBRE1A'}

response_101096 = requests.post(url, headers=headers,json={
"id": 101096,
"filters": [{
    "name": "Date Created",
    "values": [
        "DATE_ADD(SYSDATE(), -1, DAYS, 1)",
        "DATE_ADD(SYSDATE(), 0, DAYS, 1)"
    ]
    }]
})
data_101096 = response_101096.json()
print("Status code: ", response_101096.status_code)
#print(data_101096)

response_101439 = requests.post(url, headers=headers,json={
"id": 101439,
"filters": [{
    "name": "Date Created",
    "values": [
        "DATE_ADD(SYSDATE(), -1, DAYS, 1)",
        "DATE_ADD(SYSDATE(), 0, DAYS, 1)"
    ]
    }]
})
data_101439 = response_101439.json()
print("Status code: ", response_101439.status_code)
#print(data_101439)

list_rows_101439 = data_101439["rows"]
list_cols_101439 = data_101439["columnNames"]
df_101439 = pd.DataFrame(list_rows_101439, columns = list_cols_101439)
date_created = df_101439.iloc[0,3]

list_rows_101096 = data_101096["rows"]
list_cols_101096 = data_101096["columnNames"]
df_101096 = pd.DataFrame(list_rows_101096, columns = list_cols_101096)
print(df_101096)
df_101096.to_csv (r'C:\Users\Ionock_Issha\Dropbox\Python\Django\New File Name.csv', index = None)

values_count_101096=df_101096['Source'].value_counts()



try:
  email_count = values_count_101096.loc['Email'].item()
  print(email_count)
except:
  email_count = 0
  print(email_count)

try:
  ask_count = values_count_101096.loc['Ask a Question'].item()
  print(ask_count)
except:
  ask_count = 0
  print(ask_count)

try:
  phone_count = values_count_101096.loc['Phone'].item()
  print(phone_count)
except:
  phone_count = 0
  print(phone_count)

try:
  chat_count = values_count_101096.loc['Chat'].item()
  print(chat_count)
except:
  chat_count = 0
  print(chat_count)

try:
  text_count = values_count_101096.loc['Text'].item()
  print(text_count)
except:
  text_count = 0
  print(text_count)

print(email_count)
print(ask_count)
print(phone_count)
print(chat_count)

total_email = email_count+ ask_count
print(total_email)

total_today = total_email+phone_count+chat_count#


try:
  h = df_101439.query('`Product ID`=="Crisis Management"')
  topic_01_count = h.iloc[0,2]
  print(topic_01_count)
except:
  topic_01_count = 0
  print(topic_01_count)

try:
  h = df_101439.query('`Product ID`=="Vacation / Sabbatical"')
  topic_02_count = h.iloc[0,2]
  print(topic_02_count)
except:
  topic_02_count = 0
  print(topic_02_count)

try:
  h = df_101439.query('`Product ID`=="Crisis Management Vaccine"')
  topic_03_count = h.iloc[0,2]
  print(topic_03_count)
except:
  topic_03_count = 0
  print(topic_03_count)

try:
  h = df_101439.query('`Product ID`=="Sick Time"')
  topic_04_count = h.iloc[0,2]
  print(topic_04_count)
except:
  topic_04_count = 0
  print(topic_04_count)

try:
  h = df_101439.query('`Product ID`=="Crisis Management Vaccination Incentive"')
  topic_05_count = h.iloc[0,2]
  print(topic_05_count)
except:
  topic_05_count = 0
  print(topic_05_count)

try:
  h = df_101439.query('`Product ID`=="Crisis Management Masks"')
  topic_06_count = h.iloc[0,2]
  print(topic_06_count)
except:
  topic_06_count = 0
  print(topic_06_count)

try:
  h = df_101439.query('`Product ID`=="Enterprise work from home"')
  topic_07_count = h.iloc[0,2]
  print(topic_07_count)
except:
  topic_07_count = 0
  print(topic_07_count)

try:
  h = df_101439.query('`Product ID`=="Furlough"')
  topic_08_count = h.iloc[0,2]
  print(topic_08_count)
except:
  topic_08_count = 0
  print(topic_08_count)

try:
  h = df_101439.query('`Product ID`=="Crisis Management Care Giving"')
  topic_09_count = h.iloc[0,2]
  print(topic_09_count)
except:
  topic_09_count = 0
  print(topic_09_count)

try:
  h = df_101439.query('`Product ID`=="Crisis Management Door Temp"')
  topic_10_count = h.iloc[0,2]
  print(topic_10_count)
except:
  topic_10_count = 0
  print(topic_10_count)

try:
  h = df_101439.query('`Product ID`=="Unemployment"')
  topic_11_count = h.iloc[0,2]
  print(topic_11_count)
except:
  topic_11_count = 0
  print(topic_11_count)

print(topic_01_count)
print(topic_02_count)
print(topic_03_count)
print(topic_04_count)
print(topic_05_count)
print(topic_06_count)
print(topic_07_count)
print(topic_08_count)
print(topic_09_count)
print(topic_10_count)
print(topic_11_count)

#database 
#c.execute("DROP TABLE overview_7days")
#c.execute("SELECT * FROM overview_7days")
'''
df_file = pd.read_csv(r'C:\Users\Ionock_Issha\Dropbox\Python\Django\count.csv')
df_file = pd.read_csv(r'C:\Users\Ionock_Issha\Dropbox\Python\Django\topic.csv',names=['date','cri_man','cri_man_vac','cri_man_vac_inc','unem','vac_sab','sick','cri_man_mas','cri_man_doo','furl','cri_man_car_giv','ent_wor_hom'])
df_file.to_sql(name='overview_7days', con=conn, if_exists='append', index=False)
df_file.to_sql(name='critical_topic', con=conn, if_exists='append', index=False)
df_file.rename(columns={'Topic': 'Date'})
'''
conn = sqlite3.connect('test_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS overview_7days
          ([id] INTEGER PRIMARY KEY,
		  [date] INTEGER,
		  [emails] INTEGER,
		  [phone] INTEGER,
		  [chat] INTEGER,
		  [text] INTEGER,
		  [total] INTEGER)
          ''')
         
c.execute('''
          CREATE TABLE IF NOT EXISTS critical_topic
          ([id] INTEGER PRIMARY KEY,
		  [date] TEXT,
		  [cri_man] INTEGER,
		  [cri_man_vac] INTEGER,
		  [cri_man_vac_inc] INTEGER,
		  [unem] INTEGER,
		  [vac_sab] INTEGER,
		  [sick] INTEGER,
		  [cri_man_mas] INTEGER,
		  [cri_man_doo] INTEGER,
		  [furl] INTEGER,
		  [cri_man_car_giv] INTEGER,
		  [ent_wor_hom] INTEGER)
          ''')



c.execute('''
          INSERT INTO overview_7days (date,emails,phone,chat,text,total)
				VALUES(?,?,?,?,?,?)''',
				(date_created,total_email,phone_count,chat_count,text_count,total_today)
				)
conn.commit()

c.execute('''
          INSERT INTO critical_topic (date,cri_man,cri_man_vac,cri_man_vac_inc,unem,vac_sab,sick,cri_man_mas,cri_man_doo,furl,cri_man_car_giv,ent_wor_hom)
				VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''',
				(date_created,topic_01_count,topic_03_count,topic_05_count,topic_11_count,topic_02_count,topic_04_count,topic_06_count,topic_10_count,topic_08_count,topic_09_count,topic_07_count)
				)
conn.commit()

c.execute('''
SELECT * FROM (
SELECT date,emails,phone,chat,total FROM overview_7days ORDER BY id DESC LIMIT 7)
ORDER BY date ASC;
          ''')
df_count_7days = pd.DataFrame(c.fetchall(), columns=['date','emails','phone','chat','total'])

c.execute('''
SELECT * FROM (
SELECT date,cri_man,cri_man_vac,cri_man_vac_inc,unem,vac_sab,sick,cri_man_mas,cri_man_doo,furl,cri_man_car_giv,ent_wor_hom FROM critical_topic ORDER BY id DESC LIMIT 7)
ORDER BY date ASC;
          ''')
df_count_topic = pd.DataFrame(c.fetchall(), columns=['date','Crisis Management','Vacation / Sabbatical','Crisis Management Vaccine','Sick Time','Crisis Management Vaccination Incentive','Crisis Management Masks','Enterprise work from home','Furlough','Crisis Management Care Giving','Crisis Management Door Temp','Unemployment']).T
df_count_topic = df_count_topic.rename(columns=df_count_topic.iloc[0]).drop(df_count_topic.index[0])
df_count_topic["Total"] = df_count_topic.sum(axis=1)


