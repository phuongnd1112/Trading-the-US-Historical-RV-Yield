import quandl 
from datetime import date
import seaborn as sns 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
import pandas as pd
from api_key import api_key

quandl.ApiConfig.api_key = api_key

#DATA 
today = date.today()
today_str = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
limit_str = str(today.year-2)+'-'+str(today.month)+'-'+str(today.day) #download limit to 2 years 
#print(today_str)

df = quandl.get('USTREASURY/YIELD', start_date=limit_str, end_date=today_str) 
#transposing final row into a datatable 
today = df.iloc[-1, :].T
today_patch = mpatch.Patch(color='r', label='Today') 
ystd = df.iloc[-2, :].T
ystd_patch = mpatch.Patch(color='g', label='Yesterday')
seven_day = df.iloc[-8, :].T
seven_patch = mpatch.Patch(color='b', label='1 Week')
fourt_day = df.iloc[-15, :].T
fourt_patch = mpatch.Patch(color='orange', label='2 Weeks')

sns.set() 
plt.figure(figsize=(10,10)) 
plt.plot(today, color = 'r', alpha=1.0, marker='o')
plt.plot(ystd, color='g', alpha=0.6, marker = 'o') 
plt.plot(seven_day, color='b', alpha=0.4, marker='x') 
plt.plot(fourt_day, color='orange', alpha=0.2, marker='v')
plt.title('Yield curve on ' +str(df.index[-1]))
plt.xlabel('T') 
plt.ylabel('Y')
plt.legend(handles =[today_patch, ystd_patch, seven_patch, fourt_patch])
plt.show() 
