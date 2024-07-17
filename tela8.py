from futpythontrader import *
from leagues import *
from rename import *

def show_tela8():
    
    st.title("Luke v2.1")
    st.header("Backtesting")
    
    # dia = st.date_input("Data de Análise", date.today())

    @st.cache_data
    def load_data_base():

        base_luke = pd.read_csv('https://github.com/futpythontrader/YouTube/raw/main/Bases_de_Dados/FlashScore/Base_de_Dados_FlashScore_Backtesting_Luke.csv')
        return base_luke

    df = load_data_base()
    df = df[df['League'].isin(leagues) == True]
    df = drop_reset_index(df)

    # Filtro por Temporada (mesmo código da função anterior)
    sorted_seasons = sorted(df['Season'].unique())
    sorted_seasons.insert(0, "Todas as Temporadas")
    selected_seasons = st.multiselect('Filtrar por Temporada:', sorted_seasons, default="Todas as Temporadas")
    
    # Filtro de Liga
    sorted_leagues = sorted(df['League'].unique())
    sorted_leagues.insert(0, "Todas as Ligas")
    selected_leagues = st.multiselect('Filtrar por Liga:', sorted_leagues, default="ARGENTINA - COPA DE LA LIGA PROFESIONAL")

    # Filtro de Time Mandante
    sorted_teams = sorted(df['Home'].unique())
    sorted_teams.insert(0, "Todos os Times")
    selected_teams = st.multiselect('Filtrar por Times:', sorted_teams, default="Todos os Times")

    filtered_df = df.copy()
    if "Todas as Temporadas" not in selected_seasons:
        filtered_df = filtered_df[filtered_df['Season'].isin(selected_seasons)]

    if "Todas as Ligas" not in selected_leagues:
        filtered_df = filtered_df[filtered_df['League'].isin(selected_leagues)]

    if "Todos os Times" not in selected_teams:
        filtered_df = filtered_df[filtered_df['Home'].isin(selected_teams)]

    df0 = filtered_df.copy()
    
    # ligas = df.sort_values(['League'])
    # ligas = ligas['League'].unique()

    # c1, c2 = st.columns(2)
    # ligas_selecionadas = c1.multiselect('Ligas', ligas)
    # df_ligas = df[df['League'].isin(ligas_selecionadas)]
    # temporadas = df_ligas['Season'].unique()
    # temporadas_selecionadas = c2.multiselect('Temporadas', temporadas)
    # df0 = df_ligas[df_ligas['Season'].isin(temporadas_selecionadas)]

    estrategias = ['Back Home', 'Back Draw', 'Back Away',
                    'Lay Home', 'Lay Draw', 'Lay Away',
                    'Over05 HT','Under05 HT',
                    'Over05 FT','Under05 FT', 'Over15 FT','Under15 FT', 'Over25 FT','Under25 FT', 
                    'Over35 FT','Under35 FT', 'Over45 FT','Under45 FT',  
                    'BTTS Sim', 'BTTS Não',
                    'Lay 0 x 0', 'Lay 0 x 1', 'Lay 0 x 2', 'Lay 0 x 3',
                    'Lay 1 x 0', 'Lay 1 x 1', 'Lay 1 x 2', 'Lay 1 x 3',
                    'Lay 2 x 0', 'Lay 2 x 1', 'Lay 2 x 2', 'Lay 2 x 3',
                    'Lay 3 x 0', 'Lay 3 x 1', 'Lay 3 x 2', 'Lay 3 x 3',
                    'Lay Goleada Home', 'Lay Goleada Away']

    backtestes = st.selectbox('Escolha a Metodologia', estrategias)

    if backtestes == 'Back Home':
        df0.loc[(df0['FT_Goals_H'] >  df0['FT_Goals_A']), 'Profit'] = df0['FT_Odd_H'] - 1
        df0.loc[(df0['FT_Goals_H'] <= df0['FT_Goals_A']), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)

        col1, col2, col3, col4 = st.columns(4)

        # with col1:
        #     Odd_0x0_Min = st.number_input('Odd_0x0_Min', value=1.01, step=0.1)
        #     Odd_0x0_Max = st.number_input('Odd_0x0_Max', value=10.0, step=0.1)
        # with col2:
        #     Odd_0x1_Min = st.number_input('Odd_0x1_Min', value=1.01, step=0.1)
        #     Odd_0x1_Max = st.number_input('Odd_0x1_Max', value=10.0, step=0.1)
        # with col3:
        #     Odd_0x2_Min = st.number_input('Odd_0x2_Min', value=1.01, step=0.1)
        #     Odd_0x2_Max = st.number_input('Odd_0x2_Max', value=10.0, step=0.1)
        # with col4:
        #     Odd_0x3_Min = st.number_input('Odd_0x3_Min', value=1.01, step=0.1)
        #     Odd_0x3_Max = st.number_input('Odd_0x3_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]
        
        # df_filtrado['Lucro Acumulado'] = df_filtrado.groupby('Home')["Profit"].cumsum()
        # df_ranking = df_filtrado.groupby('Home')['Lucro Acumulado'].max().reset_index()
        # df_ranking1 = df_ranking.sort_values('Lucro Acumulado', ascending=False)
        # df_ranking1.columns = ['Time','Profit_Acu']
        # df_ranking2 = df_ranking.sort_values('Lucro Acumulado', ascending=True)
        # df_ranking2.columns = ['Time','Profit_Acu']

        
        
    
    if backtestes == 'Back Draw':
        df0.loc[(df0['FT_Goals_H'] == df0['FT_Goals_A']), 'Profit'] = df0['FT_Odd_D'] - 1
        df0.loc[(df0['FT_Goals_H'] != df0['FT_Goals_A']), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]

        
        
    if backtestes == 'Back Away':
        df0.loc[(df0['FT_Goals_H'] <  df0['FT_Goals_A']), 'Profit'] = df0['FT_Odd_A'] - 1
        df0.loc[(df0['FT_Goals_H'] >= df0['FT_Goals_A']), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]




    if backtestes == 'Lay Home':
        df0.loc[(df0['FT_Goals_H'] <=  df0['FT_Goals_A']), 'Profit'] = 1 / (df0['FT_Odd_H'] - 0.85)
        df0.loc[(df0['FT_Goals_H'] > df0['FT_Goals_A']), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]
        
    if backtestes == 'Lay Draw':
        df0.loc[(df0['FT_Goals_H'] != df0['FT_Goals_A']), 'Profit'] = 1 / (df0['FT_Odd_D'] - 0.85)
        df0.loc[(df0['FT_Goals_H'] == df0['FT_Goals_A']), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]

    if backtestes == 'Lay Away':
        df0.loc[(df0['FT_Goals_H'] >= df0['FT_Goals_A']), 'Profit'] = 1 / (df0['FT_Odd_A'] - 0.85)
        df0.loc[(df0['FT_Goals_H'] < df0['FT_Goals_A']), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]
        
    if backtestes == 'Over05 HT':
        df0.loc[(df0['HT_Goals_H'] + df0['HT_Goals_A']) > 0, 'Profit'] = df0['HT_Odd_Over05'] - 1
        df0.loc[(df0['HT_Goals_H'] + df0['HT_Goals_A']) == 0, 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]



    if backtestes == 'Under05 HT':
        df0.loc[(df0['HT_Goals_H'] + df0['HT_Goals_A']) == 0, 'Profit'] = df0['HT_Odd_Under05'] - 1
        df0.loc[(df0['HT_Goals_H'] + df0['HT_Goals_A']) > 0, 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]





    if backtestes == 'Over05 FT':
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) > 0, 'Profit'] = df0['FT_Odd_Over05'] - 1
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) == 0, 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]



    if backtestes == 'Under05 FT':
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) == 0, 'Profit'] = df0['FT_Odd_Under05'] - 1
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) > 0, 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]



    if backtestes == 'Over15 FT':
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) > 1, 'Profit'] = df0['FT_Odd_Over15'] - 1
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) < 2, 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]



    if backtestes == 'Under15 FT':
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) < 2, 'Profit'] = df0['FT_Odd_Under15'] - 1
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) > 1, 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]


    if backtestes == 'Over25 FT':
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) > 2, 'Profit'] = df0['FT_Odd_Over25'] - 1
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) < 3, 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]



    if backtestes == 'Under25 FT':
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) < 3, 'Profit'] = df0['FT_Odd_Under25'] - 1
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) > 2, 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]


    if backtestes == 'Over35 FT':
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) > 3, 'Profit'] = df0['FT_Odd_Over35'] - 1
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) < 4, 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]



    if backtestes == 'Under35 FT':
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) < 4, 'Profit'] = df0['FT_Odd_Under35'] - 1
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) > 3, 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]


    if backtestes == 'Over45 FT':
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) > 4, 'Profit'] = df0['FT_Odd_Over45'] - 1
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) < 5, 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]



    if backtestes == 'Under45 FT':
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) < 5, 'Profit'] = df0['FT_Odd_Under45'] - 1
        df0.loc[(df0['FT_Goals_H'] + df0['FT_Goals_A']) > 4, 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]

        
        
    if backtestes == 'BTTS Sim':

        df0['BTTS'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] > 0 and row['FT_Goals_A'] > 0) else 0, axis=1)
        
        df0.loc[(df0['BTTS'] == 1), 'Profit'] = df0['Odd_BTTS_Yes'] - 1
        df0.loc[(df0['BTTS'] == 0), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]
        



    if backtestes == 'BTTS Não':

        df0['BTTS'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] > 0 and row['FT_Goals_A'] > 0) else 0, axis=1)
        
        df0.loc[(df0['BTTS'] == 0), 'Profit'] = df0['Odd_BTTS_No'] - 1
        df0.loc[(df0['BTTS'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]

    if backtestes == 'Lay Goleada Home':

        df0['Goleada_H'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] >= 4 and row['FT_Goals_H'] > row['FT_Goals_A']) else 0, axis=1)
        
        df0.loc[(df0['Goleada_H'] == 0), 'Profit'] = 0.05
        df0.loc[(df0['Goleada_H'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]
        
    
    if backtestes == 'Lay Goleada Away':

        df0['Goleada_A'] = df0.apply(lambda row: 1 if (row['FT_Goals_A'] >= 4 and row['FT_Goals_A'] > row['FT_Goals_H']) else 0, axis=1)
        
        df0.loc[(df0['Goleada_A'] == 0), 'Profit'] = 0.025
        df0.loc[(df0['Goleada_A'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]
    
    
    if backtestes == 'Lay 0 x 0':

        df0['0x0'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 0 and row['FT_Goals_A'] == 0) else 0, axis=1)
        
        df0.loc[(df0['0x0'] == 0), 'Profit'] = 1 / (df0['CS_0x0'] + 3)
        df0.loc[(df0['0x0'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]



    if backtestes == 'Lay 0 x 1':

        df0['0x1'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 0 and row['FT_Goals_A'] == 1) else 0, axis=1)
        
        df0.loc[(df0['0x1'] == 0), 'Profit'] = 1 / (df0['CS_0x1'] + 4)
        df0.loc[(df0['0x1'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]

    
    if backtestes == 'Lay 0 x 2':

        df0['0x2'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 0 and row['FT_Goals_A'] == 2) else 0, axis=1)
        
        df0.loc[(df0['0x2'] == 0), 'Profit'] = 1 / (df0['CS_0x2'] + 5)
        df0.loc[(df0['0x2'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]      
    
    
    if backtestes == 'Lay 0 x 3':

        df0['0x3'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 0 and row['FT_Goals_A'] == 3) else 0, axis=1)
        
        df0.loc[(df0['0x3'] == 0), 'Profit'] = 1 / (df0['CS_0x3'] + 6)
        df0.loc[(df0['0x3'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]          


    if backtestes == 'Lay 1 x 0':

        df0['1x0'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 1 and row['FT_Goals_A'] == 0) else 0, axis=1)
        
        df0.loc[(df0['1x0'] == 0), 'Profit'] = 1 / (df0['CS_1x0'] + 4)
        df0.loc[(df0['1x0'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]

    
    if backtestes == 'Lay 2 x 0':

        df0['2x0'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 2 and row['FT_Goals_A'] == 0) else 0, axis=1)
        
        df0.loc[(df0['2x0'] == 0), 'Profit'] = 1 / (df0['CS_2x0'] + 5)
        df0.loc[(df0['2x0'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]       
    
    
    if backtestes == 'Lay 3 x 0':

        df0['3x0'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 3 and row['FT_Goals_A'] == 0) else 0, axis=1)
        
        df0.loc[(df0['3x0'] == 0), 'Profit'] = 1 / (df0['CS_3x0'] + 6)
        df0.loc[(df0['3x0'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]

    if backtestes == 'Lay 1 x 2':

        df0['1x2'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 1 and row['FT_Goals_A'] == 2) else 0, axis=1)
        
        df0.loc[(df0['1x2'] == 0), 'Profit'] = 1 / (df0['CS_1x2'] + 6)
        df0.loc[(df0['1x2'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]        
    
    
    if backtestes == 'Lay 2 x 1':

        df0['2x1'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 2 and row['FT_Goals_A'] == 1) else 0, axis=1)
        
        df0.loc[(df0['2x1'] == 0), 'Profit'] = 1 / (df0['CS_2x1'] + 6)
        df0.loc[(df0['2x1'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]




    if backtestes == 'Lay 1 x 1':

        df0['1x1'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 1 and row['FT_Goals_A'] == 1) else 0, axis=1)
        
        df0.loc[(df0['1x1'] == 0), 'Profit'] = 1 / (df0['CS_1x1'] + 5)
        df0.loc[(df0['1x1'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]







    if backtestes == 'Lay 1 x 3':

        df0['1x3'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 1 and row['FT_Goals_A'] == 3) else 0, axis=1)
        
        df0.loc[(df0['1x3'] == 0), 'Profit'] = 1 / (df0['CS_1x3'] + 7)
        df0.loc[(df0['1x3'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]




    if backtestes == 'Lay 2 x 2':

        df0['2x2'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 2 and row['FT_Goals_A'] == 2) else 0, axis=1)
        
        df0.loc[(df0['2x2'] == 0), 'Profit'] = 1 / (df0['CS_2x2'] + 7)
        df0.loc[(df0['2x2'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]



    if backtestes == 'Lay 2 x 3':

        df0['2x3'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 2 and row['FT_Goals_A'] == 3) else 0, axis=1)
        
        df0.loc[(df0['2x3'] == 0), 'Profit'] = 1 / (df0['CS_2x3'] + 8)
        df0.loc[(df0['2x3'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]


    if backtestes == 'Lay 3 x 1':

        df0['3x1'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 3 and row['FT_Goals_A'] == 1) else 0, axis=1)
        
        df0.loc[(df0['3x1'] == 0), 'Profit'] = 1 / (df0['CS_3x1'] + 7)
        df0.loc[(df0['3x1'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]





    if backtestes == 'Lay 3 x 2':

        df0['3x2'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 3 and row['FT_Goals_A'] == 2) else 0, axis=1)
        
        df0.loc[(df0['3x2'] == 0), 'Profit'] = 1 / (df0['CS_3x2'] + 8)
        df0.loc[(df0['3x2'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]


    if backtestes == 'Lay 3 x 3':

        df0['3x3'] = df0.apply(lambda row: 1 if (row['FT_Goals_H'] == 3 and row['FT_Goals_A'] == 3) else 0, axis=1)
        
        df0.loc[(df0['3x3'] == 0), 'Profit'] = 1 / (df0['CS_3x3'] + 9)
        df0.loc[(df0['3x3'] == 1), 'Profit'] = -1

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
            Odd_H_Max = st.number_input('Odd_H_Max', value=10.0, step=0.1)
        with col2:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
            Odd_D_Max = st.number_input('Odd_D_Max', value=10.0, step=0.1)
        with col3:
            # values_MO_H = st.slider(
            # 'Range de Odds do Favorito ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_A_Min = st.number_input('Odd_A_Min', value=1.01, step=0.1)
            Odd_A_Max = st.number_input('Odd_A_Max', value=10.0, step=0.1)
        with col4:
            # values_Over25_H = st.slider(
            # 'Range de Odds do Over 2.5 ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.01, step=0.1)
            Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=10.0, step=0.1)
        with col5:
            # values_BTTS_H = st.slider(
            # 'Range de Odds do BTTS ',
            # 1.01, 5.0, (1.50, 2.20))
            Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.01, step=0.1)
            Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=10.0, step=0.1)
        
        # Filtre o dataframe pelos valores mínimos e máximos de cada coluna
        df_filtrado = df0[(df0['FT_Odd_H'] >= Odd_H_Min) & (df0['FT_Odd_H'] <= Odd_H_Max) &
                        (df0['FT_Odd_D'] >= Odd_D_Min) & (df0['FT_Odd_D'] <= Odd_D_Max) &
                        (df0['FT_Odd_A'] >= Odd_A_Min) & (df0['FT_Odd_A'] <= Odd_A_Max) &
                        (df0['FT_Odd_Over25'] >= Odd_Over25_Min) & (df0['FT_Odd_Over25'] <= Odd_Over25_Max) &
                        (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]





    
    
    # RESULTADOS
    
    try:
        # Crie uma nova coluna no dataframe filtrado com o profit acumulado
        df_filtrado['Profit_acu'] = df_filtrado.Profit.cumsum()
        df_filtrado = df_filtrado.dropna()
        df_filtrado = df_filtrado.reset_index(drop=True)
        df_filtrado.index += 1
        profit = round(df_filtrado.Profit_acu.tail(1).item(),2)
        ROI = round((df_filtrado.Profit_acu.tail(1)/len(df_filtrado)*100).item(),2)
        # df_filtrado.Profit_acu.plot(title=backtestes, xlabel='Entradas', ylabel='Stakes')






        

        import plotly.graph_objects as go

        # Criando o gráfico
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_filtrado.index, y=df_filtrado['Profit_acu'], mode='lines'))

        # Configurando o layout do gráfico
        fig.update_layout(
            title="Profit Acumulado",
            xaxis_title="Entradas",
            yaxis_title="Stakes"
        )

        # Plotando o gráfico no Streamlit
        st.plotly_chart(fig)
        








        # Plote o gráfico com o profit acumulado do dataframe filtrado
        # st.set_option('deprecation.showPyplotGlobalUse', False)
        # plt.plot(df_filtrado['Profit_acu'])
        # st.pyplot()
        st.write("Profit:",str(profit),"stakes em", str(len(df_filtrado)),"jogos")
        st.write("ROI:",str(ROI),"%")    
        st.write('')
        df_filtrado['Profit Acumulado'] = df_filtrado.groupby('Home')['Profit'].cumsum()
        team_profit = df_filtrado.groupby('Home')['Profit Acumulado'].last().sort_values(ascending=False)
        top_teams = team_profit.head(3)  # Top 3 teams
        bottom_teams = team_profit.tail(3)  # Bottom 3 teams

        st.write("Melhores Times")
        st.table(top_teams)

        st.write("Piores Times")
        st.table(bottom_teams)

        # try:
        #     col1, col2 = st.columns(2)

        #     with col1:
        #         st.write("Times Mais Lucrativos")
        #         st.write(str(df_ranking1['Time'].iloc[0]),':', str(round(df_ranking1['Profit_Acu'].iloc[0],2)),'Stakes')
        #         st.write(str(df_ranking1['Time'].iloc[1]),':', str(round(df_ranking1['Profit_Acu'].iloc[1],2)),'Stakes')
        #         st.write(str(df_ranking1['Time'].iloc[2]),':', str(round(df_ranking1['Profit_Acu'].iloc[2],2)),'Stakes') 
        #     with col2:
        #         st.write("Times Menos Lucrativos")
        #         st.write(str(df_ranking2['Time'].iloc[0]),':', str(round(df_ranking2['Profit_Acu'].iloc[0],2)),'Stakes')
        #         st.write(str(df_ranking2['Time'].iloc[1]),':', str(round(df_ranking2['Profit_Acu'].iloc[1],2)),'Stakes')
        #         st.write(str(df_ranking2['Time'].iloc[2]),':', str(round(df_ranking2['Profit_Acu'].iloc[2],2)),'Stakes')
        # except:
        #     pass

        # Define a função que retorna a planilha em formato XLSX
        def download_excel():
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            df_filtrado.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.close()
            processed_data = output.getvalue()
            return processed_data

        # Cria o botão de download
        button = st.download_button(
            label='Download Backtesting',
            data=download_excel(),
            file_name=f'Luke_Backtesting_{backtestes}.xlsx',
            mime='application/vnd.ms-excel'
        )
    except:
        pass

    # Modifique a função para retornar os filtros como uma string
    def gerar_string_filtro(ranges_de_odds):
        conteudo_arquivo = ""
        for chave, valor in ranges_de_odds.items():
            linha = f"{chave}: {valor}\n"
            conteudo_arquivo += linha
        return conteudo_arquivo
    
    ranges_de_odds = {
        'Odd_H_Min': Odd_H_Min,
        'Odd_H_Max': Odd_H_Max,
        'Odd_D_Min': Odd_D_Min,
        'Odd_D_Max': Odd_D_Max,
        'Odd_A_Min': Odd_A_Min,
        'Odd_A_Max': Odd_A_Max,
        'Odd_Over25_Min': Odd_Over25_Min,
        'Odd_Over25_Max': Odd_Over25_Max,
        'Odd_BTTS_Min': Odd_BTTS_Min,
        'Odd_BTTS_Max': Odd_BTTS_Max,
        'selected_leagues': selected_leagues
        # Adicione todos os outros filtros aqui
    }

    # Gerar a string dos filtros
    conteudo_filtro = gerar_string_filtro(ranges_de_odds)

    # Botão para download dos filtros
    st.download_button(
        label="Download Filtros",
        data=conteudo_filtro,
        file_name="filtros.txt",
        mime="text/plain"
    )

    st.text('')
    st.text('')
    st.text('')

    st.subheader("Entradas")

    dia = st.date_input("", date.today())

    @st.cache_data
    def load_data_betfair(dia):
        betfair_url = f'https://github.com/futpythontrader/YouTube/raw/main/Jogos_do_Dia/Betfair/Jogos_do_Dia_Betfair_Back_Lay_{dia}.csv'
        betfair = pd.read_csv(betfair_url)
        return betfair

    # try:
        
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

    Jogos_do_Dia = betfair.copy()
    df0 = Jogos_do_Dia[['League','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]

    df_filtrado = df0[(df0['Odd_H'] >= Odd_H_Min) & (df0['Odd_H'] <= Odd_H_Max) &
                      (df0['Odd_D'] >= Odd_D_Min) & (df0['Odd_D'] <= Odd_D_Max) &
                      (df0['Odd_A'] >= Odd_A_Min) & (df0['Odd_A'] <= Odd_A_Max) &
                      (df0['Odd_Over25'] >= Odd_Over25_Min) & (df0['Odd_Over25'] <= Odd_Over25_Max) &
                      (df0['Odd_BTTS_Yes'] >= Odd_BTTS_Min) & (df0['Odd_BTTS_Yes'] <= Odd_BTTS_Max)]
    df_filtrado = df_filtrado[df_filtrado['League'].isin(selected_leagues) == True]

    df_filtrado = drop_reset_index(df_filtrado)

    if len(df_filtrado) != 0:
        st.dataframe(df_filtrado)
    else:
        st.write("Sem Entradas!")

    


