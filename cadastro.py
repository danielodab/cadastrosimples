import streamlit as st
import pandas as pd
from datetime import date

def gravar_Dados(nome, dt_nasc, tipo):
    if nome and dt_nasc  <= date.today():
        with open('clientes.csv', 'a', encoding='utf-8') as file:
            file.write(f'{nome},{dt_nasc},{tipo}\n')
        st.session_state["Sucesso"] = True
    else:
        st.session_state["Sucesso"] = False


st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon='🪪'
)

st.title("Cadastro de clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente",
                     key='nome_cliente')
dt_nasc = st.date_input("Digite a data de nascimento",
                        format='DD/MM/YYYY')
tipo = st.selectbox('Tipo do Cliente',
                    ['Pessoa Jurídica','Pessoa Física'])

btn_cadastrar = st.button('Cadastrar', 
                          on_click=gravar_Dados,
                          args=[nome, dt_nasc, tipo])

if btn_cadastrar:
    if st.session_state["Sucesso"]:
        st.success('Cliente cadastrado com sucesso!',
                   icon='✅')
    else:
        st.error('Houve algum problema no cadastro',
                 icon='❌')