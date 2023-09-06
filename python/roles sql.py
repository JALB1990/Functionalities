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

data = pandas.read_csv('C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/roles.csv', encoding="latin-1",engine='python')
f= open("C:/Users/KX0690/OneDrive - Assurant, Inc/Desktop/PDF/guru99.txt","w+")

r = -1
for index, row in data.iterrows():
 r += 1
 nombre = data.iloc[r,0]
 a = (""" (
'""" + data.iloc[r,0] +
"""', -- UserId
'""" + data.iloc[r,1] +"""'  -- RoleId
)
,""")
 f.write(a)
 print(index)

f.close()