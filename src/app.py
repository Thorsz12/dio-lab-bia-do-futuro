import streamlit as st
from agente import gerar_resposta

st.title("💰 Assistente Financeiro")

mensagem = st.text_input("Digite sua mensagem:")

if mensagem:
    resposta = gerar_resposta(mensagem)
    st.write(resposta)
