
import pandas as pd
import plotly.express as px
import streamlit as st

# Para rodar o app -> streamlit run codigoBase.py

# Lendo o dataset
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Melhorando os nomes das colunas"""
df = df.rename(columns={'newDeaths': 'Novos óbitos', 'newCases': 'Novos casos', 'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

# Seleção do Estado
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Qual estado?', estados)

# Seleção da coluna
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)

# Seleção das linhas que pertencem ao Estado
df = df[df['state'] == state]

# Criando a figura"
fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title={'x':0.5})

st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.')

st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')