import pandas as pd
from glob import glob
from pandas import read_csv

#carregando a base de dados 
file ='../datas/bcdata.sgs.4469.csv'
print(file)

#manipulando a base de dados
valores =(
    pd.read_csv(file, sep=';',decimal=',')
    .loc[:,['data','valor']]
    .assign(
        data=lambda df:pd.to_datetime(df['data']), # convertendo a coluna data em data
        valor=lambda df:pd.to_numeric(df['valor'], errors='coerce').fillna(0).astype(float)) # convertendo a coluna valores em pontos flutuantes 
)
print(valores)

# salvando a base de dados manipulada 
print(f"Salvando os dados")
valores.to_csv("../datas/valores.csv", index=False )

