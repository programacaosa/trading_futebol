from futpythontrader import *
from leagues import *
from rename import *

#################################################
################# Favorito Home #################
#################################################
def show_tela2():
    
    st.title("Luke v2.1")
    st.header("Favorito Home")
    
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
        
        try:
            ####################################
            ########## Filtro de Odds ##########
            ####################################
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                Odd_H_Min = st.number_input('Odd_H_Min', value=1.50, step=0.1)
                Odd_H_Max = st.number_input('Odd_H_Max', value=2.20, step=0.1)
            with col2:
                Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
                Odd_D_Max = st.number_input('Odd_D_Max', value=100.00, step=0.1)
            with col3:
                Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
                Odd_A_Max = st.number_input('Odd_A_Max', value=100.0, step=0.1)
            with col4:
                Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.50, step=0.1)
                Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=2.20, step=0.1)
            with col5:
                Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.50, step=0.1)
                Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=2.20, step=0.1)
            
            # Filtros de Odds
            Odd_Min_Back_H = Odd_H_Min
            Odd_Max_Back_H = Odd_H_Max
            Odd_Min_Back_D = Odd_D_Min
            Odd_Max_Back_D = Odd_D_Max
            Odd_Min_Back_A = Odd_A_Min
            Odd_Max_Back_A = Odd_A_Max
            Odd_Min_Over25 = Odd_Over25_Min
            Odd_Max_Over25 = Odd_Over25_Max
            Odd_Min_BTTS = Odd_BTTS_Min
            Odd_Max_BTTS = Odd_BTTS_Max

            ###################################
            ########## Favorito Home ##########
            ###################################

            # Criando o Filtro do Método de Lay CS - Favorito Home
            flt1 = ((Jogos.Odd_H >= Odd_Min_Back_H) & (Jogos.Odd_H <= Odd_Max_Back_H) & 
                    (Jogos.Odd_D >= Odd_Min_Back_D) & (Jogos.Odd_D <= Odd_Max_Back_D) & 
                    (Jogos.Odd_A >= Odd_Min_Back_A) & (Jogos.Odd_A <= Odd_Max_Back_A) & 
                    (Jogos.Odd_Over25 >= Odd_Min_Over25) & (Jogos.Odd_Over25 <= Odd_Max_Over25) & 
                    (Jogos.Odd_BTTS_Yes >= Odd_Min_BTTS) & (Jogos.Odd_BTTS_Yes <= Odd_Max_BTTS))
            df_Home = Jogos[flt1]
            df_Home = df_Home[['League','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes','IDMercado','IDEvento']]
            df_Home = drop_reset_index(df_Home)
        except:
            pass

        try:
            #############################
            ########## Análise ##########
            #############################

            # Criando a Lista com os Times
            lista_H = df_Home["Home"].tolist()
            lista = ['0x0','0x1','0x2','0x3','1x0','1x1','1x2','1x3','2x0','2x1','2x2','2x3','3x0','3x1','3x2','3x3','Goleada_H','Goleada_A']

            df0 = df_Home.copy()
            df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
            df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
            df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)
            df0['Odd_Over25'] = df0['Odd_Over25'].astype(float).map('{:.2f}'.format)
            df0['Odd_BTTS_Yes'] = df0['Odd_BTTS_Yes'].astype(float).map('{:.2f}'.format)
            st.dataframe(df0)
        except:
            pass
    

        if len(df0) != 0:
            
            try:
            
                ################################################
                ########## Importando a Base de Dados ##########
                ################################################
                
                j1, j2 = st.columns(2)
                selecao1 = j1.selectbox('Escolha o Mandante', lista_H) 
                selecao2 = j2.selectbox('Escolha o Placar', lista)
                
                Favorito = selecao1
                Placar = selecao2
                
                df_league = df_Home[df_Home.Home == Favorito].copy()
                row = df_Home.loc[df_Home['Home'] == Favorito].iloc[0]

                League = row['League'] 
                Fav_Home = row['Home'] 
                Zeb_Away = row['Away'] 
                IDEvento = row['IDEvento'] 
                IDMercado = row['IDMercado']
                IDMercado = ajustar_id_mercado(IDMercado)

                st.markdown('---')
                try:
                    # link = f'[{jogo}](https://www.betfair.com/exchange/plus/football/market/{IDMercado})'
                    link1 = f'<div style="text-align:left"><a href="https://www.betfair.com/exchange/plus/football/market/{IDMercado}">{"Betfair"}</a></div>'
                    link2 = f'<div style="text-align:left"><a href="https://bolsadeaposta.com/exchange/sport/1/market/{IDMercado}">{"Bolsa de Aposta"}</a></div>'
                    link3 = f'<div style="text-align:left"><a href="https://fulltbet.com/exchange/sport/1/market/{IDMercado}">{"Fulltbet"}</a></div>'
                
                    col1, col2, col3 = st.columns(3)

                    with col2:
                        texto = Fav_Home + ' x ' + Zeb_Away
                        st.write(texto, unsafe_allow_html=True)

                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.markdown(link1, unsafe_allow_html=True)
                    with col2:
                        st.markdown(link2, unsafe_allow_html=True)
                    with col3:
                        st.markdown(link3, unsafe_allow_html=True)
                    
                except:
                    st.write("Mercado Não Disponível.")

                st.markdown('---')
            except:
                st.markdown('---')





            try:
            
                ########## Importando a Base de Dados ##########
                @st.cache_data
                def load_data_base():

                    base_luke = pd.read_csv('https://github.com/futpythontrader/YouTube/raw/main/Bases_de_Dados/FlashScore/Base_de_Dados_FlashScore_Luke.csv')
                    return base_luke

                base_luke = load_data_base()
                base_luke = drop_reset_index(base_luke)

                df = base_luke[base_luke['League'] == League]
                df = drop_reset_index(df)
                

                df_f = df[(df['Home'] == Favorito)]
                flt2 = ((df_f.Season == '2023') | (df_f.Season == '2024') | (df_f.Season == '2022/2023') | (df_f.Season == '2023/2024'))
                df_f = df_f[flt2]
                df_filtrado = df_f[(df_f[Placar] == 1)]
                df_filtrado = df_filtrado[['Season','Date','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]
                df_filtrado.columns = ['Season','Date','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']
                df_filtrado = drop_reset_index(df_filtrado)
            except:
                st.markdown('---')

            try:
                ################################################################################
                # Jogos anteriores Terminados no Placar Selecionado
                ################################################################################

                n_H = df_filtrado[df_filtrado.columns[0]].count()

                if n_H == 0:
                    st.text("Não houve Jogos anteriores do " + Favorito + " terminados em "+ Placar)
                    st.text(f"Jogos Analisados: {len(df_f)}")
                    st.markdown('---')
                else:
                    st.text("Jogos anteriores do " + Favorito + " terminados em " + Placar)
                    df0 = df_filtrado.copy()
                    df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
                    df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
                    df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)
                    df0['Odd_Over25'] = df0['Odd_Over25'].astype(float).map('{:.2f}'.format)
                    df0['Odd_BTTS_Yes'] = df0['Odd_BTTS_Yes'].astype(float).map('{:.2f}'.format)
                    df0 = df0[['Date','Season','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]
                    df0.columns = ['Date','Season','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H_FT','Goals_A_FT','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']
                    df0 = drop_reset_index(df0)
                    st.dataframe(df0)
                    st.markdown('---')
            except:
                st.markdown('---')
            
            try:
                ################################################################################
                # Pontos de Saída
                ################################################################################
                if n_H <= 1:
                    st.text("Ponto de Saída: Ponto 3")
                    st.text(f"Jogos Analisados: {len(df_f)}")
                elif n_H == 2:
                    st.text("Ponto de Saída: Ponto 2")
                    st.text(f"Jogos Analisados: {len(df_f)}")
                elif n_H == 3:
                    st.text("Ponto de Saída: Ponto 1")
                    st.text(f"Jogos Analisados: {len(df_f)}")
                elif n_H >= 4:
                    st.text("Ponto de Saída: Não Faz Esse Placar ")
                    st.text(f"Jogos Analisados: {len(df_f)}")
                
                ################################################################################
                # Singularidade
                ################################################################################

                flt_sin_2anos = ((df.Season == '2023') | (df.Season == '2024') | (df.Season == '2022/2023') | (df.Season == '2023/2024'))
                df_sin2 = df[flt_sin_2anos]
                df_sin2 = drop_reset_index(df_sin2)
                
                # Home
                sing_H = df_sin2[df_sin2.Home == Fav_Home].copy()
                sing_H = sing_H[sing_H[Placar] == 1]
                n_sing_H = sing_H[sing_H.columns[0]].count()

                # Away
                sing_A = df_sin2[df_sin2.Away == Zeb_Away].copy()
                sing_A = sing_A[sing_A[Placar] == 1]
                n_sing_A = sing_A[sing_A.columns[0]].count()

                # Home x Away
                sing_HxA = df_sin2[(df_sin2.Home == Fav_Home) & (df_sin2.Away == Zeb_Away)].copy()
                sing_HxA = sing_HxA[sing_HxA[Placar] == 1]
                n_sing_HxA = sing_HxA[sing_HxA.columns[0]].count()
                if (n_sing_A == 0) & (n_sing_H == 0) & (n_sing_HxA == 0):
                    st.text("Este Placar é SINGULAR")

                st.markdown('---')
            except:
                st.markdown('---')

            try:
                ################################################################################
                # Odd Média do Time
                ################################################################################    
                df_Odd_Med = df[df.Home == Favorito]
                porcentagem_team_H = n_H / len(df_Odd_Med)
                odd_team_H = round((1 / porcentagem_team_H),2)
                if len(df_Odd_Med) != 0:
                    if odd_team_H != np.inf:
                        st.text("A Odd Média do " + Placar + " do " + Favorito + " é: " + str((odd_team_H)))
                    else:
                        st.text("A Odd Média do " + Placar + " do " + Favorito + " é: 1000")

                ################################################################################
                # Odd Média da Liga
                ################################################################################
                df_liga = df[df[Placar] == 1]
                porcentagem_liga = len(df_liga) / len(df)
                odd_liga = round((1 / porcentagem_liga),2)

                if odd_liga != np.inf:
                    st.text("A Odd Média do " + Placar + " da Liga " + League + " é: " + str((odd_liga)))
                else:
                    st.text("A Odd Média do " + Placar + " da Liga " + League + " é: 1000")

                ################################################################################
                # Odd Atual na Betfair
                ################################################################################
                odd_atual = Jogos[Jogos.Home == Fav_Home].copy()
                placar = 'Odd_'+ Placar
                odd_betfair = odd_atual[placar].tail(1).item()
                st.text("Odd Atual do Lay " + Placar + " do " + Fav_Home + " na Betfair é: " + str(odd_betfair))



                st.markdown('---')
            except:
                st.markdown('---')

            try:
                ################################################################################
                # Custo do Gol
                ################################################################################

                df_CG = df.copy()

                # Probabilidades
                df_CG['p_H'] = 1 / df_CG.Odd_H
                df_CG['p_D'] = 1 / df_CG.Odd_D
                df_CG['p_A'] = 1 / df_CG.Odd_A

                n_per = 5

                # Custo do Gol 1.0
                df_CG['CG_01_H'] = df_CG.Goals_H / df_CG.p_H
                df_CG['CG_01_A'] = df_CG.Goals_A / df_CG.p_A

                df_CG['Media_CG_01_H'] = df_CG.groupby('Home')['CG_01_H'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)
                df_CG['Media_CG_01_A'] = df_CG.groupby('Away')['CG_01_A'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)

                df_CG['Media_CG_01_H'] = df_CG.groupby('Home')['Media_CG_01_H'].shift(1)
                df_CG['Media_CG_01_A'] = df_CG.groupby('Away')['Media_CG_01_A'].shift(1)

                df_CG['DesvPad_CG_01_H'] = df_CG.groupby('Home')['CG_01_H'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)
                df_CG['DesvPad_CG_01_A'] = df_CG.groupby('Away')['CG_01_A'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)

                df_CG['DesvPad_CG_01_H'] = df_CG.groupby('Home')['DesvPad_CG_01_H'].shift(1)
                df_CG['DesvPad_CG_01_A'] = df_CG.groupby('Away')['DesvPad_CG_01_A'].shift(1)

                df_CG['CV_CG_01_H'] = df_CG['DesvPad_CG_01_H'] / df_CG['Media_CG_01_H']
                df_CG['CV_CG_01_A'] = df_CG['DesvPad_CG_01_A'] / df_CG['Media_CG_01_A']

                # Custo do Gol 2.0
                df_CG['CG_02_H'] = (df_CG.p_H / 2) + (df_CG.Goals_H / 2)
                df_CG['CG_02_A'] = (df_CG.p_A / 2) + (df_CG.Goals_A / 2)

                df_CG['Media_CG_02_H'] = df_CG.groupby('Home')['CG_02_H'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)
                df_CG['Media_CG_02_A'] = df_CG.groupby('Away')['CG_02_A'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)

                df_CG['Media_CG_02_H'] = df_CG.groupby('Home')['Media_CG_02_H'].shift(1)
                df_CG['Media_CG_02_A'] = df_CG.groupby('Away')['Media_CG_02_A'].shift(1)

                df_CG['DesvPad_CG_02_H'] = df_CG.groupby('Home')['CG_02_H'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)
                df_CG['DesvPad_CG_02_A'] = df_CG.groupby('Away')['CG_02_A'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)

                df_CG['DesvPad_CG_02_H'] = df_CG.groupby('Home')['DesvPad_CG_02_H'].shift(1)
                df_CG['DesvPad_CG_02_A'] = df_CG.groupby('Away')['DesvPad_CG_02_A'].shift(1)

                df_CG['CV_CG_02_H'] = df_CG['DesvPad_CG_02_H'] / df_CG['Media_CG_02_H']
                df_CG['CV_CG_02_A'] = df_CG['DesvPad_CG_02_A'] / df_CG['Media_CG_02_A']

                df_CG = drop_reset_index(df_CG)

                last = df_CG[df_CG['Home'] == Fav_Home].index[-1]
                media_cg_h = df_CG.at[last, 'Media_CG_01_H']
                
                last = df_CG[df_CG['Home'] == Fav_Home].index[-1]
                cv_cg_h = df_CG.at[last, 'CV_CG_01_H']
                
                last = df_CG[df_CG['Home'] == Fav_Home].index[-1]
                media_cg2_h = df_CG.at[last, 'Media_CG_02_H']
                
                last = df_CG[df_CG['Home'] == Fav_Home].index[-1]
                cv_cg2_h = df_CG.at[last, 'CV_CG_02_H']
                
                
                last = df_CG[df_CG['Away'] == Zeb_Away].index[-1]
                media_cg_a = df_CG.at[last, 'Media_CG_01_A']
                
                last = df_CG[df_CG['Away'] == Zeb_Away].index[-1]
                cv_cg_a = df_CG.at[last, 'CV_CG_01_A']
                
                last = df_CG[df_CG['Away'] == Zeb_Away].index[-1]
                media_cg2_a = df_CG.at[last, 'Media_CG_02_A']
                
                last = df_CG[df_CG['Away'] == Zeb_Away].index[-1]
                cv_cg2_a = df_CG.at[last, 'CV_CG_02_A']
                
                
                st.text(f'Índice de Eficiência (IF) - Ultimos {n_per} Jogos')
                st.text(f'{Fav_Home} - IF: {round(media_cg_h,2)}, CV: {round(cv_cg_h,2)}')
                st.text(f'{Zeb_Away} - IF: {round(media_cg_a,2)}, CV: {round(cv_cg_a,2)}')

                st.text('')
                st.text('')

                st.text(f'Coeficiente de Eficiência (CE) - Ultimos {n_per} Jogos')
                st.text(f'{Fav_Home} - CE: {round(media_cg2_h,2)}, CV: {round(cv_cg2_h,2)}')
                st.text(f'{Zeb_Away} - CE: {round(media_cg2_a,2)}, CV: {round(cv_cg2_a,2)}')



                st.markdown('---')
            except:
                st.markdown('---')

            try:
                ################################################################################
                # Singularidade Geral
                ################################################################################  
                # Home
                sing_H1 = df[df.Home == Fav_Home].copy()
                sing_H2 = sing_H1[sing_H1[Placar] == 1]
                por_H = (len(sing_H2) / len(sing_H1)) * 100
                # Colocar desde 2019
                st.text(f"Placar {Placar} com {round(por_H,2)} % de ocorrência para o Home (Pesquisa desde 2019)")

                sing_A1 = df[df.Away == Zeb_Away].copy()
                sing_A2 = sing_A1[sing_A1[Placar] == 1]
                por_A = (len(sing_A2) / len(sing_A1)) * 100
                st.text(f"Placar {Placar} com {round(por_A,2)} % de ocorrência para o Away (Pesquisa desde 2019)")

                # Home x Away
                sing_HxA1 = df[(df.Home == Fav_Home) & (df.Away == Zeb_Away)].copy()
                sing_HxA2 = sing_HxA1[sing_HxA1[Placar] == 1]

                if len(sing_HxA1) != 0:
                    por_HxA = (len(sing_HxA2) / len(sing_HxA1)) * 100
                    st.text(f"Placar {Placar} com {round(por_HxA,2)} % de ocorrência para o Confronto (Pesquisa desde 2019)")
                else:
                    st.text(f"Placar {Placar} com 0.0 % de ocorrência para o Confronto (Pesquisa desde 2019)")

                if (len(sing_H2) == 0) & (len(sing_A2) == 0) & (len(sing_HxA2) == 0):
                    st.text("Este placar é ULTRA SINGULAR")


                st.markdown('---')
            except:
                st.markdown('---')

            try:
                lista = ['0x0','0x1','0x2','0x3','1x0','1x1','1x2','1x3','2x0','2x1','2x2','2x3','3x0','3x1','3x2','3x3','Goleada_H','Goleada_A']

                for i in lista:
                    selecao_full = i
                    
                    # Home
                    sing_H = df_sin2[df_sin2.Home == Fav_Home].copy()
                    sing_H = sing_H[sing_H[selecao_full] == 1]
                    n_sing_H = sing_H[sing_H.columns[0]].count()

                    # Away
                    sing_A = df_sin2[df_sin2.Away == Zeb_Away].copy()
                    sing_A = sing_A[sing_A[selecao_full] == 1]
                    n_sing_A = sing_A[sing_A.columns[0]].count()

                    # Home x Away
                    sing_HxA = df_sin2[(df_sin2.Home == Fav_Home) & (df_sin2.Away == Zeb_Away)].copy()
                    sing_HxA = sing_HxA[sing_HxA[selecao_full] == 1]
                    n_sing_HxA = sing_HxA[sing_HxA.columns[0]].count()
                    if (n_sing_A == 0) & (n_sing_H == 0) & (n_sing_HxA == 0):
                        st.text(f"O Placar {selecao_full} é SINGULAR")


                # st.text('')
                # st.text('')

                # # Odd_1000

                # lista = ['0x0','0x1','0x2','0x3','1x0','1x1','1x2','1x3','2x0','2x1','2x2','2x3','3x0','3x1','3x2','3x3','Goleada_H','Goleada_A']

                # for i in lista:
                #     selecao_full = i
                    
                #     # Home
                #     df_home1000 = df[(df['Home'] == Fav_Home)]
                #     df_filtrado = df_home1000[(df_home1000[selecao_full] == 1)]
                #     df_filtrado = drop_reset_index(df_filtrado)
                #     n_H = len(df_filtrado)
                #     df1000_H = df[df.Home == Fav_Home]
                
                #     porcentagem_team_H = n_H / len(df1000_H)
                #     if porcentagem_team_H == 0:
                #         odd_team_H = float('inf')
                #     else:
                #         odd_team_H = 1 / porcentagem_team_H
                        
                #     # Away
                #     df_away1000 = df[(df['Away'] == Zeb_Away)]
                #     df_filtrado = df_away1000[(df_away1000[selecao_full] == 1)]
                #     df_filtrado = drop_reset_index(df_filtrado)
                #     n_A = len(df_filtrado)
                #     df1000_A = df[df.Away == Zeb_Away]
                
                #     porcentagem_team_A = n_A / len(df1000_A)
                #     if porcentagem_team_A == 0:
                #         odd_team_A = float('inf')
                #     else:
                #         odd_team_A = 1 / porcentagem_team_A
                
                #     if ((odd_team_H == np.inf) & (odd_team_A == np.inf)):
                #         st.text("O Placar "+ selecao_full + " é ODD 1000.")
                    
                    

                st.markdown('---')
            except:
                st.markdown('---')

            try:
            
                st.text("Odds Correct Score Pré-Live")
                st.text("")

                odd_0x0 = 'Odd_0x0'
                odd_0x1 = 'Odd_0x1'
                odd_0x2 = 'Odd_0x2'
                odd_0x3 = 'Odd_0x3'
                
                odd_1x0 = 'Odd_1x0'
                odd_1x1 = 'Odd_1x1'
                odd_1x2 = 'Odd_1x2'
                odd_1x3 = 'Odd_1x3'

                odd_2x0 = 'Odd_2x0'
                odd_2x1 = 'Odd_2x1'
                odd_2x2 = 'Odd_2x2'
                odd_2x3 = 'Odd_2x3'

                odd_3x0 = 'Odd_3x0'
                odd_3x1 = 'Odd_3x1'
                odd_3x2 = 'Odd_3x2'
                odd_3x3 = 'Odd_3x3'

                odd_goleada_h = 'Odd_Goleada_H'
                odd_goleada_a = 'Odd_Goleada_A'

                odds1, odds2, odds3, odds4, odds5 = st.columns(5)

                with odds1:
                    odd_betfair_0x0 = odd_atual[odd_0x0].tail(1).item()
                    st.text(f"0 x 0: {odd_betfair_0x0}")
                    odd_betfair_0x1 = odd_atual[odd_0x1].tail(1).item()
                    st.text(f"0 x 1: {odd_betfair_0x1}")
                    odd_betfair_0x2 = odd_atual[odd_0x2].tail(1).item()
                    st.text(f"0 x 2: {odd_betfair_0x2}")
                    odd_betfair_0x3 = odd_atual[odd_0x3].tail(1).item()
                    st.text(f"0 x 3: {odd_betfair_0x3}")
                with odds2:
                    odd_betfair_1x0 = odd_atual[odd_1x0].tail(1).item()
                    st.text(f"1 x 0: {odd_betfair_1x0}")
                    odd_betfair_1x1 = odd_atual[odd_1x1].tail(1).item()
                    st.text(f"1 x 1: {odd_betfair_1x1}")
                    odd_betfair_1x2 = odd_atual[odd_1x2].tail(1).item()
                    st.text(f"1 x 2: {odd_betfair_1x2}")
                    odd_betfair_1x3 = odd_atual[odd_1x3].tail(1).item()
                    st.text(f"1 x 3: {odd_betfair_1x3}")
                with odds3:
                    odd_betfair_2x0 = odd_atual[odd_2x0].tail(1).item()
                    st.text(f"2 x 0: {odd_betfair_2x0}")
                    odd_betfair_2x1 = odd_atual[odd_2x1].tail(1).item()
                    st.text(f"2 x 1: {odd_betfair_2x1}")
                    odd_betfair_2x2 = odd_atual[odd_2x2].tail(1).item()
                    st.text(f"2 x 2: {odd_betfair_2x2}")
                    odd_betfair_2x3 = odd_atual[odd_2x3].tail(1).item()
                    st.text(f"2 x 3: {odd_betfair_2x3}")
                with odds4:
                    odd_betfair_3x0 = odd_atual[odd_3x0].tail(1).item()
                    st.text(f"3 x 0: {odd_betfair_3x0}")
                    odd_betfair_3x1 = odd_atual[odd_3x1].tail(1).item()
                    st.text(f"3 x 1: {odd_betfair_3x1}")
                    odd_betfair_3x2 = odd_atual[odd_3x2].tail(1).item()
                    st.text(f"3 x 2: {odd_betfair_3x2}")
                    odd_betfair_3x3 = odd_atual[odd_3x3].tail(1).item()
                    st.text(f"3 x 3: {odd_betfair_3x3}")
                with odds5:
                    odd_betfair_goleada_h = odd_atual[odd_goleada_h].tail(1).item()
                    st.text(f"Goleada H: {odd_betfair_goleada_h}")
                    odd_betfair_goleada_a = odd_atual[odd_goleada_a].tail(1).item()
                    st.text(f"Goleada A: {odd_betfair_goleada_a}")
                    

                st.text('')
                st.text('')

                odd_betfair_1x0 = odd_atual['Odd_1x0'].tail(1).item()
                odd_betfair_1x1 = odd_atual['Odd_1x1'].tail(1).item()
                odd_betfair_1x2 = odd_atual['Odd_1x2'].tail(1).item()
                odd_betfair_2x0 = odd_atual['Odd_2x0'].tail(1).item()
                odd_betfair_2x2 = odd_atual['Odd_2x2'].tail(1).item()

                Ponta1 = odd_betfair_2x0 < odd_betfair_1x0
                Ponta2 = odd_betfair_2x0 < odd_betfair_1x1
                Ponta3 = odd_betfair_2x2 < odd_betfair_1x2

                if Ponta1 and Ponta2 and Ponta3:
                    st.text("Poseidon")
                elif Ponta1 and Ponta2:
                    st.text("Ponta 1 e Ponta 2")
                elif Ponta1 and Ponta3:
                    st.text("Ponta 1 e Ponta 3")
                elif Ponta2 and Ponta3:
                    st.text("Ponta 2 e Ponta 3")
                elif Ponta1:
                    st.text("Ponta 1")
                elif Ponta2:
                    st.text("Ponta 2")
                elif Ponta3:
                    st.text("Ponta 3")
                else:
                    st.text("Nenhuma Ponta Satisfeita")
                
                st.markdown('---')
            except:
                st.markdown('---')






            try:
                ################################################################################
                # Ultimos 10 Jogos do Favorito como Mandante
                ################################################################################

                df_10_jogos_H = df[df.Home == Fav_Home].tail(10)
                
                df_10_jogos_H = df_10_jogos_H[['Date', 'Season','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]
                df_10_jogos_H = drop_reset_index(df_10_jogos_H)
                df0 = df_10_jogos_H.copy()
                
                df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
                df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
                df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)
                df0['Odd_Over25'] = df0['Odd_Over25'].astype(float).map('{:.2f}'.format)
                df0['Odd_BTTS_Yes'] = df0['Odd_BTTS_Yes'].astype(float).map('{:.2f}'.format)

                df0 = df0[['Date','Season','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]
                df0.columns = ['Date','Season','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H_FT','Goals_A_FT','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']
                st.text("Ultimos 10 Jogos do Favorito como Mandante")
                st.dataframe(df0)
                st.markdown('---')
            except:
                st.markdown('---')

            try:
                ################################################################################
                # Ultimos 10 Jogos da Zebra como Visitante
                ################################################################################

                df_10_jogos_A = df[df.Away == Zeb_Away].tail(10)
                
                df_10_jogos_A = df_10_jogos_A[['Date', 'Season','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]
                df_10_jogos_A = drop_reset_index(df_10_jogos_A)

                df0 = df_10_jogos_A.copy()
                
                df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
                df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
                df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)
                df0['Odd_Over25'] = df0['Odd_Over25'].astype(float).map('{:.2f}'.format)
                df0['Odd_BTTS_Yes'] = df0['Odd_BTTS_Yes'].astype(float).map('{:.2f}'.format)

                df0 = df0[['Date','Season','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]
                df0.columns = ['Date','Season','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H_FT','Goals_A_FT','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']
                st.text("Ultimos 10 Jogos da Zebra como Visitante")
                st.dataframe(df0)

                st.markdown('---')
            except:
                st.markdown('---')


            try:
                ################################################################################
                # Confronto Direto
                ################################################################################
                
                df_Confronto = df[((df.Home == Fav_Home) & (df.Away == Zeb_Away))]
                df_Confronto = df_Confronto[['Date', 'Season','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]
                if len(df_Confronto) != 0:
                    
                    df0 = df_Confronto.copy()
                
                    df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
                    df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
                    df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)
                    df0['Odd_Over25'] = df0['Odd_Over25'].astype(float).map('{:.2f}'.format)
                    df0['Odd_BTTS_Yes'] = df0['Odd_BTTS_Yes'].astype(float).map('{:.2f}'.format)

                    df0 = df0[['Date','Season','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]
                    df0.columns = ['Date','Season','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H_FT','Goals_A_FT','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']
                    st.text("Confronto Direto - Temporadas Passadas")
                    df0 = drop_reset_index(df0)
                    st.dataframe(df0)
                    st.markdown('---')
                else:
                    st.text("Não Houve Confronto Direto nas Temporadas Passadas")
                    st.markdown('---')
            except:
                st.markdown('---')
            
            # try:
            #     ################################################################################
            #     # Classificação
            #     ################################################################################

            #     home = Fav_Home
            #     away = Zeb_Away

            #     flt = ((df_liga.Season == "2022/2023") | (df_liga.Season == '2023') )
            #     df_league = df_liga[flt]
                
            #     df_league = df_league[['Season','Home','Away','Goals_H','Goals_A']]

            #     df_league.loc[df_league['Goals_H'] > df_league['Goals_A'], 'Ptos_H'] = 3
            #     df_league.loc[df_league['Goals_H'] == df_league['Goals_A'], 'Ptos_H'] = 1
            #     df_league.loc[df_league['Goals_H'] < df_league['Goals_A'], 'Ptos_H'] = 0

            #     df_league.loc[df_league['Goals_H'] < df_league['Goals_A'], 'Ptos_A'] = 3
            #     df_league.loc[df_league['Goals_H'] == df_league['Goals_A'], 'Ptos_A'] = 1
            #     df_league.loc[df_league['Goals_H'] > df_league['Goals_A'], 'Ptos_A'] = 0

            #     teams = list(set(df_league['Home']).union(set(df_league['Away'])))
            #     classification_data = []

            #     for team in teams:
            #         home_matches = df_league[df_league['Home'] == team]
            #         away_matches = df_league[df_league['Away'] == team]
                    
            #         total_matches = pd.concat([home_matches, away_matches])
            #         points = (home_matches['Ptos_H'].sum()) + (away_matches['Ptos_A'].sum())
                    
            #         classification_data.append({
            #             'Team': team,
            #             'Points': points})

            #     classification_df_league = pd.DataFrame(classification_data)
            #     classification_df_league = classification_df_league.sort_values(by=['Points'], ascending=False)
            #     classification_df_league = classification_df_league.dropna()
            #     classification_df_league = classification_df_league.reset_index(drop=True)
            #     classification_df_league.index += 1

            #     team1 = home  # Substitua pelo nome do primeiro time
            #     team2 = away  # Substitua pelo nome do segundo time

            #     # Filtrar as linhas correspondentes aos times desejados
            #     team1_row = classification_df_league.loc[classification_df_league['Team'] == team1]
            #     team2_row = classification_df_league.loc[classification_df_league['Team'] == team2]

            #     # Obter o número da classificação (índice + 1) para cada time
            #     team1_rank = team1_row.index[0] if not team1_row.empty else None
            #     team2_rank = team2_row.index[0] if not team2_row.empty else None

            #     if team1_rank == None:
            #         st.text(f"{team1} não estava nessa divisão na temporada passada.")
            #     else:
            #         st.text(f"{team1} terminou a temporada passada classificado em {team1_rank}º lugar.")
            #     if team2_rank == None:
            #         st.text(f"{team2} não estava nessa divisão na temporada passada.")
            #     else:
            #         st.text(f"{team2} terminou a temporada passada classificado em {team2_rank}º lugar.")      
                
            #     st.text('')
            #     st.text('')

            #     home = Fav_Home
            #     away = Zeb_Away

            #     flt = ((df_liga.Season == "2023/2024") | (df_liga.Season == '2024') )
            #     df_league = df_liga[flt]
                
                
            #     df_league = df_league[['Season','Home','Away','Goals_H','Goals_A']]

            #     df_league.loc[df_league['Goals_H'] > df_league['Goals_A'], 'Ptos_H'] = 3
            #     df_league.loc[df_league['Goals_H'] == df_league['Goals_A'], 'Ptos_H'] = 1
            #     df_league.loc[df_league['Goals_H'] < df_league['Goals_A'], 'Ptos_H'] = 0

            #     df_league.loc[df_league['Goals_H'] < df_league['Goals_A'], 'Ptos_A'] = 3
            #     df_league.loc[df_league['Goals_H'] == df_league['Goals_A'], 'Ptos_A'] = 1
            #     df_league.loc[df_league['Goals_H'] > df_league['Goals_A'], 'Ptos_A'] = 0

            #     teams = list(set(df_league['Home']).union(set(df_league['Away'])))
            #     classification_data = []

            #     for team in teams:
            #         home_matches = df_league[df_league['Home'] == team]
            #         away_matches = df_league[df_league['Away'] == team]
                    
            #         total_matches = pd.concat([home_matches, away_matches])
            #         points = (home_matches['Ptos_H'].sum()) + (away_matches['Ptos_A'].sum())
                    
            #         classification_data.append({
            #             'Team': team,
            #             'Points': points})

            #     classification_df_league = pd.DataFrame(classification_data)
            #     classification_df_league = classification_df_league.sort_values(by=['Points'], ascending=False)
            #     classification_df_league = classification_df_league.dropna()
            #     classification_df_league = classification_df_league.reset_index(drop=True)
            #     classification_df_league.index += 1

            #     team1 = home  # Substitua pelo nome do primeiro time
            #     team2 = away  # Substitua pelo nome do segundo time

            #     # Filtrar as linhas correspondentes aos times desejados
            #     team1_row = classification_df_league.loc[classification_df_league['Team'] == team1]
            #     team2_row = classification_df_league.loc[classification_df_league['Team'] == team2]

            #     # Obter o número da classificação (índice + 1) para cada time
            #     team1_rank = team1_row.index[0] if not team1_row.empty else None
            #     team2_rank = team2_row.index[0] if not team2_row.empty else None

            #     if team1_rank == None:
            #         st.text(f"{team1} mudou de divisão.")
            #     else:
            #         st.text(f"{team1} está na temporada atual classificado em {team1_rank}º lugar.")
            #     if team2_rank == None:
            #         st.text(f"{team2} mudou de divisão.")
            #     else:
            #         st.text(f"{team2} está na temporada atual classificado em  {team2_rank}º lugar.")      
                
            #     st.markdown('---')
            # except:
            #     st.markdown('---')


            base = df.copy()

            ################################################################################
            # PDF do Theo
            ################################################################################
                
            df = base.copy()
            
            try:
                home = Fav_Home
                away = Zeb_Away

                df.loc[df['Goals_H'] > df['Goals_A'], 'Ptos_H'] = 3
                df.loc[df['Goals_H'] == df['Goals_A'], 'Ptos_H'] = 1
                df.loc[df['Goals_H'] < df['Goals_A'], 'Ptos_H'] = 0


                df.loc[df['Goals_H'] < df['Goals_A'], 'Ptos_A'] = 3
                df.loc[df['Goals_H'] == df['Goals_A'], 'Ptos_A'] = 1
                df.loc[df['Goals_H'] > df['Goals_A'], 'Ptos_A'] = 0
                
                df['Media_Ptos_H1'] = df.groupby('Home')['Ptos_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
                df['Media_Ptos_A1'] = df.groupby('Away')['Ptos_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
                
                df['Media_Ptos_H2'] = df.groupby('Home')['Ptos_H'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True)
                df['Media_Ptos_A2'] = df.groupby('Away')['Ptos_A'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True)
                
                df = drop_reset_index(df)
                
                flt = ((df.Season == "2023/2024") | (df.Season == '2024'))
                df = df[flt]
                
                
                flt_H = df.Home == home
                df_H = df[flt_H]
                flt_A = df.Away == away
                df_A = df[flt_A]
            
                
                df1_H = len(df_H)
                df1_H = f'{df1_H:.0f}'
                df1_A = len(df_A)
                df1_A = f'{df1_A:.0f}'
                
                # Número de Vitórias
                flt2_H = df_H.Goals_H > df_H.Goals_A
                df2_H = df_H[flt2_H]
                df2_H = df2_H.Home.count()
                
                flt2_A = df_A.Goals_H < df_A.Goals_A
                df2_A = df_A[flt2_A]
                df2_A = df2_A.Away.count()
                
                # Porcentagem de Vitórias
                por_H = round((round((df2_H / len(df_H)),2)*100))
                df3_H = str(por_H)+'%'
                por_A = round((round((df2_A / len(df_A)),2)*100))
                df3_A = por_A
                df3_A = str(por_A)+'%'
                
                # Média de Pontos Temporada Atual    
                mean_H = df.groupby(['Home'])['Ptos_H'].get_group(home).mean()
                df4_H = round(mean_H,2)
                mean_A = df.groupby(['Away'])['Ptos_A'].get_group(away).mean()
                df4_A = round(mean_A,2)
                
                # Média de Pontos Ultimos 10 Jogos
                df_H_PPG = df_H[['Home','Media_Ptos_H1']].tail(1)
                df_A_PPG = df_A[['Away','Media_Ptos_A1']].tail(1)
                df5_H = df_H_PPG.iloc[0]['Media_Ptos_H1']
                df5_A = df_A_PPG.iloc[0]['Media_Ptos_A1']
                
                # Média de Pontos Ultimos 5 Jogos
                df_H_PPG = df_H[['Home','Media_Ptos_H2']].tail(1)
                df_A_PPG = df_A[['Away','Media_Ptos_A2']].tail(1)
                df6_H = df_H_PPG.iloc[0]['Media_Ptos_H2']
                df6_A = df_A_PPG.iloc[0]['Media_Ptos_A2']
                
                
                # Jogos sem sofrer gols
                flt_gol_0_H = df_H.Goals_A == 0
                df_gol_0_H = df_H[flt_gol_0_H]
                count_gol_0_H = df_gol_0_H.Home.count() 
                por_count_gol_0_H = round((round((count_gol_0_H / len(df_H)),2)*100))
                por_count_gol_0_H = str(por_count_gol_0_H)+'%'
                
                flt_gol_0_A = df_A.Goals_H == 0
                df_gol_0_A = df_A[flt_gol_0_A]
                count_gol_0_A = df_gol_0_A.Away.count() 
                por_count_gol_0_A = round((round((count_gol_0_A / len(df_A)),2)*100))
                por_count_gol_0_A = str(por_count_gol_0_A)+'%'
                
                # Falhou em marcar
                flt_gol_failed_H = df_H.Goals_H == 0
                df_gol_failed_H = df_H[flt_gol_failed_H]
                count_gol_failed_H = df_gol_failed_H.Home.count() 
                por_count_gol_failed_H = round((round((count_gol_failed_H / len(df_H)),2)*100))
                por_count_gol_failed_H = str(por_count_gol_failed_H)+'%'
                
                flt_gol_failed_A = df_A.Goals_A == 0
                df_gol_failed_A = df_A[flt_gol_failed_A]
                count_gol_failed_A = df_gol_failed_A.Away.count() 
                por_count_gol_failed_A = round((round((count_gol_failed_A / len(df_A)),2)*100))
                por_count_gol_failed_A = str(por_count_gol_failed_A)+'%'
                
                # Ambas marcam
                flt_BTTS_H = (df_H.Goals_H != 0) & (df_H.Goals_A != 0)
                df_BTTS_H = df_H[flt_BTTS_H]
                count_BTTS_H = df_BTTS_H.Home.count() 
                por_count_BTTS_H = round((round((count_BTTS_H / len(df_H)),2)*100))
                por_count_BTTS_H = str(por_count_BTTS_H)+'%'
                
                flt_BTTS_A = (df_A.Goals_H != 0) & (df_A.Goals_A != 0)
                df_BTTS_A = df_A[flt_BTTS_A]
                count_BTTS_A = df_BTTS_A.Home.count() 
                por_count_BTTS_A = round((round((count_BTTS_A / len(df_A)),2)*100))
                por_count_BTTS_A = str(por_count_BTTS_A)+'%' 
                
                
                # Média de Gols em Casa
                
                # Gols Marcados   
                Goals_MH = df.groupby(['Home'])['Goals_H'].get_group(home).sum()
                Goals_MH = int(Goals_MH)
                Goals_MA = df.groupby(['Away'])['Goals_A'].get_group(away).sum()
                Goals_MA = int(Goals_MA)
                
                # Gols Sofridos
                Goals_SH = df.groupby(['Home'])['Goals_A'].get_group(home).sum()
                Goals_SH = int(Goals_SH)
                Goals_SA = df.groupby(['Away'])['Goals_H'].get_group(away).sum()
                Goals_SA = int(Goals_SA)
                
                # Média de gols marcados    
                mean_Goals_MH = df.groupby(['Home'])['Goals_H'].get_group(home).mean()
                mean_Goals_MH = round(mean_Goals_MH,2)
                mean_Goals_MA = df.groupby(['Away'])['Goals_A'].get_group(away).mean()
                mean_Goals_MA = round(mean_Goals_MA,2)
                
                # Média de gols sofridos    
                mean_Goals_SH = df.groupby(['Home'])['Goals_A'].get_group(home).mean()
                mean_Goals_SH = round(mean_Goals_SH,2)
                mean_Goals_SA = df.groupby(['Away'])['Goals_H'].get_group(away).mean()
                mean_Goals_SA = round(mean_Goals_SA,2)
                
                # Média total de gols 
                mean_Goals_TH = mean_Goals_MH + mean_Goals_SH
                mean_Goals_TH = f'{mean_Goals_TH:.2f}'
                mean_Goals_TA = mean_Goals_MA + mean_Goals_SA
                mean_Goals_TA = f'{mean_Goals_TA:.2f}'
                
                
                
                
                row_names = []
                df1 = pd.DataFrame([], index=row_names, columns=['Home'])
                
                row_names = ['Gols marcados','Gols sofridos','Média de gols marcados','Média de gols sofridos','Média total de gols']
                df2 = pd.DataFrame([], index=row_names, columns=['Away'])
                
                
                
                
                row_names = ['Total de Jogos','Vitórias','Pontos por Jogo (Temporada)','Pontos por Jogo (Últimos 10 Jogos)','Pontos por Jogo (Últimos 5 Jogos)',
                            'Gols Marcados','Gols Sofridos','Média de Gols Marcados','Média de Gols Sofridos','Média Total de Gols']
                df1 = pd.DataFrame([df1_H,df2_H,df4_H,df5_H,df6_H,Goals_MH,Goals_SH,mean_Goals_MH,mean_Goals_SH,mean_Goals_TH], index=row_names, columns=['Home'])
                
                row_names = ['Total de Jogos','Vitórias','Pontos por Jogo (Temporada)','Pontos por Jogo (Últimos 10 Jogos)','Pontos por Jogo (Últimos 5 Jogos)',
                            'Gols Marcados','Gols Sofridos','Média de Gols Marcados','Média de Gols Sofridos','Média Total de Gols']
                df2 = pd.DataFrame([df1_A,df2_A,df4_A,df5_A,df6_A,Goals_MA,Goals_SA,mean_Goals_MA,mean_Goals_SA,mean_Goals_TA], index=row_names, columns=['Away'])
                
                row_names = ['% de Vitórias','% Jogos sem Sofrer Gols','% Jogos sem Marcar Gols','% Ambas Marcam']
                df3 = pd.DataFrame([df3_H,por_count_gol_0_H,por_count_gol_failed_H,por_count_BTTS_H], index=row_names, columns=['Home'])
                
                row_names = ['% de Vitórias','% Jogos sem Sofrer Gols','% Jogos sem Marcar Gols','% Ambas Marcam']
                df4 = pd.DataFrame([df3_A,por_count_gol_0_A,por_count_gol_failed_A,por_count_BTTS_A], index=row_names, columns=['Away'])
                





                df12 = pd.concat([df1,df2], axis=1)
                df34 = pd.concat([df3,df4], axis=1)
                
                st.text('Aproveitamento dos Times (Mandante Jogando em Casa e Visitante Jogando Fora)')
                st.text('Temporada Atual')
                st.text('')
                texto = home + ' x ' + away
                st.write("<center>{}</center>".format(texto), unsafe_allow_html=True)
                st.write('')
                




                
                col1, col2 = st.columns(2)

                with col1:
                    st.dataframe(df12)

                with col2:
                    st.dataframe(df34)

                # st.markdown('---')  

                

            except:
                pass

            try:               
                
                # Total de Jogos 
                flt1 = df.Home == home
                df1 = df[flt1]
                flt2 = df.Away == away
                df2 = df[flt2]
                
                total_df1 = len(df1)
                total_df2 = len(df2)
                
                # Momento do Gol
                df_H = df_H.applymap(lambda x: x.replace("'","") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("[","") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("]","") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+1","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+2","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+3","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+4","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+5","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+6","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+7","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+8","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+9","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+10","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+11","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+12","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+13","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+14","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+15","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+16","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+17","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+18","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+19","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+20","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+1","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+2","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+3","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+4","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+5","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+6","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+7","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+8","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+9","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+10","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+11","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+12","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+13","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+14","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+15","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+16","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+17","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+18","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+19","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+20","90") if isinstance(x, str) else x)
                
                df_A = df_A.applymap(lambda x: x.replace("'","") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("[","") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("]","") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+1","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+2","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+3","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+4","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+5","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+6","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+7","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+8","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+9","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+10","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+11","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+12","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+13","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+14","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+15","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+16","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+17","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+18","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+19","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+20","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+1","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+2","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+3","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+4","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+5","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+6","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+7","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+8","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+9","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+10","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+10","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+11","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+12","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+13","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+14","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+15","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+16","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+17","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+18","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+19","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+20","90") if isinstance(x, str) else x)



                # Marca Primeiro
                df_H_PrimeiroGol = df_H[['Goals_H','Goals_A','Goals_Minutes_Home','Goals_Minutes_Away']]
                df_H_PrimeiroGol['TotalGoals'] = df_H_PrimeiroGol['Goals_H'] + df_H_PrimeiroGol['Goals_A'] 
                flt = df_H_PrimeiroGol.TotalGoals != 0
                df_H_PrimeiroGol = df_H_PrimeiroGol[flt]
            
                

                def deletar_conteudo_apos_virgula(valor):
                    return valor.split(',')[0]
                
                df_H_PrimeiroGol['Goals_Minutes_Home'] = df_H_PrimeiroGol['Goals_Minutes_Home'].apply(deletar_conteudo_apos_virgula)
                df_H_PrimeiroGol['Goals_Minutes_Away'] = df_H_PrimeiroGol['Goals_Minutes_Away'].apply(deletar_conteudo_apos_virgula)
                
                df_H_PrimeiroGol['Goals_Minutes_Home'] = pd.to_numeric(df_H_PrimeiroGol['Goals_Minutes_Home'], errors='coerce')
                df_H_PrimeiroGol['Goals_Minutes_Away'] = pd.to_numeric(df_H_PrimeiroGol['Goals_Minutes_Away'], errors='coerce')
                df_H_PrimeiroGol['Goals_Minutes_Home'] = df_H_PrimeiroGol['Goals_Minutes_Home'].fillna(1000)
                df_H_PrimeiroGol['Goals_Minutes_Away'] = df_H_PrimeiroGol['Goals_Minutes_Away'].fillna(1000)
                df_H_PrimeiroGol["Goals_Minutes_Home"] = df_H_PrimeiroGol["Goals_Minutes_Home"].astype('int')
                df_H_PrimeiroGol["Goals_Minutes_Away"] = df_H_PrimeiroGol["Goals_Minutes_Away"].astype('int')

                
                
                flt7 = df_H_PrimeiroGol['Goals_Minutes_Home'] < df_H_PrimeiroGol['Goals_Minutes_Away']
                marca_primeiro_H = df_H_PrimeiroGol[flt7]
                df7 = len(marca_primeiro_H) / len(df_H_PrimeiroGol)
                df7 = round((df7*100),)
                total_df7 = str(df7)+'%'
                
                
                df_A_PrimeiroGol = df_A[['Goals_H','Goals_A','Goals_Minutes_Home','Goals_Minutes_Away']]
                df_A_PrimeiroGol['TotalGoals'] = df_A_PrimeiroGol['Goals_H'] + df_A_PrimeiroGol['Goals_A'] 
                flt = df_A_PrimeiroGol.TotalGoals != 0
                df_A_PrimeiroGol = df_A_PrimeiroGol[flt]
                
                
                def deletar_conteudo_apos_virgula(valor):
                    return valor.split(',')[0]
                
                df_A_PrimeiroGol['Goals_Minutes_Home'] = df_A_PrimeiroGol['Goals_Minutes_Home'].apply(deletar_conteudo_apos_virgula)
                df_A_PrimeiroGol['Goals_Minutes_Away'] = df_A_PrimeiroGol['Goals_Minutes_Away'].apply(deletar_conteudo_apos_virgula)
                
                df_A_PrimeiroGol['Goals_Minutes_Home'] = pd.to_numeric(df_A_PrimeiroGol['Goals_Minutes_Home'], errors='coerce')
                df_A_PrimeiroGol['Goals_Minutes_Away'] = pd.to_numeric(df_A_PrimeiroGol['Goals_Minutes_Away'], errors='coerce')
                df_A_PrimeiroGol['Goals_Minutes_Home'] = df_A_PrimeiroGol['Goals_Minutes_Home'].fillna(1000)
                df_A_PrimeiroGol['Goals_Minutes_Away'] = df_A_PrimeiroGol['Goals_Minutes_Away'].fillna(1000)
                df_A_PrimeiroGol["Goals_Minutes_Home"] = df_A_PrimeiroGol["Goals_Minutes_Home"].astype('int')
                df_A_PrimeiroGol["Goals_Minutes_Away"] = df_A_PrimeiroGol["Goals_Minutes_Away"].astype('int')
                
                flt8 = df_A_PrimeiroGol['Goals_Minutes_Away'] < df_A_PrimeiroGol['Goals_Minutes_Home']
                marca_primeiro_A = df_A_PrimeiroGol[flt8]
                df8 = len(marca_primeiro_A) / len(df_A_PrimeiroGol)
                df8 = round((df8*100),)
                total_df8 = str(df8)+'%'
                
                
                flt9 = marca_primeiro_H.Goals_H > marca_primeiro_H.Goals_A
                marcou_e_ganhou = marca_primeiro_H[flt9]
                df9 = len(marcou_e_ganhou) / len(marca_primeiro_H)
                df9 = round((df9*100),)
                total_df9 = str(df9)+'%'
                
                flt10 = marca_primeiro_A.Goals_A > marca_primeiro_A.Goals_H
                marcou_e_ganhou = marca_primeiro_A[flt10]
                df10 = len(marcou_e_ganhou) / len(marca_primeiro_A)
                df10 = round((df10*100),)
                total_df10 = str(df10)+'%'
                
                flt11 = marca_primeiro_H.Goals_H == marca_primeiro_H.Goals_A
                marcou_e_empatou = marca_primeiro_H[flt11]
                df11 = len(marcou_e_empatou) / len(marca_primeiro_H)
                df11 = round((df11*100),)
                total_df11 = str(df11)+'%'
                
                flt12 = marca_primeiro_A.Goals_A == marca_primeiro_A.Goals_H
                marcou_e_empatou = marca_primeiro_A[flt12]
                df12 = len(marcou_e_empatou) / len(marca_primeiro_A)
                df12 = round((df12*100),)
                total_df12 = str(df12)+'%'
                
                flt13 = marca_primeiro_H.Goals_H < marca_primeiro_H.Goals_A
                marcou_e_perdeu = marca_primeiro_H[flt13]
                df13 = len(marcou_e_perdeu) / len(marca_primeiro_H)
                df13 = round((df13*100),)
                total_df13 = str(df13)+'%'
                
                flt14 = marca_primeiro_A.Goals_A < marca_primeiro_A.Goals_H
                marcou_e_perdeu = marca_primeiro_A[flt14]
                df14 = len(marcou_e_perdeu) / len(marca_primeiro_A)
                df14 = round((df14*100),)
                total_df14 = str(df14)+'%'
                
                flt15 = df_H_PrimeiroGol['Goals_Minutes_Home'] > df_H_PrimeiroGol['Goals_Minutes_Away']
                leva_primeiro_H = df_H_PrimeiroGol[flt15]
                df15 = len(leva_primeiro_H) / len(df_H_PrimeiroGol)
                df15 = round((df15*100),)
                total_df15 = str(df15)+'%'
                
                
                
                flt16 = df_A_PrimeiroGol['Goals_Minutes_Away'] > df_A_PrimeiroGol['Goals_Minutes_Home']
                leva_primeiro_A = df_A_PrimeiroGol[flt16]
                df16 = len(leva_primeiro_A) / len(df_A_PrimeiroGol)
                df16 = round((df16*100),)
                total_df16 = str(df16)+'%'
                
                flt17 = leva_primeiro_H['Goals_H'] > leva_primeiro_H['Goals_A']
                levou_e_ganhou = leva_primeiro_H[flt17]
                df17 = len(levou_e_ganhou) / len(leva_primeiro_H)
                df17 = round((df17*100),)
                total_df17 = str(df17)+'%'
            
                
                flt18 = leva_primeiro_A['Goals_A'] > leva_primeiro_A['Goals_H']
                levou_e_ganhou = leva_primeiro_A[flt18]
                df18 = len(levou_e_ganhou) / len(leva_primeiro_A)
                df18 = round((df18*100),)
                total_df18 = str(df18)+'%'
                
                
                
                flt19 = leva_primeiro_H.Goals_H == leva_primeiro_H.Goals_A
                levou_e_empatou = leva_primeiro_H[flt19]
                df19 = len(levou_e_empatou) / len(leva_primeiro_H)
                df19 = round((df19*100),)
                total_df19 = str(df19)+'%'
                
                
                flt20 = leva_primeiro_A.Goals_H == leva_primeiro_A.Goals_A
                levou_e_empatou = leva_primeiro_A[flt20]
                df20 = len(levou_e_empatou) / len(leva_primeiro_A)
                df20 = round((df20*100),)
                total_df20 = str(df20)+'%'
                
                
                flt21 = leva_primeiro_H.Goals_H < leva_primeiro_H.Goals_A
                levou_e_perdeu = leva_primeiro_H[flt21]
                df21 = len(levou_e_perdeu) / len(leva_primeiro_H)
                df21 = round((df21*100),)
                total_df21 = str(df21)+'%'
                
                
                flt22 = leva_primeiro_A.Goals_A < leva_primeiro_A.Goals_H
                levou_e_perdeu = leva_primeiro_A[flt22]
                df22 = len(levou_e_perdeu) / len(leva_primeiro_A)
                df22 = round((df22*100),)
                total_df22 = str(df22)+'%'
                
                # Marcou o Primeiro Gol no 1º Tempo
                flt_1T_01 = ((df_H_PrimeiroGol.Goals_Minutes_Home < 46) 
                    & (df_H_PrimeiroGol.Goals_Minutes_Home < df_H_PrimeiroGol.Goals_Minutes_Away))
                        
                df_1T_01 = df_H_PrimeiroGol[flt_1T_01]
                num_1T_01 = len(df_1T_01) / len(df_H_PrimeiroGol)
                df_1T_01 = round((num_1T_01*100),)
                df_1T_01 = str(df_1T_01)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Ganhou
                flt_1T_02 = ((df_H_PrimeiroGol.Goals_Minutes_Home < 46) 
                    & (df_H_PrimeiroGol.Goals_Minutes_Home < df_H_PrimeiroGol.Goals_Minutes_Away)
                    & (df_H_PrimeiroGol.Goals_H > df_H_PrimeiroGol.Goals_A))
                        
                df_1T_02 = df_H_PrimeiroGol[flt_1T_02]
                num_1T_02 = len(df_1T_02) / len(df_H_PrimeiroGol)
                df_1T_02 = round((num_1T_02*100),)
                df_1T_02 = str(df_1T_02)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Empatou
                flt_1T_03 = ((df_H_PrimeiroGol.Goals_Minutes_Home < 46) 
                    & (df_H_PrimeiroGol.Goals_Minutes_Home < df_H_PrimeiroGol.Goals_Minutes_Away)
                    & (df_H_PrimeiroGol.Goals_H == df_H_PrimeiroGol.Goals_A))
                        
                df_1T_03 = df_H_PrimeiroGol[flt_1T_03]
                num_1T_03 = len(df_1T_03) / len(df_H_PrimeiroGol)
                df_1T_03 = round((num_1T_03*100),)
                df_1T_03 = str(df_1T_03)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Perdeu
                flt_1T_04 = ((df_H_PrimeiroGol.Goals_Minutes_Home < 46) 
                    & (df_H_PrimeiroGol.Goals_Minutes_Home < df_H_PrimeiroGol.Goals_Minutes_Away)
                    & (df_H_PrimeiroGol.Goals_H < df_H_PrimeiroGol.Goals_A))
                        
                df_1T_04 = df_H_PrimeiroGol[flt_1T_04]
                num_1T_04 = len(df_1T_04) / len(df_H_PrimeiroGol)
                df_1T_04 = round((num_1T_04*100),)
                df_1T_04 = str(df_1T_04)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo
                flt_1T_05 = ((df_A_PrimeiroGol.Goals_Minutes_Away < 46) 
                    & (df_A_PrimeiroGol.Goals_Minutes_Away < df_A_PrimeiroGol.Goals_Minutes_Home))
                        
                df_1T_05 = df_A_PrimeiroGol[flt_1T_05]
                num_1T_05 = len(df_1T_05) / len(df_A_PrimeiroGol)
                df_1T_05 = round((num_1T_05*100),)
                df_1T_05 = str(df_1T_05)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Ganhou
                flt_1T_06 = ((df_A_PrimeiroGol.Goals_Minutes_Away < 46) 
                            & (df_A_PrimeiroGol.Goals_Minutes_Away < df_A_PrimeiroGol.Goals_Minutes_Home)
                            & (df_A_PrimeiroGol.Goals_A > df_A_PrimeiroGol.Goals_H))
                        
                df_1T_06 = df_A_PrimeiroGol[flt_1T_06]
                num_1T_06 = len(df_1T_06) / len(df_A_PrimeiroGol)
                df_1T_06 = round((num_1T_06*100),)
                df_1T_06 = str(df_1T_06)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Empatou
                flt_1T_07 = ((df_A_PrimeiroGol.Goals_Minutes_Away < 46) 
                            & (df_A_PrimeiroGol.Goals_Minutes_Away < df_A_PrimeiroGol.Goals_Minutes_Home)
                            & (df_A_PrimeiroGol.Goals_A == df_A_PrimeiroGol.Goals_H))
                        
                df_1T_07 = df_A_PrimeiroGol[flt_1T_07]
                num_1T_07 = len(df_1T_07) / len(df_A_PrimeiroGol)
                df_1T_07 = round((num_1T_07*100),)
                df_1T_07 = str(df_1T_07)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Perdeu
                flt_1T_08 = ((df_A_PrimeiroGol.Goals_Minutes_Away < 46) 
                            & (df_A_PrimeiroGol.Goals_Minutes_Away < df_A_PrimeiroGol.Goals_Minutes_Home)
                            & (df_A_PrimeiroGol.Goals_A < df_A_PrimeiroGol.Goals_H))
                        
                df_1T_08 = df_A_PrimeiroGol[flt_1T_08]
                num_1T_08 = len(df_1T_08) / len(df_A_PrimeiroGol)
                df_1T_08 = round((num_1T_08*100),)
                df_1T_08 = str(df_1T_08)+'%'
                
                
                
                
                row_names = ['% Jogos que Marcou 1º Gol','% Jogos que Marcou 1º Gol e Venceu','% Jogos que Marcou 1º Gol e Empatou','% Jogos que Marcou 1º Gol e Perdeu',
                            '% Jogos que Sofreu 1º Gol','% Jogos que Sofreu 1º Gol e Venceu','% Jogos que Sofreu 1º Gol e Empatou','% Jogos que Sofreu 1º Gol e Perdeu',
                            '% Jogos que Marcou o Primeiro Gol no 1º Tempo','% Jogos que Marcou o Primeiro Gol no 1º Tempo e Venceu','% Jogos que Marcou o Primeiro Gol no 1º Tempo e Empatou','% Jogos que Marcou o Primeiro Gol no 1º Tempo e Perdeu']
                df1 = pd.DataFrame([total_df7,total_df9,total_df11,total_df13,total_df15,total_df17,total_df19,total_df21,df_1T_01,df_1T_02,df_1T_03,df_1T_04], index=row_names, columns=['Home'])
                
                row_names = ['% Jogos que Marcou 1º Gol','% Jogos que Marcou 1º Gol e Venceu','% Jogos que Marcou 1º Gol e Empatou','% Jogos que Marcou 1º Gol e Perdeu',
                            '% Jogos que Sofreu 1º Gol','% Jogos que Sofreu 1º Gol e Venceu','% Jogos que Sofreu 1º Gol e Empatou','% Jogos que Sofreu 1º Gol e Perdeu',
                            '% Jogos que Marcou o Primeiro Gol no 1º Tempo','% Jogos que Marcou o Primeiro Gol no 1º Tempo e Venceu','% Jogos que Marcou o Primeiro Gol no 1º Tempo e Empatou','% Jogos que Marcou o Primeiro Gol no 1º Tempo e Perdeu']
                df2 = pd.DataFrame([total_df8,total_df10,total_df12,total_df14,total_df16,total_df18,total_df20,total_df22,df_1T_05,df_1T_06,df_1T_07,df_1T_08], index=row_names, columns=['Away'])
                
                
                df0 = pd.concat([df1,df2], axis=1)
                st.text('Análise do 1º Gol - Mandante Jogando em Casa e Visitante Jogando Fora')
                st.write(df0)
                # st.markdown('---')
                
            except:
                pass

            try:    
                    
                # Time Mandante - Gols Marcados
                
                min_gols_H = df_H[['Goals_H','Goals_Minutes_Home']]
                flt = min_gols_H.Goals_H != 0
                min_gols_H = min_gols_H[flt]
                min_gols_H = min_gols_H[['Goals_Minutes_Home']]
                
                # Time Mandante - Gols Sofridos
                
                min_gols_HS = df_H[['Goals_A','Goals_Minutes_Away']]
                flt = min_gols_HS.Goals_A != 0
                min_gols_HS = min_gols_HS[flt]
                min_gols_HS = min_gols_HS[['Goals_Minutes_Away']]
                
                # Time Visitante - Gols Marcados
                
                min_gols_A = df_A[['Goals_A','Goals_Minutes_Away']]
                flt = min_gols_A.Goals_A != 0
                min_gols_A = min_gols_A[flt]
                min_gols_A = min_gols_A[['Goals_Minutes_Away']]
                
                # Time Visitante - Gols Sofridos
                
                min_gols_AS = df_A[['Goals_H','Goals_Minutes_Home']]
                flt = min_gols_AS.Goals_H != 0
                min_gols_AS = min_gols_AS[flt]
                min_gols_AS = min_gols_AS[['Goals_Minutes_Home']]
                
                
                # Gols Marcados - Mandante
                Momentos_GM_H = list(min_gols_H['Goals_Minutes_Home'])
                string_concatenada_GM_H = ', '.join(Momentos_GM_H)
                lista_numeros_GM_H = list(map(int, string_concatenada_GM_H.split(", ")))
                lista_numeros_GM_H.sort()
                
                contador_0_15 = 0
                
                for numero in lista_numeros_GM_H:
                    if numero >= 0 and numero <= 15:
                        contador_0_15 += 1
                GM_H_0_15 = contador_0_15
                GM_H_0_15 = round(((GM_H_0_15 / len(lista_numeros_GM_H)) * 100), 2)
                GM_H_0_15 = str(GM_H_0_15)+'%'
                
                contador_16_30 = 0
                
                for numero in lista_numeros_GM_H:
                    if numero >= 16 and numero <= 30:
                        contador_16_30 += 1
                GM_H_16_30 = contador_16_30
                GM_H_16_30 = round(((GM_H_16_30 / len(lista_numeros_GM_H)) * 100), 2)
                GM_H_16_30 = str(GM_H_16_30)+'%'
                
                contador_31_45 = 0
                
                for numero in lista_numeros_GM_H:
                    if numero >= 31 and numero <= 45:
                        contador_31_45 += 1
                GM_H_31_45 = contador_31_45
                GM_H_31_45 = round(((GM_H_31_45 / len(lista_numeros_GM_H)) * 100), 2)
                GM_H_31_45 = str(GM_H_31_45)+'%'
                
                contador_46_60 = 0
                
                for numero in lista_numeros_GM_H:
                    if numero >= 46 and numero <= 60:
                        contador_46_60 += 1
                GM_H_46_60 = contador_46_60
                GM_H_46_60 = round(((GM_H_46_60 / len(lista_numeros_GM_H)) * 100), 2)
                GM_H_46_60 = str(GM_H_46_60)+'%'
                
                contador_61_75 = 0
                
                for numero in lista_numeros_GM_H:
                    if numero >= 61 and numero <= 75:
                        contador_61_75 += 1
                GM_H_61_75 = contador_61_75
                GM_H_61_75 = round(((GM_H_61_75 / len(lista_numeros_GM_H)) * 100), 2)
                GM_H_61_75 = str(GM_H_61_75)+'%'
                
                contador_76_90 = 0
                
                for numero in lista_numeros_GM_H:
                    if numero >= 76 and numero <= 90:
                        contador_76_90 += 1
                GM_H_76_90 = contador_76_90
                GM_H_76_90 = round(((GM_H_76_90 / len(lista_numeros_GM_H)) * 100), 2)
                GM_H_76_90 = str(GM_H_76_90)+'%'
                
                
                # Gols Sofridos - Mandante
                Momentos_GS_H = list(min_gols_HS['Goals_Minutes_Away'])
                try:
                    string_concatenada_GS_H = ', '.join(Momentos_GS_H)
                    lista_numeros_GS_H = list(map(int, string_concatenada_GS_H.split(", ")))
                    lista_numeros_GS_H.sort()
                except:
                    lista_numeros_GS_H = [-1]
                
                
                contador_0_15 = 0
                
                for numero in lista_numeros_GS_H:
                    if numero >= 0 and numero <= 15:
                        contador_0_15 += 1
                GS_H_0_15 = contador_0_15
                GS_H_0_15 = round(((GS_H_0_15 / len(lista_numeros_GS_H)) * 100), 2)
                GS_H_0_15 = str(GS_H_0_15)+'%'
                
                contador_16_30 = 0
                
                for numero in lista_numeros_GS_H:
                    if numero >= 16 and numero <= 30:
                        contador_16_30 += 1
                GS_H_16_30 = contador_16_30
                GS_H_16_30 = round(((GS_H_16_30 / len(lista_numeros_GS_H)) * 100), 2)
                GS_H_16_30 = str(GS_H_16_30)+'%'
                
                contador_31_45 = 0
                
                for numero in lista_numeros_GS_H:
                    if numero >= 31 and numero <= 45:
                        contador_31_45 += 1
                GS_H_31_45 = contador_31_45
                GS_H_31_45 = round(((GS_H_31_45 / len(lista_numeros_GS_H)) * 100), 2)
                GS_H_31_45 = str(GS_H_31_45)+'%'
                
                contador_46_60 = 0
                
                for numero in lista_numeros_GS_H:
                    if numero >= 46 and numero <= 60:
                        contador_46_60 += 1
                GS_H_46_60 = contador_46_60
                GS_H_46_60 = round(((GS_H_46_60 / len(lista_numeros_GS_H)) * 100), 2)
                GS_H_46_60 = str(GS_H_46_60)+'%'
                
                contador_61_75 = 0
                
                for numero in lista_numeros_GS_H:
                    if numero >= 61 and numero <= 75:
                        contador_61_75 += 1
                GS_H_61_75 = contador_61_75
                GS_H_61_75 = round(((GS_H_61_75 / len(lista_numeros_GS_H)) * 100), 2)
                GS_H_61_75 = str(GS_H_61_75)+'%'
                
                contador_76_90 = 0
                
                for numero in lista_numeros_GS_H:
                    if numero >= 76 and numero <= 90:
                        contador_76_90 += 1
                GS_H_76_90 = contador_76_90
                GS_H_76_90 = round(((GS_H_76_90 / len(lista_numeros_GS_H)) * 100), 2)
                GS_H_76_90 = str(GS_H_76_90)+'%'
                
                
                
                
                
                # Gols Marcados - Visitante
                Momentos_GM_A = list(min_gols_A['Goals_Minutes_Away'])
                string_concatenada_GM_A = ', '.join(Momentos_GM_A)
                lista_numeros_GM_A = list(map(int, string_concatenada_GM_A.split(", ")))
                lista_numeros_GM_A.sort()
                
                contador_0_15 = 0
                
                for numero in lista_numeros_GM_A:
                    if numero >= 0 and numero <= 15:
                        contador_0_15 += 1
                GM_A_0_15 = contador_0_15
                GM_A_0_15 = round(((GM_A_0_15 / len(lista_numeros_GS_H)) * 100), 2)
                GM_A_0_15 = str(GM_A_0_15)+'%'
                
                contador_16_30 = 0
                
                for numero in lista_numeros_GM_A:
                    if numero >= 16 and numero <= 30:
                        contador_16_30 += 1
                GM_A_16_30 = contador_16_30
                GM_A_16_30 = round(((GM_A_16_30 / len(lista_numeros_GS_H)) * 100), 2)
                GM_A_16_30 = str(GM_A_16_30)+'%'
                
                contador_31_45 = 0
                
                for numero in lista_numeros_GM_A:
                    if numero >= 31 and numero <= 45:
                        contador_31_45 += 1
                GM_A_31_45 = contador_31_45
                GM_A_31_45 = round(((GM_A_31_45 / len(lista_numeros_GS_H)) * 100), 2)
                GM_A_31_45 = str(GM_A_31_45)+'%'
                
                contador_46_60 = 0
                
                for numero in lista_numeros_GM_A:
                    if numero >= 46 and numero <= 60:
                        contador_46_60 += 1
                GM_A_46_60 = contador_46_60
                GM_A_46_60 = round(((GM_A_46_60 / len(lista_numeros_GS_H)) * 100), 2)
                GM_A_46_60 = str(GM_A_46_60)+'%'
                
                contador_61_75 = 0
                
                for numero in lista_numeros_GM_A:
                    if numero >= 61 and numero <= 75:
                        contador_61_75 += 1
                GM_A_61_75 = contador_61_75
                GM_A_61_75 = round(((GM_A_61_75 / len(lista_numeros_GS_H)) * 100), 2)
                GM_A_61_75 = str(GM_A_61_75)+'%'
                
                contador_76_90 = 0
                
                for numero in lista_numeros_GM_A:
                    if numero >= 76 and numero <= 90:
                        contador_76_90 += 1
                GM_A_76_90 = contador_76_90
                GM_A_76_90 = round(((GM_A_76_90 / len(lista_numeros_GS_H)) * 100), 2)
                GM_A_76_90 = str(GM_A_76_90)+'%'
                
                
                # Gols Sofridos - Visitante
                Momentos_GS_A = list(min_gols_AS['Goals_Minutes_Home'])
                string_concatenada_GS_A = ', '.join(Momentos_GS_A)
                lista_numeros_GS_A = list(map(int, string_concatenada_GS_A.split(", ")))
                lista_numeros_GS_A.sort()
                
                contador_0_15 = 0
                
                for numero in lista_numeros_GS_A:
                    if numero >= 0 and numero <= 15:
                        contador_0_15 += 1
                GS_A_0_15 = contador_0_15
                GS_A_0_15 = round(((GS_A_0_15 / len(lista_numeros_GS_H)) * 100), 2)
                GS_A_0_15 = str(GS_A_0_15)+'%'
                
                contador_16_30 = 0
                
                for numero in lista_numeros_GS_A:
                    if numero >= 16 and numero <= 30:
                        contador_16_30 += 1
                GS_A_16_30 = contador_16_30
                GS_A_16_30 = round(((GS_A_16_30 / len(lista_numeros_GS_H)) * 100), 2)
                GS_A_16_30 = str(GS_A_16_30)+'%'
                
                contador_31_45 = 0
                
                for numero in lista_numeros_GS_A:
                    if numero >= 31 and numero <= 45:
                        contador_31_45 += 1
                GS_A_31_45 = contador_31_45
                GS_A_31_45 = round(((GS_A_31_45 / len(lista_numeros_GS_H)) * 100), 2)
                GS_A_31_45 = str(GS_A_31_45)+'%'
                
                contador_46_60 = 0
                
                for numero in lista_numeros_GS_A:
                    if numero >= 46 and numero <= 60:
                        contador_46_60 += 1
                GS_A_46_60 = contador_46_60
                GS_A_46_60 = round(((GS_A_46_60 / len(lista_numeros_GS_H)) * 100), 2)
                GS_A_46_60 = str(GS_A_46_60)+'%'
                
                contador_61_75 = 0
                
                for numero in lista_numeros_GS_A:
                    if numero >= 61 and numero <= 75:
                        contador_61_75 += 1
                GS_A_61_75 = contador_61_75
                GS_A_61_75 = round(((GS_A_61_75 / len(lista_numeros_GS_H)) * 100), 2)
                GS_A_61_75 = str(GS_A_61_75)+'%'
                
                contador_76_90 = 0
                
                for numero in lista_numeros_GS_A:
                    if numero >= 76 and numero <= 90:
                        contador_76_90 += 1
                GS_A_76_90 = contador_76_90
                GS_A_76_90 = round(((GS_A_76_90 / len(lista_numeros_GS_H)) * 100), 2)
                GS_A_76_90 = str(GS_A_76_90)+'%'
                
                
                
                
                
                row_names = ['00 - 15','16 - 30','31 - 45','46 - 60','61 - 75','76 - 90']
                df1 = pd.DataFrame([GM_H_0_15, GM_H_16_30, GM_H_31_45, GM_H_46_60, GM_H_61_75, GM_H_76_90], index=row_names, columns=['Marcados'])
                
                row_names = ['00 - 15','16 - 30','31 - 45','46 - 60','61 - 75','76 - 90']
                df2 = pd.DataFrame([GS_H_0_15, GS_H_16_30, GS_H_31_45, GS_H_46_60, GS_H_61_75, GS_H_76_90], index=row_names, columns=['Sofridos'])
                
                row_names = ['00 - 15','16 - 30','31 - 45','46 - 60','61 - 75','76 - 90']
                df3 = pd.DataFrame([GM_A_0_15, GM_A_16_30, GM_A_31_45, GM_A_46_60, GM_A_61_75, GM_A_76_90], index=row_names, columns=['Marcados'])
                
                row_names = ['00 - 15','16 - 30','31 - 45','46 - 60','61 - 75','76 - 90']
                df4 = pd.DataFrame([GS_A_0_15, GS_A_16_30, GS_A_31_45, GS_A_46_60, GS_A_61_75, GS_A_76_90], index=row_names, columns=['Sofridos'])
                
                
                # Colocar com cores (acrescentar as quantidades)
                df1 = pd.concat([df1,df2], axis=1)
                print('Minutos dos Gols -',home)

                
                df2 = pd.concat([df3,df4], axis=1)
                print('Minutos dos Gols -',away)

                # col1, col2 = st.columns(2)

                # with col1:
                #     st.write('Minutos dos Gols -',home)
                #     st.write(df1)

                # with col2:
                #     st.write('Minutos dos Gols -',away)
                #     st.write(df2)

                tt1 = df1.copy()
                tt2 = df2.copy()

                # st.markdown('---')        

            

                flt_Over05_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 0)
                df_Over05_H = df_H[flt_Over05_H]
                count_Over05_H = df_Over05_H.Home.count() 
                por_count_Over05_H = round((round((count_Over05_H / len(df_H)),2)*100))
                por_count_Over05_H = str(por_count_Over05_H)+'%'
                
                flt_Over05_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 0)
                df_Over05_A = df_A[flt_Over05_A]
                count_Over05_A = df_Over05_A.Away.count() 
                por_count_Over05_A = round((round((count_Over05_A / len(df_A)),2)*100))
                por_count_Over05_A = str(por_count_Over05_A)+'%'
                
                flt_Over15_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 1)
                df_Over15_H = df_H[flt_Over15_H]
                count_Over15_H = df_Over15_H.Home.count() 
                por_count_Over15_H = round((round((count_Over15_H / len(df_H)),2)*100))
                por_count_Over15_H = str(por_count_Over15_H)+'%'
                
                flt_Over15_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 1)
                df_Over15_A = df_A[flt_Over15_A]
                count_Over15_A = df_Over15_A.Away.count() 
                por_count_Over15_A = round((round((count_Over15_A / len(df_A)),2)*100))
                por_count_Over15_A = str(por_count_Over15_A)+'%'
                
                flt_Over25_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 2)
                df_Over25_H = df_H[flt_Over25_H]
                count_Over25_H = df_Over25_H.Home.count() 
                por_count_Over25_H = round((round((count_Over25_H / len(df_H)),2)*100))
                por_count_Over25_H = str(por_count_Over25_H)+'%'
                
                flt_Over25_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 2)
                df_Over25_A = df_A[flt_Over25_A]
                count_Over25_A = df_Over25_A.Away.count() 
                por_count_Over25_A = round((round((count_Over25_A / len(df_A)),2)*100))
                por_count_Over25_A = str(por_count_Over25_A)+'%'
                
                flt_Over35_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 3)
                df_Over35_H = df_H[flt_Over35_H]
                count_Over35_H = df_Over35_H.Home.count() 
                por_count_Over35_H = round((round((count_Over35_H / len(df_H)),2)*100))
                por_count_Over35_H = str(por_count_Over35_H)+'%'
                
                flt_Over35_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 3)
                df_Over35_A = df_A[flt_Over35_A]
                count_Over35_A = df_Over35_A.Away.count() 
                por_count_Over35_A = round((round((count_Over35_A / len(df_A)),2)*100))
                por_count_Over35_A = str(por_count_Over35_A)+'%'
                
                flt_Over45_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 4)
                df_Over45_H = df_H[flt_Over45_H]
                count_Over45_H = df_Over45_H.Home.count() 
                por_count_Over45_H = round((round((count_Over45_H / len(df_H)),2)*100))
                por_count_Over45_H = str(por_count_Over45_H)+'%'
                
                flt_Over45_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 4)
                df_Over45_A = df_A[flt_Over45_A]
                count_Over45_A = df_Over45_A.Away.count() 
                por_count_Over45_A = round((round((count_Over45_A / len(df_A)),2)*100))
                por_count_Over45_A = str(por_count_Over45_A)+'%'
                
                flt_Over55_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 5)
                df_Over55_H = df_H[flt_Over55_H]
                count_Over55_H = df_Over55_H.Home.count() 
                por_count_Over55_H = round((round((count_Over55_H / len(df_H)),2)*100))
                por_count_Over55_H = str(por_count_Over55_H)+'%'
                
                flt_Over55_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 5)
                df_Over55_A = df_A[flt_Over55_A]
                count_Over55_A = df_Over55_A.Away.count() 
                por_count_Over55_A = round((round((count_Over55_A / len(df_A)),2)*100))
                por_count_Over55_A = str(por_count_Over55_A)+'%'
                
                flt_Over65_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 6)
                df_Over65_H = df_H[flt_Over65_H]
                count_Over65_H = df_Over65_H.Home.count() 
                por_count_Over65_H = round((round((count_Over65_H / len(df_H)),2)*100))
                por_count_Over65_H = str(por_count_Over65_H)+'%'
                
                flt_Over65_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 6)
                df_Over65_A = df_A[flt_Over65_A]
                count_Over65_A = df_Over65_A.Away.count() 
                por_count_Over65_A = round((round((count_Over65_A / len(df_A)),2)*100))
                por_count_Over65_A = str(por_count_Over65_A)+'%'
                
                flt_Over75_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 7)
                df_Over75_H = df_H[flt_Over75_H]
                count_Over75_H = df_Over75_H.Home.count() 
                por_count_Over75_H = round((round((count_Over75_H / len(df_H)),2)*100))
                por_count_Over75_H = str(por_count_Over75_H)+'%'
                
                flt_Over75_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 7)
                df_Over75_A = df_A[flt_Over75_A]
                count_Over75_A = df_Over75_A.Away.count() 
                por_count_Over75_A = round((round((count_Over75_A / len(df_A)),2)*100))
                por_count_Over75_A = str(por_count_Over75_A)+'%'
                
                flt_Over85_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 7)
                df_Over85_H = df_H[flt_Over85_H]
                count_Over85_H = df_Over85_H.Home.count() 
                por_count_Over85_H = round((round((count_Over85_H / len(df_H)),2)*100))
                por_count_Over85_H = str(por_count_Over85_H)+'%'
                
                flt_Over85_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 7)
                df_Over85_A = df_A[flt_Over85_A]
                count_Over85_A = df_Over85_A.Away.count() 
                por_count_Over85_A = round((round((count_Over85_A / len(df_A)),2)*100))
                por_count_Over85_A = str(por_count_Over85_A)+'%'
                
                
                row_names = ['Over 0.5','Over 1.5','Over 2.5','Over 3.5','Over 4.5','Over 5.5','Over 6.5','Over 7.5','Over 8.5']
                df1 = pd.DataFrame([por_count_Over05_H,por_count_Over15_H,por_count_Over25_H,por_count_Over35_H,por_count_Over45_H,por_count_Over55_H,por_count_Over65_H,por_count_Over75_H,por_count_Over85_H], index=row_names, columns=['Home'])
                
                row_names = ['Over 0.5','Over 1.5','Over 2.5','Over 3.5','Over 4.5','Over 5.5','Over 6.5','Over 7.5','Over 8.5']
                df2 = pd.DataFrame([por_count_Over05_A,por_count_Over15_A,por_count_Over25_A,por_count_Over35_A,por_count_Over45_A,por_count_Over55_A,por_count_Over65_A,por_count_Over75_A,por_count_Over85_A], index=row_names, columns=['Away'])
                
                
                df0 = pd.concat([df1,df2], axis=1)
                # st.write('Total de Gols')
                # st.write(df0)
                # st.markdown('---')

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.write('');st.write('');st.write('');st.write('')
                    st.write('Minutos dos Gols -',home)
                    st.write(tt1)

                with col2:
                    st.write('');st.write('');st.write('');st.write('')
                    st.write('Minutos dos Gols -',away)
                    st.write(tt2)

                with col3:
                    st.write('Total de Gols')
                    st.write(df0)

                
                st.markdown('---')



            except:
                st.markdown('---')



            ################################################################################
            # PDF do Theo
            ################################################################################
            
            df = base.copy()

            try:
                home = Fav_Home
                away = Zeb_Away

                df.loc[df['Goals_H'] > df['Goals_A'], 'Ptos_H'] = 3
                df.loc[df['Goals_H'] == df['Goals_A'], 'Ptos_H'] = 1
                df.loc[df['Goals_H'] < df['Goals_A'], 'Ptos_H'] = 0


                df.loc[df['Goals_H'] < df['Goals_A'], 'Ptos_A'] = 3
                df.loc[df['Goals_H'] == df['Goals_A'], 'Ptos_A'] = 1
                df.loc[df['Goals_H'] > df['Goals_A'], 'Ptos_A'] = 0
                
                df['Media_Ptos_H1'] = df.groupby('Home')['Ptos_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
                df['Media_Ptos_A1'] = df.groupby('Away')['Ptos_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
                
                df['Media_Ptos_H2'] = df.groupby('Home')['Ptos_H'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True)
                df['Media_Ptos_A2'] = df.groupby('Away')['Ptos_A'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True)
                
                df = drop_reset_index(df)
                
                flt = ((df.Season == "2022/2023") | (df.Season == '2023') | (df.Season == "2023/2024") | (df.Season == '2024'))
                df = df[flt]
 
                
                flt_H = df.Home == home
                df_H = df[flt_H]
                flt_A = df.Away == away
                df_A = df[flt_A]
            
                
                df1_H = len(df_H)
                df1_H = f'{df1_H:.0f}'
                df1_A = len(df_A)
                df1_A = f'{df1_A:.0f}'
                
                # Número de Vitórias
                flt2_H = df_H.Goals_H > df_H.Goals_A
                df2_H = df_H[flt2_H]
                df2_H = df2_H.Home.count()
                
                flt2_A = df_A.Goals_H < df_A.Goals_A
                df2_A = df_A[flt2_A]
                df2_A = df2_A.Away.count()
                
                # Porcentagem de Vitórias
                por_H = round((round((df2_H / len(df_H)),2)*100))
                df3_H = str(por_H)+'%'
                por_A = round((round((df2_A / len(df_A)),2)*100))
                df3_A = por_A
                df3_A = str(por_A)+'%'
                
                # Média de Pontos Temporada Atual    
                mean_H = df.groupby(['Home'])['Ptos_H'].get_group(home).mean()
                df4_H = round(mean_H,2)
                mean_A = df.groupby(['Away'])['Ptos_A'].get_group(away).mean()
                df4_A = round(mean_A,2)
                
                # Média de Pontos Ultimos 10 Jogos
                df_H_PPG = df_H[['Home','Media_Ptos_H1']].tail(1)
                df_A_PPG = df_A[['Away','Media_Ptos_A1']].tail(1)
                df5_H = df_H_PPG.iloc[0]['Media_Ptos_H1']
                df5_A = df_A_PPG.iloc[0]['Media_Ptos_A1']
                
                # Média de Pontos Ultimos 5 Jogos
                df_H_PPG = df_H[['Home','Media_Ptos_H2']].tail(1)
                df_A_PPG = df_A[['Away','Media_Ptos_A2']].tail(1)
                df6_H = df_H_PPG.iloc[0]['Media_Ptos_H2']
                df6_A = df_A_PPG.iloc[0]['Media_Ptos_A2']
                
                
                # Jogos sem sofrer gols
                flt_gol_0_H = df_H.Goals_A == 0
                df_gol_0_H = df_H[flt_gol_0_H]
                count_gol_0_H = df_gol_0_H.Home.count() 
                por_count_gol_0_H = round((round((count_gol_0_H / len(df_H)),2)*100))
                por_count_gol_0_H = str(por_count_gol_0_H)+'%'
                
                flt_gol_0_A = df_A.Goals_H == 0
                df_gol_0_A = df_A[flt_gol_0_A]
                count_gol_0_A = df_gol_0_A.Away.count() 
                por_count_gol_0_A = round((round((count_gol_0_A / len(df_A)),2)*100))
                por_count_gol_0_A = str(por_count_gol_0_A)+'%'
                
                # Falhou em marcar
                flt_gol_failed_H = df_H.Goals_H == 0
                df_gol_failed_H = df_H[flt_gol_failed_H]
                count_gol_failed_H = df_gol_failed_H.Home.count() 
                por_count_gol_failed_H = round((round((count_gol_failed_H / len(df_H)),2)*100))
                por_count_gol_failed_H = str(por_count_gol_failed_H)+'%'
                
                flt_gol_failed_A = df_A.Goals_A == 0
                df_gol_failed_A = df_A[flt_gol_failed_A]
                count_gol_failed_A = df_gol_failed_A.Away.count() 
                por_count_gol_failed_A = round((round((count_gol_failed_A / len(df_A)),2)*100))
                por_count_gol_failed_A = str(por_count_gol_failed_A)+'%'
                
                # Ambas marcam
                flt_BTTS_H = (df_H.Goals_H != 0) & (df_H.Goals_A != 0)
                df_BTTS_H = df_H[flt_BTTS_H]
                count_BTTS_H = df_BTTS_H.Home.count() 
                por_count_BTTS_H = round((round((count_BTTS_H / len(df_H)),2)*100))
                por_count_BTTS_H = str(por_count_BTTS_H)+'%'
                
                flt_BTTS_A = (df_A.Goals_H != 0) & (df_A.Goals_A != 0)
                df_BTTS_A = df_A[flt_BTTS_A]
                count_BTTS_A = df_BTTS_A.Home.count() 
                por_count_BTTS_A = round((round((count_BTTS_A / len(df_A)),2)*100))
                por_count_BTTS_A = str(por_count_BTTS_A)+'%' 
                
                
                # Média de Gols em Casa
                
                # Gols Marcados   
                Goals_MH = df.groupby(['Home'])['Goals_H'].get_group(home).sum()
                Goals_MH = int(Goals_MH)
                Goals_MA = df.groupby(['Away'])['Goals_A'].get_group(away).sum()
                Goals_MA = int(Goals_MA)
                
                # Gols Sofridos
                Goals_SH = df.groupby(['Home'])['Goals_A'].get_group(home).sum()
                Goals_SH = int(Goals_SH)
                Goals_SA = df.groupby(['Away'])['Goals_H'].get_group(away).sum()
                Goals_SA = int(Goals_SA)
                
                # Média de gols marcados    
                mean_Goals_MH = df.groupby(['Home'])['Goals_H'].get_group(home).mean()
                mean_Goals_MH = round(mean_Goals_MH,2)
                mean_Goals_MA = df.groupby(['Away'])['Goals_A'].get_group(away).mean()
                mean_Goals_MA = round(mean_Goals_MA,2)
                
                # Média de gols sofridos    
                mean_Goals_SH = df.groupby(['Home'])['Goals_A'].get_group(home).mean()
                mean_Goals_SH = round(mean_Goals_SH,2)
                mean_Goals_SA = df.groupby(['Away'])['Goals_H'].get_group(away).mean()
                mean_Goals_SA = round(mean_Goals_SA,2)
                
                # Média total de gols 
                mean_Goals_TH = mean_Goals_MH + mean_Goals_SH
                mean_Goals_TH = f'{mean_Goals_TH:.2f}'
                mean_Goals_TA = mean_Goals_MA + mean_Goals_SA
                mean_Goals_TA = f'{mean_Goals_TA:.2f}'
                
                
                
                
                row_names = []
                df1 = pd.DataFrame([], index=row_names, columns=['Home'])
                
                row_names = ['Gols marcados','Gols sofridos','Média de gols marcados','Média de gols sofridos','Média total de gols']
                df2 = pd.DataFrame([], index=row_names, columns=['Away'])
                
                
                
                
                row_names = ['Total de Jogos','Vitórias','Pontos por Jogo (Temporada)','Pontos por Jogo (Últimos 10 Jogos)','Pontos por Jogo (Últimos 5 Jogos)',
                            'Gols Marcados','Gols Sofridos','Média de Gols Marcados','Média de Gols Sofridos','Média Total de Gols']
                df1 = pd.DataFrame([df1_H,df2_H,df4_H,df5_H,df6_H,Goals_MH,Goals_SH,mean_Goals_MH,mean_Goals_SH,mean_Goals_TH], index=row_names, columns=['Home'])
                
                row_names = ['Total de Jogos','Vitórias','Pontos por Jogo (Temporada)','Pontos por Jogo (Últimos 10 Jogos)','Pontos por Jogo (Últimos 5 Jogos)',
                            'Gols Marcados','Gols Sofridos','Média de Gols Marcados','Média de Gols Sofridos','Média Total de Gols']
                df2 = pd.DataFrame([df1_A,df2_A,df4_A,df5_A,df6_A,Goals_MA,Goals_SA,mean_Goals_MA,mean_Goals_SA,mean_Goals_TA], index=row_names, columns=['Away'])
                
                row_names = ['% de Vitórias','% Jogos sem Sofrer Gols','% Jogos sem Marcar Gols','% Ambas Marcam']
                df3 = pd.DataFrame([df3_H,por_count_gol_0_H,por_count_gol_failed_H,por_count_BTTS_H], index=row_names, columns=['Home'])
                
                row_names = ['% de Vitórias','% Jogos sem Sofrer Gols','% Jogos sem Marcar Gols','% Ambas Marcam']
                df4 = pd.DataFrame([df3_A,por_count_gol_0_A,por_count_gol_failed_A,por_count_BTTS_A], index=row_names, columns=['Away'])
                





                df12 = pd.concat([df1,df2], axis=1)
                df34 = pd.concat([df3,df4], axis=1)
       
                st.text('Aproveitamento dos Times (Mandante Jogando em Casa e Visitante Jogando Fora)')
                st.text('Temporada Atual + Temporada Anterior')
                st.text('')
                texto = home + ' x ' + away
                st.write("<center>{}</center>".format(texto), unsafe_allow_html=True)
                st.write('')
                




                
                col1, col2 = st.columns(2)

                with col1:
                    st.dataframe(df12)

                with col2:
                    st.dataframe(df34)

                # st.markdown('---')  

                

            except:
                pass

            try:               
                
                # Total de Jogos 
                flt1 = df.Home == home
                df1 = df[flt1]
                flt2 = df.Away == away
                df2 = df[flt2]
                
                total_df1 = len(df1)
                total_df2 = len(df2)
                
                # Momento do Gol
                df_H = df_H.applymap(lambda x: x.replace("'","") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("[","") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("]","") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+1","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+2","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+3","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+4","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+5","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+6","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+7","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+8","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+9","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+10","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+11","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+12","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+13","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+14","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+15","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+16","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+17","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+18","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+19","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("45+20","45") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+1","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+2","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+3","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+4","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+5","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+6","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+7","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+8","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+9","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+10","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+11","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+12","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+13","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+14","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+15","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+16","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+17","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+18","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+19","90") if isinstance(x, str) else x)
                df_H = df_H.applymap(lambda x: x.replace("90+20","90") if isinstance(x, str) else x)
                
                df_A = df_A.applymap(lambda x: x.replace("'","") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("[","") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("]","") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+1","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+2","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+3","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+4","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+5","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+6","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+7","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+8","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+9","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+10","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+11","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+12","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+13","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+14","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+15","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+16","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+17","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+18","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+19","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("45+20","45") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+1","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+2","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+3","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+4","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+5","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+6","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+7","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+8","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+9","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+10","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+10","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+11","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+12","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+13","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+14","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+15","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+16","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+17","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+18","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+19","90") if isinstance(x, str) else x)
                df_A = df_A.applymap(lambda x: x.replace("90+20","90") if isinstance(x, str) else x)



                # Marca Primeiro
                df_H_PrimeiroGol = df_H[['Goals_H','Goals_A','Goals_Minutes_Home','Goals_Minutes_Away']]
                df_H_PrimeiroGol['TotalGoals'] = df_H_PrimeiroGol['Goals_H'] + df_H_PrimeiroGol['Goals_A'] 
                flt = df_H_PrimeiroGol.TotalGoals != 0
                df_H_PrimeiroGol = df_H_PrimeiroGol[flt]
            
                

                def deletar_conteudo_apos_virgula(valor):
                    return valor.split(',')[0]
                
                df_H_PrimeiroGol['Goals_Minutes_Home'] = df_H_PrimeiroGol['Goals_Minutes_Home'].apply(deletar_conteudo_apos_virgula)
                df_H_PrimeiroGol['Goals_Minutes_Away'] = df_H_PrimeiroGol['Goals_Minutes_Away'].apply(deletar_conteudo_apos_virgula)
                
                df_H_PrimeiroGol['Goals_Minutes_Home'] = pd.to_numeric(df_H_PrimeiroGol['Goals_Minutes_Home'], errors='coerce')
                df_H_PrimeiroGol['Goals_Minutes_Away'] = pd.to_numeric(df_H_PrimeiroGol['Goals_Minutes_Away'], errors='coerce')
                df_H_PrimeiroGol['Goals_Minutes_Home'] = df_H_PrimeiroGol['Goals_Minutes_Home'].fillna(1000)
                df_H_PrimeiroGol['Goals_Minutes_Away'] = df_H_PrimeiroGol['Goals_Minutes_Away'].fillna(1000)
                df_H_PrimeiroGol["Goals_Minutes_Home"] = df_H_PrimeiroGol["Goals_Minutes_Home"].astype('int')
                df_H_PrimeiroGol["Goals_Minutes_Away"] = df_H_PrimeiroGol["Goals_Minutes_Away"].astype('int')

                
                
                flt7 = df_H_PrimeiroGol['Goals_Minutes_Home'] < df_H_PrimeiroGol['Goals_Minutes_Away']
                marca_primeiro_H = df_H_PrimeiroGol[flt7]
                df7 = len(marca_primeiro_H) / len(df_H_PrimeiroGol)
                df7 = round((df7*100),)
                total_df7 = str(df7)+'%'
                
                
                df_A_PrimeiroGol = df_A[['Goals_H','Goals_A','Goals_Minutes_Home','Goals_Minutes_Away']]
                df_A_PrimeiroGol['TotalGoals'] = df_A_PrimeiroGol['Goals_H'] + df_A_PrimeiroGol['Goals_A'] 
                flt = df_A_PrimeiroGol.TotalGoals != 0
                df_A_PrimeiroGol = df_A_PrimeiroGol[flt]
                
                
                def deletar_conteudo_apos_virgula(valor):
                    return valor.split(',')[0]
                
                df_A_PrimeiroGol['Goals_Minutes_Home'] = df_A_PrimeiroGol['Goals_Minutes_Home'].apply(deletar_conteudo_apos_virgula)
                df_A_PrimeiroGol['Goals_Minutes_Away'] = df_A_PrimeiroGol['Goals_Minutes_Away'].apply(deletar_conteudo_apos_virgula)
                
                df_A_PrimeiroGol['Goals_Minutes_Home'] = pd.to_numeric(df_A_PrimeiroGol['Goals_Minutes_Home'], errors='coerce')
                df_A_PrimeiroGol['Goals_Minutes_Away'] = pd.to_numeric(df_A_PrimeiroGol['Goals_Minutes_Away'], errors='coerce')
                df_A_PrimeiroGol['Goals_Minutes_Home'] = df_A_PrimeiroGol['Goals_Minutes_Home'].fillna(1000)
                df_A_PrimeiroGol['Goals_Minutes_Away'] = df_A_PrimeiroGol['Goals_Minutes_Away'].fillna(1000)
                df_A_PrimeiroGol["Goals_Minutes_Home"] = df_A_PrimeiroGol["Goals_Minutes_Home"].astype('int')
                df_A_PrimeiroGol["Goals_Minutes_Away"] = df_A_PrimeiroGol["Goals_Minutes_Away"].astype('int')
                
                flt8 = df_A_PrimeiroGol['Goals_Minutes_Away'] < df_A_PrimeiroGol['Goals_Minutes_Home']
                marca_primeiro_A = df_A_PrimeiroGol[flt8]
                df8 = len(marca_primeiro_A) / len(df_A_PrimeiroGol)
                df8 = round((df8*100),)
                total_df8 = str(df8)+'%'
                
                
                flt9 = marca_primeiro_H.Goals_H > marca_primeiro_H.Goals_A
                marcou_e_ganhou = marca_primeiro_H[flt9]
                df9 = len(marcou_e_ganhou) / len(marca_primeiro_H)
                df9 = round((df9*100),)
                total_df9 = str(df9)+'%'
                
                flt10 = marca_primeiro_A.Goals_A > marca_primeiro_A.Goals_H
                marcou_e_ganhou = marca_primeiro_A[flt10]
                df10 = len(marcou_e_ganhou) / len(marca_primeiro_A)
                df10 = round((df10*100),)
                total_df10 = str(df10)+'%'
                
                flt11 = marca_primeiro_H.Goals_H == marca_primeiro_H.Goals_A
                marcou_e_empatou = marca_primeiro_H[flt11]
                df11 = len(marcou_e_empatou) / len(marca_primeiro_H)
                df11 = round((df11*100),)
                total_df11 = str(df11)+'%'
                
                flt12 = marca_primeiro_A.Goals_A == marca_primeiro_A.Goals_H
                marcou_e_empatou = marca_primeiro_A[flt12]
                df12 = len(marcou_e_empatou) / len(marca_primeiro_A)
                df12 = round((df12*100),)
                total_df12 = str(df12)+'%'
                
                flt13 = marca_primeiro_H.Goals_H < marca_primeiro_H.Goals_A
                marcou_e_perdeu = marca_primeiro_H[flt13]
                df13 = len(marcou_e_perdeu) / len(marca_primeiro_H)
                df13 = round((df13*100),)
                total_df13 = str(df13)+'%'
                
                flt14 = marca_primeiro_A.Goals_A < marca_primeiro_A.Goals_H
                marcou_e_perdeu = marca_primeiro_A[flt14]
                df14 = len(marcou_e_perdeu) / len(marca_primeiro_A)
                df14 = round((df14*100),)
                total_df14 = str(df14)+'%'
                
                flt15 = df_H_PrimeiroGol['Goals_Minutes_Home'] > df_H_PrimeiroGol['Goals_Minutes_Away']
                leva_primeiro_H = df_H_PrimeiroGol[flt15]
                df15 = len(leva_primeiro_H) / len(df_H_PrimeiroGol)
                df15 = round((df15*100),)
                total_df15 = str(df15)+'%'
                
                
                
                flt16 = df_A_PrimeiroGol['Goals_Minutes_Away'] > df_A_PrimeiroGol['Goals_Minutes_Home']
                leva_primeiro_A = df_A_PrimeiroGol[flt16]
                df16 = len(leva_primeiro_A) / len(df_A_PrimeiroGol)
                df16 = round((df16*100),)
                total_df16 = str(df16)+'%'
                
                flt17 = leva_primeiro_H['Goals_H'] > leva_primeiro_H['Goals_A']
                levou_e_ganhou = leva_primeiro_H[flt17]
                df17 = len(levou_e_ganhou) / len(leva_primeiro_H)
                df17 = round((df17*100),)
                total_df17 = str(df17)+'%'
            
                
                flt18 = leva_primeiro_A['Goals_A'] > leva_primeiro_A['Goals_H']
                levou_e_ganhou = leva_primeiro_A[flt18]
                df18 = len(levou_e_ganhou) / len(leva_primeiro_A)
                df18 = round((df18*100),)
                total_df18 = str(df18)+'%'
                
                
                
                flt19 = leva_primeiro_H.Goals_H == leva_primeiro_H.Goals_A
                levou_e_empatou = leva_primeiro_H[flt19]
                df19 = len(levou_e_empatou) / len(leva_primeiro_H)
                df19 = round((df19*100),)
                total_df19 = str(df19)+'%'
                
                
                flt20 = leva_primeiro_A.Goals_H == leva_primeiro_A.Goals_A
                levou_e_empatou = leva_primeiro_A[flt20]
                df20 = len(levou_e_empatou) / len(leva_primeiro_A)
                df20 = round((df20*100),)
                total_df20 = str(df20)+'%'
                
                
                flt21 = leva_primeiro_H.Goals_H < leva_primeiro_H.Goals_A
                levou_e_perdeu = leva_primeiro_H[flt21]
                df21 = len(levou_e_perdeu) / len(leva_primeiro_H)
                df21 = round((df21*100),)
                total_df21 = str(df21)+'%'
                
                
                flt22 = leva_primeiro_A.Goals_A < leva_primeiro_A.Goals_H
                levou_e_perdeu = leva_primeiro_A[flt22]
                df22 = len(levou_e_perdeu) / len(leva_primeiro_A)
                df22 = round((df22*100),)
                total_df22 = str(df22)+'%'
                
                # Marcou o Primeiro Gol no 1º Tempo
                flt_1T_01 = ((df_H_PrimeiroGol.Goals_Minutes_Home < 46) 
                    & (df_H_PrimeiroGol.Goals_Minutes_Home < df_H_PrimeiroGol.Goals_Minutes_Away))
                        
                df_1T_01 = df_H_PrimeiroGol[flt_1T_01]
                num_1T_01 = len(df_1T_01) / len(df_H_PrimeiroGol)
                df_1T_01 = round((num_1T_01*100),)
                df_1T_01 = str(df_1T_01)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Ganhou
                flt_1T_02 = ((df_H_PrimeiroGol.Goals_Minutes_Home < 46) 
                    & (df_H_PrimeiroGol.Goals_Minutes_Home < df_H_PrimeiroGol.Goals_Minutes_Away)
                    & (df_H_PrimeiroGol.Goals_H > df_H_PrimeiroGol.Goals_A))
                        
                df_1T_02 = df_H_PrimeiroGol[flt_1T_02]
                num_1T_02 = len(df_1T_02) / len(df_H_PrimeiroGol)
                df_1T_02 = round((num_1T_02*100),)
                df_1T_02 = str(df_1T_02)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Empatou
                flt_1T_03 = ((df_H_PrimeiroGol.Goals_Minutes_Home < 46) 
                    & (df_H_PrimeiroGol.Goals_Minutes_Home < df_H_PrimeiroGol.Goals_Minutes_Away)
                    & (df_H_PrimeiroGol.Goals_H == df_H_PrimeiroGol.Goals_A))
                        
                df_1T_03 = df_H_PrimeiroGol[flt_1T_03]
                num_1T_03 = len(df_1T_03) / len(df_H_PrimeiroGol)
                df_1T_03 = round((num_1T_03*100),)
                df_1T_03 = str(df_1T_03)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Perdeu
                flt_1T_04 = ((df_H_PrimeiroGol.Goals_Minutes_Home < 46) 
                    & (df_H_PrimeiroGol.Goals_Minutes_Home < df_H_PrimeiroGol.Goals_Minutes_Away)
                    & (df_H_PrimeiroGol.Goals_H < df_H_PrimeiroGol.Goals_A))
                        
                df_1T_04 = df_H_PrimeiroGol[flt_1T_04]
                num_1T_04 = len(df_1T_04) / len(df_H_PrimeiroGol)
                df_1T_04 = round((num_1T_04*100),)
                df_1T_04 = str(df_1T_04)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo
                flt_1T_05 = ((df_A_PrimeiroGol.Goals_Minutes_Away < 46) 
                    & (df_A_PrimeiroGol.Goals_Minutes_Away < df_A_PrimeiroGol.Goals_Minutes_Home))
                        
                df_1T_05 = df_A_PrimeiroGol[flt_1T_05]
                num_1T_05 = len(df_1T_05) / len(df_A_PrimeiroGol)
                df_1T_05 = round((num_1T_05*100),)
                df_1T_05 = str(df_1T_05)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Ganhou
                flt_1T_06 = ((df_A_PrimeiroGol.Goals_Minutes_Away < 46) 
                            & (df_A_PrimeiroGol.Goals_Minutes_Away < df_A_PrimeiroGol.Goals_Minutes_Home)
                            & (df_A_PrimeiroGol.Goals_A > df_A_PrimeiroGol.Goals_H))
                        
                df_1T_06 = df_A_PrimeiroGol[flt_1T_06]
                num_1T_06 = len(df_1T_06) / len(df_A_PrimeiroGol)
                df_1T_06 = round((num_1T_06*100),)
                df_1T_06 = str(df_1T_06)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Empatou
                flt_1T_07 = ((df_A_PrimeiroGol.Goals_Minutes_Away < 46) 
                            & (df_A_PrimeiroGol.Goals_Minutes_Away < df_A_PrimeiroGol.Goals_Minutes_Home)
                            & (df_A_PrimeiroGol.Goals_A == df_A_PrimeiroGol.Goals_H))
                        
                df_1T_07 = df_A_PrimeiroGol[flt_1T_07]
                num_1T_07 = len(df_1T_07) / len(df_A_PrimeiroGol)
                df_1T_07 = round((num_1T_07*100),)
                df_1T_07 = str(df_1T_07)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Perdeu
                flt_1T_08 = ((df_A_PrimeiroGol.Goals_Minutes_Away < 46) 
                            & (df_A_PrimeiroGol.Goals_Minutes_Away < df_A_PrimeiroGol.Goals_Minutes_Home)
                            & (df_A_PrimeiroGol.Goals_A < df_A_PrimeiroGol.Goals_H))
                        
                df_1T_08 = df_A_PrimeiroGol[flt_1T_08]
                num_1T_08 = len(df_1T_08) / len(df_A_PrimeiroGol)
                df_1T_08 = round((num_1T_08*100),)
                df_1T_08 = str(df_1T_08)+'%'
                
                
                
                
                row_names = ['% Jogos que Marcou 1º Gol','% Jogos que Marcou 1º Gol e Venceu','% Jogos que Marcou 1º Gol e Empatou','% Jogos que Marcou 1º Gol e Perdeu',
                            '% Jogos que Sofreu 1º Gol','% Jogos que Sofreu 1º Gol e Venceu','% Jogos que Sofreu 1º Gol e Empatou','% Jogos que Sofreu 1º Gol e Perdeu',
                            '% Jogos que Marcou o Primeiro Gol no 1º Tempo','% Jogos que Marcou o Primeiro Gol no 1º Tempo e Venceu','% Jogos que Marcou o Primeiro Gol no 1º Tempo e Empatou','% Jogos que Marcou o Primeiro Gol no 1º Tempo e Perdeu']
                df1 = pd.DataFrame([total_df7,total_df9,total_df11,total_df13,total_df15,total_df17,total_df19,total_df21,df_1T_01,df_1T_02,df_1T_03,df_1T_04], index=row_names, columns=['Home'])
                
                row_names = ['% Jogos que Marcou 1º Gol','% Jogos que Marcou 1º Gol e Venceu','% Jogos que Marcou 1º Gol e Empatou','% Jogos que Marcou 1º Gol e Perdeu',
                            '% Jogos que Sofreu 1º Gol','% Jogos que Sofreu 1º Gol e Venceu','% Jogos que Sofreu 1º Gol e Empatou','% Jogos que Sofreu 1º Gol e Perdeu',
                            '% Jogos que Marcou o Primeiro Gol no 1º Tempo','% Jogos que Marcou o Primeiro Gol no 1º Tempo e Venceu','% Jogos que Marcou o Primeiro Gol no 1º Tempo e Empatou','% Jogos que Marcou o Primeiro Gol no 1º Tempo e Perdeu']
                df2 = pd.DataFrame([total_df8,total_df10,total_df12,total_df14,total_df16,total_df18,total_df20,total_df22,df_1T_05,df_1T_06,df_1T_07,df_1T_08], index=row_names, columns=['Away'])
                
                
                df0 = pd.concat([df1,df2], axis=1)
                st.text('Análise do 1º Gol - Mandante Jogando em Casa e Visitante Jogando Fora')
                st.write(df0)
                # st.markdown('---')
                
            except:
                pass

            try:    
                    
                # Time Mandante - Gols Marcados
                
                min_gols_H = df_H[['Goals_H','Goals_Minutes_Home']]
                flt = min_gols_H.Goals_H != 0
                min_gols_H = min_gols_H[flt]
                min_gols_H = min_gols_H[['Goals_Minutes_Home']]
                
                # Time Mandante - Gols Sofridos
                
                min_gols_HS = df_H[['Goals_A','Goals_Minutes_Away']]
                flt = min_gols_HS.Goals_A != 0
                min_gols_HS = min_gols_HS[flt]
                min_gols_HS = min_gols_HS[['Goals_Minutes_Away']]
                
                # Time Visitante - Gols Marcados
                
                min_gols_A = df_A[['Goals_A','Goals_Minutes_Away']]
                flt = min_gols_A.Goals_A != 0
                min_gols_A = min_gols_A[flt]
                min_gols_A = min_gols_A[['Goals_Minutes_Away']]
                
                # Time Visitante - Gols Sofridos
                
                min_gols_AS = df_A[['Goals_H','Goals_Minutes_Home']]
                flt = min_gols_AS.Goals_H != 0
                min_gols_AS = min_gols_AS[flt]
                min_gols_AS = min_gols_AS[['Goals_Minutes_Home']]
                
                
                # Gols Marcados - Mandante
                Momentos_GM_H = list(min_gols_H['Goals_Minutes_Home'])
                string_concatenada_GM_H = ', '.join(Momentos_GM_H)
                lista_numeros_GM_H = list(map(int, string_concatenada_GM_H.split(", ")))
                lista_numeros_GM_H.sort()
                
                contador_0_15 = 0
                
                for numero in lista_numeros_GM_H:
                    if numero >= 0 and numero <= 15:
                        contador_0_15 += 1
                GM_H_0_15 = contador_0_15
                GM_H_0_15 = round(((GM_H_0_15 / len(lista_numeros_GM_H)) * 100), 2)
                GM_H_0_15 = str(GM_H_0_15)+'%'
                
                contador_16_30 = 0
                
                for numero in lista_numeros_GM_H:
                    if numero >= 16 and numero <= 30:
                        contador_16_30 += 1
                GM_H_16_30 = contador_16_30
                GM_H_16_30 = round(((GM_H_16_30 / len(lista_numeros_GM_H)) * 100), 2)
                GM_H_16_30 = str(GM_H_16_30)+'%'
                
                contador_31_45 = 0
                
                for numero in lista_numeros_GM_H:
                    if numero >= 31 and numero <= 45:
                        contador_31_45 += 1
                GM_H_31_45 = contador_31_45
                GM_H_31_45 = round(((GM_H_31_45 / len(lista_numeros_GM_H)) * 100), 2)
                GM_H_31_45 = str(GM_H_31_45)+'%'
                
                contador_46_60 = 0
                
                for numero in lista_numeros_GM_H:
                    if numero >= 46 and numero <= 60:
                        contador_46_60 += 1
                GM_H_46_60 = contador_46_60
                GM_H_46_60 = round(((GM_H_46_60 / len(lista_numeros_GM_H)) * 100), 2)
                GM_H_46_60 = str(GM_H_46_60)+'%'
                
                contador_61_75 = 0
                
                for numero in lista_numeros_GM_H:
                    if numero >= 61 and numero <= 75:
                        contador_61_75 += 1
                GM_H_61_75 = contador_61_75
                GM_H_61_75 = round(((GM_H_61_75 / len(lista_numeros_GM_H)) * 100), 2)
                GM_H_61_75 = str(GM_H_61_75)+'%'
                
                contador_76_90 = 0
                
                for numero in lista_numeros_GM_H:
                    if numero >= 76 and numero <= 90:
                        contador_76_90 += 1
                GM_H_76_90 = contador_76_90
                GM_H_76_90 = round(((GM_H_76_90 / len(lista_numeros_GM_H)) * 100), 2)
                GM_H_76_90 = str(GM_H_76_90)+'%'
                
                
                # Gols Sofridos - Mandante
                Momentos_GS_H = list(min_gols_HS['Goals_Minutes_Away'])
                try:
                    string_concatenada_GS_H = ', '.join(Momentos_GS_H)
                    lista_numeros_GS_H = list(map(int, string_concatenada_GS_H.split(", ")))
                    lista_numeros_GS_H.sort()
                except:
                    lista_numeros_GS_H = [-1]
                
                
                contador_0_15 = 0
                
                for numero in lista_numeros_GS_H:
                    if numero >= 0 and numero <= 15:
                        contador_0_15 += 1
                GS_H_0_15 = contador_0_15
                GS_H_0_15 = round(((GS_H_0_15 / len(lista_numeros_GS_H)) * 100), 2)
                GS_H_0_15 = str(GS_H_0_15)+'%'
                
                contador_16_30 = 0
                
                for numero in lista_numeros_GS_H:
                    if numero >= 16 and numero <= 30:
                        contador_16_30 += 1
                GS_H_16_30 = contador_16_30
                GS_H_16_30 = round(((GS_H_16_30 / len(lista_numeros_GS_H)) * 100), 2)
                GS_H_16_30 = str(GS_H_16_30)+'%'
                
                contador_31_45 = 0
                
                for numero in lista_numeros_GS_H:
                    if numero >= 31 and numero <= 45:
                        contador_31_45 += 1
                GS_H_31_45 = contador_31_45
                GS_H_31_45 = round(((GS_H_31_45 / len(lista_numeros_GS_H)) * 100), 2)
                GS_H_31_45 = str(GS_H_31_45)+'%'
                
                contador_46_60 = 0
                
                for numero in lista_numeros_GS_H:
                    if numero >= 46 and numero <= 60:
                        contador_46_60 += 1
                GS_H_46_60 = contador_46_60
                GS_H_46_60 = round(((GS_H_46_60 / len(lista_numeros_GS_H)) * 100), 2)
                GS_H_46_60 = str(GS_H_46_60)+'%'
                
                contador_61_75 = 0
                
                for numero in lista_numeros_GS_H:
                    if numero >= 61 and numero <= 75:
                        contador_61_75 += 1
                GS_H_61_75 = contador_61_75
                GS_H_61_75 = round(((GS_H_61_75 / len(lista_numeros_GS_H)) * 100), 2)
                GS_H_61_75 = str(GS_H_61_75)+'%'
                
                contador_76_90 = 0
                
                for numero in lista_numeros_GS_H:
                    if numero >= 76 and numero <= 90:
                        contador_76_90 += 1
                GS_H_76_90 = contador_76_90
                GS_H_76_90 = round(((GS_H_76_90 / len(lista_numeros_GS_H)) * 100), 2)
                GS_H_76_90 = str(GS_H_76_90)+'%'
                
                
                
                
                
                # Gols Marcados - Visitante
                Momentos_GM_A = list(min_gols_A['Goals_Minutes_Away'])
                string_concatenada_GM_A = ', '.join(Momentos_GM_A)
                lista_numeros_GM_A = list(map(int, string_concatenada_GM_A.split(", ")))
                lista_numeros_GM_A.sort()
                
                contador_0_15 = 0
                
                for numero in lista_numeros_GM_A:
                    if numero >= 0 and numero <= 15:
                        contador_0_15 += 1
                GM_A_0_15 = contador_0_15
                GM_A_0_15 = round(((GM_A_0_15 / len(lista_numeros_GS_H)) * 100), 2)
                GM_A_0_15 = str(GM_A_0_15)+'%'
                
                contador_16_30 = 0
                
                for numero in lista_numeros_GM_A:
                    if numero >= 16 and numero <= 30:
                        contador_16_30 += 1
                GM_A_16_30 = contador_16_30
                GM_A_16_30 = round(((GM_A_16_30 / len(lista_numeros_GS_H)) * 100), 2)
                GM_A_16_30 = str(GM_A_16_30)+'%'
                
                contador_31_45 = 0
                
                for numero in lista_numeros_GM_A:
                    if numero >= 31 and numero <= 45:
                        contador_31_45 += 1
                GM_A_31_45 = contador_31_45
                GM_A_31_45 = round(((GM_A_31_45 / len(lista_numeros_GS_H)) * 100), 2)
                GM_A_31_45 = str(GM_A_31_45)+'%'
                
                contador_46_60 = 0
                
                for numero in lista_numeros_GM_A:
                    if numero >= 46 and numero <= 60:
                        contador_46_60 += 1
                GM_A_46_60 = contador_46_60
                GM_A_46_60 = round(((GM_A_46_60 / len(lista_numeros_GS_H)) * 100), 2)
                GM_A_46_60 = str(GM_A_46_60)+'%'
                
                contador_61_75 = 0
                
                for numero in lista_numeros_GM_A:
                    if numero >= 61 and numero <= 75:
                        contador_61_75 += 1
                GM_A_61_75 = contador_61_75
                GM_A_61_75 = round(((GM_A_61_75 / len(lista_numeros_GS_H)) * 100), 2)
                GM_A_61_75 = str(GM_A_61_75)+'%'
                
                contador_76_90 = 0
                
                for numero in lista_numeros_GM_A:
                    if numero >= 76 and numero <= 90:
                        contador_76_90 += 1
                GM_A_76_90 = contador_76_90
                GM_A_76_90 = round(((GM_A_76_90 / len(lista_numeros_GS_H)) * 100), 2)
                GM_A_76_90 = str(GM_A_76_90)+'%'
                
                
                # Gols Sofridos - Visitante
                Momentos_GS_A = list(min_gols_AS['Goals_Minutes_Home'])
                string_concatenada_GS_A = ', '.join(Momentos_GS_A)
                lista_numeros_GS_A = list(map(int, string_concatenada_GS_A.split(", ")))
                lista_numeros_GS_A.sort()
                
                contador_0_15 = 0
                
                for numero in lista_numeros_GS_A:
                    if numero >= 0 and numero <= 15:
                        contador_0_15 += 1
                GS_A_0_15 = contador_0_15
                GS_A_0_15 = round(((GS_A_0_15 / len(lista_numeros_GS_H)) * 100), 2)
                GS_A_0_15 = str(GS_A_0_15)+'%'
                
                contador_16_30 = 0
                
                for numero in lista_numeros_GS_A:
                    if numero >= 16 and numero <= 30:
                        contador_16_30 += 1
                GS_A_16_30 = contador_16_30
                GS_A_16_30 = round(((GS_A_16_30 / len(lista_numeros_GS_H)) * 100), 2)
                GS_A_16_30 = str(GS_A_16_30)+'%'
                
                contador_31_45 = 0
                
                for numero in lista_numeros_GS_A:
                    if numero >= 31 and numero <= 45:
                        contador_31_45 += 1
                GS_A_31_45 = contador_31_45
                GS_A_31_45 = round(((GS_A_31_45 / len(lista_numeros_GS_H)) * 100), 2)
                GS_A_31_45 = str(GS_A_31_45)+'%'
                
                contador_46_60 = 0
                
                for numero in lista_numeros_GS_A:
                    if numero >= 46 and numero <= 60:
                        contador_46_60 += 1
                GS_A_46_60 = contador_46_60
                GS_A_46_60 = round(((GS_A_46_60 / len(lista_numeros_GS_H)) * 100), 2)
                GS_A_46_60 = str(GS_A_46_60)+'%'
                
                contador_61_75 = 0
                
                for numero in lista_numeros_GS_A:
                    if numero >= 61 and numero <= 75:
                        contador_61_75 += 1
                GS_A_61_75 = contador_61_75
                GS_A_61_75 = round(((GS_A_61_75 / len(lista_numeros_GS_H)) * 100), 2)
                GS_A_61_75 = str(GS_A_61_75)+'%'
                
                contador_76_90 = 0
                
                for numero in lista_numeros_GS_A:
                    if numero >= 76 and numero <= 90:
                        contador_76_90 += 1
                GS_A_76_90 = contador_76_90
                GS_A_76_90 = round(((GS_A_76_90 / len(lista_numeros_GS_H)) * 100), 2)
                GS_A_76_90 = str(GS_A_76_90)+'%'
                
                
                
                
                
                row_names = ['00 - 15','16 - 30','31 - 45','46 - 60','61 - 75','76 - 90']
                df1 = pd.DataFrame([GM_H_0_15, GM_H_16_30, GM_H_31_45, GM_H_46_60, GM_H_61_75, GM_H_76_90], index=row_names, columns=['Marcados'])
                
                row_names = ['00 - 15','16 - 30','31 - 45','46 - 60','61 - 75','76 - 90']
                df2 = pd.DataFrame([GS_H_0_15, GS_H_16_30, GS_H_31_45, GS_H_46_60, GS_H_61_75, GS_H_76_90], index=row_names, columns=['Sofridos'])
                
                row_names = ['00 - 15','16 - 30','31 - 45','46 - 60','61 - 75','76 - 90']
                df3 = pd.DataFrame([GM_A_0_15, GM_A_16_30, GM_A_31_45, GM_A_46_60, GM_A_61_75, GM_A_76_90], index=row_names, columns=['Marcados'])
                
                row_names = ['00 - 15','16 - 30','31 - 45','46 - 60','61 - 75','76 - 90']
                df4 = pd.DataFrame([GS_A_0_15, GS_A_16_30, GS_A_31_45, GS_A_46_60, GS_A_61_75, GS_A_76_90], index=row_names, columns=['Sofridos'])
                
                
                # Colocar com cores (acrescentar as quantidades)
                df1 = pd.concat([df1,df2], axis=1)
                print('Minutos dos Gols -',home)

                
                df2 = pd.concat([df3,df4], axis=1)
                print('Minutos dos Gols -',away)

                # col1, col2 = st.columns(2)

                # with col1:
                #     st.write('Minutos dos Gols -',home)
                #     st.write(df1)

                # with col2:
                #     st.write('Minutos dos Gols -',away)
                #     st.write(df2)

                # st.markdown('---')  
                tt1 = df1.copy()
                tt2 = df2.copy()      

            

                flt_Over05_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 0)
                df_Over05_H = df_H[flt_Over05_H]
                count_Over05_H = df_Over05_H.Home.count() 
                por_count_Over05_H = round((round((count_Over05_H / len(df_H)),2)*100))
                por_count_Over05_H = str(por_count_Over05_H)+'%'
                
                flt_Over05_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 0)
                df_Over05_A = df_A[flt_Over05_A]
                count_Over05_A = df_Over05_A.Away.count() 
                por_count_Over05_A = round((round((count_Over05_A / len(df_A)),2)*100))
                por_count_Over05_A = str(por_count_Over05_A)+'%'
                
                flt_Over15_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 1)
                df_Over15_H = df_H[flt_Over15_H]
                count_Over15_H = df_Over15_H.Home.count() 
                por_count_Over15_H = round((round((count_Over15_H / len(df_H)),2)*100))
                por_count_Over15_H = str(por_count_Over15_H)+'%'
                
                flt_Over15_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 1)
                df_Over15_A = df_A[flt_Over15_A]
                count_Over15_A = df_Over15_A.Away.count() 
                por_count_Over15_A = round((round((count_Over15_A / len(df_A)),2)*100))
                por_count_Over15_A = str(por_count_Over15_A)+'%'
                
                flt_Over25_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 2)
                df_Over25_H = df_H[flt_Over25_H]
                count_Over25_H = df_Over25_H.Home.count() 
                por_count_Over25_H = round((round((count_Over25_H / len(df_H)),2)*100))
                por_count_Over25_H = str(por_count_Over25_H)+'%'
                
                flt_Over25_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 2)
                df_Over25_A = df_A[flt_Over25_A]
                count_Over25_A = df_Over25_A.Away.count() 
                por_count_Over25_A = round((round((count_Over25_A / len(df_A)),2)*100))
                por_count_Over25_A = str(por_count_Over25_A)+'%'
                
                flt_Over35_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 3)
                df_Over35_H = df_H[flt_Over35_H]
                count_Over35_H = df_Over35_H.Home.count() 
                por_count_Over35_H = round((round((count_Over35_H / len(df_H)),2)*100))
                por_count_Over35_H = str(por_count_Over35_H)+'%'
                
                flt_Over35_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 3)
                df_Over35_A = df_A[flt_Over35_A]
                count_Over35_A = df_Over35_A.Away.count() 
                por_count_Over35_A = round((round((count_Over35_A / len(df_A)),2)*100))
                por_count_Over35_A = str(por_count_Over35_A)+'%'
                
                flt_Over45_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 4)
                df_Over45_H = df_H[flt_Over45_H]
                count_Over45_H = df_Over45_H.Home.count() 
                por_count_Over45_H = round((round((count_Over45_H / len(df_H)),2)*100))
                por_count_Over45_H = str(por_count_Over45_H)+'%'
                
                flt_Over45_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 4)
                df_Over45_A = df_A[flt_Over45_A]
                count_Over45_A = df_Over45_A.Away.count() 
                por_count_Over45_A = round((round((count_Over45_A / len(df_A)),2)*100))
                por_count_Over45_A = str(por_count_Over45_A)+'%'
                
                flt_Over55_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 5)
                df_Over55_H = df_H[flt_Over55_H]
                count_Over55_H = df_Over55_H.Home.count() 
                por_count_Over55_H = round((round((count_Over55_H / len(df_H)),2)*100))
                por_count_Over55_H = str(por_count_Over55_H)+'%'
                
                flt_Over55_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 5)
                df_Over55_A = df_A[flt_Over55_A]
                count_Over55_A = df_Over55_A.Away.count() 
                por_count_Over55_A = round((round((count_Over55_A / len(df_A)),2)*100))
                por_count_Over55_A = str(por_count_Over55_A)+'%'
                
                flt_Over65_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 6)
                df_Over65_H = df_H[flt_Over65_H]
                count_Over65_H = df_Over65_H.Home.count() 
                por_count_Over65_H = round((round((count_Over65_H / len(df_H)),2)*100))
                por_count_Over65_H = str(por_count_Over65_H)+'%'
                
                flt_Over65_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 6)
                df_Over65_A = df_A[flt_Over65_A]
                count_Over65_A = df_Over65_A.Away.count() 
                por_count_Over65_A = round((round((count_Over65_A / len(df_A)),2)*100))
                por_count_Over65_A = str(por_count_Over65_A)+'%'
                
                flt_Over75_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 7)
                df_Over75_H = df_H[flt_Over75_H]
                count_Over75_H = df_Over75_H.Home.count() 
                por_count_Over75_H = round((round((count_Over75_H / len(df_H)),2)*100))
                por_count_Over75_H = str(por_count_Over75_H)+'%'
                
                flt_Over75_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 7)
                df_Over75_A = df_A[flt_Over75_A]
                count_Over75_A = df_Over75_A.Away.count() 
                por_count_Over75_A = round((round((count_Over75_A / len(df_A)),2)*100))
                por_count_Over75_A = str(por_count_Over75_A)+'%'
                
                flt_Over85_H = ((df_H['Goals_H'] + df_H['Goals_A']) > 7)
                df_Over85_H = df_H[flt_Over85_H]
                count_Over85_H = df_Over85_H.Home.count() 
                por_count_Over85_H = round((round((count_Over85_H / len(df_H)),2)*100))
                por_count_Over85_H = str(por_count_Over85_H)+'%'
                
                flt_Over85_A = ((df_A['Goals_H'] + df_A['Goals_A']) > 7)
                df_Over85_A = df_A[flt_Over85_A]
                count_Over85_A = df_Over85_A.Away.count() 
                por_count_Over85_A = round((round((count_Over85_A / len(df_A)),2)*100))
                por_count_Over85_A = str(por_count_Over85_A)+'%'
                
                
                row_names = ['Over 0.5','Over 1.5','Over 2.5','Over 3.5','Over 4.5','Over 5.5','Over 6.5','Over 7.5','Over 8.5']
                df1 = pd.DataFrame([por_count_Over05_H,por_count_Over15_H,por_count_Over25_H,por_count_Over35_H,por_count_Over45_H,por_count_Over55_H,por_count_Over65_H,por_count_Over75_H,por_count_Over85_H], index=row_names, columns=['Home'])
                
                row_names = ['Over 0.5','Over 1.5','Over 2.5','Over 3.5','Over 4.5','Over 5.5','Over 6.5','Over 7.5','Over 8.5']
                df2 = pd.DataFrame([por_count_Over05_A,por_count_Over15_A,por_count_Over25_A,por_count_Over35_A,por_count_Over45_A,por_count_Over55_A,por_count_Over65_A,por_count_Over75_A,por_count_Over85_A], index=row_names, columns=['Away'])
                
                
                df0 = pd.concat([df1,df2], axis=1)
                # st.write('Total de Gols')
                # st.write(df0)

                
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.write('');st.write('');st.write('');st.write('')
                    st.write('Minutos dos Gols -',home)
                    st.write(tt1)

                with col2:
                    st.write('');st.write('');st.write('');st.write('')
                    st.write('Minutos dos Gols -',away)
                    st.write(tt2)

                with col3:
                    st.write('Total de Gols')
                    st.write(df0)
                    
                st.markdown('---')
            except:
                st.markdown('---')





        
        else:
            st.write("Nenhum jogo atende aos filtros selecionados!")
    except:
        st.write("Jogos desse dia ainda não disponíveis.")
        st.write("Por Favor. Aguarde!")
