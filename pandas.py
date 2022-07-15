from numpy import dtype
import pandas as pd

a={'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}

def est_not(notas):
    notas=pd.Series(notas)
    estad= pd.Series([notas.min(),notas.max(),notas.mean(), notas.std()])
    return estad

print(est_not(a))