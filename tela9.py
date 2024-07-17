import streamlit as st
import plotly.graph_objects as go
from futpythontrader import *

def drop_reset_index(df):
    df = df.dropna()
    df = df.reset_index(drop=True)
    df.index += 1
    return df

def show_tela9():
    st.title("Luke v2.1")
    st.header("Backtesting")
    st.write('Selecione os filtros desejados enquanto preparamos a Base de Dados')

    # Atualizado com todas as suas colunas
    colunas = [
        'Odd_H', 'Odd_D', 'Odd_A',
        'Odd_Over25_FT', 'Odd_Under25_FT',
        'Odd_BTTS_Yes', 'Odd_BTTS_No',
        'Odd_0x0', 'Odd_0x1', 'Odd_0x2', 'Odd_0x3',  
        'Odd_1x0', 'Odd_1x1', 'Odd_1x2', 'Odd_1x3', 
        'Odd_2x0', 'Odd_2x1', 'Odd_2x2', 'Odd_2x3',
        'Odd_3x0', 'Odd_3x1', 'Odd_3x2', 'Odd_3x3', 
        'Ind_Efi_H', 'CV_IF_H', 'Ind_Efi_A',  'CV_IF_A',
        'Coe_Efi_H', 'CV_CE_H', 'Coe_Efi_A',  'CV_CE_A',
        'Media_Ptos_H', 'CV_Ptos_H', 'Media_Ptos_A',  'CV_Ptos_A',
        'Media_GM_H', 'CV_GM_H', 'Media_GM_A', 'CV_GM_A',
        'Media_GS_H', 'CV_GS_H', 'Media_GS_A',  'CV_GS_A',
        'Media_SG_H', 'CV_SG_H',  'Media_SG_A','CV_SG_A' 
    ]
    
    # Dividir as colunas de forma mais equilibrada entre quatro colunas de checkboxes
    n_colunas = 4  # Número de colunas para checkboxes
    col_chunks = [colunas[i::n_colunas] for i in range(n_colunas)]  # Divide as colunas em 4 listas

    file_path = 'Legenda_Filtros.pdf'
        
    with open(file_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    
    st.download_button(
        label="Legenda Filtros Backtesting",
        data=PDFbyte,
        file_name="Legenda_Filtros.pdf",
        mime="application/octet-stream"
    )
    st.text('')
    # Inicializa um dicionário para armazenar os valores dos inputs
    valores_input = {}

    # Criação dinâmica de colunas no Streamlit e associação dos checkboxes
    st_cols = st.columns(n_colunas)
    user_selections = {}
    for idx, chunk in enumerate(col_chunks):
        with st_cols[idx]:
            for col in chunk:
                # A chave é adaptada para permitir identificação única também nas colunas
                user_selections[col] = st.checkbox(col, key=f"chk_{col}")

    # Detalhes de cada odd - a ser completado conforme seu exemplo
    odd_details = {
    'Odd_H': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_D': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_A': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_Over25_FT': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_Under25_FT': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_BTTS_Yes': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_BTTS_No': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_0x0': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_0x1': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_0x2': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_0x3': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_1x0': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_1x1': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_1x2': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_1x3': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_2x0': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_2x1': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_2x2': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_2x3': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_3x0': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_3x1': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_3x2': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Odd_3x3': {"min_value": 1.01, "max_value": 10.0, "step": 0.1},
    'Ind_Efi_H': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'Ind_Efi_A': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'CV_IF_H': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'CV_IF_A': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'Coe_Efi_H': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'Coe_Efi_A': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'CV_CE_H': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'CV_CE_A': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'Media_Ptos_H': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'Media_Ptos_A': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'CV_Ptos_H': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'CV_Ptos_A': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'Media_GM_H': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'Media_GM_A': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'CV_GM_H': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'CV_GM_A': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'Media_GS_H': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'Media_GS_A': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'CV_GS_H': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'CV_GS_A': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'Media_SG_H': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'Media_SG_A': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'CV_SG_H': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    'CV_SG_A': {"min_value": 0.00, "max_value": 10.0, "step": 0.1},
    }


    for coluna, is_selected in user_selections.items():
        if is_selected:
            details = odd_details[coluna]
            min_value, max_value = st.columns(2)
            with min_value:
                valores_input[f"{coluna}_Min"] = st.number_input(f"{coluna}_Min", value=details["min_value"], step=details["step"], key=f"{coluna}_Min")
            with max_value:
                valores_input[f"{coluna}_Max"] = st.number_input(f"{coluna}_Max", value=details["max_value"], step=details["step"], key=f"{coluna}_Max")


    @st.cache_data
    def load_data_base():

        base_luke = pd.read_csv('https://github.com/futpythontrader/YouTube/raw/main/Bases_de_Dados/FlashScore/Base_de_Dados_FlashScore_Backtesting_Luke.csv')
        return base_luke

    df = load_data_base()

    
    st.text('');st.text('')
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

    # st.write('Base de Dados pronta para análise.')

    # st.write('Selecione a estratégia desejada.')

    estrategias = ['Back Home','Back Draw','Back Away',
                   'Lay Home','Lay Draw','Lay Away',
                    'Over05 HT','Under05 HT','Over05 FT','Under05 FT', 
                    'Over15 FT','Under15 FT','Over25 FT','Under25 FT', 
                    'BTTS Sim','BTTS Não',
                    'Lay 0 x 0','Lay 0 x 1','Lay 0 x 2','Lay 0 x 3',
                    'Lay 1 x 0','Lay 1 x 1','Lay 1 x 2','Lay 1 x 3',
                    'Lay 2 x 0','Lay 2 x 1','Lay 2 x 2','Lay 2 x 3',
                    'Lay 3 x 0','Lay 3 x 1','Lay 3 x 2','Lay 3 x 3',
                    'Lay Goleada Home', 'Lay Goleada Away',
                    'Poseidon Home','Poseidon Away',
                    'Odds MO Home', 'Odds MO Away']
    st.text('');st.text('')
    backtestes = st.selectbox('Escolha a Metodologia', estrategias)

    if ((backtestes == 'Poseidon Home') | (backtestes == 'Poseidon Away') | (backtestes == 'Odds MO Home') | (backtestes == 'Odds MO Away')):
        placares = ['0 x 0', '0 x 1', '0 x 2', '0 x 3',
                '1 x 0', '1 x 1', '1 x 2', '1 x 3',
                '2 x 0', '2 x 1', '2 x 2', '2 x 3',
                '3 x 0', '3 x 1', '3 x 2', '3 x 3',
                'Goleada Home', 'Goleada Away']

        backtestes2 = st.selectbox('Escolha o Placar', placares)

    else:
        backtestes2 = ''
    st.text('');st.text('')

    def calcular_profit(df, estrategia, placar, odd_limits):
        
        if estrategia == 'Back Home':
            df.loc[(df['Goals_H_FT'] > df['Goals_A_FT']), 'Profit'] = df['Odd_H'] - 1
            df.loc[(df['Goals_H_FT'] <= df['Goals_A_FT']), 'Profit'] = -1
        
        if estrategia == 'Back Draw':
            df.loc[(df['Goals_H_FT'] == df['Goals_A_FT']), 'Profit'] = df['Odd_D'] - 1
            df.loc[(df['Goals_H_FT'] != df['Goals_A_FT']), 'Profit'] = -1
        
        if estrategia == 'Back Away':
            df.loc[(df['Goals_A_FT'] > df['Goals_H_FT']), 'Profit'] = df['Odd_A'] - 1
            df.loc[(df['Goals_A_FT'] <= df['Goals_H_FT']), 'Profit'] = -1
        
        if estrategia == 'Lay Home':
            df.loc[(df['Goals_H_FT'] <= df['Goals_A_FT']), 'Profit'] = df['Odd_Lay_Home'] - 1
            df.loc[(df['Goals_H_FT'] > df['Goals_A_FT']), 'Profit'] = -1
        
        if estrategia == 'Lay Draw':
            df.loc[(df['Goals_H_FT'] != df['Goals_A_FT']), 'Profit'] = 1 / (df['Odd_D'] - 0.75)
            df.loc[(df['Goals_H_FT'] == df['Goals_A_FT']), 'Profit'] = -1
        
        if estrategia == 'Lay Away':
            df.loc[(df['Goals_A_FT'] <= df['Goals_H_FT']), 'Profit'] = df['Odd_Lay_Away'] - 1
            df.loc[(df['Goals_A_FT'] > df['Goals_H_FT']), 'Profit'] = -1

        if estrategia == 'Over05 HT':
            df.loc[(df['Goals_A_HT'] + df['Goals_H_HT']) > 0, 'Profit'] = df['Odd_Over05_HT'] - 1
            df.loc[(df['Goals_A_HT'] + df['Goals_H_HT']) < 1, 'Profit'] = -1

        if estrategia == 'Under05 HT':
            df.loc[(df['Goals_A_HT'] + df['Goals_H_HT']) < 1, 'Profit'] = df['Odd_Under05_HT'] - 1
            df.loc[(df['Goals_A_HT'] + df['Goals_H_HT']) > 0, 'Profit'] = -1

        if estrategia == 'Over05 FT':
            df.loc[(df['Goals_A_FT'] + df['Goals_H_FT']) > 0, 'Profit'] = df['Odd_Over05_FT'] - 1
            df.loc[(df['Goals_A_FT'] + df['Goals_H_FT']) < 1, 'Profit'] = -1

        if estrategia == 'Under05 FT':
            df.loc[(df['Goals_A_FT'] + df['Goals_H_FT']) < 1, 'Profit'] = df['Odd_Under05_FT'] - 1
            df.loc[(df['Goals_A_FT'] + df['Goals_H_FT']) > 0, 'Profit'] = -1

        if estrategia == 'Over15 FT':
            df.loc[(df['Goals_A_FT'] + df['Goals_H_FT']) > 1, 'Profit'] = df['Odd_Over15_FT'] - 1
            df.loc[(df['Goals_A_FT'] + df['Goals_H_FT']) < 2, 'Profit'] = -1

        if estrategia == 'Under15 FT':
            df.loc[(df['Goals_A_FT'] + df['Goals_H_FT']) < 2, 'Profit'] = df['Odd_Under15_FT'] - 1
            df.loc[(df['Goals_A_FT'] + df['Goals_H_FT']) > 1, 'Profit'] = -1

        if estrategia == 'Over25 FT':
            df.loc[(df['Goals_A_FT'] + df['Goals_H_FT']) > 2, 'Profit'] = df['Odd_Over25_FT'] - 1
            df.loc[(df['Goals_A_FT'] + df['Goals_H_FT']) < 3, 'Profit'] = -1

        if estrategia == 'Under25 FT':
            df.loc[(df['Goals_A_FT'] + df['Goals_H_FT']) < 3, 'Profit'] = df['Odd_Under25_FT'] - 1
            df.loc[(df['Goals_A_FT'] + df['Goals_H_FT']) > 2, 'Profit'] = -1

        if estrategia == 'BTTS Sim':
            df['BTTS'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] > 0 and row['Goals_A_FT'] > 0) else 0, axis=1)
            
            df.loc[(df['BTTS'] == 1), 'Profit'] = df['Odd_BTTS_Yes'] - 1
            df.loc[(df['BTTS'] == 0), 'Profit'] = -1

        if estrategia == 'BTTS Não':
            df['BTTS'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] > 0 and row['Goals_A_FT'] > 0) else 0, axis=1)
            
            df.loc[(df['BTTS'] == 0), 'Profit'] = df['Odd_BTTS_No'] - 1
            df.loc[(df['BTTS'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 0 x 0':

            df['0x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 0) else 0, axis=1)
            
            df.loc[(df['0x0'] == 0), 'Profit'] = 1 / (df['Odd_0x0'] + 5)
            df.loc[(df['0x0'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 0 x 1':

            df['0x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 1) else 0, axis=1)
            
            df.loc[(df['0x1'] == 0), 'Profit'] = 1 / (df['Odd_0x1'] + 5)
            df.loc[(df['0x1'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 0 x 2':

            df['0x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 2) else 0, axis=1)
            
            df.loc[(df['0x2'] == 0), 'Profit'] = 1 / (df['Odd_0x2'] + 5)
            df.loc[(df['0x2'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 0 x 3':

            df['0x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 3) else 0, axis=1)
            
            df.loc[(df['0x3'] == 0), 'Profit'] = 1 / (df['Odd_0x3'] + 5)
            df.loc[(df['0x3'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 1 x 0':

            df['1x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 0) else 0, axis=1)
            
            df.loc[(df['1x0'] == 0), 'Profit'] = 1 / (df['Odd_1x0'] + 5)
            df.loc[(df['1x0'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 1 x 1':

            df['1x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 1) else 0, axis=1)
            
            df.loc[(df['1x1'] == 0), 'Profit'] = 1 / (df['Odd_1x1'] + 5)
            df.loc[(df['1x1'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 1 x 2':

            df['1x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 2) else 0, axis=1)
            
            df.loc[(df['1x2'] == 0), 'Profit'] = 1 / (df['Odd_1x2'] + 5)
            df.loc[(df['1x2'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 1 x 3':

            df['1x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 3) else 0, axis=1)
            
            df.loc[(df['1x3'] == 0), 'Profit'] = 1 / (df['Odd_1x3'] + 5)
            df.loc[(df['1x3'] == 1), 'Profit'] = -1

        if estrategia == 'Lay Goleada Home':

            df['Goleada_H'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] >= 4 and row['Goals_H_FT'] > row['Goals_A_FT']) else 0, axis=1)
            
            df.loc[(df['Goleada_H'] == 0), 'Profit'] = 0.025
            df.loc[(df['Goleada_H'] == 1), 'Profit'] = -1

        if estrategia == 'Lay Goleada Away':

            df['Goleada_A'] = df.apply(lambda row: 1 if (row['Goals_A_FT'] >= 4 and row['Goals_A_FT'] > row['Goals_H_FT']) else 0, axis=1)
            
            df.loc[(df['Goleada_A'] == 0), 'Profit'] = 0.025
            df.loc[(df['Goleada_A'] == 1), 'Profit'] = -1


        if estrategia == 'Lay 2 x 0':

            df['2x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 0) else 0, axis=1)
            
            df.loc[(df['2x0'] == 0), 'Profit'] = 1 / (df['Odd_2x0'] + 5)
            df.loc[(df['2x0'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 2 x 1':

            df['2x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 1) else 0, axis=1)
            
            df.loc[(df['2x1'] == 0), 'Profit'] = 1 / (df['Odd_2x1'] + 5)
            df.loc[(df['2x1'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 2 x 2':

            df['2x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 2) else 0, axis=1)
            
            df.loc[(df['2x2'] == 0), 'Profit'] = 1 / (df['Odd_2x2'] + 5)
            df.loc[(df['2x2'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 2 x 3':

            df['2x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 3) else 0, axis=1)
            
            df.loc[(df['2x3'] == 0), 'Profit'] = 1 / (df['Odd_2x3'] + 5)
            df.loc[(df['2x3'] == 1), 'Profit'] = -1 

        if estrategia == 'Lay 3 x 0':

            df['3x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 0) else 0, axis=1)
            
            df.loc[(df['3x0'] == 0), 'Profit'] = 1 / (df['Odd_3x0'] + 5)
            df.loc[(df['3x0'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 3 x 1':

            df['3x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 1) else 0, axis=1)
            
            df.loc[(df['3x1'] == 0), 'Profit'] = 1 / (df['Odd_3x1'] + 5)
            df.loc[(df['3x1'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 3 x 2':

            df['3x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 2) else 0, axis=1)
            
            df.loc[(df['3x2'] == 0), 'Profit'] = 1 / (df['Odd_3x2'] + 5)
            df.loc[(df['3x2'] == 1), 'Profit'] = -1

        if estrategia == 'Lay 3 x 3':

            df['3x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 3) else 0, axis=1)
            
            df.loc[(df['3x3'] == 0), 'Profit'] = 1 / (df['Odd_3x3'] + 5)
            df.loc[(df['3x3'] == 1), 'Profit'] = -1           

        if estrategia == 'Poseidon Home':
            
            flt_Poseidon_Home = ((df.Odd_2x0 < df.Odd_1x0) & 
                                 (df.Odd_2x0 < df.Odd_1x1) & 
                                 (df.Odd_2x2 < df.Odd_1x2))
            df = df[flt_Poseidon_Home]
            df = drop_reset_index(df)
            
            if placar == '0 x 0':
            
              df['0x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 0) else 0, axis=1)
              
              df.loc[(df['0x0'] == 0), 'Profit'] = 1 / (df['Odd_0x0'] + 5)
              df.loc[(df['0x0'] == 1), 'Profit'] = -1

            if placar == '0 x 1':

                df['0x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['0x1'] == 0), 'Profit'] = 1 / (df['Odd_0x1'] + 5)
                df.loc[(df['0x1'] == 1), 'Profit'] = -1

            if placar == '0 x 2':

                df['0x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['0x2'] == 0), 'Profit'] = 1 / (df['Odd_0x2'] + 5)
                df.loc[(df['0x2'] == 1), 'Profit'] = -1

            if placar == '0 x 3':

                df['0x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['0x3'] == 0), 'Profit'] = 1 / (df['Odd_0x3'] + 5)
                df.loc[(df['0x3'] == 1), 'Profit'] = -1

            if placar == '1 x 0':

                df['1x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 0) else 0, axis=1)
                
                df.loc[(df['1x0'] == 0), 'Profit'] = 1 / (df['Odd_1x0'] + 5)
                df.loc[(df['1x0'] == 1), 'Profit'] = -1

            if placar == '1 x 1':

                df['1x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['1x1'] == 0), 'Profit'] = 1 / (df['Odd_1x1'] + 5)
                df.loc[(df['1x1'] == 1), 'Profit'] = -1

            if placar == '1 x 2':

                df['1x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['1x2'] == 0), 'Profit'] = 1 / (df['Odd_1x2'] + 5)
                df.loc[(df['1x2'] == 1), 'Profit'] = -1

            if placar == '1 x 3':

                df['1x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['1x3'] == 0), 'Profit'] = 1 / (df['Odd_1x3'] + 5)
                df.loc[(df['1x3'] == 1), 'Profit'] = -1

            if placar == 'Goleada Home':

                df['Goleada_H'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] >= 4 and row['Goals_H_FT'] > row['Goals_A_FT']) else 0, axis=1)
                
                df.loc[(df['Goleada_H'] == 0), 'Profit'] = 0.025
                df.loc[(df['Goleada_H'] == 1), 'Profit'] = -1

            if placar == 'Goleada Away':

                df['Goleada_A'] = df.apply(lambda row: 1 if (row['Goals_A_FT'] >= 4 and row['Goals_A_FT'] > row['Goals_H_FT']) else 0, axis=1)
                
                df.loc[(df['Goleada_A'] == 0), 'Profit'] = 0.025
                df.loc[(df['Goleada_A'] == 1), 'Profit'] = -1

            if placar == '2 x 0':

                df['2x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 0) else 0, axis=1)
                
                df.loc[(df['2x0'] == 0), 'Profit'] = 1 / (df['Odd_2x0'] + 5)
                df.loc[(df['2x0'] == 1), 'Profit'] = -1

            if placar == '2 x 1':

                df['2x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['2x1'] == 0), 'Profit'] = 1 / (df['Odd_2x1'] + 5)
                df.loc[(df['2x1'] == 1), 'Profit'] = -1

            if placar == '2 x 2':

                df['2x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['2x2'] == 0), 'Profit'] = 1 / (df['Odd_2x2'] + 5)
                df.loc[(df['2x2'] == 1), 'Profit'] = -1

            if placar == '2 x 3':

                df['2x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['2x3'] == 0), 'Profit'] = 1 / (df['Odd_2x3'] + 5)
                df.loc[(df['2x3'] == 1), 'Profit'] = -1 

            if placar == '3 x 0':

                df['3x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 0) else 0, axis=1)
                
                df.loc[(df['3x0'] == 0), 'Profit'] = 1 / (df['Odd_3x0'] + 5)
                df.loc[(df['3x0'] == 1), 'Profit'] = -1

            if placar == '3 x 1':

                df['3x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['3x1'] == 0), 'Profit'] = 1 / (df['Odd_3x1'] + 5)
                df.loc[(df['3x1'] == 1), 'Profit'] = -1

            if placar == '3 x 2':

                df['3x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['3x2'] == 0), 'Profit'] = 1 / (df['Odd_3x2'] + 5)
                df.loc[(df['3x2'] == 1), 'Profit'] = -1

            if placar == '3 x 3':

                df['3x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['3x3'] == 0), 'Profit'] = 1 / (df['Odd_3x3'] + 5)
                df.loc[(df['3x3'] == 1), 'Profit'] = -1     
                
        if estrategia == 'Poseidon Away':
            
            flt_Poseidon_Away = ((df.Odd_0x2 < df.Odd_0x1) & 
                                 (df.Odd_0x2 < df.Odd_1x1) & 
                                 (df.Odd_2x2 < df.Odd_2x1))
            df = df[flt_Poseidon_Away]
            df = drop_reset_index(df)
            
            if placar == '0 x 0':
            
              df['0x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 0) else 0, axis=1)
              
              df.loc[(df['0x0'] == 0), 'Profit'] = 1 / (df['Odd_0x0'] + 5)
              df.loc[(df['0x0'] == 1), 'Profit'] = -1

            if placar == '0 x 1':

                df['0x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['0x1'] == 0), 'Profit'] = 1 / (df['Odd_0x1'] + 5)
                df.loc[(df['0x1'] == 1), 'Profit'] = -1

            if placar == '0 x 2':

                df['0x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['0x2'] == 0), 'Profit'] = 1 / (df['Odd_0x2'] + 5)
                df.loc[(df['0x2'] == 1), 'Profit'] = -1

            if placar == '0 x 3':

                df['0x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['0x3'] == 0), 'Profit'] = 1 / (df['Odd_0x3'] + 5)
                df.loc[(df['0x3'] == 1), 'Profit'] = -1

            if placar == '1 x 0':

                df['1x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 0) else 0, axis=1)
                
                df.loc[(df['1x0'] == 0), 'Profit'] = 1 / (df['Odd_1x0'] + 5)
                df.loc[(df['1x0'] == 1), 'Profit'] = -1

            if placar == '1 x 1':

                df['1x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['1x1'] == 0), 'Profit'] = 1 / (df['Odd_1x1'] + 5)
                df.loc[(df['1x1'] == 1), 'Profit'] = -1

            if placar == '1 x 2':

                df['1x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['1x2'] == 0), 'Profit'] = 1 / (df['Odd_1x2'] + 5)
                df.loc[(df['1x2'] == 1), 'Profit'] = -1

            if placar == '1 x 3':

                df['1x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['1x3'] == 0), 'Profit'] = 1 / (df['Odd_1x3'] + 5)
                df.loc[(df['1x3'] == 1), 'Profit'] = -1

            if placar == 'Goleada Home':

                df['Goleada_H'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] >= 4 and row['Goals_H_FT'] > row['Goals_A_FT']) else 0, axis=1)
                
                df.loc[(df['Goleada_H'] == 0), 'Profit'] = 0.025
                df.loc[(df['Goleada_H'] == 1), 'Profit'] = -1

            if placar == 'Goleada Away':

                df['Goleada_A'] = df.apply(lambda row: 1 if (row['Goals_A_FT'] >= 4 and row['Goals_A_FT'] > row['Goals_H_FT']) else 0, axis=1)
                
                df.loc[(df['Goleada_A'] == 0), 'Profit'] = 0.025
                df.loc[(df['Goleada_A'] == 1), 'Profit'] = -1

            if placar == '2 x 0':

                df['2x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 0) else 0, axis=1)
                
                df.loc[(df['2x0'] == 0), 'Profit'] = 1 / (df['Odd_2x0'] + 5)
                df.loc[(df['2x0'] == 1), 'Profit'] = -1

            if placar == '2 x 1':

                df['2x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['2x1'] == 0), 'Profit'] = 1 / (df['Odd_2x1'] + 5)
                df.loc[(df['2x1'] == 1), 'Profit'] = -1

            if placar == '2 x 2':

                df['2x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['2x2'] == 0), 'Profit'] = 1 / (df['Odd_2x2'] + 5)
                df.loc[(df['2x2'] == 1), 'Profit'] = -1

            if placar == '2 x 3':

                df['2x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['2x3'] == 0), 'Profit'] = 1 / (df['Odd_2x3'] + 5)
                df.loc[(df['2x3'] == 1), 'Profit'] = -1 

            if placar == '3 x 0':

                df['3x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 0) else 0, axis=1)
                
                df.loc[(df['3x0'] == 0), 'Profit'] = 1 / (df['Odd_3x0'] + 5)
                df.loc[(df['3x0'] == 1), 'Profit'] = -1

            if placar == '3 x 1':

                df['3x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['3x1'] == 0), 'Profit'] = 1 / (df['Odd_3x1'] + 5)
                df.loc[(df['3x1'] == 1), 'Profit'] = -1

            if placar == '3 x 2':

                df['3x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['3x2'] == 0), 'Profit'] = 1 / (df['Odd_3x2'] + 5)
                df.loc[(df['3x2'] == 1), 'Profit'] = -1

            if placar == '3 x 3':

                df['3x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['3x3'] == 0), 'Profit'] = 1 / (df['Odd_3x3'] + 5)
                df.loc[(df['3x3'] == 1), 'Profit'] = -1
                

        if estrategia == 'Odds MO Home':
            
            flt_MO_Home = ((df.Odd_H >= 1.30) & (df.Odd_H <= 1.80) & 
                           (df.Odd_D >= 3.50) & (df.Odd_D <= 7.00) & 
                           (df.Odd_A >= 4.00) & (df.Odd_A <= 11.00))
            df = df[flt_MO_Home]
            df = drop_reset_index(df)
                    
            if placar == '0 x 0':
            
              df['0x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 0) else 0, axis=1)
              
              df.loc[(df['0x0'] == 0), 'Profit'] = 1 / (df['Odd_0x0'] + 5)
              df.loc[(df['0x0'] == 1), 'Profit'] = -1

            if placar == '0 x 1':

                df['0x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['0x1'] == 0), 'Profit'] = 1 / (df['Odd_0x1'] + 5)
                df.loc[(df['0x1'] == 1), 'Profit'] = -1

            if placar == '0 x 2':

                df['0x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['0x2'] == 0), 'Profit'] = 1 / (df['Odd_0x2'] + 5)
                df.loc[(df['0x2'] == 1), 'Profit'] = -1

            if placar == '0 x 3':

                df['0x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['0x3'] == 0), 'Profit'] = 1 / (df['Odd_0x3'] + 5)
                df.loc[(df['0x3'] == 1), 'Profit'] = -1

            if placar == '1 x 0':

                df['1x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 0) else 0, axis=1)
                
                df.loc[(df['1x0'] == 0), 'Profit'] = 1 / (df['Odd_1x0'] + 5)
                df.loc[(df['1x0'] == 1), 'Profit'] = -1

            if placar == '1 x 1':

                df['1x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['1x1'] == 0), 'Profit'] = 1 / (df['Odd_1x1'] + 5)
                df.loc[(df['1x1'] == 1), 'Profit'] = -1

            if placar == '1 x 2':

                df['1x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['1x2'] == 0), 'Profit'] = 1 / (df['Odd_1x2'] + 5)
                df.loc[(df['1x2'] == 1), 'Profit'] = -1

            if placar == '1 x 3':

                df['1x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['1x3'] == 0), 'Profit'] = 1 / (df['Odd_1x3'] + 5)
                df.loc[(df['1x3'] == 1), 'Profit'] = -1

            if placar == 'Goleada Home':

                df['Goleada_H'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] >= 4 and row['Goals_H_FT'] > row['Goals_A_FT']) else 0, axis=1)
                
                df.loc[(df['Goleada_H'] == 0), 'Profit'] = 0.025
                df.loc[(df['Goleada_H'] == 1), 'Profit'] = -1

            if placar == 'Goleada Away':

                df['Goleada_A'] = df.apply(lambda row: 1 if (row['Goals_A_FT'] >= 4 and row['Goals_A_FT'] > row['Goals_H_FT']) else 0, axis=1)
                
                df.loc[(df['Goleada_A'] == 0), 'Profit'] = 0.025
                df.loc[(df['Goleada_A'] == 1), 'Profit'] = -1

            if placar == '2 x 0':

                df['2x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 0) else 0, axis=1)
                
                df.loc[(df['2x0'] == 0), 'Profit'] = 1 / (df['Odd_2x0'] + 5)
                df.loc[(df['2x0'] == 1), 'Profit'] = -1

            if placar == '2 x 1':

                df['2x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['2x1'] == 0), 'Profit'] = 1 / (df['Odd_2x1'] + 5)
                df.loc[(df['2x1'] == 1), 'Profit'] = -1

            if placar == '2 x 2':

                df['2x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['2x2'] == 0), 'Profit'] = 1 / (df['Odd_2x2'] + 5)
                df.loc[(df['2x2'] == 1), 'Profit'] = -1

            if placar == '2 x 3':

                df['2x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['2x3'] == 0), 'Profit'] = 1 / (df['Odd_2x3'] + 5)
                df.loc[(df['2x3'] == 1), 'Profit'] = -1 

            if placar == '3 x 0':

                df['3x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 0) else 0, axis=1)
                
                df.loc[(df['3x0'] == 0), 'Profit'] = 1 / (df['Odd_3x0'] + 5)
                df.loc[(df['3x0'] == 1), 'Profit'] = -1

            if placar == '3 x 1':

                df['3x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['3x1'] == 0), 'Profit'] = 1 / (df['Odd_3x1'] + 5)
                df.loc[(df['3x1'] == 1), 'Profit'] = -1

            if placar == '3 x 2':

                df['3x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['3x2'] == 0), 'Profit'] = 1 / (df['Odd_3x2'] + 5)
                df.loc[(df['3x2'] == 1), 'Profit'] = -1

            if placar == '3 x 3':

                df['3x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['3x3'] == 0), 'Profit'] = 1 / (df['Odd_3x3'] + 5)
                df.loc[(df['3x3'] == 1), 'Profit'] = -1     
                
        if estrategia == 'Odds MO Away':
            
            flt_MO_Away = ((df.Odd_H >= 4.00) & (df.Odd_H <= 11.00) & 
                           (df.Odd_D >= 3.50) & (df.Odd_D <= 7.00) & 
                           (df.Odd_A >= 1.30) & (df.Odd_A <= 1.80))
            df = df[flt_MO_Away]
            df = drop_reset_index(df)
            
            if placar == '0 x 0':
            
              df['0x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 0) else 0, axis=1)
              
              df.loc[(df['0x0'] == 0), 'Profit'] = 1 / (df['Odd_0x0'] + 5)
              df.loc[(df['0x0'] == 1), 'Profit'] = -1

            if placar == '0 x 1':

                df['0x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['0x1'] == 0), 'Profit'] = 1 / (df['Odd_0x1'] + 5)
                df.loc[(df['0x1'] == 1), 'Profit'] = -1

            if placar == '0 x 2':

                df['0x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['0x2'] == 0), 'Profit'] = 1 / (df['Odd_0x2'] + 5)
                df.loc[(df['0x2'] == 1), 'Profit'] = -1

            if placar == '0 x 3':

                df['0x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 0 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['0x3'] == 0), 'Profit'] = 1 / (df['Odd_0x3'] + 5)
                df.loc[(df['0x3'] == 1), 'Profit'] = -1

            if placar == '1 x 0':

                df['1x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 0) else 0, axis=1)
                
                df.loc[(df['1x0'] == 0), 'Profit'] = 1 / (df['Odd_1x0'] + 5)
                df.loc[(df['1x0'] == 1), 'Profit'] = -1

            if placar == '1 x 1':

                df['1x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['1x1'] == 0), 'Profit'] = 1 / (df['Odd_1x1'] + 5)
                df.loc[(df['1x1'] == 1), 'Profit'] = -1

            if placar == '1 x 2':

                df['1x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['1x2'] == 0), 'Profit'] = 1 / (df['Odd_1x2'] + 5)
                df.loc[(df['1x2'] == 1), 'Profit'] = -1

            if placar == '1 x 3':

                df['1x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 1 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['1x3'] == 0), 'Profit'] = 1 / (df['Odd_1x3'] + 5)
                df.loc[(df['1x3'] == 1), 'Profit'] = -1

            if placar == 'Goleada Home':

                df['Goleada_H'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] >= 4 and row['Goals_H_FT'] > row['Goals_A_FT']) else 0, axis=1)
                
                df.loc[(df['Goleada_H'] == 0), 'Profit'] = 0.025
                df.loc[(df['Goleada_H'] == 1), 'Profit'] = -1

            if placar == 'Goleada Away':

                df['Goleada_A'] = df.apply(lambda row: 1 if (row['Goals_A_FT'] >= 4 and row['Goals_A_FT'] > row['Goals_H_FT']) else 0, axis=1)
                
                df.loc[(df['Goleada_A'] == 0), 'Profit'] = 0.025
                df.loc[(df['Goleada_A'] == 1), 'Profit'] = -1

            if placar == '2 x 0':

                df['2x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 0) else 0, axis=1)
                
                df.loc[(df['2x0'] == 0), 'Profit'] = 1 / (df['Odd_2x0'] + 5)
                df.loc[(df['2x0'] == 1), 'Profit'] = -1

            if placar == '2 x 1':

                df['2x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['2x1'] == 0), 'Profit'] = 1 / (df['Odd_2x1'] + 5)
                df.loc[(df['2x1'] == 1), 'Profit'] = -1

            if placar == '2 x 2':

                df['2x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['2x2'] == 0), 'Profit'] = 1 / (df['Odd_2x2'] + 5)
                df.loc[(df['2x2'] == 1), 'Profit'] = -1

            if placar == '2 x 3':

                df['2x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 2 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['2x3'] == 0), 'Profit'] = 1 / (df['Odd_2x3'] + 5)
                df.loc[(df['2x3'] == 1), 'Profit'] = -1 

            if placar == '3 x 0':

                df['3x0'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 0) else 0, axis=1)
                
                df.loc[(df['3x0'] == 0), 'Profit'] = 1 / (df['Odd_3x0'] + 5)
                df.loc[(df['3x0'] == 1), 'Profit'] = -1

            if placar == '3 x 1':

                df['3x1'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 1) else 0, axis=1)
                
                df.loc[(df['3x1'] == 0), 'Profit'] = 1 / (df['Odd_3x1'] + 5)
                df.loc[(df['3x1'] == 1), 'Profit'] = -1

            if placar == '3 x 2':

                df['3x2'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 2) else 0, axis=1)
                
                df.loc[(df['3x2'] == 0), 'Profit'] = 1 / (df['Odd_3x2'] + 5)
                df.loc[(df['3x2'] == 1), 'Profit'] = -1

            if placar == '3 x 3':

                df['3x3'] = df.apply(lambda row: 1 if (row['Goals_H_FT'] == 3 and row['Goals_A_FT'] == 3) else 0, axis=1)
                
                df.loc[(df['3x3'] == 0), 'Profit'] = 1 / (df['Odd_3x3'] + 5)
                df.loc[(df['3x3'] == 1), 'Profit'] = -1           

        
        # Aplicar filtros de odds
        for odd_type, limits in odd_limits.items():
            df = df[(df[odd_type] >= limits['min']) & (df[odd_type] <= limits['max'])]

        return df
    
    if st.button('Executar Backtest'):
        # Inicializa um dicionário vazio para os limites das odds selecionadas
        odd_limits = {}
        
        # Percorre cada seleção do usuário e adiciona ao dicionário odd_limits apenas se a coluna foi selecionada
        for coluna, is_selected in user_selections.items():
            if is_selected:
                odd_limits[coluna] = {
                    'min': valores_input[f'{coluna}_Min'],
                    'max': valores_input[f'{coluna}_Max']
                }
        
        # Calcula o profit baseado na estratégia selecionada e nos filtros de odds
        df_filtrado = calcular_profit(df0, backtestes, backtestes2, odd_limits)
        
        try:
            
            # Crie uma nova coluna no dataframe filtrado com o profit acumulado
            df_filtrado['Profit_acu'] = df_filtrado.Profit.cumsum()
            df_filtrado = df_filtrado.dropna()
            df_filtrado = df_filtrado.reset_index(drop=True)
            df_filtrado.index += 1
            profit = round(df_filtrado.Profit_acu.tail(1).item(),2)
            ROI = round((df_filtrado.Profit_acu.tail(1)/len(df_filtrado)*100).item(),2)
            
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



        


        odd_limits = {}
        for coluna, is_selected in user_selections.items():
            if is_selected:
                # Para as ligas selecionadas, o tratamento é diferente
                if coluna == 'selected_leagues':
                    odd_limits[coluna] = valores_input[coluna]
                else:
                    odd_limits[coluna] = {
                        'min': valores_input[f'{coluna}_Min'],
                        'max': valores_input[f'{coluna}_Max']
                    }

        def gerar_string_filtro(ranges_de_odds):
            conteudo_arquivo = ""
            for chave, valor in ranges_de_odds.items():
                if isinstance(valor, dict):  # Se o valor for um dicionário (para min e max)
                    linha = f"{chave}: Min={valor['min']}, Max={valor['max']}\n"
                elif isinstance(valor, list):  # Se o valor for uma lista (para as ligas selecionadas)
                    ligas = ", ".join(valor)  # Transforma a lista em uma string separada por vírgulas
                    linha = f"{chave}: {ligas}\n"
                else:  # Para valores que não são nem dicionário nem lista (caso existam)
                    linha = f"{chave}: {valor}\n"
                conteudo_arquivo += linha
            return conteudo_arquivo

        odd_limits['selected_leagues'] = selected_leagues
        # Exemplo de uso com odd_limits (ajustar conforme o nome da sua variável para os limites)
        conteudo_filtro = gerar_string_filtro(odd_limits)

        # Supondo que você esteja usando o Streamlit, aqui está o botão para download
        st.download_button(
            label="Download Filtros",
            data=conteudo_filtro,
            file_name="filtros.txt",
            mime="text/plain"
            )

    # st.write("Backtest concluído!")





        

        
