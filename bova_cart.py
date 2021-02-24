import pandas as pd
from pandas_datareader import data as wb
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import adfuller

#%%
start = datetime(2010,12,1)
end = datetime(2020, 12, 1)

df=wb.DataReader('bova11.SA', data_source='yahoo',start=start,end=end)
ver =df.index.to_numpy('d')

close=df['Close'].to_numpy()
#%% carteira 70 bova 30 caixa

cap = 100000
perc_bova = 0.70
rentLS = 1
n_bova = np.floor(perc_bova*cap/close[0])
caixa = cap - n_bova*close[0]
LS = cap
capvec =[cap]
print('n_bovas: '+str(n_bova))
for i in range(1,close.shape[0]):
    cap = caixa + n_bova*close[i]
    capvec.append(cap)
    # media 1,5% por mes de LS
    if(i%20==0):
        caixa = (1+((rentLS/100)/(1-perc_bova)))*caixa

    if((n_bova*close[i])/(n_bova*close[i]+caixa) > perc_bova+0.10):
         n_bova = np.floor(perc_bova*cap/close[i])
         caixa = cap - n_bova*close[i] 
         print('retira dia ' + str(df.index[i]))
         print('n_bovas: '+str(n_bova))
         print('==============================')

    if((n_bova*close[i])/(n_bova*close[i]+caixa) <  perc_bova-0.05):
         n_bova = np.floor(perc_bova*cap/close[i])
         caixa = cap - n_bova*close[i] 
         print('add dia ' + str(df.index[i]))
         print('n_bovas: '+str(n_bova))
         print(i)
         print('==============================')

# plot rentabilidade
capvec = 100*np.array(capvec)/capvec[0]
allin_bova = 100*close/close[0]
plt.figure()
plt.plot(df.index,allin_bova,df.index,capvec)
l2 = str(100*perc_bova) + '% bova+LS(' + str(rentLS) + '%)'
plt.legend(['bova_only_',l2])

