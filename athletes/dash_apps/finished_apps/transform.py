
import pandas as pd
import numpy as np
import datetime

#constants for converting scores to values out of ten
mapping = dict(Sickness=1.428571429, 
                Fatigue=1.428571429,
                Menstruation=1.428571429,
                SleepQual=1.428571429,
                Stress=1.428571429,
                Training=2.5,
                Feeling=1,
                Pulse=1,
                Sleep_Hours=1,
                Soreness=1,
                Weight_Kg=1,
                Injury=1)


df=pd.read_csv("athletes/static/AB_metrics_Oct.csv")
def f(row):
    if row['Type'] == 'Overall Feeling':
        val = 'Feeling'
    elif row['Type'] == 'Pulse':
        val = 'Pulse'
    elif row['Type'] == 'Sickness':
        val = 'Sickness'
    elif row['Type'] == 'Sleep Hours':
        val = 'Sleep_Hours' 
    elif row['Type'] == 'Sleep Qualilty':
        val = 'SleepQual' 
    elif row['Type'] == 'Soreness':
        val = 'Soreness'
    elif row['Type'] == 'Stress':
        val = 'Stress'
    elif row['Type'] == 'Weight Kilograms':
        val = 'Weight_Kg' 
    elif row['Type'] == 'Yesterday\'s Training':
        val = 'Training' 
    elif row['Type'] == 'Fatigue':
        val = 'Fatigue' 
    elif row['Type'] == 'Menstruation':
        val = 'Menstruation'
    elif row['Type'] == 'Injury':
        val = 'Injury'
    else:
        val = 'NA'
    return val

df['Type']= df.apply(f, axis=1)

df=df[['Type','Timestamp','Value']]
df=df.rename(columns={"Type": "Metric"})


#calculation for converting dcores to value out of 10
def calc(number, condition):
    return number * mapping[condition]

df['Score'] = df.apply(lambda x: calc(x['Value'], x['Metric']), axis=1)
df['Score'] = np.round(df.Score)
df = df.fillna(np.nan).replace([np.nan], [None])
#print(df)

#convert Timestamp from str to date obj

def dates(date_to_convert):
     return datetime.datetime.strptime(date_to_convert, '%Y-%m-%d %H:%M:%S').date()
    
df['Date'] = df.apply(lambda x: dates(x['Timestamp']), axis=1)

df_wide= pd.pivot(df, index=['Date'], columns='Metric', values='Score').reset_index()

df = df.fillna(np.nan).replace([np.nan], [None])
#print(df_wide)
