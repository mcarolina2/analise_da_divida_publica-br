import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv
import streamlit as st
import matplotlib.dates as mdates
import matplotlib.ticker as ticker


#Carregar base de dados manipulada:
dados = pd.read_csv('datas/valores.csv')

#customizando a abada da janela 
st.set_page_config(page_icon='<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#5f6368"><path d="M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h360v80H200v560h560v-360h80v360q0 33-23.5 56.5T760-120H200Zm80-160h80v-280h-80v280Zm160 0h80v-400h-80v400Zm160 0h80v-160h-80v160Zm80-320v-80h-80v-80h80v-80h80v80h80v80h-80v80h-80ZM480-480Z"/></svg>', page_title='CDN-divida pública')

#Cabeçalho
a, b = st.columns([1,10])
with a :
    st.image('img/logo-cdn.png')
    
with b :
    st.title('Análise da dívida pública do Brasil')
    
# Introdução:
st.markdown(
    """ 
    Esse APP visa apresentar a dívida pública interna do brasil ao longo do tempo
            
     """)
with st.expander('você conhece a dívida pública do brasil ?', False):
    st.markdown(
        """
        A dívida pública interna do Brasil refere-se ao total de recursos financeiros que o governo
federal deve a credores dentro do país, sendo uma parte fundamental da dívida pública total.
Esses valores são utilizados pelo governo para financiar despesas públicas, como investimentos
em infraestrutura, saúde, educação, ou até para cobrir déficits orçamentários. A dívida pública interna do Brasil é formada principalmente por títulos emitidos pelo governo,
como as Letras do Tesouro Nacional (LTN), Notas do Tesouro Nacional – Série B (NTN-B) e Letras
Financeiras do Tesouro (LFT). Esses títulos são comprados por bancos, empresas, fundos de
investimento e até pessoas físicas. Os principais credores são instituições financeiras e
investidores privados. O governo emite esses títulos principalmente para cobrir o déficit fiscal
(quando gasta mais do que arrecada) e controlar a economia, ajustando a inflação e a liquide
No entanto, pagar os juros sobre essa dívida pode ser um custo alto e, se a dívida crescer sem
controle, pode afetar a confiança dos investidores e prejudicar a economia, elevando os juros e 
diminuindo o espaço no orçamento. Quando bem administrada, a dívida pode ajudar no
crescimento econômico, mas se mal gerida, pode tornar a situação fiscal mais arriscada
                """)
    

#st.sidebar.header("📅 Filtro de Datas")
dados['data'] = pd.to_datetime(dados['data'], errors='coerce')
dados = dados.dropna(subset=['data'])
min_ano = int(dados['data'].dt.year.min())  # Garantindo que o valor seja um inteiro
max_ano = int(dados['data'].dt.year.max())
anos_selecionados =st.sidebar.slider("Selecione o intervalo de anos:", min_ano, max_ano, (min_ano, max_ano))
dados_filtrados = dados[(dados['data'].dt.year >= anos_selecionados[0]) & (dados['data'].dt.year <= anos_selecionados[1])]


# Gráfico
st.title("Evolução da Dívida Pública")
fig, ax =plt.subplots(figsize=(10, 8))
ax.plot(dados_filtrados['data'],dados_filtrados['valor'], linestyle=':', color='b')
ax.set_xlabel("Ano")
ax.set_ylabel("Valor da Dívida Pública")
ax.set_title("Dívida Pública ao longo do tempo")
plt.xticks(rotation=45)


# observações dos eixos do grafico:
# configurando o eixo X para exibir apenas os anos
ax.xaxis.set_major_locator(mdates.YearLocator())  
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  

# configurando o eixo Y para intervalos de 25.000
max_valor = dados_filtrados['valor'].max()
#yticks = list(range(0, int(max_valor) + 25000, 25000))  
#ax.set_yticks(yticks)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))
ax.grid(True, linestyle='--', alpha=0.9)

#exibindo o gráfico no streamlit
st.pyplot(fig)
