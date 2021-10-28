import quandl 
from datetime import date
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

quandl.ApiConfig.api_key = #INPUT YOURS HERE

#DATA 
today = date.today()
today_str = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
limit_str = str(today.year-2)+'-'+str(today.month)+'-'+str(today.day) #download limit to 2 years 
#print(today_str)

df = quandl.get('USTREASURY/YIELD', start_date=limit_str, end_date=today_str) 
#print(df)

#COMPOSING MATRIX
tenors = [1,2,3,5,7,10,20,30]

df_spread = pd.DataFrame() 
df_spread['Tenors'] = tenors
for t in tenors: 
    df_spread[t] = [None]*len(tenors) 
df_spread = df_spread.set_index(df_spread['Tenors'], inplace=False, drop=True)

#print(df_spread)
for i in tenors: 
    for j in tenors: 
        #print(j, i)
        sspread = df[str(j)+' YR'] - df[str(i)+' YR'] 
        #print(sspread)
        #print(sspread.dtype)
        x = sspread[-1]
        mean = sspread[-31:-1].mean()#spot fix for rolling data
        sigma = sspread[-31:-1].std(ddof=1)

        z = (x-mean)/sigma
        #print(z)
        #print(x, mean, sigma)

        #appointt to "slot" 
        try:
            df_spread[j][i] = round(z,5)
        except:
            pass

#j - i and col = j ; rows = i 
df_spread = df_spread.drop(columns='Tenors')
df_spread = df_spread.fillna(0)
print(df_spread)

sns.set() 
plt.figure()
ax = sns.heatmap(df_spread, cmap='PiYG', annot=True)
ax.set_xlabel("Tenor (J)")
ax.set_ylabel("Tenor (I)")
ax.set_title('1 Month Rolling IsJs Spread Z-Score')
plt.show()


for i in tenors: 
    for j in tenors: 
        #print(j, i)
        sspread = df[str(j)+' YR'] - df[str(i)+' YR'] 
        #print(sspread)
        #print(sspread.dtype)
        x = sspread[-1]
        mean = sspread[-8:-1].mean()#spot fix for rolling data
        sigma = sspread[-8:-1].std(ddof=1)

        z = (x-mean)/sigma
        #print(z)
        #print(x, mean, sigma)

        #appointt to "slot" 
        try:
            df_spread[j][i] = round(z,5)
        except:
            pass

#j - i and col = j ; rows = i 
#df_spread = df_spread.drop(columns='Tenors')
df_spread = df_spread.fillna(0)
print(df_spread)

sns.set() 
plt.figure()
ax = sns.heatmap(df_spread, cmap='PiYG', annot=True)
ax.set_xlabel("Tenor (J)")
ax.set_ylabel("Tenor (I)")
ax.set_title('7 Days Rolling IsJs Spread Z-Score')
plt.show()

for i in tenors: 
    for j in tenors: 
        #print(j, i)
        sspread = df[str(j)+' YR'] - df[str(i)+' YR'] 
        #print(sspread)
        #print(sspread.dtype)
        x = sspread[-1]
        mean = sspread[-15:-1].mean()#spot fix for rolling data
        sigma = sspread[-15:-1].std(ddof=1)

        z = (x-mean)/sigma
        #print(z)
        #print(x, mean, sigma)

        #appointt to "slot" 
        try:
            df_spread[j][i] = round(z,5)
        except:
            pass

#j - i and col = j ; rows = i 
df_spread = df_spread.fillna(0)
print(df_spread)

sns.set() 
plt.figure()
ax = sns.heatmap(df_spread, cmap='PiYG', annot=True)
ax.set_xlabel("Tenor (J)")
ax.set_ylabel("Tenor (I)")
ax.set_title('14 Days Rolling IsJs Spread Z-Score')
plt.show()