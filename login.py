# login.py
import streamlit as st
from usuarios import usuarios_permitidos  

def show_login_page():
    # Usando colunas para centralizar o formulário de login horizontalmente
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.write("## Login")
        username = st.text_input("Username", "")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            # Verificação do usuário e senha
            user_found = False
            for usuario in usuarios_permitidos:
                if username == usuario["login"] and password == usuario["senha"]:
                    user_found = True
                    break
            
            if user_found:
                st.success("Login bem-sucedido!")
                return True
            else:
                st.error("Usuário ou senha incorretos!")
                return False
        
        st.warning("Por favor insira seu nome de Usuário e Senha")
        st.write("Se ainda não é assinante [clique aqui](https://hub.la/g/P863owYDtnjS1X064ugB).")
        