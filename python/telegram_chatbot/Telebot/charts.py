import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from textwrap import wrap


def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

def chart_01(df_count_topic): #important 11 Topics per week / Critical 5
 df_count_topic = df_count_topic.iloc[: , :-1]
 df_chart = df_count_topic.T
 a0 = df_chart.iloc[:, 0].values.tolist()
 a1 = df_chart.iloc[:, 1].values.tolist()
 a2 = df_chart.iloc[:, 2].values.tolist()
 a3 = df_chart.iloc[:, 3].values.tolist()
 a4 = df_chart.iloc[:, 4].values.tolist()
 a5 = df_chart.iloc[:, 5].values.tolist()
 a6 = df_chart.iloc[:, 6].values.tolist()
 a7 = df_chart.iloc[:, 7].values.tolist()
 a8 = df_chart.iloc[:, 8].values.tolist()
 a9 = df_chart.iloc[:, 9].values.tolist()
 a10 = df_chart.iloc[:, 10].values.tolist()
 x= df_chart.index.tolist()
 new_x =[]
 for item in x:
  date = custom_strftime('%d-%b', datetime.strptime(item,'%Y/%m/%d'))
  new_x.append(date.upper())
 labels= list(df_chart)
 #del x[-1]
 fig, ax = plt.subplots()
 ax.grid(axis='y')
 rect1=ax.bar([0,12,24,36,48,60,71],a0,width=1,bottom=None,label=labels[0])
 rect2=ax.bar([1,13,25,37,49,61,72],a1,width=1,bottom=None,label=labels[1])
 rect3=ax.bar([2,14,26,38,50,62,73],a2,width=1,bottom=None,label=labels[2])
 rect4=ax.bar([3,15,27,39,51,63,74],a3,width=1,bottom=None,label=labels[3])
 rect5=ax.bar([4,16,28,40,52,64,75],a4,width=1,bottom=None,label=labels[4])
 rect6=ax.bar([5,17,29,41,53,65,76],a5,width=1,bottom=None,label=labels[5])
 rect7=ax.bar([6,18,30,42,54,66,77],a6,width=1,bottom=None,label=labels[6])
 rect8=ax.bar([7,19,31,43,55,67,78],a7,width=1,bottom=None,label=labels[7])
 rect9=ax.bar([8,20,32,44,56,68,79],a8,width=1,bottom=None,label=labels[8])
 rect10=ax.bar([9,21,33,45,57,69,80],a9,width=1,bottom=None,label=labels[9])
 rect11=ax.bar([10,22,34,46,58,70,81],a10,width=1,bottom=None,label=labels[10]) 
 ax.set_title('Important 11 Topics per Week')
 ax.set_xticks([5,17,29,41,53,65,76], new_x)
 ax.legend()
 ax.bar_label(rect1, padding=3)
 ax.bar_label(rect2, padding=3)
 ax.bar_label(rect3, padding=3)
 ax.bar_label(rect4, padding=3)
 ax.bar_label(rect5, padding=3)
 ax.bar_label(rect6, padding=3)
 ax.bar_label(rect7, padding=3)
 ax.bar_label(rect8, padding=3)
 ax.bar_label(rect9, padding=3)
 ax.bar_label(rect10, padding=3)
 ax.bar_label(rect11, padding=3)
 fig.tight_layout()
 plt.show()


def chart_02(df_count_topic): #11 Key topics - totals for period / Critical 5
 totals = df_count_topic['Total']
 df_count_topic = df_count_topic.iloc[: , :-1]
 df_count_topic = df_count_topic.T
 x= list(df_count_topic.index.values)
 date_1 = custom_strftime('%B {S}', datetime.strptime(x[0],'%Y/%m/%d'))
 date_2 = custom_strftime('%B {S}', datetime.strptime(x[-1],'%Y/%m/%d'))
 fig, ax = plt.subplots()
 ax.grid(axis='y')
 totals = totals.sort_values(ascending=False)
 labels= list(totals.index.values)
 labels = [ '\n'.join(wrap(l, 15)) for l in labels ]
 rect1=ax.bar([0],totals.iloc[0],width=1,bottom=None,label=labels[0])
 rect2=ax.bar([2],totals.iloc[1],width=1,bottom=None,label=labels[1])
 rect3=ax.bar([4],totals.iloc[2],width=1,bottom=None,label=labels[2])
 rect4=ax.bar([6],totals.iloc[3],width=1,bottom=None,label=labels[3])
 rect5=ax.bar([8],totals.iloc[4],width=1,bottom=None,label=labels[4])
 rect6=ax.bar([10],totals.iloc[5],width=1,bottom=None,label=labels[5])
 rect7=ax.bar([12],totals.iloc[6],width=1,bottom=None,label=labels[6])
 rect8=ax.bar([14],totals.iloc[7],width=1,bottom=None,label=labels[7])
 rect9=ax.bar([16],totals.iloc[8],width=1,bottom=None,label=labels[8])
 rect10=ax.bar([18],totals.iloc[9],width=1,bottom=None,label=labels[9])
 rect11=ax.bar([20],totals.iloc[10],width=1,bottom=None,label=labels[10])
 ax.set_title('11 Key topics - totals for period: ' + date_1 + ' - ' + date_2)
 ax.set_xticks([0,2,4,6,8,10,12,14,16,18,20], labels)
 ax.set_yticks([])
 #print(ax.set_xticks([0,2,4,6,8,10,12,14,16,18,20], x))
 ax.legend()
 ax.bar_label(rect1, padding=3)
 ax.bar_label(rect2, padding=3)
 ax.bar_label(rect3, padding=3)
 ax.bar_label(rect4, padding=3)
 ax.bar_label(rect5, padding=3)
 ax.bar_label(rect6, padding=3)
 ax.bar_label(rect7, padding=3)
 ax.bar_label(rect8, padding=3)
 ax.bar_label(rect9, padding=3)
 ax.bar_label(rect10, padding=3)
 ax.bar_label(rect11, padding=3)
 fig.tight_layout()
 plt.show()