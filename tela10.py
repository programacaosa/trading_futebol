from futpythontrader import *
from leagues import *
from rename import *

def show_tela10():
    st.title("Luke v2.1")
    st.header("Filtros Backtesting")

    dia = st.date_input("Data de Análise", date.today())

    @st.cache_data
    def load_data_betfair(dia):
        betfair_url = f'https://github.com/futpythontrader/YouTube/raw/main/Jogos_do_Dia/Betfair/Jogos_do_Dia_Betfair_Back_Lay_{dia}.csv'
        betfair = pd.read_csv(betfair_url)
        return betfair

        
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

    @st.cache_data
    def load_data_base():

        base_luke = pd.read_csv('https://github.com/futpythontrader/YouTube/raw/main/Bases_de_Dados/FlashScore/Base_de_Dados_FlashScore_Backtesting_Luke.csv')
        return base_luke

    df = load_data_base()  
     

    base_H = df[['Home','Ind_Efi_H','CV_IF_H','Coe_Efi_H','CV_CE_H','Media_Ptos_H','CV_Ptos_H',
                 'Media_GM_H','CV_GM_H','Media_GS_H','CV_GS_H','Media_SG_H','CV_SG_H']]

    base_A = df[['Away','Ind_Efi_A','CV_IF_A','Coe_Efi_A','CV_CE_A','Media_Ptos_A','CV_Ptos_A',
                 'Media_GM_A','CV_GM_A','Media_GS_A','CV_GS_A','Media_SG_A','CV_SG_A']]

    ultima_base_H = base_H.groupby('Home').last().reset_index()
    ultima_base_A = base_A.groupby('Away').last().reset_index()

    df0 = pd.merge(betfair, ultima_base_H, how='left', left_on='Home', right_on='Home')
    df0 = pd.merge(df0, ultima_base_A, how='left', left_on='Away', right_on='Away')

    df0 = drop_reset_index(df0)
    
    def aplicar_filtros(df_jogos, filtro_texto):
        linhas = filtro_texto.strip().split('\n')
        
        for linha in linhas:
            partes = linha.split(':')
            chave = partes[0].strip()
            valor = partes[1].strip()
            
            if chave == 'selected_leagues':
                if valor != "Todas as Ligas":
                    # Aplica o filtro somente para a liga especificada
                    df_jogos = df_jogos[df_jogos['League'] == valor]
            else:
                # Para outros tipos de filtros numéricos
                min_max_partes = valor.split(',')
                minimo = float(min_max_partes[0].split('=')[1].strip())
                maximo = float(min_max_partes[1].split('=')[1].strip())
                df_jogos = df_jogos[(df_jogos[chave] >= minimo) & (df_jogos[chave] <= maximo)]
        
        return df_jogos

    st.write("Por favor, faça o upload do arquivo de filtros.")

    uploaded_file = st.file_uploader("Escolha o arquivo de filtros", type=['txt'])


    if uploaded_file is not None:
        filtro_texto = uploaded_file.getvalue().decode('utf-8')
        st.write("Filtros carregados com sucesso:")
        st.text(filtro_texto)
        
        df_jogos_filtrados = aplicar_filtros(df0, filtro_texto)
        st.write("Entradas:")
        df_jogos_filtrados = drop_reset_index(df_jogos_filtrados)
        st.dataframe(df_jogos_filtrados)

        def download_excel():
                output = BytesIO()
                writer = pd.ExcelWriter(output, engine='xlsxwriter')
                df_jogos_filtrados.to_excel(writer, index=False, sheet_name='Sheet1')
                writer.close()
                processed_data = output.getvalue()
                return processed_data

        # Cria o botão de download
        button = st.download_button(
            label='Download Entradas',
            data=download_excel(),
            file_name=f'Entradas_{dia}.xlsx',
            mime='application/vnd.ms-excel')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    