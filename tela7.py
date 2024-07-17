from futpythontrader import *
from leagues import *
from rename import *

def show_tela7():
    
    st.title("Luke v2.1")
    st.header("Base de Dados")
    
    # dia = st.date_input("Data de Análise", date.today())

    @st.cache_data
    def load_data_base():

        base_luke = pd.read_csv('https://github.com/futpythontrader/YouTube/raw/main/Bases_de_Dados/FlashScore/Base_de_Dados_FlashScore_v2.csv')
        return base_luke

    df = load_data_base()
    df = drop_reset_index(df)

    # Ordenar a lista de ligas por ordem alfabética 
    sorted_leagues = sorted(df['League'].unique())
    sorted_leagues.insert(0, "Todas as Ligas")
    selected_leagues = st.multiselect('Filtrar por Liga:', sorted_leagues, default="Todas as Ligas")

    # Ordenar a lista de temporadas por ordem alfabética 
    sorted_seasons = sorted(df['Season'].unique())
    sorted_seasons.insert(0, "Todas as Temporadas")
    selected_seasons = st.multiselect('Filtrar por Temporada:', sorted_seasons, default="Todas as Temporadas")

    # Aplicar os filtros selecionados ao DataFrame original 
    filtered_df = df.copy()
    if "Todas as Ligas" not in selected_leagues:
        filtered_df = filtered_df[filtered_df['League'].isin(selected_leagues)]

    if "Todas as Temporadas" not in selected_seasons:
        filtered_df = filtered_df[filtered_df['Season'].isin(selected_seasons)]

    # Verificar se o DataFrame filtrado não está vazio 
    if filtered_df.empty:
        st.warning("Nenhum dado encontrado para os filtros selecionados.")
    else:
        # Selecionar apenas as colunas desejadas
        base_full = filtered_df[['Date','Time','League','Season','Round','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H','Goals_A',
                                    'Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_Under25',
                                    'Odd_BTTS_Yes','Odd_BTTS_No','Goals_Minutes_Home','Goals_Minutes_Away']]
        # Renomear as colunas do DataFrame
        df0 = base_full.copy()
        df0 = df0[['Date','League','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A']]
        # Converter as colunas 'HT_Goals_H', 'HT_Goals_A', 'FT_Goals_H' e 'FT_Goals_A' para o tipo inteiro
        df0['Goals_H'] = df0['Goals_H'].astype(int)
        df0['Goals_A'] = df0['Goals_A'].astype(int)
        # Converter as colunas 'Odd_H', 'Odd_D', 'Odd_A', 'Odd_Over25', 'Odd_Under25' e 'Odd_BTTS_Yes' para float e formatar para duas casas decimais
        df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
        df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
        df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)

        df0 = df0.dropna()
        df0 = df0.reset_index(drop=True)
        df0.index += 1
        st.dataframe(df0)

        # Define a função que retorna a planilha em formato XLSX
        def download_excel():
            output = BytesIO()
            writer = pd.ExcelWriter(output, engine='xlsxwriter')
            base_full.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.close()
            processed_data = output.getvalue()
            return processed_data

        # Cria o botão de download
        button = st.download_button(
            label='Download',
            data=download_excel(),
            file_name=f'Luke_Bases_de_Dados.xlsx',
            mime='application/vnd.ms-excel'
        )


