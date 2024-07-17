import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path
from tela1 import show_tela1
from tela2 import show_tela2
from tela3 import show_tela3
from tela4 import show_tela4
from tela5 import show_tela5
from tela6 import show_tela6
from tela7 import show_tela7
from tela8 import show_tela8
from tela9 import show_tela9
from tela10 import show_tela10
from users import *

########## Criação do Aplicativo ##########

st.set_page_config(
        page_title = "Luke v2.1", layout="wide"
    )

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "luke_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Usuario ou Senha estão errados.")

if authentication_status == None:
    st.warning("Por favor insira seu nome de Usuário e Senha")
    st.write("Se ainda não é assinante [clique aqui](https://wa.me/5579999689464
).")

if authentication_status: 
    st.sidebar.image('logo.jpg', width=200)
    # st.sidebar.subheader(f"Usuário: {name}")
    # st.sidebar.subheader(f"Software Luke v2.1\n by @FutPythonTrader and \n @GetUpTrading")
    st.sidebar.markdown('---')

    paginas = ['Página Inicial',  # Adicionado uma opção de Boas-vindas
               'Oportunidades do Dia',
               'Favorito Home',
               'Favorito Away',
               'Lay Goleada Favorito',
               'Singularidades',
            #    'Odd 1000',
               'Base de Dados',
               'Backtesting',
               'Filtros Backtesting']
    
    escolha = st.sidebar.radio('', paginas)
    
    # Se a escolha for 'Boas-vindas', mostre a tela de boas-vindas
    if escolha == 'Página Inicial':
        st.subheader(f'Seja Bem-vindo {name}')

        st.write('');st.write('')

        # st.subheader(f'Por favor selecione uma opção no menu à esquerda.')

        # st.write('');st.write('');st.write('');st.write('');st.write('')

        # st.write(f'Web App desenvolvido por @FutPythonTrader e Idealizado por @GetUpTrading')

        st.write('Bem vindo ao melhor software de pré análise, para Correct Score, do Brasil!!!')
        st.write('O LUKE foi desenvolvido por @FutPythonTrader e idealizado por @GetUpTrading, ambos operadores do Correct Score.')
        st.write('Este software não vai trazer um milagre na tua vida, tampouco vai ser o responsável pela tua vitória no Trading Esportivo, mas uma coisa ele vai fazer, te trazer as melhores informações, atualizadas, para que suas decisões sejam as mais técnicas possíveis.')
        st.write('Neste link abaixo tem um video tutorial de como utilizar suas funções, porém, não vai te ensinar a interpretar as informações, isso depende do seu entendimento sobre a bolsa esportiva.')
        link = f'<div style="text-align:left"><a href="https://www.youtube.com/watch?v=EJh9ZX8VMd8">{"LUKE v.2.1"}</a></div>'
        st.markdown(link, unsafe_allow_html=True)
        st.write('')
        st.write('Desejamos que usem com sabedoria e que o LUKE seja para você, o que ele é para nós....')
        st.write('INDISPENSÁVEL!!!!!!!')

        
        

    elif escolha == 'Oportunidades do Dia':
        show_tela1()

    elif escolha == 'Favorito Home':
        show_tela2()

    elif escolha == 'Favorito Away':
        show_tela3()

    elif escolha == 'Lay Goleada Favorito':
        show_tela4()

    elif escolha == 'Singularidades':
        show_tela5()
    
    # elif escolha == 'Odd 1000':
    #     show_tela6()
    
    elif escolha == 'Base de Dados':
        show_tela7()

    elif escolha == 'Backtesting':
        show_tela9()

    elif escolha == 'Filtros Backtesting':
        show_tela10()


        

    st.sidebar.markdown('---')
    
    authenticator.logout("Logout", "sidebar")
