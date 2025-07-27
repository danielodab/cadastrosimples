import streamlit as st
import pandas as pd

dados = pd.read_csv('clientes.csv')

st.title('Clientes cadastrados')
st.divider()

st.dataframe(dados)

st.title('Gráfico')

contagem_tipo = dados['tipo'].value_counts()

mostrar_grafico = st.toggle('Mostrar Gráfico Tipo')

if mostrar_grafico:
    st.bar_chart(contagem_tipo)