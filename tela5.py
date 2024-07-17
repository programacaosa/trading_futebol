from futpythontrader import *
from leagues import *
from rename import *

def show_tela5():
    
    st.title("Luke v2.1")
    st.header("Singularidades")
    
    dia = st.date_input("Data de Análise", date.today())

    @st.cache_data
    def load_data_betfair(dia):
        betfair_url = f'https://github.com/futpythontrader/YouTube/raw/main/Jogos_do_Dia/Betfair/Jogos_do_Dia_Betfair_Back_Lay_{dia}.csv'
        betfair = pd.read_csv(betfair_url)
        return betfair

    try:
        
        betfair = load_data_betfair(dia)

        betfair = betfair[['Date','Time','League','Home','Away',
                        'Odd_H_Back','Odd_D_Back','Odd_A_Back',
                        'Odd_Over25_FT_Back','Odd_Under25_FT_Back','Odd_BTTS_Yes_Back','Odd_BTTS_No_Back',
                        'Odd_CS_0x0_Lay','Odd_CS_0x1_Lay','Odd_CS_0x2_Lay','Odd_CS_0x3_Lay',
                        'Odd_CS_1x0_Lay','Odd_CS_1x1_Lay','Odd_CS_1x2_Lay','Odd_CS_1x3_Lay',
                        'Odd_CS_2x0_Lay','Odd_CS_2x1_Lay','Odd_CS_2x2_Lay','Odd_CS_2x3_Lay',
                        'Odd_CS_3x0_Lay','Odd_CS_3x1_Lay','Odd_CS_3x2_Lay','Odd_CS_3x3_Lay',
                        'Odd_CS_Goleada_H_Lay','Odd_CS_Goleada_A_Lay',
                        'ID_Evento','IDMercado_Correct_Score']]
        betfair.columns = ['Date','Time','League','Home','Away',
                        'Odd_H','Odd_D','Odd_A',
                        'Odd_Over25','Odd_Under25','Odd_BTTS_Yes','Odd_BTTS_No',
                        'Odd_0x0','Odd_0x1','Odd_0x2','Odd_0x3',
                        'Odd_1x0','Odd_1x1','Odd_1x2','Odd_1x3',
                        'Odd_2x0','Odd_2x1','Odd_2x2','Odd_2x3',
                        'Odd_3x0','Odd_3x1','Odd_3x2','Odd_3x3',
                        'Odd_Goleada_H','Odd_Goleada_A',
                        'IDEvento','IDMercado']

        rename_leagues(betfair)
        betfair = betfair[betfair['League'].isin(leagues) == True]
        rename_teams(betfair)
        betfair = drop_reset_index(betfair)

        Jogos = betfair.copy()

        ########## Importando a Base de Dados ##########
        @st.cache_data
        def load_data_base():

            base_luke = pd.read_csv('https://github.com/futpythontrader/YouTube/raw/main/Bases_de_Dados/FlashScore/Base_de_Dados_FlashScore_Luke.csv')
            
            return base_luke

        base_luke = load_data_base()
        base_luke = drop_reset_index(base_luke)

        df = base_luke.copy()

        flt_sin_2anos = ((df.Season == '2023') | (df.Season == '2024') | (df.Season == '2022/2023') | (df.Season == '2023/2024'))
        df_sin2 = df[flt_sin_2anos]
        df_sin2 = drop_reset_index(df_sin2)

        lista = ['0x0','0x1','0x2','0x3','1x0','1x1','1x2','1x3','2x0','2x1','2x2','2x3','3x0','3x1','3x2','3x3','Goleada_H','Goleada_A']

        j1, j2, j3 = st.columns(3)
        Placar = j2.selectbox('Escolha o Placar', lista) 

        st.subheader(f"Jogos Singulares para o Placar {Placar}")
        st.text('')

        for a,b,c,d,e,f in zip(betfair.Home,
                               betfair.Away,
                               betfair.IDEvento,
                               betfair.IDMercado,
                               betfair.League, 
                               betfair.Time):
            home = a
            away = b
            id_evento = c
            id_mercado = ajustar_id_mercado(d)
            liga = e
            hora = f

            ########## Placar 0x0 ##########
            # Home
            sing_H = df_sin2[df_sin2.Home == home].copy()
            sing_H = sing_H[sing_H[Placar] == 1]
            n_sing_H = sing_H[sing_H.columns[0]].count()

            # Away
            sing_A = df_sin2[df_sin2.Away == away].copy()
            sing_A = sing_A[sing_A[Placar] == 1]
            n_sing_A = sing_A[sing_A.columns[0]].count()

            # Home x Away
            sing_HxA = df_sin2[(df_sin2.Home == home) & (df_sin2.Away == away)].copy()
            sing_HxA = sing_HxA[sing_HxA[Placar] == 1]
            n_sing_HxA = sing_HxA[sing_HxA.columns[0]].count()
            if (n_sing_A == 0) & (n_sing_H == 0) & (n_sing_HxA == 0):
                st.text(f"Liga: {liga}")
                st.text(f"Jogo: {home} x {away}")
                st.text(f"Horário: {hora}")
                link1 = f'<div style="text-align:left"><a href="https://bolsadeaposta.com/exchange/sport/1/market/{id_mercado}">{"Bolsa de Aposta"}</a></div>'
                st.markdown(link1, unsafe_allow_html=True)
                link2 = f'<div style="text-align:left"><a href="https://bolsadeaposta.com/widget/radar?id={id_evento}">{"Radar"}</a></div>'
                st.markdown(link2, unsafe_allow_html=True)
                st.text('')
                st.text('')
                st.text('')

            else:
                pass


            # st.text("---")

        st.text(" ")
        st.text(" ")
        st.text("Good Luke!!!")






        
    except:
        pass