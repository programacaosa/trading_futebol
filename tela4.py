from futpythontrader import *
from leagues import *
from rename import *

def show_tela4():
    
    st.title("Luke v2.1")
    st.header("Lay Goleada Favorito")
    
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
        
        # Filtros de Odds
        Odd_Min_Back_Fav = 1.50
        Odd_Max_Back_Fav = 2.20
        Odd_Min_Over25 = 1.50
        Odd_Max_Over25 = 2.20
        Odd_Min_BTTS = 1.50
        Odd_Max_BTTS = 2.20

        flt = (
            (Jogos.Odd_H >= Odd_Min_Back_Fav)  
            & (Jogos.Odd_H <= Odd_Max_Back_Fav) 
            & (Jogos.Odd_Over25 >= Odd_Min_Over25) 
            & (Jogos.Odd_Over25 <= Odd_Max_Over25) 
            & (Jogos.Odd_BTTS_Yes >= Odd_Min_BTTS)
            & (Jogos.Odd_BTTS_Yes <= Odd_Max_BTTS) 
            )

        df_LGP = Jogos[flt]
        df_LGP = drop_reset_index(df_LGP)

        ########## Importando a Base de Dados ##########
        @st.cache_data
        def load_data_base():

            base_luke = pd.read_csv('https://github.com/futpythontrader/YouTube/raw/main/Bases_de_Dados/FlashScore/Base_de_Dados_FlashScore_Luke.csv')
            return base_luke

        base_luke = load_data_base()
        base_luke = drop_reset_index(base_luke)

        for a,b,c,d,e,f,g in zip(df_LGP.League, 
                                df_LGP.Time, 
                                df_LGP.Home, 
                                df_LGP.Away,
                                df_LGP.Odd_Goleada_H,
                                df_LGP.IDEvento,
                                df_LGP.IDMercado):
                liga = a
                hora = b
                mandante = c
                visitante = d
                odd = e
                id_evento = f
                id_mercado = ajustar_id_mercado(g)
                
                df = base_luke[base_luke['League'] == liga]
                flt_lgp = ((df.Season == '2024') | (df.Season == '2023/2024'))
                df1 = df[flt_lgp]
                df1 = drop_reset_index(df1)
                
                Gols_Marcados_Home = df1[['Home','Goals_H']].groupby('Home').sum()
                Gols_Marcados_Away = df1[['Away','Goals_A']].groupby('Away').sum()
                Gols_Marcados = pd.concat([Gols_Marcados_Home, Gols_Marcados_Away],axis=1)
                Gols_Marcados['Gols_Marcados'] = Gols_Marcados.Goals_H + Gols_Marcados.Goals_A
                Gols_Marcados = Gols_Marcados[['Gols_Marcados']]
                Gols_Marcados.index = Gols_Marcados.index.set_names(['Time'])
                Gols_Marcados = Gols_Marcados.sort_values(['Gols_Marcados'], ascending=False)
                Gols_Marcados = Gols_Marcados.rename_axis('index').reset_index()
                Gols_Marcados = drop_reset_index(Gols_Marcados) 
                Gols_Marcados.columns = ['Time','Gols Marcados']

                Gols_Sofridos_Home = df1[['Home','Goals_A']].groupby('Home').sum()
                Gols_Sofridos_Away = df1[['Away','Goals_H']].groupby('Away').sum()
                Gols_Sofridos = pd.concat([Gols_Sofridos_Home, Gols_Sofridos_Away],axis=1)
                Gols_Sofridos['Gols_Sofridos'] = Gols_Sofridos.Goals_H + Gols_Sofridos.Goals_A
                Gols_Sofridos = Gols_Sofridos[['Gols_Sofridos']]
                Gols_Sofridos.index = Gols_Sofridos.index.set_names(['Time'])
                Gols_Sofridos = Gols_Sofridos.sort_values(['Gols_Sofridos'], ascending=True)
                Gols_Sofridos = Gols_Sofridos.rename_axis('index').reset_index()
                Gols_Sofridos = drop_reset_index(Gols_Sofridos) 
                Gols_Sofridos.columns = ['Time','Gols Sofridos']        

                flt_goleada1 = (Gols_Marcados.index > 5) & (Gols_Marcados.index <=15);
                df_gol1 = Gols_Marcados[flt_goleada1]
                lista1 = (sorted(df_gol1['Time'].unique()));
                flt_goleada2 = (Gols_Sofridos.index <=15);
                df_gol2 = Gols_Sofridos[flt_goleada2]
                lista2 = (sorted(df_gol2['Time'].unique()));
                if mandante in lista1 and mandante in lista2 and visitante in lista1 and visitante in lista2:
                    st.text(f"Liga: {liga}")
                    st.text(f"Jogo: {mandante} x {visitante}")
                    st.text(f"Horário: {hora}")
                    st.text(f"Odd: {odd}")
                    link1 = f'<div style="text-align:left"><a href="https://bolsadeaposta.com/exchange/sport/1/market/{id_mercado}">{"Bolsa de Aposta"}</a></div>'
                    st.markdown(link1, unsafe_allow_html=True)
                    link2 = f'<div style="text-align:left"><a href="https://bolsadeaposta.com/widget/radar?id={id_evento}">{"Radar"}</a></div>'
                    st.markdown(link2, unsafe_allow_html=True)
                    st.text("")
                    st.text("")
                    st.text("---")
                else:
                    pass
        st.text("Good Luke!!!")
    except:
        pass