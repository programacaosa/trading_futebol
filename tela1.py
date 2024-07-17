from futpythontrader import *
from leagues import *
from rename import *
import ast

def show_tela1():
    st.title("Luke v2.1")
    st.header("Oportunidades do Dia")

    dia = st.date_input("Data de Análise", date.today())

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
    Jogos_do_Dia = Jogos_do_Dia[['League','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]

    st.dataframe(Jogos_do_Dia)

    def download_excel():
                output = BytesIO()
                writer = pd.ExcelWriter(output, engine='xlsxwriter')
                betfair.to_excel(writer, index=False, sheet_name='Sheet1')
                writer.close()
                processed_data = output.getvalue()
                return processed_data

    # Cria o botão de download
    button = st.download_button(
        label='Download',
        data=download_excel(),
        file_name=f'Luke_Jogos_do_Dia_{dia}.xlsx',
        mime='application/vnd.ms-excel')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Filtros da Get Up Trading
    st.subheader("Filtros Get Up Trading")

    def convert_string_to_list(string):
        if pd.isnull(string) or string == "[]":
            return []
        else:
            return ast.literal_eval(string)

    def who_scored_first(home_goals, away_goals):
        first_overall = (None, None)
        first_before_45 = (None, None)

        if home_goals or away_goals:
            if not home_goals:
                first_overall = (0, 1)
            elif not away_goals or (home_goals and min(home_goals) < min(away_goals)):
                first_overall = (1, 0)
            else:
                first_overall = (0, 1)

        home_goals_before_45 = [goal for goal in home_goals if goal < 45]
        away_goals_before_45 = [goal for goal in away_goals if goal < 45]

        if home_goals_before_45 or away_goals_before_45:
            if not home_goals_before_45:
                first_before_45 = (0, 1)
            elif not away_goals_before_45 or (home_goals_before_45 and min(home_goals_before_45) < min(away_goals_before_45)):
                first_before_45 = (1, 0)
            else:
                first_before_45 = (0, 1)

        return (*first_overall, *first_before_45)

    @st.cache_data
    def load_data_base():

        base = pd.read_csv('https://github.com/futpythontrader/YouTube/raw/main/Bases_de_Dados/FlashScore/Base_de_Dados_FlashScore_v2.csv')
        
        return base

    base_orig = load_data_base()
    base_orig["Date"] = pd.to_datetime(base_orig["Date"])
    base_orig = base_orig.sort_values('Date')
    flt = base_orig.Date < str(dia)
    base = base_orig[flt]

    flt = (base.Season == '2024') | (base.Season == '2023/2024')
    df = base[flt]
    df = drop_reset_index(df)
    df = df[['Date','League','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Goals_Minutes_Home','Goals_Minutes_Away']]
    
    df['Goals_Minutes_Home'] = df['Goals_Minutes_Home'].apply(convert_string_to_list)
    df['Goals_Minutes_Away'] = df['Goals_Minutes_Away'].apply(convert_string_to_list)

    df[['First_H', 'First_A', 'First_45_H', 'First_45_A']] = df.apply(
        lambda row: who_scored_first(row['Goals_Minutes_Home'], row['Goals_Minutes_Away']), axis=1, result_type='expand'
    )
    df[['First_H', 'First_A', 'First_45_H', 'First_45_A']] = df[['First_H', 'First_A', 'First_45_H', 'First_45_A']].fillna(0)

    n_per = 5

    df['p_H'] = 1 / df.Odd_H
    df['p_D'] = 1 / df.Odd_D
    df['p_A'] = 1 / df.Odd_A

    df['Total_Goals_HT'] = df.apply(lambda row: (row['Goals_H_HT'] + row['Goals_A_HT']), axis=1)
    df['Total_Goals_FT'] = df.apply(lambda row: (row['Goals_H'] + row['Goals_A']), axis=1)

    df['Over05_HT'] = df.apply(lambda row: 1 if (row['Total_Goals_HT'] > 0) else 0, axis=1)
    df['Over05_FT'] = df.apply(lambda row: 1 if (row['Total_Goals_FT'] > 0) else 0, axis=1)

    df['M_GM_H'] = df.groupby('Home')['Goals_H'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)
    df['M_GM_A'] = df.groupby('Away')['Goals_A'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)

    df['M_GolsMar_H'] = (df.groupby('Home')['Goals_H'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True) * 100)
    df['M_GolsSof_A'] = (df.groupby('Away')['Goals_H'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True) * 100)

    df['Porc_Over05HT_Home'] = (df.groupby('Home')['Over05_HT'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True) * 100)
    df['Porc_Over05HT_Away'] = (df.groupby('Away')['Over05_HT'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True) * 100)
    df['Porc_Over05FT_Home'] = (df.groupby('Home')['Over05_FT'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True) * 100)
    df['Porc_Over05FT_Away'] = (df.groupby('Away')['Over05_FT'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True) * 100)

    df['Porc_GM_45_Home'] = (df.groupby('Home')['First_45_H'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True) * 100)
    df['Porc_GM_45_Away'] = (df.groupby('Away')['First_45_A'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True) * 100)
    df['Porc_GS_45_Home'] = (df.groupby('Home')['First_45_A'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True) * 100)
    df['Porc_GS_45_Away'] = (df.groupby('Away')['First_45_H'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True) * 100)

    df['Mean_GM_HT_Home'] = (df.groupby('Home')['Goals_H_HT'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True))
    df['Mean_GS_HT_Home'] = (df.groupby('Home')['Goals_A_HT'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True))
    df['Mean_GM_HT_Away'] = (df.groupby('Away')['Goals_A_HT'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True))
    df['Mean_GS_HT_Away'] = (df.groupby('Away')['Goals_H_HT'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True))

    df['CG1_H'] = df.Goals_H / df.p_H
    df['CG1_A'] = df.Goals_A / df.p_A
    df['M_CG1_H'] = df.groupby('Home')['CG1_H'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)
    df['M_CG1_A'] = df.groupby('Away')['CG1_A'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)
    df['DP_CG1_H'] = df.groupby('Home')['CG1_H'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)
    df['DP_CG1_A'] = df.groupby('Away')['CG1_A'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)
    df['CV_CG1_H'] = df['DP_CG1_H'] / df['M_CG1_H']
    df['CV_CG1_A'] = df['DP_CG1_A'] / df['M_CG1_A']

    df['CG2_H'] = (df.p_H / 2) + (df.Goals_H / 2)
    df['CG2_A'] = (df.p_A / 2) + (df.Goals_A / 2)
    df['M_CG2_H'] = df.groupby('Home')['CG2_H'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)
    df['M_CG2_A'] = df.groupby('Away')['CG2_A'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)
    df['DP_CG2_H'] = df.groupby('Home')['CG2_H'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)
    df['DP_CG2_A'] = df.groupby('Away')['CG2_A'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)
    df['CV_CG2_H'] = df['DP_CG2_H'] / df['M_CG2_H']
    df['CV_CG2_A'] = df['DP_CG2_A'] / df['M_CG2_A']

    # Lay 0 x 0 HT
    Jogos_do_Dia = betfair.copy()
    Jogos_do_Dia = Jogos_do_Dia[['Date','League','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]

    base_H = df[['Home','M_GM_H','M_GolsMar_H',
                'Porc_Over05HT_Home','Porc_Over05FT_Home',
                'Porc_GM_45_Home','Porc_GS_45_Home',
                'Mean_GM_HT_Home','Mean_GS_HT_Home',
                'M_CG1_H','CV_CG1_H','M_CG2_H','CV_CG2_H']]
    base_A = df[['Away','M_GM_A','M_GolsSof_A',
                'Porc_Over05HT_Away','Porc_Over05FT_Away',
                'Porc_GM_45_Away','Porc_GS_45_Away',
                'Mean_GM_HT_Away','Mean_GS_HT_Away',
                'M_CG1_A','CV_CG1_A','M_CG2_A','CV_CG2_A']]

    ultima_base_H = base_H.groupby('Home').last().reset_index()
    ultima_base_A = base_A.groupby('Away').last().reset_index()

    Jogos = pd.merge(Jogos_do_Dia, ultima_base_H, how='left', left_on='Home', right_on='Home')
    Jogos = pd.merge(Jogos, ultima_base_A, how='left', left_on='Away', right_on='Away')

    Jogos = drop_reset_index(Jogos)
    flt = (Jogos.Porc_Over05HT_Home >= 75) & (Jogos.Porc_Over05HT_Away >= 75) & (Jogos.M_CG2_H >= 1) & (Jogos.M_CG2_A >= 1) & (Jogos.CV_CG2_H <= 0.5)
    Jogos = Jogos[flt]
    Lay_0x0_HT = drop_reset_index(Jogos)

    # Lay 0 x 1
    Jogos_do_Dia = betfair.copy()
    Jogos_do_Dia = Jogos_do_Dia[['Date','League','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]

    base_H = df[['Home','M_GM_H','M_GolsMar_H',
                'Porc_Over05HT_Home','Porc_Over05FT_Home',
                'Porc_GM_45_Home','Porc_GS_45_Home',
                'Mean_GM_HT_Home','Mean_GS_HT_Home',
                'M_CG1_H','CV_CG1_H','M_CG2_H','CV_CG2_H']]
    base_A = df[['Away','M_GM_A','M_GolsSof_A',
                'Porc_Over05HT_Away','Porc_Over05FT_Away',
                'Porc_GM_45_Away','Porc_GS_45_Away',
                'Mean_GM_HT_Away','Mean_GS_HT_Away',
                'M_CG1_A','CV_CG1_A','M_CG2_A','CV_CG2_A']]

    ultima_base_H = base_H.groupby('Home').last().reset_index()
    ultima_base_A = base_A.groupby('Away').last().reset_index()

    Jogos = pd.merge(Jogos_do_Dia, ultima_base_H, how='left', left_on='Home', right_on='Home')
    Jogos = pd.merge(Jogos, ultima_base_A, how='left', left_on='Away', right_on='Away')

    Jogos = drop_reset_index(Jogos)
    flt = ((Jogos.M_GolsMar_H >= 85) & (Jogos.M_GolsSof_A >= 75) &
        (Jogos.M_CG1_H >= 3) & (Jogos.M_CG2_A >= 0.8) & (Jogos.CV_CG2_H <= 0.8) &
        (Jogos.Odd_H >= 1.25) & (Jogos.Odd_H <= 2.20) &
        (Jogos.Odd_A >= Jogos.Odd_D))
    Jogos = Jogos[flt]
    Lay_0x1 = drop_reset_index(Jogos)

    # Lay 0 x 2
    Jogos_do_Dia = betfair.copy()
    Jogos_do_Dia = Jogos_do_Dia[['Date','League','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]

    base_H = df[['Home','M_GM_H','M_GolsMar_H',
                'Porc_Over05HT_Home','Porc_Over05FT_Home',
                'Porc_GM_45_Home','Porc_GS_45_Home',
                'Mean_GM_HT_Home','Mean_GS_HT_Home',
                'M_CG1_H','CV_CG1_H','M_CG2_H','CV_CG2_H']]
    base_A = df[['Away','M_GM_A','M_GolsSof_A',
                'Porc_Over05HT_Away','Porc_Over05FT_Away',
                'Porc_GM_45_Away','Porc_GS_45_Away',
                'Mean_GM_HT_Away','Mean_GS_HT_Away',
                'M_CG1_A','CV_CG1_A','M_CG2_A','CV_CG2_A']]

    ultima_base_H = base_H.groupby('Home').last().reset_index()
    ultima_base_A = base_A.groupby('Away').last().reset_index()

    Jogos = pd.merge(Jogos_do_Dia, ultima_base_H, how='left', left_on='Home', right_on='Home')
    Jogos = pd.merge(Jogos, ultima_base_A, how='left', left_on='Away', right_on='Away')

    Jogos = drop_reset_index(Jogos)
    flt = ((Jogos.Mean_GM_HT_Home >= 1) & (Jogos.Mean_GS_HT_Away >= 1) &
        # (Jogos.Porc_GM_45_Home >= 50) & (Jogos.Porc_GS_45_Away >= 45) &
        (Jogos.M_GM_H >= 2) & (Jogos.Odd_H < Jogos.Odd_A))
    Jogos = Jogos[flt]
    Lay_0x2 = drop_reset_index(Jogos)

    # Lay Goleada Away
    Jogos_do_Dia = betfair.copy()
    Jogos_do_Dia = Jogos_do_Dia[['Date','League','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]

    base_H = df[['Home','M_GM_H','M_GolsMar_H',
                'Porc_Over05HT_Home','Porc_Over05FT_Home',
                'Porc_GM_45_Home','Porc_GS_45_Home',
                'Mean_GM_HT_Home','Mean_GS_HT_Home',
                'M_CG1_H','CV_CG1_H','M_CG2_H','CV_CG2_H']]
    base_A = df[['Away','M_GM_A','M_GolsSof_A',
                'Porc_Over05HT_Away','Porc_Over05FT_Away',
                'Porc_GM_45_Away','Porc_GS_45_Away',
                'Mean_GM_HT_Away','Mean_GS_HT_Away',
                'M_CG1_A','CV_CG1_A','M_CG2_A','CV_CG2_A']]

    ultima_base_H = base_H.groupby('Home').last().reset_index()
    ultima_base_A = base_A.groupby('Away').last().reset_index()

    Jogos = pd.merge(Jogos_do_Dia, ultima_base_H, how='left', left_on='Home', right_on='Home')
    Jogos = pd.merge(Jogos, ultima_base_A, how='left', left_on='Away', right_on='Away')

    Jogos = drop_reset_index(Jogos)
    flt = (Jogos.M_CG2_A < 1) & (Jogos.CV_CG2_A > 0.5) & (Jogos.Odd_A >= 2)
    Jogos = Jogos[flt]
    LG_Away = drop_reset_index(Jogos)

    if len(Lay_0x0_HT) != 0:
        st.write("Oportunidades para o Lay 0 x 0 - HT")
        Lay_0x0_HT = Lay_0x0_HT[['Time','League','Home','Away']]
        st.dataframe(Lay_0x0_HT)
    else:
        st.write("Sem Oportunidades para o Lay 0 x 0 - HT")
        st.write('')

    try:
        flt = base_orig.Date == str(dia)
        base_today = base_orig[flt]
        base_today = base_today[['League','Home','Away','Goals_H_HT','Goals_A_HT']]
        base_today = drop_reset_index(base_today)
        
        Entradas_Lay0x0 = pd.merge(Lay_0x0_HT, base_today, on=['League','Home', 'Away'])
        Entradas_Lay0x0 = drop_reset_index(Entradas_Lay0x0)
        Entradas_Lay0x0['Result'] = np.where((Entradas_Lay0x0['Goals_H_HT'] != 0) | (Entradas_Lay0x0['Goals_A_HT'] != 0), 'GREEN', 'RED')
        
        flt_0x0 = Entradas_Lay0x0.Result == 'GREEN'
        green_0x0 = Entradas_Lay0x0[flt_0x0]
        green = len(green_0x0)
        reds = len( Entradas_Lay0x0) - green

        if len(Entradas_Lay0x0) != 0:
            st.write("Resultados do Filtro Lay 0 x 0 HT:")
            st.dataframe(Entradas_Lay0x0)
            col1, col2, col3, col4 = st.columns(4)
            with col2:
                st.write(f'Greens: {green}', unsafe_allow_html=True)
            with col3:
                st.write(f'Reds: {reds}', unsafe_allow_html=True)
            st.write('');st.write('');st.write('') 
        else:
            pass

    except:
        pass
    
    
    if len(Lay_0x1) != 0:
        st.write("Oportunidades para o Lay 0 x 1")
        Lay_0x1 = Lay_0x1[['Time','League','Home','Away']]
        
        st.dataframe(Lay_0x1)
    else:
        st.write("Sem Oportunidades para o Lay 0 x 1")
        st.write('')



    try:
        flt = base_orig.Date == str(dia)
        base_today = base_orig[flt]
        base_today = base_today[['League','Home','Away','Goals_H','Goals_A']]
        base_today = drop_reset_index(base_today)
        
        Entradas_Lay0x1 = pd.merge(Lay_0x1, base_today, on=['League','Home', 'Away'])
        Entradas_Lay0x1 = drop_reset_index(Entradas_Lay0x1)
        Entradas_Lay0x1['Result'] = np.where((Entradas_Lay0x1['Goals_H'] == 0) & (Entradas_Lay0x1['Goals_A'] == 1), 'RED', 'GREEN')
        
        flt_0x1 = Entradas_Lay0x1.Result == 'GREEN'
        green_0x1 = Entradas_Lay0x1[flt_0x1]
        green = len(green_0x1)
        reds = len( Entradas_Lay0x1) - green
        
        if len(Entradas_Lay0x1) != 0:
            st.write("Resultados do Filtro Lay 0 x 1:")
            st.dataframe(Entradas_Lay0x1)
            col1, col2, col3, col4 = st.columns(4)
            with col2:
                st.write(f'Greens: {green}', unsafe_allow_html=True)
            with col3:
                st.write(f'Reds: {reds}', unsafe_allow_html=True)
            st.write('');st.write('');st.write('')
        else:
            pass

    except:
        pass
    
    if len(Lay_0x2) != 0:
        st.write("Oportunidades para o Lay 0 x 2")
        Lay_0x2 = Lay_0x2[['Time','League','Home','Away']]
        st.dataframe(Lay_0x2)
    else:
        st.write("Sem Oportunidades para o Lay 0 x 2")
        st.write('')

    try:
        flt = base_orig.Date == str(dia)
        base_today = base_orig[flt]
        base_today = base_today[['League','Home','Away','Goals_H','Goals_A']]
        base_today = drop_reset_index(base_today)
        
        Entradas_Lay0x2 = pd.merge(Lay_0x2, base_today, on=['League','Home', 'Away'])
        Entradas_Lay0x2 = drop_reset_index(Entradas_Lay0x2)
        Entradas_Lay0x2['Result'] = np.where((Entradas_Lay0x2['Goals_H'] == 0) & (Entradas_Lay0x2['Goals_A'] == 2), 'RED', 'GREEN')
        
        flt_0x2 = Entradas_Lay0x2.Result == 'GREEN'
        green_0x2 = Entradas_Lay0x2[flt_0x2]
        green = len(green_0x2)
        reds = len( Entradas_Lay0x2) - green
        
        if len(Entradas_Lay0x2) != 0:
            st.write("Resultados do Filtro Lay 0 x 2:")
            st.dataframe(Entradas_Lay0x2)
            col1, col2, col3, col4 = st.columns(4)
            with col2:
                st.write(f'Greens: {green}', unsafe_allow_html=True)
            with col3:
                st.write(f'Reds: {reds}', unsafe_allow_html=True)
            st.write('');st.write('');st.write('') 
        else:
            pass

    except:
        pass
    
    if len(LG_Away) != 0:
        st.write("Oportunidades para o Lay Goleada Away")
        LG_Away = LG_Away[['Time','League','Home','Away']]
        st.dataframe(LG_Away)
    else:
        st.write("Sem Oportunidades para o Lay Goleada Away")
        st.write('')

    try:
        flt = base_orig.Date == str(dia)
        base_today = base_orig[flt]
        base_today = base_today[['League','Home','Away','Goals_H','Goals_A']]
        base_today = drop_reset_index(base_today)
        
        Entradas_LG_Away = pd.merge(LG_Away, base_today, on=['League','Home', 'Away'])
        Entradas_LG_Away = drop_reset_index(Entradas_LG_Away)
        Entradas_LG_Away['Result'] = np.where((Entradas_LG_Away['Goals_A'] > Entradas_LG_Away['Goals_H']) & (Entradas_LG_Away['Goals_A'] >= 4), 'RED', 'GREEN')
        
        flt_LG_Away = Entradas_LG_Away.Result == 'GREEN'
        green_LG_Away = Entradas_LG_Away[flt_LG_Away]
        green = len(green_LG_Away)
        reds = len(Entradas_LG_Away) - green

        if len(Entradas_LG_Away) != 0:
            st.write("Resultados do Filtro Lay Goleada Away:")
            st.dataframe(Entradas_LG_Away)
            col1, col2, col3, col4 = st.columns(4)
            with col2:
                st.write(f'Greens: {green}', unsafe_allow_html=True)
            with col3:
                st.write(f'Reds: {reds}', unsafe_allow_html=True)
            st.write('');st.write('');st.write('')
        else:
            pass

    except:
        pass

    st.subheader("Outros Filtros")

    
    flt_Poseidon_Home = ((betfair.Odd_2x0 < betfair.Odd_1x0) & 
                        (betfair.Odd_2x0 < betfair.Odd_1x1) & 
                        (betfair.Odd_2x2 < betfair.Odd_1x2))
    Poseidon_Home = betfair[flt_Poseidon_Home]
    Poseidon_Home = drop_reset_index(Poseidon_Home)
    if len(Poseidon_Home) != 0:
        st.write("Poseidon Home")
        st.dataframe(Poseidon_Home)
    else:
        st.write("Sem Oportunidades para o Poseidon Home")
        st.write('')

    




    flt_Poseidon_Away = ((betfair.Odd_0x2 < betfair.Odd_0x1) & 
                         (betfair.Odd_0x2 < betfair.Odd_1x1) & 
                         (betfair.Odd_2x2 < betfair.Odd_2x1))
    Poseidon_Away = betfair[flt_Poseidon_Away]
    Poseidon_Away = drop_reset_index(Poseidon_Away)
    Poseidon_Away
    if len(Poseidon_Away) != 0:
        st.write("Poseidon Away")
        st.dataframe(Poseidon_Away)
    else:
        st.write("Sem Oportunidades para o Poseidon Away")
        st.write('')


    flt_MO_Home = ((betfair.Odd_H >= 1.30) & (betfair.Odd_H <= 1.80) & 
                   (betfair.Odd_D >= 3.50) & (betfair.Odd_D <= 7.00) & 
                   (betfair.Odd_A >= 4.00) & (betfair.Odd_A <= 11.00))
    MO_Home = betfair[flt_MO_Home]
    MO_Home = drop_reset_index(MO_Home)
    if len(MO_Home) != 0:
        st.write("Match Odds Home")
        st.dataframe(MO_Home)
    else:
        st.write("Sem Oportunidades para Match Odds Home")
        st.write('')

    




    flt_MO_Away = ((betfair.Odd_H >= 4.00) & (betfair.Odd_H <= 11.00) & 
                   (betfair.Odd_D >= 3.50) & (betfair.Odd_D <= 7.00) & 
                   (betfair.Odd_A >= 1.30) & (betfair.Odd_A <= 1.80))
    MO_Away = betfair[flt_MO_Away]
    MO_Away = drop_reset_index(MO_Away)
    MO_Away
    if len(MO_Away) != 0:
        st.write("Match Odds Away")
        st.dataframe(MO_Away)
    else:
        st.write("Sem Oportunidades para o Match Odds Away")
        st.write('')


    
    
    
























