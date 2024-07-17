from futpythontrader import *
from pathlib import Path

########## Importando as Bibliotecas ##########

# from x_futpythontrader_x import *
# from x_rename_leagues_x import *
# from x_rename_teams_Betfair_Flashscore_x import *
# from io import BytesIO
# import plotly.graph_objects as go
# import streamlit_authenticator as stauth

########## Criação do Aplicativo ##########

st.set_page_config(
        page_title = "Luke", layout="wide"
    )

########## User Authenticator ##########

names = ["Alexandre Silva", "Christian Farina", "Leandro Filho", "Geraldo", "Luiz Uchoa", "Leandra Palma",
"Thiago Rodrigues",
"Anderson Castro",
"Renato do Nascimento",
"Fernando Henrique",
"Vinicius Tardelli",
"Saulo Senna",
"Gilson Paulino",
"Diego Brunelli",
"Nettuno",
"Theo Borges",
"Tiquinho",
# "Alessandro Minutti",
"Anderson Salvi",
"Janeilson José",
"Wilian Malaquias",
"Iago Maia",
"Rodrigo Giannoni",
"Alyson David",
"Rayson Bernardo",
"Dirso Ament",
"Wanderson Silva",
"Maicon Texeira",
"Pedro Bastos",
"Yuichi Kobayashi",
"Geraldo Pereira",
"Daniel Bragança",
"Eduardo Rubik",
"Aurelio Felicio",
"Ronie Araujo",
"Rafael Cavalcante",
"Anderson Salvi",
"Willyan Ribeiro",
"Mozer Barreto",
"João Marcelo Farina",
"Marcelo Cavalcanti",
"Rapha Ferreira",
"Aurelio Felicio",
# "Giovani da Costa",
"Marcelo Cruz",
"Herbert Chagas",
"Mauro Pedro",
"Thalia Alves",
# "Claudir Jr Martins",
"Giovane Larangeira",
"Marcão",
"Jose Alberto",
"Alex Lima",
"Andre Muzzo",
"Nicson Silva",
"Pedro Raso",
"Ivson Alves",
"Rafael Ferreyro",
"Rodrigo Bonotto",
"Aurelio Felicio",
"Tiago Passos",
"Cleilson Bezerra",
"Yuri Moura",
"Robson Moraes",
"Paulo Roque",
"Michell Silva",
"Dario Medeiros",
"Deivid Santana",
"Felipe Silva",
"Ivan Bianzeno",
"Marcello Murakami",
"Francisco Teixeira",
"Diefferson Juarez",
# "Moises Sousa",
# "Jhonatan Vargas",
# "Luis Antonio",
"Michael Eudes",
"Hiam Costa",
"Alexandre Nemetz",
"Johannes Van leeuwen",
"Bruno Quatrochi",
"Gercina Veloso",
"Lucas Oliveira",
"Edson da Silva",
"Rafael Trevizani",
"Oscar Mouriño",
"Leonardo Barbosa",
"Leonardo Dambrós",
"Juliane Borges",
"Rondinei Machado",
"Marco Gil Morais",
"Carlos Santos",
"Wesley Penido",
"Maicon Texeira",
"Leonardo Leite",
"Paulo Dallabona",
"Rafael Lopez",
"Daniel Carvalho",
"Mendonça Bezerra",
"Henrique França",
"Breno Barbedo",
"Fabio Costa",
"Mateus Hessel",
"Eduardo Hugo",
"Tiago Moullim",
"Abel Thiago",
"Casio Rabello",
"Wasley Both",
"Edmundo Luna",
"Leandro Maciel",
# "Get Up Trading",
"Leandro Vinicius",
"Thyago Danilo",
"Marcos Castro",
"Diego Rangel",
"Alan Pereira",
"Renato Vieira",
"Bruno Henrique",
"Cleyton Ruiz",
"Lucio Silva",
"Jaime Costa",
"Jonathan Gomes",
"Rafael Collaço",
"Danilo Fuentes",
"Luciane Gonçalves",
"Lucas Araujo",
"Ivan Ferrari",
"Ricardo Filho"]

usernames = ["alexandre", "christian", "leandro", "geraldo", "luiz", "leandra",
"thiago_rodrigues",
"anderson_castro",
"renato_do_nascimento",
"fernando_henrique",
"vinicius_tardelli",
"saulo_senna",
"gilson_paulino",
"diego_brunelli",
"nettuno",
"theo_borges",
"tiquinho",
# "alessandro_minutti",
"anderson_salvi",
"janeilson_jose",
"wilian_malaquias",
"iago_maia",
"rodrigo_giannoni",
"alyson_david",
"rayson_bernardo",
"dirso_ament",
"wanderson_silva",
"maicon_texeira",
"pedro_bastos",
"@Yuichi1998",
"@geraldojhpereira",
"@DanielBraganca",
"eduardo_rubik",
"aurelio_felicio",
"ronie_araujo",
"rafael_cavalcante",
"anderson_salvi",
"willyan_ribeiro",
"mozer_barreto",
"jmfarina",
"marcelo_cavalcanti",
"rapha_ferreira",
"aurelio_felicio",
# "giovani_costa",
"marcelo_cruz",
"herbert_chagas",
"mauro_pedro",
"thalia_alves",
# "claudir_martins",
"giovane_larangeira",
"marcao",
"jose_alberto",
"alex_lima",
"AndreMuzzo",
"NicsonSilva",
"PedroRaso",
"IvsonAlves",
"RafaelFerreyro",
"RodrigoBonotto",
"AurelioFelicio",
"TiagoPassos",
"CleilsonBezerra",
"YuriMoura",
"RobsonMoraes",
"PauloRoque",
"MichellSilva",
"DarioMedeiros",
"DeividSantana",
"FelipeSilva",
"IvanBianzeno",
"MarcelloMurakami",
"FranciscoTeixeira",
"DieffersonJuarez",
# "MoisesSousa",
# "JhonatanVargas",
# "LuisAntonio",
"MichaelEudes",
"HiamCosta",
"AlexandreNemetz",
"Johannes",
"BrunoQuatrochi",
"GercinaVeloso",
"LucasOliveira",
"EdsonSilva",
"RafaelTrevizani",
"OscarMourino",
"LeonardoBarbosa",
"LeonardoDambros",
"JulianeBorges",
"RondineiMachado",
"MarcoGilMorais",
"CarlosSantos",
"WesleyPenido",
"MaiconTexeira",
"LeonardoLeite",
"PauloDallabona",
"RafaelLopez",
"DanielCarvalho",
"MendonçaBezerra",
"HenriqueFrança",
"BrenoBarbedo",
"FabioCosta",
"MateusHessel",
"EduardoHugo",
"TiagoMoullim",
"AbelThiago",
"CasioRabello",
"WasleyBoth",
"EdmundoLuna",
"LeandroMaciel",
# "GetUpTrading",
"LeandroVinicius",
"ThyagoDanilo",
"MarcosCastro",
"DiegoRangel",
"AlanPereira",
"RenatoVieira",
"BrunoHenrique",
"CleytonRuiz",
"LucioSilva",
"JaimeCosta",
"JonathanGomes",
"RafaelCollaco",
"DaniloFuentes",
"LucianeGoncalves",
"LucasAraujo",
"IvanFerrari",
"RicardoFilho"]    
  

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=5)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Usuario ou Senha estão errados.")

if authentication_status == None:
    st.warning("Por favor insira seu nome de Usuário e Senha")
    st.write("Se ainda não é assinante [clique aqui](https://hub.la/g/P863owYDtnjS1X064ugB).")

if authentication_status: 
    st.sidebar.image('logo.jpg', width=250)
    st.sidebar.subheader(f"Welcome {name}")
    st.sidebar.subheader(f"Luke Software\n by @FutPythonTrader and \n @GetUpTrading")











































    

    #################################################
    ################# Jogos do Dia ##################
    #################################################
    
    def jogos_do_dia():
        
        st.header("Luke")
        st.subheader("Jogos do Dia")

        dia = st.date_input(
            "Data de Análise",
            date.today())

        ########## Importando os Jogos do Dia ########## 
        def load_data_jogos():
            key = "20e2d4aa7479a657c52935c4a743a626941b0a1f41b12156642dd7b62d893145"

            url1 = f"https://api.football-data-api.com/todays-matches?key={key}&date={dia}&page=1"
            data1 = requests.get(url1)
            resp = data1.json()['data']
            dados1 = pd.DataFrame.from_dict(resp)

            url2 = f"https://api.football-data-api.com/todays-matches?key={key}&date={dia}&page=2"
            data2 = requests.get(url2)
            resp = data2.json()['data']

            dados2 = pd.DataFrame.from_dict(resp)

            data_jogos = pd.concat([dados1, dados2],ignore_index=True)

            return data_jogos

        df_jogos = load_data_jogos()

        try:
        
            df_jogos = df_jogos[['competition_id','season','date_unix','game_week','home_name','away_name','odds_ft_1','odds_ft_x','odds_ft_2','odds_ft_over25','odds_ft_under25','odds_btts_yes','odds_btts_no','team_a_xg_prematch', 'team_b_xg_prematch', 'total_xg_prematch']]
            df_jogos.columns = ['League','Season','Date','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No','xG_Home_Pre', 'xG_Away_Pre', 'xG_Total_Pre']
            df_jogos['Date'] = pd.to_datetime(df_jogos['Date'], unit='s') - pd.DateOffset(hours=3)
            df_jogos = df_jogos.dropna()
            df_jogos['Date'] = df_jogos['Date'].astype('str')
            df_jogos[['Date2','Time']] = df_jogos['Date'].str.split(' ',expand=True)
            df_jogos = df_jogos[['League','Season','Date2','Time','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No','xG_Home_Pre', 'xG_Away_Pre', 'xG_Total_Pre']]
            df_jogos.columns = ['League','Season','Date','Time','Rodada','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_Under25','Odd_BTTS_Yes','Odd_BTTS_No','xG_Home_Pre', 'xG_Away_Pre', 'xG_Total_Pre']
            flt = df_jogos.Date == str(dia)
            jogos_footystats = df_jogos[flt]
            jogos_footystats = drop_reset_index(jogos_footystats)

            rename_leagues_footystats(jogos_footystats)
            rename_leagues_footystats_flashscore(jogos_footystats)
            jogos_footystats = jogos_footystats[jogos_footystats['League'].isin(['Russia Russian Premier League']) == False]
            jogos_footystats = drop_reset_index(jogos_footystats)
            jogos_do_dia = jogos_footystats[['League','Season','Date','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes','xG_Home_Pre','xG_Away_Pre','xG_Total_Pre']]
            rename_teams_footystats_flashscore(jogos_do_dia)

            def load_data_betfair():

                betfair = pd.read_csv(f'https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_Betfair/{dia}_Jogos_do_Dia.csv?raw=true')

                return betfair
        
            try:
                betfair = load_data_betfair()
                rename_leagues(betfair)
                rename_teams(betfair)
                betfair = betfair[['League','Home','Away',
                'CS_0x0','CS_0x1','CS_0x2','CS_0x3',
                'CS_1x0','CS_1x1','CS_1x2','CS_1x3',
                'CS_2x0','CS_2x1','CS_2x2','CS_2x3',
                'CS_3x0','CS_3x1','CS_3x2','CS_3x3',
                'CS_Goleada_H','CS_Goleada_A','ID_Evento','IDMercado']]
                betfair.columns = ['League','Home','Away',
                'Odd_0x0','Odd_0x1','Odd_0x2','Odd_0x3',
                'Odd_1x0','Odd_1x1','Odd_1x2','Odd_1x3',
                'Odd_2x0','Odd_2x1','Odd_2x2','Odd_2x3',
                'Odd_3x0','Odd_3x1','Odd_3x2','Odd_3x3',
                'Odd_Goleada_H','Odd_Goleada_A','ID_Evento','IDMercado']
            
                Jogos = jogos_do_dia.merge(betfair, on=['League','Home','Away'])
                Jogos = drop_reset_index(Jogos)
                jogos_rounded = Jogos.round(2)
                jogos_rounded = jogos_rounded[['League','Season','Date','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes','xG_Home_Pre','xG_Away_Pre','xG_Total_Pre']]
                st.dataframe(jogos_rounded)
            
                def download_excel():
                    output = BytesIO()
                    writer = pd.ExcelWriter(output, engine='xlsxwriter')
                    Jogos.to_excel(writer, index=False, sheet_name='Sheet1')
                    writer.save()
                    processed_data = output.getvalue()
                    return processed_data

                button = st.download_button(
                    label='Download',
                    data=download_excel(),
                    file_name=f'Luke_Jogos_do_Dia_{dia}.xlsx',
                    mime='application/vnd.ms-excel'
                )
            except:
                # st.dataframe(jogos_do_dia)
                pass
        except:
            st.write("Jogos desse dia não disponíveis.")
        
        



















              
        
        
        

        





















































    #################################################
    ################# Favorito Home #################
    #################################################
    def favorito_home():

        st.title("Luke")
        st.header("Favorito Home")
        
        dia = st.date_input(
            "Data de Análise",
            date.today())  

        ########## Importando os Jogos do Dia ##########   
        ########## Importando os Jogos do Dia ########## 
        def load_data_jogos():
            key = "20e2d4aa7479a657c52935c4a743a626941b0a1f41b12156642dd7b62d893145"

            url1 = f"https://api.football-data-api.com/todays-matches?key={key}&date={dia}&page=1"
            data1 = requests.get(url1)
            resp = data1.json()['data']
            dados1 = pd.DataFrame.from_dict(resp)

            url2 = f"https://api.football-data-api.com/todays-matches?key={key}&date={dia}&page=2"
            data2 = requests.get(url2)
            resp = data2.json()['data']

            dados2 = pd.DataFrame.from_dict(resp)

            data_jogos = pd.concat([dados1, dados2],ignore_index=True)

            return data_jogos

        df_jogos = load_data_jogos()

        try:
        
            df_jogos = df_jogos[['competition_id','season','date_unix','game_week','home_name','away_name','odds_ft_1','odds_ft_x','odds_ft_2','odds_ft_over25','odds_ft_under25','odds_btts_yes','odds_btts_no','team_a_xg_prematch', 'team_b_xg_prematch', 'total_xg_prematch']]
            df_jogos.columns = ['League','Season','Date','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No','xG_Home_Pre', 'xG_Away_Pre', 'xG_Total_Pre']
            df_jogos['Date'] = pd.to_datetime(df_jogos['Date'], unit='s') - pd.DateOffset(hours=3)
            df_jogos = df_jogos.dropna()
            df_jogos['Date'] = df_jogos['Date'].astype('str')
            df_jogos[['Date2','Time']] = df_jogos['Date'].str.split(' ',expand=True)
            df_jogos = df_jogos[['League','Season','Date2','Time','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No','xG_Home_Pre', 'xG_Away_Pre', 'xG_Total_Pre']]
            df_jogos.columns = ['League','Season','Date','Time','Rodada','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_Under25','Odd_BTTS_Yes','Odd_BTTS_No','xG_Home_Pre', 'xG_Away_Pre', 'xG_Total_Pre']
            flt = df_jogos.Date == str(dia)
            jogos_footystats = df_jogos[flt]
            jogos_footystats = drop_reset_index(jogos_footystats)

            rename_leagues_footystats(jogos_footystats)
            rename_leagues_footystats_flashscore(jogos_footystats)
            jogos_footystats = jogos_footystats[jogos_footystats['League'].isin(['Russia Russian Premier League']) == False]
            jogos_footystats = drop_reset_index(jogos_footystats)
            jogos_do_dia = jogos_footystats[['League','Season','Date','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes','xG_Home_Pre','xG_Away_Pre','xG_Total_Pre']]
            rename_teams_footystats_flashscore(jogos_do_dia)

            def load_data_betfair():

                betfair = pd.read_csv(f'https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_Betfair/{dia}_Jogos_do_Dia.csv?raw=true')

                return betfair
        
            try:
                betfair = load_data_betfair()
                rename_leagues(betfair)
                rename_teams(betfair)
                betfair = betfair[['League','Home','Away',
                'CS_0x0','CS_0x1','CS_0x2','CS_0x3',
                'CS_1x0','CS_1x1','CS_1x2','CS_1x3',
                'CS_2x0','CS_2x1','CS_2x2','CS_2x3',
                'CS_3x0','CS_3x1','CS_3x2','CS_3x3',
                'CS_Goleada_H','CS_Goleada_A','ID_Evento','IDMercado']]
                betfair.columns = ['League','Home','Away',
                'Odd_0x0','Odd_0x1','Odd_0x2','Odd_0x3',
                'Odd_1x0','Odd_1x1','Odd_1x2','Odd_1x3',
                'Odd_2x0','Odd_2x1','Odd_2x2','Odd_2x3',
                'Odd_3x0','Odd_3x1','Odd_3x2','Odd_3x3',
                'Odd_Goleada_H','Odd_Goleada_A','ID_Evento','IDMercado']
            
                Jogos = jogos_do_dia.merge(betfair, on=['League','Home','Away'])
                Jogos = drop_reset_index(Jogos)

            except:
                st.dataframe(jogos_do_dia)
        except:
            st.write("Jogos desse dia não disponíveis.")
    

        try:
            df_jogos = Jogos
        
            ####################################
            ########## Filtro de Odds ##########
            ####################################
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                Odd_H_Min = st.number_input('Odd_H_Min', value=1.50, step=0.1)
                Odd_H_Max = st.number_input('Odd_H_Max', value=2.20, step=0.1)
            with col2:
                Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
                Odd_D_Max = st.number_input('Odd_D_Max', value=100.0, step=0.1)
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
            Odd_Min_Back_Fav = Odd_H_Min
            Odd_Max_Back_Fav = Odd_H_Max
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
            flt1 = ((df_jogos.Odd_H >= Odd_Min_Back_Fav) & (df_jogos.Odd_H <= Odd_Max_Back_Fav) & 
                    (df_jogos.Odd_D >= Odd_Min_Back_D) & (df_jogos.Odd_D <= Odd_Max_Back_D) & 
                    (df_jogos.Odd_A >= Odd_Min_Back_A) & (df_jogos.Odd_A <= Odd_Max_Back_A) & 
                    (df_jogos.Odd_Over25 >= Odd_Min_Over25) & (df_jogos.Odd_Over25 <= Odd_Max_Over25) & 
                    (df_jogos.Odd_BTTS_Yes >= Odd_Min_BTTS) & (df_jogos.Odd_BTTS_Yes <= Odd_Max_BTTS))
            df_H = df_jogos[flt1]
            df_H = df_H[['League','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]
            df_H = drop_reset_index(df_H)

            #############################
            ########## Análise ##########
            #############################

            # Criando a Lista com os Times
            lista_H = df_H["Home"].tolist()
            lista_HT = ['0x0','0x1','0x2','1x0','1x1','1x2','2x0','2x1','2x2','Goleada_HT']
            lista_FT = ['0x0','0x1','0x2','0x3','1x0','1x1','1x2','1x3','2x0','2x1','2x2','2x3','3x0','3x1','3x2','3x3','Goleada_H','Goleada_A']

            df_H2 = df_H[['League','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]
            df_H2.columns = ['League','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over','Odd_BTTS']
            
            df0 = df_H2.copy()
            df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
            df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
            df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)
            df0['Odd_Over'] = df0['Odd_Over'].astype(float).map('{:.2f}'.format)
            df0['Odd_BTTS'] = df0['Odd_BTTS'].astype(float).map('{:.2f}'.format)
            st.dataframe(df0)
        except:
            st.write("Jogos desse dia não disponíveis.")


        try:
        
            ################################################
            ########## Importando a Base de Dados ##########
            ################################################
            
            j1, j2, j3 = st.columns(3)
            selecao1 = j1.selectbox('Escolha o Mandante', lista_H) 
            selecao2 = j2.selectbox('Escolha o Placar FT', lista_FT)
            # selecao3 = j3.selectbox('Escolha o Placar FT', lista_FT)
            
            df_league = df_H[df_H.Home == selecao1].copy()
            liga = df_league.iat[0,0]

        except:
            pass

        try:

            df_Home = df_jogos[df_jogos.Home == selecao1].copy()
            zebra = df_Home.iat[0,5]
            home = selecao1
            away = zebra
            

            IDMercado = str(df_Home.iat[0,33])
            IDMercado = ajustar_id_mercado(IDMercado)
            st.write('')


            jogo = str(home +' x '+ away)
            # link = f'[{jogo}](https://www.betfair.com/exchange/plus/football/market/{IDMercado})'
            link1 = f'<div style="text-align:left"><a href="https://www.betfair.com/exchange/plus/football/market/{IDMercado}">{"Betfair"}</a></div>'
            link2 = f'<div style="text-align:left"><a href="https://bolsadeaposta.com/exchange/sport/1/market/{IDMercado}">{"Bolsa de Aposta"}</a></div>'
            link3 = f'<div style="text-align:left"><a href="https://fulltbet.com/exchange/sport/1/market/{IDMercado}">{"Fulltbet"}</a></div>'

            
            col1, col2, col3 = st.columns(3)

            with col2:
                texto = home + ' x ' + away
                st.write(texto, unsafe_allow_html=True)

            # st.text('')
            
            # st.write('')

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
        ########## Importando a Base de Dados ##########

        try:

            # @st.cache
            @st.cache_data
            def load_data_base():

                base_luke = pd.read_csv("./Bases/x_Luke_x.csv")
                
                return base_luke

            base = load_data_base()

                
            df = base[base['League'] == liga]
            
        except:
            pass
        
        
        try:
            df_f = df[(df['Home'] == selecao1)]
            df_filtrado = df_f[(df_f[selecao2] == 1)]
            df_filtrado = df_filtrado[['Season','Date','Home','Away','HT_Goals_H','HT_Goals_A','FT_Goals_H','FT_Goals_A','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','Odd_BTTS_Yes']]
            df_filtrado.columns = ['Season','Date','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H_FT','Goals_A_FT','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']
            df_filtrado = drop_reset_index(df_filtrado)
        except:
            pass    

        try:
            ################################################################################
            # Jogos anteriores Terminados no Placar Selecionado
            ################################################################################

            n_H = df_filtrado[df_filtrado.columns[0]].count()
            
            if n_H == 0:
                st.text("Não houve Jogos anteriores do " + selecao1 + " terminados em "+ selecao2)
            else:
                st.text("Jogos anteriores do " + selecao1 + " terminados em " + selecao2)
                df0 = df_filtrado.copy()
                # st.dataframe(df0)
                
                df0['Odd_H'] = df0['FT_Odd_H'].astype(float).map('{:.2f}'.format)
                df0['Odd_D'] = df0['FT_Odd_D'].astype(float).map('{:.2f}'.format)
                df0['Odd_A'] = df0['FT_Odd_A'].astype(float).map('{:.2f}'.format)
                df0['Odd_Over'] = df0['FT_Odd_Over25'].astype(float).map('{:.2f}'.format)
                df0['Odd_BTTS'] = df0['Odd_BTTS_Yes'].astype(float).map('{:.2f}'.format)
                df0 = df0[['Date','Season','Home','Away','FT_Goals_H','FT_Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over','Odd_BTTS']]
                df0.columns = ['Date','Season','Home','Away','FT_HG','FT_AG','Odd_H','Odd_D','Odd_A','Odd_Over','Odd_BTTS']
                df0.reset_index(inplace=True, drop=True)
                df0.index = df0.index.set_names(['Nº'])
                df0 = df0.rename(index=lambda x: x + 1)
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
            df_10_jogos_A = df_H[df_H.Home == selecao1].copy()
            zebra = df_10_jogos_A.iat[0,3]
            df_sing_2anos_H = df[df.Home == selecao1].copy()
            df_sing_2anos_A = df[df.Away == zebra].copy()
            df_sing_2anos_H = df_sing_2anos_H[df_sing_2anos_H[selecao2] == 1]
            df_sing_2anos_A = df_sing_2anos_A[df_sing_2anos_A[selecao2] == 1]
            n_sing_2anos_H = df_sing_2anos_H[df_sing_2anos_H.columns[0]].count()
            n_sing_2anos_A = df_sing_2anos_A[df_sing_2anos_A.columns[0]].count()
            ###
            #st.text("2 anos H")
            #st.dataframe(df_sing_2anos_H)
            #st.text("2 anos A")
            #st.dataframe(df_sing_2anos_A)
            df_sing_10jogos = df[df.Home == selecao1].copy()
            df_sing_10jogos = df_sing_10jogos[df_sing_10jogos.Away == zebra]
            # df_sing_10jogos = df_sing_10jogos.tail(10)
            df_sing_10jogos = df_sing_10jogos[df_sing_10jogos[selecao2] == 1]
            #st.text("10 jogos 1 x 2")
            #st.dataframe(df_sing_10jogos)
            ###
            n_sing_10jogos = df_sing_10jogos[df_sing_10jogos.columns[0]].count()
            if ((n_sing_2anos_H < 1) & (n_sing_2anos_A < 1) & (n_sing_10jogos < 1)):
                st.text("Este Placar é SINGULAR")
            st.markdown('---') 
        except:
            st.markdown('---')


        try:
            ################################################################################
            # Odd Média do Time
            ################################################################################    
            df2_H = df[df.Home == selecao1]
            porcentagem_team_H = n_H / len(df2_H)
            odd_team_H = round((1 / porcentagem_team_H),2)
            if len(df2_H) != 0:
                if odd_team_H != np.inf:
                    st.text("A Odd Média do " + selecao2 + " do " + selecao1 + " é: " + str((odd_team_H)))
                else:
                    st.text("A Odd Média do " + selecao2 + " do " + selecao1 + " é: 1000")
            else:
                pass
        
        except:
            pass

        try:        
            ################################################################################
            # Odd Média da Liga
            ################################################################################

            df_league = df_H[df_H.Home == selecao1].copy()
            
            liga = df_league.iat[0,0] 
            
            try:
                df_liga = df[df['League'] == liga]
                                
                df_liga2 = df_liga[df_liga[selecao2] == 1]
                n_liga = df_liga2[df_liga2.columns[0]].count()
                porcentagem_liga = n_liga / len(df_liga)
                odd_liga = round((1 / porcentagem_liga),2)
                
                if odd_liga != np.inf:
                    st.text("A Odd Média do " + selecao2 + " da Liga " + liga + " é: " + str((odd_liga)))
                else:
                    st.text("A Odd Média do " + selecao2 + " da Liga " + liga + " é: 1000")
            except:
                pass
        
        except:
            pass


        try:
            ################################################################################
            # Odd Atual na Betfair
            ################################################################################

            try:
                odd_atual = df_Home[df_Home.Home == selecao1].copy()
                placar = 'Odd_'+ selecao2
                odd_betfair = odd_atual[placar].tail(1).item()
                st.text("Odd Atual do Lay " + selecao2 + " do " + selecao1 + " na Betfair é: " + str(odd_betfair))
                st.markdown('---') 
            except:
                st.markdown('---') 

        except:
            st.markdown('---')

        
        try:
            ################################################################################
            # Custo do Gol
            ################################################################################
            st.text("Índice de Eficiência")

            lista_per = [5, 10, 20]
            p1,p2,p3,p4,p5 = st.columns(5)
            n_per = p1.selectbox('Número de Períodos', lista_per)

            tt = df.copy()
 
            try:
                # Probabilidades
                tt['p_H'] = 1 / tt.FT_Odd_H
                tt['p_D'] = 1 / tt.FT_Odd_D
                tt['p_A'] = 1 / tt.FT_Odd_A

                # n_per = 5

                # Custo do Gol 1.0
                tt['CG_01_H'] = tt.FT_Goals_H / tt.p_H
                tt['CG_01_A'] = tt.FT_Goals_A / tt.p_A

                tt['Media_CG_01_H'] = tt.groupby('Home')['CG_01_H'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)
                tt['Media_CG_01_A'] = tt.groupby('Away')['CG_01_A'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)

                tt['Media_CG_01_H'] = tt.groupby('Home')['Media_CG_01_H'].shift(1)
                tt['Media_CG_01_A'] = tt.groupby('Away')['Media_CG_01_A'].shift(1)

                tt['DesvPad_CG_01_H'] = tt.groupby('Home')['CG_01_H'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)
                tt['DesvPad_CG_01_A'] = tt.groupby('Away')['CG_01_A'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)

                tt['DesvPad_CG_01_H'] = tt.groupby('Home')['DesvPad_CG_01_H'].shift(1)
                tt['DesvPad_CG_01_A'] = tt.groupby('Away')['DesvPad_CG_01_A'].shift(1)

                tt['CV_CG_01_H'] = tt['DesvPad_CG_01_H'] / tt['Media_CG_01_H']
                tt['CV_CG_01_A'] = tt['DesvPad_CG_01_A'] / tt['Media_CG_01_A']

                # Custo do Gol 2.0
                tt['CG_02_H'] = (tt.p_H / 2) + (tt.FT_Goals_H / 2)
                tt['CG_02_A'] = (tt.p_A / 2) + (tt.FT_Goals_A / 2)

                tt['Media_CG_02_H'] = tt.groupby('Home')['CG_02_H'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)
                tt['Media_CG_02_A'] = tt.groupby('Away')['CG_02_A'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)

                tt['Media_CG_02_H'] = tt.groupby('Home')['Media_CG_02_H'].shift(1)
                tt['Media_CG_02_A'] = tt.groupby('Away')['Media_CG_02_A'].shift(1)

                tt['DesvPad_CG_02_H'] = tt.groupby('Home')['CG_02_H'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)
                tt['DesvPad_CG_02_A'] = tt.groupby('Away')['CG_02_A'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)

                tt['DesvPad_CG_02_H'] = tt.groupby('Home')['DesvPad_CG_02_H'].shift(1)
                tt['DesvPad_CG_02_A'] = tt.groupby('Away')['DesvPad_CG_02_A'].shift(1)

                tt['CV_CG_02_H'] = tt['DesvPad_CG_02_H'] / tt['Media_CG_02_H']
                tt['CV_CG_02_A'] = tt['DesvPad_CG_02_A'] / tt['Media_CG_02_A']

                ttt = df_jogos[df_jogos.Home == selecao1].copy()
                zebra = ttt.iat[0,5]
                home = selecao1
                away = zebra

                cg_h = tt[tt.Home == home].tail(1)
                media_cg_h = cg_h.iat[0,42]

                cv_cg_h = tt[tt.Home == home].tail(1)
                cv_h = cv_cg_h.iat[0,46]

                cg_a = tt[tt.Away == away].tail(1)
                media_cg_a = cg_a.iat[0,43]

                cv_cg_a = tt[tt.Away == away].tail(1)
                cv_a = cv_cg_a.iat[0,47]
                
                st.text('') 
                
                st.text(f'Índice de Eficiência (Coeficiente de Eficiência) - Ultimos {n_per} Jogos')
                
                # st.dataframe(cg_h) 
                # st.dataframe(cg_a) 
                st.text(f'{home} - CG: {round(media_cg_h,2)}, CV: {round(cv_h,2)}')
                st.text(f'{away} - CG: {round(media_cg_a,2)}, CV: {round(cv_a,2)}')

                cg_h2 = tt[tt.Home == home].tail(1)
                media_cg_h2 = cg_h2.iat[0,50]

                cv_cg_h2 = tt[tt.Home == home].tail(1)
                cv_h2 = cv_cg_h2.iat[0,54]

                cg_a2 = tt[tt.Away == away].tail(1)
                media_cg_a2 = cg_a2.iat[0,51]

                cv_cg_a2 = tt[tt.Away == away].tail(1)
                cv_a2 = cv_cg_a2.iat[0,55]
            
                st.text('')
                st.text('')
                st.text(f'Índice de Eficiência (Quociente de Eficiência) - Ultimos {n_per} Jogos')
                
                # st.dataframe(cg_h2) 
                # st.dataframe(cg_a2) 
                st.text(f'{home} - CG: {round(media_cg_h2,2)}, CV: {round(cv_h2,2)}')
                st.text(f'{away} - CG: {round(media_cg_a2,2)}, CV: {round(cv_a2,2)}')





                st.markdown('---')
            except:
                st.markdown('---') 

        except:
            st.markdown('---')





        try:
            ################################################################################
            # Análise Poseidon Home
            ################################################################################


            try:
                odd_atual = df_Home[df_Home.Home == selecao1].copy()
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

                st.text("Odds Correct Score Pré-Live")
                st.text("")

                odds1, odds2, odds3, odds4 = st.columns(4)

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

                st.text("")

                Ponta1 = odd_betfair_2x0 < odd_betfair_1x0
                Ponta2 = odd_betfair_2x0 < odd_betfair_1x1
                Ponta3 = odd_betfair_2x2 < odd_betfair_1x2
                
                # Condição Poseidon
                if ((Ponta1 == True) & (Ponta2 == True) & (Ponta3 == True)):
                    st.text("Poseidon")
                    # st.text("Ponta1 = odd_2x0 < odd_1x0")
                    # st.text("Ponta2 = odd_2x0 < odd_1x1")
                    # st.text("Ponta3 = odd_2x2 < odd_1x2")
                elif ((Ponta1 == True) & (Ponta2 == True)):
                    st.text("Ponta 1 e Ponta 2")
                    # st.text("Ponta1 = odd_2x0 < odd_1x0")
                    # st.text("Ponta2 = odd_2x0 < odd_1x1")
                elif ((Ponta1 == True) & (Ponta3 == True)):
                    st.text("Ponta 1 e Ponta 3")
                    # st.text("Ponta1 = odd_2x0 < odd_1x0")
                    # st.text("Ponta3 = odd_2x2 < odd_1x2")
                elif ((Ponta2 == True) & (Ponta3 == True)):
                    st.text("Ponta 2 e Ponta 3")
                    # st.text("Ponta2 = odd_2x0 < odd_1x1")
                    # st.text("Ponta3 = odd_2x2 < odd_1x2")
                elif (Ponta1 == True):
                    st.text("Ponta 1")
                    # st.text("Ponta1 = odd_2x0 < odd_1x0")
                elif (Ponta2 == True):
                    st.text("Ponta 2")
                    # st.text("Ponta2 = odd_2x0 < odd_1x1")
                elif (Ponta3 == True):
                    st.text("Ponta 3")
                    # st.text("Ponta3 = odd_2x2 < odd_1x2")
                else:
                    st.text("Nenhuma Ponta Satisfeita")

                
                st.markdown('---') 
            except:
                st.markdown('---') 

        except:
            st.markdown('---')

        try:
            ################################################################################
            # Ultimos 10 Jogos do Favorito como Mandante
            ################################################################################

            
            
            df_10_jogos_H = df[df.Home == selecao1].tail(10)
            
            df_10_jogos_H = df_10_jogos_H[['Date', 'Season','Home','Away','FT_Goals_H','FT_Goals_A','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','Odd_BTTS_Yes']]
            df_10_jogos_H.columns = ['Date','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']
            df_10_jogos_H.reset_index(inplace=True, drop=True)
            df_10_jogos_H.index = df_10_jogos_H.index.set_names(['Nº'])
            df_10_jogos_H = df_10_jogos_H.rename(index=lambda x: x + 1)

            df0 = df_10_jogos_H.copy()
            
            df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
            df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
            df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)
            df0['Odd_Over'] = df0['Odd_Over25'].astype(float).map('{:.2f}'.format)
            df0['Odd_BTTS'] = df0['Odd_BTTS_Yes'].astype(float).map('{:.2f}'.format)

            df0 = df0[['Date','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over','Odd_BTTS']]
            st.text("Ultimos 10 Jogos do Favorito como Mandante")
            st.dataframe(df0)
            st.markdown('---')
        except:
            st.markdown('---')

        try:
            ################################################################################
            # Ultimos 10 Jogos da Zebra como Visitante
            ################################################################################
            
       

            df_10_jogos_A = df_H[df_H.Home == selecao1].copy()
            zebra = df_10_jogos_A.iat[0,3]
            # st.write(zebra)
            df_10_jogos_A = df[df.Away == zebra].tail(10)
            
            df_10_jogos_A = df_10_jogos_A[['Date', 'Season','Home','Away','FT_Goals_H','FT_Goals_A','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','Odd_BTTS_Yes']]
            df_10_jogos_A.columns = ['Date','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']
            df_10_jogos_A.reset_index(inplace=True, drop=True)
            df_10_jogos_A.index = df_10_jogos_A.index.set_names(['Nº'])
            df_10_jogos_A = df_10_jogos_A.rename(index=lambda x: x + 1)

            df0 = df_10_jogos_A.copy()
            
            df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
            df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
            df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)
            df0['Odd_Over'] = df0['Odd_Over25'].astype(float).map('{:.2f}'.format)
            df0['Odd_BTTS'] = df0['Odd_BTTS_Yes'].astype(float).map('{:.2f}'.format)

            df0 = df0[['Date','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over','Odd_BTTS']]
            st.text("Ultimos 10 Jogos da Zebra como Visitante")
            st.dataframe(df0)

            st.markdown('---')
        except:
            st.markdown('---')

        try:
            
            ################################################################################
            # Confronto Direto
            ################################################################################
            
            df_Confronto = df_H[df_H.Home == selecao1].copy()
            zebra = df_Confronto.iat[0,3]
            df_Confronto = df[((df.Home == selecao1) & (df.Away == zebra))]
            df_Confronto = df_Confronto[['Date', 'Season','Home','Away','FT_Goals_H','FT_Goals_A','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','Odd_BTTS_Yes']]
            df_Confronto.columns = ['Date','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']
            if len(df_Confronto) != 0:
                
                df0 = df_Confronto.copy()
            
                df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
                df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
                df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)
                df0['Odd_Over'] = df0['Odd_Over25'].astype(float).map('{:.2f}'.format)
                df0['Odd_BTTS'] = df0['Odd_BTTS_Yes'].astype(float).map('{:.2f}'.format)

                df0 = df0[['Date','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over','Odd_BTTS']]
                st.text("Confronto Direto - Temporadas Passadas")
                df0 = drop_reset_index(df0)
                st.dataframe(df0)
                st.markdown('---')
            else:
                st.markdown('---')
        except:
            st.markdown('---')
        try:

            # Classificação
            
            try:
                home = selecao1
                away = zebra
            

                flt = ((df_liga.Season == "2022/2023") | (df_liga.Season == '2022') )
                df_league = df_liga[flt]
                
                
                df_league = df_league[['Season','Home','Away','FT_Goals_H','FT_Goals_A']]
                df_league.columns = ['Season','Home','Away','Goals_H','Goals_A']
            
                df_league.loc[df_league['Goals_H'] > df_league['Goals_A'], 'Ptos_H'] = 3
                df_league.loc[df_league['Goals_H'] == df_league['Goals_A'], 'Ptos_H'] = 1
                df_league.loc[df_league['Goals_H'] < df_league['Goals_A'], 'Ptos_H'] = 0

                df_league.loc[df_league['Goals_H'] < df_league['Goals_A'], 'Ptos_A'] = 3
                df_league.loc[df_league['Goals_H'] == df_league['Goals_A'], 'Ptos_A'] = 1
                df_league.loc[df_league['Goals_H'] > df_league['Goals_A'], 'Ptos_A'] = 0

                teams = list(set(df_league['Home']).union(set(df_league['Away'])))
                classification_data = []

                for team in teams:
                    home_matches = df_league[df_league['Home'] == team]
                    away_matches = df_league[df_league['Away'] == team]
                    
                    total_matches = pd.concat([home_matches, away_matches])
                    points = (home_matches['Ptos_H'].sum()) + (away_matches['Ptos_A'].sum())
                    
                    classification_data.append({
                        'Team': team,
                        'Points': points})

                classification_df_league = pd.DataFrame(classification_data)
                classification_df_league = classification_df_league.sort_values(by=['Points'], ascending=False)
                classification_df_league = classification_df_league.dropna()
                classification_df_league = classification_df_league.reset_index(drop=True)
                classification_df_league.index += 1

                team1 = home  # Substitua pelo nome do primeiro time
                team2 = away  # Substitua pelo nome do segundo time

                # Filtrar as linhas correspondentes aos times desejados
                team1_row = classification_df_league.loc[classification_df_league['Team'] == team1]
                team2_row = classification_df_league.loc[classification_df_league['Team'] == team2]

                # Obter o número da classificação (índice + 1) para cada time
                team1_rank = team1_row.index[0] if not team1_row.empty else None
                team2_rank = team2_row.index[0] if not team2_row.empty else None

                if team1_rank == None:
                    st.text(f"{team1} não estava nessa divisão na temporada passada.")
                else:
                    st.text(f"{team1} terminou a temporada passada classificado em {team1_rank}º lugar.")
                if team2_rank == None:
                    st.text(f"{team2} não estava nessa divisão na temporada passada.")
                else:
                    st.text(f"{team2} terminou a temporada passada classificado em {team2_rank}º lugar.")      
                
                # st.markdown('---')

                # Classificação
                
                home = selecao1
                away = zebra
            

                flt = ((df_liga.Season == "2023/2024") | (df_liga.Season == '2023') )
                df_league = df_liga[flt]
                
                
                df_league = df_league[['Season','Home','Away','FT_Goals_H','FT_Goals_A']]
                df_league.columns = ['Season','Home','Away','Goals_H','Goals_A']
            
                df_league.loc[df_league['Goals_H'] > df_league['Goals_A'], 'Ptos_H'] = 3
                df_league.loc[df_league['Goals_H'] == df_league['Goals_A'], 'Ptos_H'] = 1
                df_league.loc[df_league['Goals_H'] < df_league['Goals_A'], 'Ptos_H'] = 0

                df_league.loc[df_league['Goals_H'] < df_league['Goals_A'], 'Ptos_A'] = 3
                df_league.loc[df_league['Goals_H'] == df_league['Goals_A'], 'Ptos_A'] = 1
                df_league.loc[df_league['Goals_H'] > df_league['Goals_A'], 'Ptos_A'] = 0

                teams = list(set(df_league['Home']).union(set(df_league['Away'])))
                classification_data = []

                for team in teams:
                    home_matches = df_league[df_league['Home'] == team]
                    away_matches = df_league[df_league['Away'] == team]
                    
                    total_matches = pd.concat([home_matches, away_matches])
                    points = (home_matches['Ptos_H'].sum()) + (away_matches['Ptos_A'].sum())
                    
                    classification_data.append({
                        'Team': team,
                        'Points': points})

                classification_df_league = pd.DataFrame(classification_data)
                classification_df_league = classification_df_league.sort_values(by=['Points'], ascending=False)
                classification_df_league = classification_df_league.dropna()
                classification_df_league = classification_df_league.reset_index(drop=True)
                classification_df_league.index += 1

                team1 = home  # Substitua pelo nome do primeiro time
                team2 = away  # Substitua pelo nome do segundo time

                # Filtrar as linhas correspondentes aos times desejados
                team1_row = classification_df_league.loc[classification_df_league['Team'] == team1]
                team2_row = classification_df_league.loc[classification_df_league['Team'] == team2]

                # Obter o número da classificação (índice + 1) para cada time
                team1_rank = team1_row.index[0] if not team1_row.empty else None
                team2_rank = team2_row.index[0] if not team2_row.empty else None

                if team1_rank == None:
                    st.text(f"{team1} mudou de divisão.")
                else:
                    st.text(f"{team1} está na temporada atual classificado em {team1_rank}º lugar.")
                if team2_rank == None:
                    st.text(f"{team2} mudou de divisão.")
                else:
                    st.text(f"{team2} está na temporada atual classificado em  {team2_rank}º lugar.")      
                
                st.markdown('---')
            except:
                st.markdown('---')



            ################################################################################
            # PDF do Theo
            ################################################################################
            
            try:
                home = selecao1
                away = zebra

                # df_xg = df_jogos[df_jogos.Home == home]

                # xg_h = df_xg['xG_Home_Pre'].iloc[0]
                # xg_a = df_xg['xG_Away_Pre'].iloc[0]
                # xg_tot = df_xg['xG_Total_Pre'].iloc[0]

                df.loc[df['FT_Goals_H'] > df['FT_Goals_A'], 'Ptos_H'] = 3
                df.loc[df['FT_Goals_H'] == df['FT_Goals_A'], 'Ptos_H'] = 1
                df.loc[df['FT_Goals_H'] < df['FT_Goals_A'], 'Ptos_H'] = 0


                df.loc[df['FT_Goals_H'] < df['FT_Goals_A'], 'Ptos_A'] = 3
                df.loc[df['FT_Goals_H'] == df['FT_Goals_A'], 'Ptos_A'] = 1
                df.loc[df['FT_Goals_H'] > df['FT_Goals_A'], 'Ptos_A'] = 0
                
                df['Media_Ptos_H1'] = df.groupby('Home')['Ptos_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
                df['Media_Ptos_A1'] = df.groupby('Away')['Ptos_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
                
                df['Media_Ptos_H2'] = df.groupby('Home')['Ptos_H'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True)
                df['Media_Ptos_A2'] = df.groupby('Away')['Ptos_A'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True)
                
                df.dropna(inplace=True)
                df.reset_index(inplace=True, drop=True)
                df.index = df.index.set_names(['Nº'])
                df = df.rename(index=lambda x: x + 1)
                
                flt = ((df.Season == "2022/2023") | (df.Season == "2023/2024") | (df.Season == '2023') )
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
                flt2_H = df_H.FT_Goals_H > df_H.FT_Goals_A
                df2_H = df_H[flt2_H]
                df2_H = df2_H.Home.count()
                
                flt2_A = df_A.FT_Goals_H < df_A.FT_Goals_A
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
                flt_gol_0_H = df_H.FT_Goals_A == 0
                df_gol_0_H = df_H[flt_gol_0_H]
                count_gol_0_H = df_gol_0_H.Home.count() 
                por_count_gol_0_H = round((round((count_gol_0_H / len(df_H)),2)*100))
                por_count_gol_0_H = str(por_count_gol_0_H)+'%'
                
                flt_gol_0_A = df_A.FT_Goals_H == 0
                df_gol_0_A = df_A[flt_gol_0_A]
                count_gol_0_A = df_gol_0_A.Away.count() 
                por_count_gol_0_A = round((round((count_gol_0_A / len(df_A)),2)*100))
                por_count_gol_0_A = str(por_count_gol_0_A)+'%'
                
                # Falhou em marcar
                flt_gol_failed_H = df_H.FT_Goals_H == 0
                df_gol_failed_H = df_H[flt_gol_failed_H]
                count_gol_failed_H = df_gol_failed_H.Home.count() 
                por_count_gol_failed_H = round((round((count_gol_failed_H / len(df_H)),2)*100))
                por_count_gol_failed_H = str(por_count_gol_failed_H)+'%'
                
                flt_gol_failed_A = df_A.FT_Goals_A == 0
                df_gol_failed_A = df_A[flt_gol_failed_A]
                count_gol_failed_A = df_gol_failed_A.Away.count() 
                por_count_gol_failed_A = round((round((count_gol_failed_A / len(df_A)),2)*100))
                por_count_gol_failed_A = str(por_count_gol_failed_A)+'%'
                
                # Ambas marcam
                flt_BTTS_H = (df_H.FT_Goals_H != 0) & (df_H.FT_Goals_A != 0)
                df_BTTS_H = df_H[flt_BTTS_H]
                count_BTTS_H = df_BTTS_H.Home.count() 
                por_count_BTTS_H = round((round((count_BTTS_H / len(df_H)),2)*100))
                por_count_BTTS_H = str(por_count_BTTS_H)+'%'
                
                flt_BTTS_A = (df_A.FT_Goals_H != 0) & (df_A.FT_Goals_A != 0)
                df_BTTS_A = df_A[flt_BTTS_A]
                count_BTTS_A = df_BTTS_A.Home.count() 
                por_count_BTTS_A = round((round((count_BTTS_A / len(df_A)),2)*100))
                por_count_BTTS_A = str(por_count_BTTS_A)+'%' 
                
                
                # Média de Gols em Casa
                
                # Gols Marcados   
                Goals_MH = df.groupby(['Home'])['FT_Goals_H'].get_group(home).sum()
                Goals_MH = int(Goals_MH)
                Goals_MA = df.groupby(['Away'])['FT_Goals_A'].get_group(away).sum()
                Goals_MA = int(Goals_MA)
                
                # Gols Sofridos
                Goals_SH = df.groupby(['Home'])['FT_Goals_A'].get_group(home).sum()
                Goals_SH = int(Goals_SH)
                Goals_SA = df.groupby(['Away'])['FT_Goals_H'].get_group(away).sum()
                Goals_SA = int(Goals_SA)
                
                # Média de gols marcados    
                mean_Goals_MH = df.groupby(['Home'])['FT_Goals_H'].get_group(home).mean()
                mean_Goals_MH = round(mean_Goals_MH,2)
                mean_Goals_MA = df.groupby(['Away'])['FT_Goals_A'].get_group(away).mean()
                mean_Goals_MA = round(mean_Goals_MA,2)
                
                # Média de gols sofridos    
                mean_Goals_SH = df.groupby(['Home'])['FT_Goals_A'].get_group(home).mean()
                mean_Goals_SH = round(mean_Goals_SH,2)
                mean_Goals_SA = df.groupby(['Away'])['FT_Goals_H'].get_group(away).mean()
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
                
                st.text('Aproveitamento dos Times - Mandante Jogando em Casa e Visitante Jogando Fora')
                st.text('')
                texto = home + ' x ' + away
                st.write("<center>{}</center>".format(texto), unsafe_allow_html=True)
                st.write('')
                




                
                col1, col2 = st.columns(2)

                with col1:
                    st.dataframe(df12)

                with col2:
                    st.dataframe(df34)

                st.markdown('---')  

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
                df_H_PrimeiroGol = df_H[['FT_Goals_H','FT_Goals_A','Goals_Minutes_Home','Goals_Minutes_Away']]
                df_H_PrimeiroGol['FT_TotalGoals'] = df_H_PrimeiroGol['FT_Goals_H'] + df_H_PrimeiroGol['FT_Goals_A'] 
                flt = df_H_PrimeiroGol.FT_TotalGoals != 0
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
                
                
                df_A_PrimeiroGol = df_A[['FT_Goals_H','FT_Goals_A','Goals_Minutes_Home','Goals_Minutes_Away']]
                df_A_PrimeiroGol['FT_TotalGoals'] = df_A_PrimeiroGol['FT_Goals_H'] + df_A_PrimeiroGol['FT_Goals_A'] 
                flt = df_A_PrimeiroGol.FT_TotalGoals != 0
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
                
                
                flt9 = marca_primeiro_H.FT_Goals_H > marca_primeiro_H.FT_Goals_A
                marcou_e_ganhou = marca_primeiro_H[flt9]
                df9 = len(marcou_e_ganhou) / len(marca_primeiro_H)
                df9 = round((df9*100),)
                total_df9 = str(df9)+'%'
                
                flt10 = marca_primeiro_A.FT_Goals_A > marca_primeiro_A.FT_Goals_H
                marcou_e_ganhou = marca_primeiro_A[flt10]
                df10 = len(marcou_e_ganhou) / len(marca_primeiro_A)
                df10 = round((df10*100),)
                total_df10 = str(df10)+'%'
                
                flt11 = marca_primeiro_H.FT_Goals_H == marca_primeiro_H.FT_Goals_A
                marcou_e_empatou = marca_primeiro_H[flt11]
                df11 = len(marcou_e_empatou) / len(marca_primeiro_H)
                df11 = round((df11*100),)
                total_df11 = str(df11)+'%'
                
                flt12 = marca_primeiro_A.FT_Goals_A == marca_primeiro_A.FT_Goals_H
                marcou_e_empatou = marca_primeiro_A[flt12]
                df12 = len(marcou_e_empatou) / len(marca_primeiro_A)
                df12 = round((df12*100),)
                total_df12 = str(df12)+'%'
                
                flt13 = marca_primeiro_H.FT_Goals_H < marca_primeiro_H.FT_Goals_A
                marcou_e_perdeu = marca_primeiro_H[flt13]
                df13 = len(marcou_e_perdeu) / len(marca_primeiro_H)
                df13 = round((df13*100),)
                total_df13 = str(df13)+'%'
                
                flt14 = marca_primeiro_A.FT_Goals_A < marca_primeiro_A.FT_Goals_H
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
                
                flt17 = leva_primeiro_H['FT_Goals_H'] > leva_primeiro_H['FT_Goals_A']
                levou_e_ganhou = leva_primeiro_H[flt17]
                df17 = len(levou_e_ganhou) / len(leva_primeiro_H)
                df17 = round((df17*100),)
                total_df17 = str(df17)+'%'
            
                
                flt18 = leva_primeiro_A['FT_Goals_A'] > leva_primeiro_A['FT_Goals_H']
                levou_e_ganhou = leva_primeiro_A[flt18]
                df18 = len(levou_e_ganhou) / len(leva_primeiro_A)
                df18 = round((df18*100),)
                total_df18 = str(df18)+'%'
                
                
                
                flt19 = leva_primeiro_H.FT_Goals_H == leva_primeiro_H.FT_Goals_A
                levou_e_empatou = leva_primeiro_H[flt19]
                df19 = len(levou_e_empatou) / len(leva_primeiro_H)
                df19 = round((df19*100),)
                total_df19 = str(df19)+'%'
                
                
                flt20 = leva_primeiro_A.FT_Goals_H == leva_primeiro_A.FT_Goals_A
                levou_e_empatou = leva_primeiro_A[flt20]
                df20 = len(levou_e_empatou) / len(leva_primeiro_A)
                df20 = round((df20*100),)
                total_df20 = str(df20)+'%'
                
                
                flt21 = leva_primeiro_H.FT_Goals_H < leva_primeiro_H.FT_Goals_A
                levou_e_perdeu = leva_primeiro_H[flt21]
                df21 = len(levou_e_perdeu) / len(leva_primeiro_H)
                df21 = round((df21*100),)
                total_df21 = str(df21)+'%'
                
                
                flt22 = leva_primeiro_A.FT_Goals_A < leva_primeiro_A.FT_Goals_H
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
                    & (df_H_PrimeiroGol.FT_Goals_H > df_H_PrimeiroGol.FT_Goals_A))
                        
                df_1T_02 = df_H_PrimeiroGol[flt_1T_02]
                num_1T_02 = len(df_1T_02) / len(df_H_PrimeiroGol)
                df_1T_02 = round((num_1T_02*100),)
                df_1T_02 = str(df_1T_02)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Empatou
                flt_1T_03 = ((df_H_PrimeiroGol.Goals_Minutes_Home < 46) 
                    & (df_H_PrimeiroGol.Goals_Minutes_Home < df_H_PrimeiroGol.Goals_Minutes_Away)
                    & (df_H_PrimeiroGol.FT_Goals_H == df_H_PrimeiroGol.FT_Goals_A))
                        
                df_1T_03 = df_H_PrimeiroGol[flt_1T_03]
                num_1T_03 = len(df_1T_03) / len(df_H_PrimeiroGol)
                df_1T_03 = round((num_1T_03*100),)
                df_1T_03 = str(df_1T_03)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Perdeu
                flt_1T_04 = ((df_H_PrimeiroGol.Goals_Minutes_Home < 46) 
                    & (df_H_PrimeiroGol.Goals_Minutes_Home < df_H_PrimeiroGol.Goals_Minutes_Away)
                    & (df_H_PrimeiroGol.FT_Goals_H < df_H_PrimeiroGol.FT_Goals_A))
                        
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
                            & (df_A_PrimeiroGol.FT_Goals_A > df_A_PrimeiroGol.FT_Goals_H))
                        
                df_1T_06 = df_A_PrimeiroGol[flt_1T_06]
                num_1T_06 = len(df_1T_06) / len(df_A_PrimeiroGol)
                df_1T_06 = round((num_1T_06*100),)
                df_1T_06 = str(df_1T_06)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Empatou
                flt_1T_07 = ((df_A_PrimeiroGol.Goals_Minutes_Away < 46) 
                            & (df_A_PrimeiroGol.Goals_Minutes_Away < df_A_PrimeiroGol.Goals_Minutes_Home)
                            & (df_A_PrimeiroGol.FT_Goals_A == df_A_PrimeiroGol.FT_Goals_H))
                        
                df_1T_07 = df_A_PrimeiroGol[flt_1T_07]
                num_1T_07 = len(df_1T_07) / len(df_A_PrimeiroGol)
                df_1T_07 = round((num_1T_07*100),)
                df_1T_07 = str(df_1T_07)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Perdeu
                flt_1T_08 = ((df_A_PrimeiroGol.Goals_Minutes_Away < 46) 
                            & (df_A_PrimeiroGol.Goals_Minutes_Away < df_A_PrimeiroGol.Goals_Minutes_Home)
                            & (df_A_PrimeiroGol.FT_Goals_A < df_A_PrimeiroGol.FT_Goals_H))
                        
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
                st.markdown('---')
                
            except:
                pass

            try:    
                 
                # Time Mandante - Gols Marcados
                
                min_gols_H = df_H[['FT_Goals_H','Goals_Minutes_Home']]
                flt = min_gols_H.FT_Goals_H != 0
                min_gols_H = min_gols_H[flt]
                min_gols_H = min_gols_H[['Goals_Minutes_Home']]
                
                # Time Mandante - Gols Sofridos
                
                min_gols_HS = df_H[['FT_Goals_A','Goals_Minutes_Away']]
                flt = min_gols_HS.FT_Goals_A != 0
                min_gols_HS = min_gols_HS[flt]
                min_gols_HS = min_gols_HS[['Goals_Minutes_Away']]
                
                # Time Visitante - Gols Marcados
                
                min_gols_A = df_A[['FT_Goals_A','Goals_Minutes_Away']]
                flt = min_gols_A.FT_Goals_A != 0
                min_gols_A = min_gols_A[flt]
                min_gols_A = min_gols_A[['Goals_Minutes_Away']]
                
                # Time Visitante - Gols Sofridos
                
                min_gols_AS = df_A[['FT_Goals_H','Goals_Minutes_Home']]
                flt = min_gols_AS.FT_Goals_H != 0
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
                
                
                
                df1 = pd.concat([df1,df2], axis=1)
                print('Minutos dos Gols -',home)

                
                df2 = pd.concat([df3,df4], axis=1)
                print('Minutos dos Gols -',away)

                col1, col2 = st.columns(2)

                with col1:
                    st.write('Minutos dos Gols -',home)
                    st.write(df1)

                with col2:
                    st.write('Minutos dos Gols -',away)
                    st.write(df2)

                st.markdown('---')        

            

                flt_Over05_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 0)
                df_Over05_H = df_H[flt_Over05_H]
                count_Over05_H = df_Over05_H.Home.count() 
                por_count_Over05_H = round((round((count_Over05_H / len(df_H)),2)*100))
                por_count_Over05_H = str(por_count_Over05_H)+'%'
                
                flt_Over05_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 0)
                df_Over05_A = df_A[flt_Over05_A]
                count_Over05_A = df_Over05_A.Away.count() 
                por_count_Over05_A = round((round((count_Over05_A / len(df_A)),2)*100))
                por_count_Over05_A = str(por_count_Over05_A)+'%'
                
                flt_Over15_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 1)
                df_Over15_H = df_H[flt_Over15_H]
                count_Over15_H = df_Over15_H.Home.count() 
                por_count_Over15_H = round((round((count_Over15_H / len(df_H)),2)*100))
                por_count_Over15_H = str(por_count_Over15_H)+'%'
                
                flt_Over15_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 1)
                df_Over15_A = df_A[flt_Over15_A]
                count_Over15_A = df_Over15_A.Away.count() 
                por_count_Over15_A = round((round((count_Over15_A / len(df_A)),2)*100))
                por_count_Over15_A = str(por_count_Over15_A)+'%'
                
                flt_Over25_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 2)
                df_Over25_H = df_H[flt_Over25_H]
                count_Over25_H = df_Over25_H.Home.count() 
                por_count_Over25_H = round((round((count_Over25_H / len(df_H)),2)*100))
                por_count_Over25_H = str(por_count_Over25_H)+'%'
                
                flt_Over25_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 2)
                df_Over25_A = df_A[flt_Over25_A]
                count_Over25_A = df_Over25_A.Away.count() 
                por_count_Over25_A = round((round((count_Over25_A / len(df_A)),2)*100))
                por_count_Over25_A = str(por_count_Over25_A)+'%'
                
                flt_Over35_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 3)
                df_Over35_H = df_H[flt_Over35_H]
                count_Over35_H = df_Over35_H.Home.count() 
                por_count_Over35_H = round((round((count_Over35_H / len(df_H)),2)*100))
                por_count_Over35_H = str(por_count_Over35_H)+'%'
                
                flt_Over35_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 3)
                df_Over35_A = df_A[flt_Over35_A]
                count_Over35_A = df_Over35_A.Away.count() 
                por_count_Over35_A = round((round((count_Over35_A / len(df_A)),2)*100))
                por_count_Over35_A = str(por_count_Over35_A)+'%'
                
                flt_Over45_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 4)
                df_Over45_H = df_H[flt_Over45_H]
                count_Over45_H = df_Over45_H.Home.count() 
                por_count_Over45_H = round((round((count_Over45_H / len(df_H)),2)*100))
                por_count_Over45_H = str(por_count_Over45_H)+'%'
                
                flt_Over45_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 4)
                df_Over45_A = df_A[flt_Over45_A]
                count_Over45_A = df_Over45_A.Away.count() 
                por_count_Over45_A = round((round((count_Over45_A / len(df_A)),2)*100))
                por_count_Over45_A = str(por_count_Over45_A)+'%'
                
                flt_Over55_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 5)
                df_Over55_H = df_H[flt_Over55_H]
                count_Over55_H = df_Over55_H.Home.count() 
                por_count_Over55_H = round((round((count_Over55_H / len(df_H)),2)*100))
                por_count_Over55_H = str(por_count_Over55_H)+'%'
                
                flt_Over55_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 5)
                df_Over55_A = df_A[flt_Over55_A]
                count_Over55_A = df_Over55_A.Away.count() 
                por_count_Over55_A = round((round((count_Over55_A / len(df_A)),2)*100))
                por_count_Over55_A = str(por_count_Over55_A)+'%'
                
                flt_Over65_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 6)
                df_Over65_H = df_H[flt_Over65_H]
                count_Over65_H = df_Over65_H.Home.count() 
                por_count_Over65_H = round((round((count_Over65_H / len(df_H)),2)*100))
                por_count_Over65_H = str(por_count_Over65_H)+'%'
                
                flt_Over65_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 6)
                df_Over65_A = df_A[flt_Over65_A]
                count_Over65_A = df_Over65_A.Away.count() 
                por_count_Over65_A = round((round((count_Over65_A / len(df_A)),2)*100))
                por_count_Over65_A = str(por_count_Over65_A)+'%'
                
                flt_Over75_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 7)
                df_Over75_H = df_H[flt_Over75_H]
                count_Over75_H = df_Over75_H.Home.count() 
                por_count_Over75_H = round((round((count_Over75_H / len(df_H)),2)*100))
                por_count_Over75_H = str(por_count_Over75_H)+'%'
                
                flt_Over75_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 7)
                df_Over75_A = df_A[flt_Over75_A]
                count_Over75_A = df_Over75_A.Away.count() 
                por_count_Over75_A = round((round((count_Over75_A / len(df_A)),2)*100))
                por_count_Over75_A = str(por_count_Over75_A)+'%'
                
                flt_Over85_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 7)
                df_Over85_H = df_H[flt_Over85_H]
                count_Over85_H = df_Over85_H.Home.count() 
                por_count_Over85_H = round((round((count_Over85_H / len(df_H)),2)*100))
                por_count_Over85_H = str(por_count_Over85_H)+'%'
                
                flt_Over85_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 7)
                df_Over85_A = df_A[flt_Over85_A]
                count_Over85_A = df_Over85_A.Away.count() 
                por_count_Over85_A = round((round((count_Over85_A / len(df_A)),2)*100))
                por_count_Over85_A = str(por_count_Over85_A)+'%'
                
                
                row_names = ['Over 0.5','Over 1.5','Over 2.5','Over 3.5','Over 4.5','Over 5.5','Over 6.5','Over 7.5','Over 8.5']
                df1 = pd.DataFrame([por_count_Over05_H,por_count_Over15_H,por_count_Over25_H,por_count_Over35_H,por_count_Over45_H,por_count_Over55_H,por_count_Over65_H,por_count_Over75_H,por_count_Over85_H], index=row_names, columns=['Home'])
                
                row_names = ['Over 0.5','Over 1.5','Over 2.5','Over 3.5','Over 4.5','Over 5.5','Over 6.5','Over 7.5','Over 8.5']
                df2 = pd.DataFrame([por_count_Over05_A,por_count_Over15_A,por_count_Over25_A,por_count_Over35_A,por_count_Over45_A,por_count_Over55_A,por_count_Over65_A,por_count_Over75_A,por_count_Over85_A], index=row_names, columns=['Away'])
                
                
                df0 = pd.concat([df1,df2], axis=1)
                st.write('Total de Gols')
                st.write(df0)
                st.markdown('---')
            except:
                pass
        except:
            pass


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        































































    #################################################
    ################# Favorito Away #################
    #################################################       
    def favorito_away():

        st.title("Luke")
        st.header("Favorito Away")
        
        dia = st.date_input(
            "Data de Análise",
            date.today())

        ########## Importando os Jogos do Dia ##########   
        ########## Importando os Jogos do Dia ########## 
        def load_data_jogos():
            key = "20e2d4aa7479a657c52935c4a743a626941b0a1f41b12156642dd7b62d893145"

            url1 = f"https://api.football-data-api.com/todays-matches?key={key}&date={dia}&page=1"
            data1 = requests.get(url1)
            resp = data1.json()['data']
            dados1 = pd.DataFrame.from_dict(resp)

            url2 = f"https://api.football-data-api.com/todays-matches?key={key}&date={dia}&page=2"
            data2 = requests.get(url2)
            resp = data2.json()['data']

            dados2 = pd.DataFrame.from_dict(resp)

            data_jogos = pd.concat([dados1, dados2],ignore_index=True)

            return data_jogos

        df_jogos = load_data_jogos()

        try:
        
            df_jogos = df_jogos[['competition_id','season','date_unix','game_week','home_name','away_name','odds_ft_1','odds_ft_x','odds_ft_2','odds_ft_over25','odds_ft_under25','odds_btts_yes','odds_btts_no','team_a_xg_prematch', 'team_b_xg_prematch', 'total_xg_prematch']]
            df_jogos.columns = ['League','Season','Date','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No','xG_Home_Pre', 'xG_Away_Pre', 'xG_Total_Pre']
            df_jogos['Date'] = pd.to_datetime(df_jogos['Date'], unit='s') - pd.DateOffset(hours=3)
            df_jogos = df_jogos.dropna()
            df_jogos['Date'] = df_jogos['Date'].astype('str')
            df_jogos[['Date2','Time']] = df_jogos['Date'].str.split(' ',expand=True)
            df_jogos = df_jogos[['League','Season','Date2','Time','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_Under25','FT_Odd_BTTS_Yes','FT_Odd_BTTS_No','xG_Home_Pre', 'xG_Away_Pre', 'xG_Total_Pre']]
            df_jogos.columns = ['League','Season','Date','Time','Rodada','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_Under25','Odd_BTTS_Yes','Odd_BTTS_No','xG_Home_Pre', 'xG_Away_Pre', 'xG_Total_Pre']
            flt = df_jogos.Date == str(dia)
            jogos_footystats = df_jogos[flt]
            jogos_footystats = drop_reset_index(jogos_footystats)

            rename_leagues_footystats(jogos_footystats)
            rename_leagues_footystats_flashscore(jogos_footystats)
            jogos_footystats = jogos_footystats[jogos_footystats['League'].isin(['Russia Russian Premier League']) == False]
            jogos_footystats = drop_reset_index(jogos_footystats)
            jogos_do_dia = jogos_footystats[['League','Season','Date','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes','xG_Home_Pre','xG_Away_Pre','xG_Total_Pre']]
            rename_teams_footystats_flashscore(jogos_do_dia)

            def load_data_betfair():

                betfair = pd.read_csv(f'https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia_Betfair/{dia}_Jogos_do_Dia.csv?raw=true')

                return betfair
        
            try:
                betfair = load_data_betfair()
                rename_leagues(betfair)
                rename_teams(betfair)
                betfair = betfair[['League','Home','Away',
                'CS_0x0','CS_0x1','CS_0x2','CS_0x3',
                'CS_1x0','CS_1x1','CS_1x2','CS_1x3',
                'CS_2x0','CS_2x1','CS_2x2','CS_2x3',
                'CS_3x0','CS_3x1','CS_3x2','CS_3x3',
                'CS_Goleada_H','CS_Goleada_A','ID_Evento','IDMercado']]
                betfair.columns = ['League','Home','Away',
                'Odd_0x0','Odd_0x1','Odd_0x2','Odd_0x3',
                'Odd_1x0','Odd_1x1','Odd_1x2','Odd_1x3',
                'Odd_2x0','Odd_2x1','Odd_2x2','Odd_2x3',
                'Odd_3x0','Odd_3x1','Odd_3x2','Odd_3x3',
                'Odd_Goleada_H','Odd_Goleada_A','ID_Evento','IDMercado']
            
                Jogos = jogos_do_dia.merge(betfair, on=['League','Home','Away'])
                Jogos = drop_reset_index(Jogos)

            except:
                st.dataframe(jogos_do_dia)
        except:
            st.write("Jogos desse dia não disponíveis.")
    

        try:
            df_jogos = Jogos

            ####################################
            ########## Filtro de Odds ##########
            ####################################
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                Odd_H_Min = st.number_input('Odd_H_Min', value=1.01, step=0.1)
                Odd_H_Max = st.number_input('Odd_H_Max', value=100.0, step=0.1)
            with col2:
                Odd_D_Min = st.number_input('Odd_D_Min', value=1.01, step=0.1)
                Odd_D_Max = st.number_input('Odd_D_Max', value=100.0, step=0.1)
            with col3:
                Odd_A_Min = st.number_input('Odd_A_Min', value=1.50, step=0.1)
                Odd_A_Max = st.number_input('Odd_A_Max', value=2.20, step=0.1)
            with col4:
                Odd_Over25_Min = st.number_input('Odd_Over25_Min', value=1.50, step=0.1)
                Odd_Over25_Max = st.number_input('Odd_Over25_Max', value=2.20, step=0.1)
            with col5:
                Odd_BTTS_Min = st.number_input('Odd_BTTS_Min', value=1.50, step=0.1)
                Odd_BTTS_Max = st.number_input('Odd_BTTS_Max', value=2.20, step=0.1)
            
            # Filtros de Odds
            Odd_Min_Back_Fav = Odd_A_Min
            Odd_Max_Back_Fav = Odd_A_Max
            Odd_Min_Back_H = Odd_H_Min
            Odd_Max_Back_H = Odd_H_Max
            Odd_Min_Back_D = Odd_D_Min
            Odd_Max_Back_D = Odd_D_Max
            Odd_Min_Over25 = Odd_Over25_Min
            Odd_Max_Over25 = Odd_Over25_Max
            Odd_Min_BTTS = Odd_BTTS_Min
            Odd_Max_BTTS = Odd_BTTS_Max

            ###################################
            ########## Favorito Home ##########
            ###################################

            # Criando o Filtro do Método de Lay CS - Favorito Home
            flt1 = ((df_jogos.Odd_A >= Odd_Min_Back_Fav) & (df_jogos.Odd_A <= Odd_Max_Back_Fav) & 
                    (df_jogos.Odd_H >= Odd_Min_Back_H) & (df_jogos.Odd_H <= Odd_Max_Back_H) &
                    (df_jogos.Odd_D >= Odd_Min_Back_D) & (df_jogos.Odd_D <= Odd_Max_Back_D) &
                    (df_jogos.Odd_Over25 >= Odd_Min_Over25) & (df_jogos.Odd_Over25 <= Odd_Max_Over25) & 
                    (df_jogos.Odd_BTTS_Yes >= Odd_Min_BTTS) & (df_jogos.Odd_BTTS_Yes <= Odd_Max_BTTS))
            df_H = df_jogos[flt1]
            df_H = df_H[['League','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']]
            df_H = drop_reset_index(df_H)

            #############################
            ########## Análise ##########
            #############################

            # Criando a Lista com os Times
            lista_H = df_H["Away"].tolist()
            lista_HT = ['0x0','0x1','0x2','1x0','1x1','1x2','2x0','2x1','2x2','Goleada_HT']
            lista_FT = ['0x0','0x1','0x2','0x3','1x0','1x1','1x2','1x3','2x0','2x1','2x2','2x3','3x0','3x1','3x2','3x3','Goleada_H','Goleada_A']

            df_H2 = df_H[['League','Time','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','Odd_BTTS_Yes']]
            df_H2.columns = ['League','Time','Home','Away','Odd_H','Odd_D','Odd_A','Odd_Over','Odd_BTTS']
            
            df0 = df_H2.copy()
            df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
            df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
            df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)
            df0['Odd_Over'] = df0['Odd_Over'].astype(float).map('{:.2f}'.format)
            df0['Odd_BTTS'] = df0['Odd_BTTS'].astype(float).map('{:.2f}'.format)
            st.dataframe(df0)
        except:
                st.write("Jogos desse dia não disponíveis.")
        try:
        
            ################################################
            ########## Importando a Base de Dados ##########
            ################################################
            
            j1, j2, j3 = st.columns(3)
            selecao1 = j1.selectbox('Escolha o Visitante', lista_H) 
            selecao2 = j2.selectbox('Escolha o Placar FT', lista_FT)
            # selecao3 = j3.selectbox('Escolha o Placar FT', lista_FT)
            

            df_league = df_H[df_H.Away == selecao1].copy()
            liga = df_league.iat[0,0]

        except:
            pass

        try:
            df_Home = df_jogos[df_jogos.Away == selecao1].copy()
            zebra = df_Home.iat[0,4]
            home = zebra
            away = selecao1
            
            IDMercado = str(df_Home.iat[0,33])
            IDMercado = ajustar_id_mercado(IDMercado)
            

            st.write('')


            jogo = str(home +' x '+ away)
            # link = f'[{jogo}](https://www.betfair.com/exchange/plus/football/market/{IDMercado})'
            link1 = f'<div style="text-align:left"><a href="https://www.betfair.com/exchange/plus/football/market/{IDMercado}">{"Betfair"}</a></div>'
            link2 = f'<div style="text-align:left"><a href="https://bolsadeaposta.com/exchange/sport/1/market/{IDMercado}">{"Bolsa de Aposta"}</a></div>'
            link3 = f'<div style="text-align:left"><a href="https://fulltbet.com/exchange/sport/1/market/{IDMercado}">{"Fulltbet"}</a></div>'

            
            col1, col2, col3 = st.columns(3)

            with col2:
                texto = home + ' x ' + away
                st.write(texto, unsafe_allow_html=True)

            # st.text('')
            
            # st.write('')

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
        ########## Importando a Base de Dados ##########

        
        try:

            # @st.cache
            @st.cache_data
            def load_data_base():

                base_luke = pd.read_csv("./Bases/x_Luke_x.csv")
                
                return base_luke

            base = load_data_base()

                
            df = base[base['League'] == liga]
        except:
            pass

        try:
            df_f = df[(df['Away'] == selecao1)]
            df_filtrado = df_f[(df_f[selecao2] == 1)]
            df_filtrado = df_filtrado[['Season','Date','Home','Away','HT_Goals_H','HT_Goals_A','FT_Goals_H','FT_Goals_A','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','Odd_BTTS_Yes']]
            df_filtrado.columns = ['Season','Date','Home','Away','Goals_H_HT','Goals_A_HT','Goals_H_FT','Goals_A_FT','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']
            df_filtrado = drop_reset_index(df_filtrado)
        except:
            pass

        try:
            ################################################################################
            # Jogos anteriores Terminados no Placar Selecionado
            ################################################################################

            n_H = df_filtrado[df_filtrado.columns[0]].count()
            if n_H == 0:
                st.text("Não houve Jogos anteriores do " + selecao1 + " terminados em "+ selecao2)
            else:
                st.text("Jogos anteriores do " + selecao1 + " terminados em " + selecao2)
                df0 = df_filtrado.copy()
                
                df0['Odd_H'] = df0['FT_Odd_H'].astype(float).map('{:.2f}'.format)
                df0['Odd_D'] = df0['FT_Odd_D'].astype(float).map('{:.2f}'.format)
                df0['Odd_A'] = df0['FT_Odd_A'].astype(float).map('{:.2f}'.format)
                df0['Odd_Over'] = df0['FT_Odd_Over25'].astype(float).map('{:.2f}'.format)
                df0['Odd_BTTS'] = df0['Odd_BTTS_Yes'].astype(float).map('{:.2f}'.format)
                df0 = df0[['Date','Season','Home','Away','FT_Goals_H','FT_Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over','Odd_BTTS']]
                df0.columns = ['Date','Season','Home','Away','FT_HG','FT_AG','Odd_H','Odd_D','Odd_A','Odd_Over','Odd_BTTS']
                df0.reset_index(inplace=True, drop=True)
                df0.index = df0.index.set_names(['Nº'])
                df0 = df0.rename(index=lambda x: x + 1)
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
            df_10_jogos_A = df_H[df_H.Away == selecao1].copy()
            zebra = df_10_jogos_A.iat[0,2]
            df_sing_2anos_H = df[df.Away == selecao1].copy()
            df_sing_2anos_A = df[df.Home == zebra].copy()
            df_sing_2anos_H = df_sing_2anos_H[df_sing_2anos_H[selecao2] == 1]
            df_sing_2anos_A = df_sing_2anos_A[df_sing_2anos_A[selecao2] == 1]
            n_sing_2anos_H = df_sing_2anos_H[df_sing_2anos_H.columns[0]].count()
            n_sing_2anos_A = df_sing_2anos_A[df_sing_2anos_A.columns[0]].count()
            ###
            #st.text("2 anos H")
            #st.dataframe(df_sing_2anos_H)
            #st.text("2 anos A")
            #st.dataframe(df_sing_2anos_A)
            df_sing_10jogos = df[df.Away == selecao1].copy()
            df_sing_10jogos = df_sing_10jogos[df_sing_10jogos.Home == zebra]
            # df_sing_10jogos = df_sing_10jogos.tail(10)
            df_sing_10jogos = df_sing_10jogos[df_sing_10jogos[selecao2] == 1]
            #st.text("10 jogos 1 x 2")
            #st.dataframe(df_sing_10jogos)
            ###
            n_sing_10jogos = df_sing_10jogos[df_sing_10jogos.columns[0]].count()
            if ((n_sing_2anos_H < 1) & (n_sing_2anos_A < 1) & (n_sing_10jogos < 1)):
                st.text("Este Placar é SINGULAR")
            st.markdown('---')   
        except:
            st.markdown('---')
        try:
            ################################################################################
            # Odd Média do Time
            ################################################################################    
            df2_H = df[df.Away == selecao1]
            porcentagem_team_H = n_H / len(df2_H)
            odd_team_H = round((1 / porcentagem_team_H),2)
            if len(df2_H) != 0:
                if odd_team_H != np.inf:
                    st.text("A Odd Média do " + selecao2 + " do " + selecao1 + " é: " + str((odd_team_H)))
                else:
                    st.text("A Odd Média do " + selecao2 + " do " + selecao1 + " é: 1000")
            else:
                pass
        except:
            pass

        try:
            ################################################################################
            # Odd Média da Liga
            ################################################################################

            df_league = df_H[df_H.Away == selecao1].copy()
            
            liga = df_league.iat[0,0] 

            try:
                df_liga = df[df['League'] == liga]
                
                df_liga2 = df_liga[df_liga[selecao2] == 1]
                n_liga = df_liga2[df_liga2.columns[0]].count()
                porcentagem_liga = n_liga / len(df_liga)
                odd_liga = round((1 / porcentagem_liga),2)
                
                if odd_liga != np.inf:
                    st.text("A Odd Média do " + selecao2 + " da Liga " + liga + " é: " + str((odd_liga)))
                else:
                    st.text("A Odd Média do " + selecao2 + " da Liga " + liga + " é: 1000")
            except:
                pass
        except:
            pass
        try:
            ################################################################################
            # Odd Atual na Betfair
            ################################################################################
            try:
                odd_atual = df_Home[df_Home.Away == selecao1].copy()
                placar = 'Odd_'+ selecao2
                odd_betfair = odd_atual[placar].tail(1).item()
                st.text("Odd Atual do Lay " + selecao2 + " do " + selecao1 + " na Betfair é: " + str(odd_betfair))
                st.markdown('---') 
            except:
                st.markdown('---') 
        except:
            st.markdown('---') 



        try:
            ################################################################################
            # Custo do Gol
            ################################################################################
            st.text("Média do Custo do Gol")

            lista_per = [5, 10, 20]
            p1,p2,p3,p4,p5 = st.columns(5)
            n_per = p1.selectbox('Número de Períodos', lista_per)

            tt = df.copy()
 
            try:
                # Probabilidades
                tt['p_H'] = 1 / tt.FT_Odd_H
                tt['p_D'] = 1 / tt.FT_Odd_D
                tt['p_A'] = 1 / tt.FT_Odd_A

                # n_per = 5

                # Custo do Gol 1.0
                tt['CG_01_H'] = tt.FT_Goals_H / tt.p_H
                tt['CG_01_A'] = tt.FT_Goals_A / tt.p_A

                tt['Media_CG_01_H'] = tt.groupby('Home')['CG_01_H'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)
                tt['Media_CG_01_A'] = tt.groupby('Away')['CG_01_A'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)

                tt['Media_CG_01_H'] = tt.groupby('Home')['Media_CG_01_H'].shift(1)
                tt['Media_CG_01_A'] = tt.groupby('Away')['Media_CG_01_A'].shift(1)

                tt['DesvPad_CG_01_H'] = tt.groupby('Home')['CG_01_H'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)
                tt['DesvPad_CG_01_A'] = tt.groupby('Away')['CG_01_A'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)

                tt['DesvPad_CG_01_H'] = tt.groupby('Home')['DesvPad_CG_01_H'].shift(1)
                tt['DesvPad_CG_01_A'] = tt.groupby('Away')['DesvPad_CG_01_A'].shift(1)

                tt['CV_CG_01_H'] = tt['DesvPad_CG_01_H'] / tt['Media_CG_01_H']
                tt['CV_CG_01_A'] = tt['DesvPad_CG_01_A'] / tt['Media_CG_01_A']

                # Custo do Gol 2.0
                tt['CG_02_H'] = (tt.p_H / 2) + (tt.FT_Goals_H / 2)
                tt['CG_02_A'] = (tt.p_A / 2) + (tt.FT_Goals_A / 2)

                tt['Media_CG_02_H'] = tt.groupby('Home')['CG_02_H'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)
                tt['Media_CG_02_A'] = tt.groupby('Away')['CG_02_A'].rolling(window=n_per, min_periods=n_per).mean().reset_index(0,drop=True)

                tt['Media_CG_02_H'] = tt.groupby('Home')['Media_CG_02_H'].shift(1)
                tt['Media_CG_02_A'] = tt.groupby('Away')['Media_CG_02_A'].shift(1)

                tt['DesvPad_CG_02_H'] = tt.groupby('Home')['CG_02_H'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)
                tt['DesvPad_CG_02_A'] = tt.groupby('Away')['CG_02_A'].rolling(window=n_per, min_periods=n_per).std(ddof=0).reset_index(0,drop=True)

                tt['DesvPad_CG_02_H'] = tt.groupby('Home')['DesvPad_CG_02_H'].shift(1)
                tt['DesvPad_CG_02_A'] = tt.groupby('Away')['DesvPad_CG_02_A'].shift(1)

                tt['CV_CG_02_H'] = tt['DesvPad_CG_02_H'] / tt['Media_CG_02_H']
                tt['CV_CG_02_A'] = tt['DesvPad_CG_02_A'] / tt['Media_CG_02_A']

                ttt = df_jogos[df_jogos.Home == selecao1].copy()
                zebra = df_Home.iat[0,4]
                home = zebra
                away = selecao1

                cg_h = tt[tt.Home == home].tail(1)
                media_cg_h = cg_h.iat[0,42]

                cv_cg_h = tt[tt.Home == home].tail(1)
                cv_h = cv_cg_h.iat[0,46]

                cg_a = tt[tt.Away == away].tail(1)
                media_cg_a = cg_a.iat[0,43]

                cv_cg_a = tt[tt.Away == away].tail(1)
                cv_a = cv_cg_a.iat[0,47]
                
                st.text('') 
                
                st.text(f'Índice de Eficiência (Coeficiente de Eficiência) - Ultimos {n_per} Jogos')
                
                # st.dataframe(cg_h) 
                # st.dataframe(cg_a) 
                st.text(f'{home} - CG: {round(media_cg_h,2)}, CV: {round(cv_h,2)}')
                st.text(f'{away} - CG: {round(media_cg_a,2)}, CV: {round(cv_a,2)}')

                cg_h2 = tt[tt.Home == home].tail(1)
                media_cg_h2 = cg_h2.iat[0,50]

                cv_cg_h2 = tt[tt.Home == home].tail(1)
                cv_h2 = cv_cg_h2.iat[0,54]

                cg_a2 = tt[tt.Away == away].tail(1)
                media_cg_a2 = cg_a2.iat[0,51]

                cv_cg_a2 = tt[tt.Away == away].tail(1)
                cv_a2 = cv_cg_a2.iat[0,55]
            
                st.text('')
                st.text('')
                st.text(f'Índice de Eficiência (Quociente de Eficiência) - Ultimos {n_per} Jogos')
                
                # st.dataframe(cg_h2) 
                # st.dataframe(cg_a2) 
                st.text(f'{home} - CG: {round(media_cg_h2,2)}, CV: {round(cv_h2,2)}')
                st.text(f'{away} - CG: {round(media_cg_a2,2)}, CV: {round(cv_a2,2)}')





                st.markdown('---')
            except:
                st.markdown('---')
        except:
                st.markdown('---')
















        try:
            ################################################################################
            # Análise Poseidon Away
            ################################################################################

            try:
                odd_atual = df_Home[df_Home.Away == selecao1].copy()
                
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

                st.text("Odds Correct Score Pré-Live")
                st.text("")

                odds1, odds2, odds3, odds4 = st.columns(4)

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

                st.text("")
                
                
                Ponta1 = odd_betfair_0x2 < odd_betfair_0x1
                Ponta2 = odd_betfair_0x2 < odd_betfair_1x1
                Ponta3 = odd_betfair_2x2 < odd_betfair_2x1
                
                # Condição Poseidon
                if ((Ponta1 == True) & (Ponta2 == True) & (Ponta3 == True)):
                    st.text("Poseidon")
                    # st.text("Ponta1 = odd_0x2 < odd_0x1")
                    # st.text("Ponta2 = odd_0x2 < odd_1x1")
                    # st.text("Ponta3 = odd_2x2 < odd_2x1")
                elif ((Ponta1 == True) & (Ponta2 == True)):
                    st.text("Ponta 1 e Ponta 2")
                    # st.text("Ponta1 = odd_0x2 < odd_0x1")
                    # st.text("Ponta2 = odd_0x2 < odd_1x1")
                elif ((Ponta1 == True) & (Ponta3 == True)):
                    st.text("Ponta 1 e Ponta 3")
                    # st.text("Ponta1 = odd_0x2 < odd_0x1")
                    # st.text("Ponta3 = odd_2x2 < odd_2x1")
                elif ((Ponta2 == True) & (Ponta3 == True)):
                    st.text("Ponta 2 e Ponta 3")
                    # st.text("Ponta2 = odd_0x2 < odd_1x1")
                    # st.text("Ponta3 = odd_2x2 < odd_2x1")
                elif (Ponta1 == True):
                    st.text("Ponta 1")
                    # st.text("Ponta1 = odd_0x2 < odd_0x1")
                elif (Ponta2 == True):
                    st.text("Ponta 2")
                    # st.text("Ponta2 = odd_0x2 < odd_1x1")
                elif (Ponta3 == True):
                    st.text("Ponta 3")
                    # st.text("Ponta3 = odd_2x2 < odd_2x1")
                else:
                    st.text("Nenhuma Ponta Satisfeita")


                st.markdown('---') 
            except:
                st.markdown('---') 
        except:
            st.markdown('---')

        try:
            ################################################################################
            # Ultimos 10 Jogos do Favorito como Visitante
            ################################################################################
            
            df_10_jogos_H = df[df.Away == selecao1].tail(10)
            df_10_jogos_H = df_10_jogos_H[['Date', 'Season','Home','Away','FT_Goals_H','FT_Goals_A','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','Odd_BTTS_Yes']]
            df_10_jogos_H.columns = ['Date','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']
            df_10_jogos_H.reset_index(inplace=True, drop=True)
            df_10_jogos_H.index = df_10_jogos_H.index.set_names(['Nº'])
            df_10_jogos_H = df_10_jogos_H.rename(index=lambda x: x + 1)
            df0 = df_10_jogos_H.copy()
                
            df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
            df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
            df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)
            df0['Odd_Over'] = df0['Odd_Over25'].astype(float).map('{:.2f}'.format)
            df0['Odd_BTTS'] = df0['Odd_BTTS_Yes'].astype(float).map('{:.2f}'.format)

            df0 = df0[['Date','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over','Odd_BTTS']]
            st.text("Ultimos 10 Jogos do Favorito como Visitante")
            st.dataframe(df0)
            st.markdown('---')
        except:
            st.markdown('---')
            
        try:
            ################################################################################
            # Ultimos 10 Jogos da Zebra como Mandante
            ################################################################################
            

            df_10_jogos_A = df_H[df_H.Away == selecao1].copy()
            zebra = df_10_jogos_A.iat[0,2]
            # st.write(zebra)
            df_10_jogos_A = df[df.Home == zebra].tail(10)
            
            df_10_jogos_A = df_10_jogos_A[['Date', 'Season','Home','Away','FT_Goals_H','FT_Goals_A','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','Odd_BTTS_Yes']]
            df_10_jogos_A.columns = ['Date','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']
            df_10_jogos_A.reset_index(inplace=True, drop=True)
            df_10_jogos_A.index = df_10_jogos_A.index.set_names(['Nº'])
            df_10_jogos_A = df_10_jogos_A.rename(index=lambda x: x + 1)
            df0 = df_10_jogos_A.copy()
                
            df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
            df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
            df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)
            df0['Odd_Over'] = df0['Odd_Over25'].astype(float).map('{:.2f}'.format)
            df0['Odd_BTTS'] = df0['Odd_BTTS_Yes'].astype(float).map('{:.2f}'.format)

            df0 = df0[['Date','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over','Odd_BTTS']]
            st.text("Ultimos 10 Jogos da Zebra como Mandante")
            st.dataframe(df0)
            st.markdown('---')
        except:
            st.markdown('---')
        try:

            ################################################################################
            # Confronto Direto
            ################################################################################
            
            df_Confronto = df_H[df_H.Away == selecao1].copy()
            zebra = df_Confronto.iat[0,2]
            df_Confronto = df[((df.Home == zebra) & (df.Away == selecao1))]
            df_Confronto = df_Confronto[['Date', 'Season','Home','Away','FT_Goals_H','FT_Goals_A','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','Odd_BTTS_Yes']]
            df_Confronto.columns = ['Date','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS_Yes']
            if len(df_Confronto) != 0:
                df0 = df_Confronto.copy()
                
                df0['Odd_H'] = df0['Odd_H'].astype(float).map('{:.2f}'.format)
                df0['Odd_D'] = df0['Odd_D'].astype(float).map('{:.2f}'.format)
                df0['Odd_A'] = df0['Odd_A'].astype(float).map('{:.2f}'.format)
                df0['Odd_Over'] = df0['Odd_Over25'].astype(float).map('{:.2f}'.format)
                df0['Odd_BTTS'] = df0['Odd_BTTS_Yes'].astype(float).map('{:.2f}'.format)

                df0 = df0[['Date','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over','Odd_BTTS']]
                st.text("Confronto Direto - Temporadas Passadas")
                df0 = drop_reset_index(df0)
                st.dataframe(df0)
                st.markdown('---')
            else:
                st.markdown('---')     
        except:
            st.markdown('---')

        try:

            # Classificação
            
            try:
                home = zebra
                away = selecao1
            

                flt = ((df_liga.Season == "2022/2023") | (df_liga.Season == '2022') )
                df_league = df_liga[flt]
                
                
                df_league = df_league[['Season','Home','Away','FT_Goals_H','FT_Goals_A']]
                df_league.columns = ['Season','Home','Away','Goals_H','Goals_A']
            
                df_league.loc[df_league['Goals_H'] > df_league['Goals_A'], 'Ptos_H'] = 3
                df_league.loc[df_league['Goals_H'] == df_league['Goals_A'], 'Ptos_H'] = 1
                df_league.loc[df_league['Goals_H'] < df_league['Goals_A'], 'Ptos_H'] = 0

                df_league.loc[df_league['Goals_H'] < df_league['Goals_A'], 'Ptos_A'] = 3
                df_league.loc[df_league['Goals_H'] == df_league['Goals_A'], 'Ptos_A'] = 1
                df_league.loc[df_league['Goals_H'] > df_league['Goals_A'], 'Ptos_A'] = 0

                teams = list(set(df_league['Home']).union(set(df_league['Away'])))
                classification_data = []

                for team in teams:
                    home_matches = df_league[df_league['Home'] == team]
                    away_matches = df_league[df_league['Away'] == team]
                    
                    total_matches = pd.concat([home_matches, away_matches])
                    points = (home_matches['Ptos_H'].sum()) + (away_matches['Ptos_A'].sum())
                    
                    classification_data.append({
                        'Team': team,
                        'Points': points})

                classification_df_league = pd.DataFrame(classification_data)
                classification_df_league = classification_df_league.sort_values(by=['Points'], ascending=False)
                classification_df_league = classification_df_league.dropna()
                classification_df_league = classification_df_league.reset_index(drop=True)
                classification_df_league.index += 1

                team1 = home  # Substitua pelo nome do primeiro time
                team2 = away  # Substitua pelo nome do segundo time

                # Filtrar as linhas correspondentes aos times desejados
                team1_row = classification_df_league.loc[classification_df_league['Team'] == team1]
                team2_row = classification_df_league.loc[classification_df_league['Team'] == team2]

                # Obter o número da classificação (índice + 1) para cada time
                team1_rank = team1_row.index[0] if not team1_row.empty else None
                team2_rank = team2_row.index[0] if not team2_row.empty else None

                if team1_rank == None:
                    st.text(f"{team1} não estava nessa divisão na temporada passada.")
                else:
                    st.text(f"{team1} terminou a temporada passada classificado em {team1_rank}º lugar.")
                if team2_rank == None:
                    st.text(f"{team2} não estava nessa divisão na temporada passada.")
                else:
                    st.text(f"{team2} terminou a temporada passada classificado em {team2_rank}º lugar.")      
                
                # st.markdown('---')

                # Classificação
                
                home = zebra
                away = selecao1
            

                flt = ((df_liga.Season == "2023/2024") | (df_liga.Season == '2023') )
                df_league = df_liga[flt]
                
                
                df_league = df_league[['Season','Home','Away','FT_Goals_H','FT_Goals_A']]
                df_league.columns = ['Season','Home','Away','Goals_H','Goals_A']
            
                df_league.loc[df_league['Goals_H'] > df_league['Goals_A'], 'Ptos_H'] = 3
                df_league.loc[df_league['Goals_H'] == df_league['Goals_A'], 'Ptos_H'] = 1
                df_league.loc[df_league['Goals_H'] < df_league['Goals_A'], 'Ptos_H'] = 0

                df_league.loc[df_league['Goals_H'] < df_league['Goals_A'], 'Ptos_A'] = 3
                df_league.loc[df_league['Goals_H'] == df_league['Goals_A'], 'Ptos_A'] = 1
                df_league.loc[df_league['Goals_H'] > df_league['Goals_A'], 'Ptos_A'] = 0

                teams = list(set(df_league['Home']).union(set(df_league['Away'])))
                classification_data = []

                for team in teams:
                    home_matches = df_league[df_league['Home'] == team]
                    away_matches = df_league[df_league['Away'] == team]
                    
                    total_matches = pd.concat([home_matches, away_matches])
                    points = (home_matches['Ptos_H'].sum()) + (away_matches['Ptos_A'].sum())
                    
                    classification_data.append({
                        'Team': team,
                        'Points': points})

                classification_df_league = pd.DataFrame(classification_data)
                classification_df_league = classification_df_league.sort_values(by=['Points'], ascending=False)
                classification_df_league = classification_df_league.dropna()
                classification_df_league = classification_df_league.reset_index(drop=True)
                classification_df_league.index += 1

                team1 = home  # Substitua pelo nome do primeiro time
                team2 = away  # Substitua pelo nome do segundo time

                # Filtrar as linhas correspondentes aos times desejados
                team1_row = classification_df_league.loc[classification_df_league['Team'] == team1]
                team2_row = classification_df_league.loc[classification_df_league['Team'] == team2]

                # Obter o número da classificação (índice + 1) para cada time
                team1_rank = team1_row.index[0] if not team1_row.empty else None
                team2_rank = team2_row.index[0] if not team2_row.empty else None

                if team1_rank == None:
                    st.text(f"{team1} mudou de divisão.")
                else:
                    st.text(f"{team1} está na temporada atual classificado em {team1_rank}º lugar.")
                if team2_rank == None:
                    st.text(f"{team2} mudou de divisão.")
                else:
                    st.text(f"{team2} está na temporada atual classificado em  {team2_rank}º lugar.")      
                
                st.markdown('---')
            except:
                st.markdown('---')



            ################################################################################
            # PDF do Theo
            ################################################################################
            
            try:
                home = zebra
                away = selecao1

                # df_xg = df_jogos[df_jogos.Home == home]

                # xg_h = df_xg['xG_Home_Pre'].iloc[0]
                # xg_a = df_xg['xG_Away_Pre'].iloc[0]
                # xg_tot = df_xg['xG_Total_Pre'].iloc[0]

                df.loc[df['FT_Goals_H'] > df['FT_Goals_A'], 'Ptos_H'] = 3
                df.loc[df['FT_Goals_H'] == df['FT_Goals_A'], 'Ptos_H'] = 1
                df.loc[df['FT_Goals_H'] < df['FT_Goals_A'], 'Ptos_H'] = 0


                df.loc[df['FT_Goals_H'] < df['FT_Goals_A'], 'Ptos_A'] = 3
                df.loc[df['FT_Goals_H'] == df['FT_Goals_A'], 'Ptos_A'] = 1
                df.loc[df['FT_Goals_H'] > df['FT_Goals_A'], 'Ptos_A'] = 0
                
                df['Media_Ptos_H1'] = df.groupby('Home')['Ptos_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
                df['Media_Ptos_A1'] = df.groupby('Away')['Ptos_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
                
                df['Media_Ptos_H2'] = df.groupby('Home')['Ptos_H'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True)
                df['Media_Ptos_A2'] = df.groupby('Away')['Ptos_A'].rolling(window=5, min_periods=1).mean().reset_index(0,drop=True)
                
                df.dropna(inplace=True)
                df.reset_index(inplace=True, drop=True)
                df.index = df.index.set_names(['Nº'])
                df = df.rename(index=lambda x: x + 1)
                
                flt = ((df.Season == "2022/2023") | (df.Season == "2023/2024") | (df.Season == '2023') )
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
                flt2_H = df_H.FT_Goals_H > df_H.FT_Goals_A
                df2_H = df_H[flt2_H]
                df2_H = df2_H.Home.count()
                
                flt2_A = df_A.FT_Goals_H < df_A.FT_Goals_A
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
                flt_gol_0_H = df_H.FT_Goals_A == 0
                df_gol_0_H = df_H[flt_gol_0_H]
                count_gol_0_H = df_gol_0_H.Home.count() 
                por_count_gol_0_H = round((round((count_gol_0_H / len(df_H)),2)*100))
                por_count_gol_0_H = str(por_count_gol_0_H)+'%'
                
                flt_gol_0_A = df_A.FT_Goals_H == 0
                df_gol_0_A = df_A[flt_gol_0_A]
                count_gol_0_A = df_gol_0_A.Away.count() 
                por_count_gol_0_A = round((round((count_gol_0_A / len(df_A)),2)*100))
                por_count_gol_0_A = str(por_count_gol_0_A)+'%'
                
                # Falhou em marcar
                flt_gol_failed_H = df_H.FT_Goals_H == 0
                df_gol_failed_H = df_H[flt_gol_failed_H]
                count_gol_failed_H = df_gol_failed_H.Home.count() 
                por_count_gol_failed_H = round((round((count_gol_failed_H / len(df_H)),2)*100))
                por_count_gol_failed_H = str(por_count_gol_failed_H)+'%'
                
                flt_gol_failed_A = df_A.FT_Goals_A == 0
                df_gol_failed_A = df_A[flt_gol_failed_A]
                count_gol_failed_A = df_gol_failed_A.Away.count() 
                por_count_gol_failed_A = round((round((count_gol_failed_A / len(df_A)),2)*100))
                por_count_gol_failed_A = str(por_count_gol_failed_A)+'%'
                
                # Ambas marcam
                flt_BTTS_H = (df_H.FT_Goals_H != 0) & (df_H.FT_Goals_A != 0)
                df_BTTS_H = df_H[flt_BTTS_H]
                count_BTTS_H = df_BTTS_H.Home.count() 
                por_count_BTTS_H = round((round((count_BTTS_H / len(df_H)),2)*100))
                por_count_BTTS_H = str(por_count_BTTS_H)+'%'
                
                flt_BTTS_A = (df_A.FT_Goals_H != 0) & (df_A.FT_Goals_A != 0)
                df_BTTS_A = df_A[flt_BTTS_A]
                count_BTTS_A = df_BTTS_A.Home.count() 
                por_count_BTTS_A = round((round((count_BTTS_A / len(df_A)),2)*100))
                por_count_BTTS_A = str(por_count_BTTS_A)+'%' 
                
                
                # Média de Gols em Casa
                
                # Gols Marcados   
                Goals_MH = df.groupby(['Home'])['FT_Goals_H'].get_group(home).sum()
                Goals_MH = int(Goals_MH)
                Goals_MA = df.groupby(['Away'])['FT_Goals_A'].get_group(away).sum()
                Goals_MA = int(Goals_MA)
                
                # Gols Sofridos
                Goals_SH = df.groupby(['Home'])['FT_Goals_A'].get_group(home).sum()
                Goals_SH = int(Goals_SH)
                Goals_SA = df.groupby(['Away'])['FT_Goals_H'].get_group(away).sum()
                Goals_SA = int(Goals_SA)
                
                # Média de gols marcados    
                mean_Goals_MH = df.groupby(['Home'])['FT_Goals_H'].get_group(home).mean()
                mean_Goals_MH = round(mean_Goals_MH,2)
                mean_Goals_MA = df.groupby(['Away'])['FT_Goals_A'].get_group(away).mean()
                mean_Goals_MA = round(mean_Goals_MA,2)
                
                # Média de gols sofridos    
                mean_Goals_SH = df.groupby(['Home'])['FT_Goals_A'].get_group(home).mean()
                mean_Goals_SH = round(mean_Goals_SH,2)
                mean_Goals_SA = df.groupby(['Away'])['FT_Goals_H'].get_group(away).mean()
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
                
                st.text('Aproveitamento dos Times - Mandante Jogando em Casa e Visitante Jogando Fora')
                st.text('')
                texto = home + ' x ' + away
                st.write("<center>{}</center>".format(texto), unsafe_allow_html=True)
                st.write('')
                




                
                col1, col2 = st.columns(2)

                with col1:
                    st.dataframe(df12)

                with col2:
                    st.dataframe(df34)

                st.markdown('---')  

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
                df_H_PrimeiroGol = df_H[['FT_Goals_H','FT_Goals_A','Goals_Minutes_Home','Goals_Minutes_Away']]
                df_H_PrimeiroGol['FT_TotalGoals'] = df_H_PrimeiroGol['FT_Goals_H'] + df_H_PrimeiroGol['FT_Goals_A'] 
                flt = df_H_PrimeiroGol.FT_TotalGoals != 0
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
                
                
                df_A_PrimeiroGol = df_A[['FT_Goals_H','FT_Goals_A','Goals_Minutes_Home','Goals_Minutes_Away']]
                df_A_PrimeiroGol['FT_TotalGoals'] = df_A_PrimeiroGol['FT_Goals_H'] + df_A_PrimeiroGol['FT_Goals_A'] 
                flt = df_A_PrimeiroGol.FT_TotalGoals != 0
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
                
                
                flt9 = marca_primeiro_H.FT_Goals_H > marca_primeiro_H.FT_Goals_A
                marcou_e_ganhou = marca_primeiro_H[flt9]
                df9 = len(marcou_e_ganhou) / len(marca_primeiro_H)
                df9 = round((df9*100),)
                total_df9 = str(df9)+'%'
                
                flt10 = marca_primeiro_A.FT_Goals_A > marca_primeiro_A.FT_Goals_H
                marcou_e_ganhou = marca_primeiro_A[flt10]
                df10 = len(marcou_e_ganhou) / len(marca_primeiro_A)
                df10 = round((df10*100),)
                total_df10 = str(df10)+'%'
                
                flt11 = marca_primeiro_H.FT_Goals_H == marca_primeiro_H.FT_Goals_A
                marcou_e_empatou = marca_primeiro_H[flt11]
                df11 = len(marcou_e_empatou) / len(marca_primeiro_H)
                df11 = round((df11*100),)
                total_df11 = str(df11)+'%'
                
                flt12 = marca_primeiro_A.FT_Goals_A == marca_primeiro_A.FT_Goals_H
                marcou_e_empatou = marca_primeiro_A[flt12]
                df12 = len(marcou_e_empatou) / len(marca_primeiro_A)
                df12 = round((df12*100),)
                total_df12 = str(df12)+'%'
                
                flt13 = marca_primeiro_H.FT_Goals_H < marca_primeiro_H.FT_Goals_A
                marcou_e_perdeu = marca_primeiro_H[flt13]
                df13 = len(marcou_e_perdeu) / len(marca_primeiro_H)
                df13 = round((df13*100),)
                total_df13 = str(df13)+'%'
                
                flt14 = marca_primeiro_A.FT_Goals_A < marca_primeiro_A.FT_Goals_H
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
                
                flt17 = leva_primeiro_H['FT_Goals_H'] > leva_primeiro_H['FT_Goals_A']
                levou_e_ganhou = leva_primeiro_H[flt17]
                df17 = len(levou_e_ganhou) / len(leva_primeiro_H)
                df17 = round((df17*100),)
                total_df17 = str(df17)+'%'
            
                
                flt18 = leva_primeiro_A['FT_Goals_A'] > leva_primeiro_A['FT_Goals_H']
                levou_e_ganhou = leva_primeiro_A[flt18]
                df18 = len(levou_e_ganhou) / len(leva_primeiro_A)
                df18 = round((df18*100),)
                total_df18 = str(df18)+'%'
                
                
                
                flt19 = leva_primeiro_H.FT_Goals_H == leva_primeiro_H.FT_Goals_A
                levou_e_empatou = leva_primeiro_H[flt19]
                df19 = len(levou_e_empatou) / len(leva_primeiro_H)
                df19 = round((df19*100),)
                total_df19 = str(df19)+'%'
                
                
                flt20 = leva_primeiro_A.FT_Goals_H == leva_primeiro_A.FT_Goals_A
                levou_e_empatou = leva_primeiro_A[flt20]
                df20 = len(levou_e_empatou) / len(leva_primeiro_A)
                df20 = round((df20*100),)
                total_df20 = str(df20)+'%'
                
                
                flt21 = leva_primeiro_H.FT_Goals_H < leva_primeiro_H.FT_Goals_A
                levou_e_perdeu = leva_primeiro_H[flt21]
                df21 = len(levou_e_perdeu) / len(leva_primeiro_H)
                df21 = round((df21*100),)
                total_df21 = str(df21)+'%'
                
                
                flt22 = leva_primeiro_A.FT_Goals_A < leva_primeiro_A.FT_Goals_H
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
                    & (df_H_PrimeiroGol.FT_Goals_H > df_H_PrimeiroGol.FT_Goals_A))
                        
                df_1T_02 = df_H_PrimeiroGol[flt_1T_02]
                num_1T_02 = len(df_1T_02) / len(df_H_PrimeiroGol)
                df_1T_02 = round((num_1T_02*100),)
                df_1T_02 = str(df_1T_02)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Empatou
                flt_1T_03 = ((df_H_PrimeiroGol.Goals_Minutes_Home < 46) 
                    & (df_H_PrimeiroGol.Goals_Minutes_Home < df_H_PrimeiroGol.Goals_Minutes_Away)
                    & (df_H_PrimeiroGol.FT_Goals_H == df_H_PrimeiroGol.FT_Goals_A))
                        
                df_1T_03 = df_H_PrimeiroGol[flt_1T_03]
                num_1T_03 = len(df_1T_03) / len(df_H_PrimeiroGol)
                df_1T_03 = round((num_1T_03*100),)
                df_1T_03 = str(df_1T_03)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Perdeu
                flt_1T_04 = ((df_H_PrimeiroGol.Goals_Minutes_Home < 46) 
                    & (df_H_PrimeiroGol.Goals_Minutes_Home < df_H_PrimeiroGol.Goals_Minutes_Away)
                    & (df_H_PrimeiroGol.FT_Goals_H < df_H_PrimeiroGol.FT_Goals_A))
                        
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
                            & (df_A_PrimeiroGol.FT_Goals_A > df_A_PrimeiroGol.FT_Goals_H))
                        
                df_1T_06 = df_A_PrimeiroGol[flt_1T_06]
                num_1T_06 = len(df_1T_06) / len(df_A_PrimeiroGol)
                df_1T_06 = round((num_1T_06*100),)
                df_1T_06 = str(df_1T_06)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Empatou
                flt_1T_07 = ((df_A_PrimeiroGol.Goals_Minutes_Away < 46) 
                            & (df_A_PrimeiroGol.Goals_Minutes_Away < df_A_PrimeiroGol.Goals_Minutes_Home)
                            & (df_A_PrimeiroGol.FT_Goals_A == df_A_PrimeiroGol.FT_Goals_H))
                        
                df_1T_07 = df_A_PrimeiroGol[flt_1T_07]
                num_1T_07 = len(df_1T_07) / len(df_A_PrimeiroGol)
                df_1T_07 = round((num_1T_07*100),)
                df_1T_07 = str(df_1T_07)+'%'
                
                
                # Marcou o Primeiro Gol no 1º Tempo e Perdeu
                flt_1T_08 = ((df_A_PrimeiroGol.Goals_Minutes_Away < 46) 
                            & (df_A_PrimeiroGol.Goals_Minutes_Away < df_A_PrimeiroGol.Goals_Minutes_Home)
                            & (df_A_PrimeiroGol.FT_Goals_A < df_A_PrimeiroGol.FT_Goals_H))
                        
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
                st.markdown('---')
                
            except:
                pass

            try:    
                 
                # Time Mandante - Gols Marcados
                
                min_gols_H = df_H[['FT_Goals_H','Goals_Minutes_Home']]
                flt = min_gols_H.FT_Goals_H != 0
                min_gols_H = min_gols_H[flt]
                min_gols_H = min_gols_H[['Goals_Minutes_Home']]
                
                # Time Mandante - Gols Sofridos
                
                min_gols_HS = df_H[['FT_Goals_A','Goals_Minutes_Away']]
                flt = min_gols_HS.FT_Goals_A != 0
                min_gols_HS = min_gols_HS[flt]
                min_gols_HS = min_gols_HS[['Goals_Minutes_Away']]
                
                # Time Visitante - Gols Marcados
                
                min_gols_A = df_A[['FT_Goals_A','Goals_Minutes_Away']]
                flt = min_gols_A.FT_Goals_A != 0
                min_gols_A = min_gols_A[flt]
                min_gols_A = min_gols_A[['Goals_Minutes_Away']]
                
                # Time Visitante - Gols Sofridos
                
                min_gols_AS = df_A[['FT_Goals_H','Goals_Minutes_Home']]
                flt = min_gols_AS.FT_Goals_H != 0
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
                
                
                
                df1 = pd.concat([df1,df2], axis=1)
                print('Minutos dos Gols -',home)

                
                df2 = pd.concat([df3,df4], axis=1)
                print('Minutos dos Gols -',away)

                col1, col2 = st.columns(2)

                with col1:
                    st.write('Minutos dos Gols -',home)
                    st.write(df1)

                with col2:
                    st.write('Minutos dos Gols -',away)
                    st.write(df2)

                st.markdown('---')        

            

                flt_Over05_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 0)
                df_Over05_H = df_H[flt_Over05_H]
                count_Over05_H = df_Over05_H.Home.count() 
                por_count_Over05_H = round((round((count_Over05_H / len(df_H)),2)*100))
                por_count_Over05_H = str(por_count_Over05_H)+'%'
                
                flt_Over05_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 0)
                df_Over05_A = df_A[flt_Over05_A]
                count_Over05_A = df_Over05_A.Away.count() 
                por_count_Over05_A = round((round((count_Over05_A / len(df_A)),2)*100))
                por_count_Over05_A = str(por_count_Over05_A)+'%'
                
                flt_Over15_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 1)
                df_Over15_H = df_H[flt_Over15_H]
                count_Over15_H = df_Over15_H.Home.count() 
                por_count_Over15_H = round((round((count_Over15_H / len(df_H)),2)*100))
                por_count_Over15_H = str(por_count_Over15_H)+'%'
                
                flt_Over15_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 1)
                df_Over15_A = df_A[flt_Over15_A]
                count_Over15_A = df_Over15_A.Away.count() 
                por_count_Over15_A = round((round((count_Over15_A / len(df_A)),2)*100))
                por_count_Over15_A = str(por_count_Over15_A)+'%'
                
                flt_Over25_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 2)
                df_Over25_H = df_H[flt_Over25_H]
                count_Over25_H = df_Over25_H.Home.count() 
                por_count_Over25_H = round((round((count_Over25_H / len(df_H)),2)*100))
                por_count_Over25_H = str(por_count_Over25_H)+'%'
                
                flt_Over25_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 2)
                df_Over25_A = df_A[flt_Over25_A]
                count_Over25_A = df_Over25_A.Away.count() 
                por_count_Over25_A = round((round((count_Over25_A / len(df_A)),2)*100))
                por_count_Over25_A = str(por_count_Over25_A)+'%'
                
                flt_Over35_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 3)
                df_Over35_H = df_H[flt_Over35_H]
                count_Over35_H = df_Over35_H.Home.count() 
                por_count_Over35_H = round((round((count_Over35_H / len(df_H)),2)*100))
                por_count_Over35_H = str(por_count_Over35_H)+'%'
                
                flt_Over35_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 3)
                df_Over35_A = df_A[flt_Over35_A]
                count_Over35_A = df_Over35_A.Away.count() 
                por_count_Over35_A = round((round((count_Over35_A / len(df_A)),2)*100))
                por_count_Over35_A = str(por_count_Over35_A)+'%'
                
                flt_Over45_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 4)
                df_Over45_H = df_H[flt_Over45_H]
                count_Over45_H = df_Over45_H.Home.count() 
                por_count_Over45_H = round((round((count_Over45_H / len(df_H)),2)*100))
                por_count_Over45_H = str(por_count_Over45_H)+'%'
                
                flt_Over45_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 4)
                df_Over45_A = df_A[flt_Over45_A]
                count_Over45_A = df_Over45_A.Away.count() 
                por_count_Over45_A = round((round((count_Over45_A / len(df_A)),2)*100))
                por_count_Over45_A = str(por_count_Over45_A)+'%'
                
                flt_Over55_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 5)
                df_Over55_H = df_H[flt_Over55_H]
                count_Over55_H = df_Over55_H.Home.count() 
                por_count_Over55_H = round((round((count_Over55_H / len(df_H)),2)*100))
                por_count_Over55_H = str(por_count_Over55_H)+'%'
                
                flt_Over55_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 5)
                df_Over55_A = df_A[flt_Over55_A]
                count_Over55_A = df_Over55_A.Away.count() 
                por_count_Over55_A = round((round((count_Over55_A / len(df_A)),2)*100))
                por_count_Over55_A = str(por_count_Over55_A)+'%'
                
                flt_Over65_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 6)
                df_Over65_H = df_H[flt_Over65_H]
                count_Over65_H = df_Over65_H.Home.count() 
                por_count_Over65_H = round((round((count_Over65_H / len(df_H)),2)*100))
                por_count_Over65_H = str(por_count_Over65_H)+'%'
                
                flt_Over65_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 6)
                df_Over65_A = df_A[flt_Over65_A]
                count_Over65_A = df_Over65_A.Away.count() 
                por_count_Over65_A = round((round((count_Over65_A / len(df_A)),2)*100))
                por_count_Over65_A = str(por_count_Over65_A)+'%'
                
                flt_Over75_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 7)
                df_Over75_H = df_H[flt_Over75_H]
                count_Over75_H = df_Over75_H.Home.count() 
                por_count_Over75_H = round((round((count_Over75_H / len(df_H)),2)*100))
                por_count_Over75_H = str(por_count_Over75_H)+'%'
                
                flt_Over75_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 7)
                df_Over75_A = df_A[flt_Over75_A]
                count_Over75_A = df_Over75_A.Away.count() 
                por_count_Over75_A = round((round((count_Over75_A / len(df_A)),2)*100))
                por_count_Over75_A = str(por_count_Over75_A)+'%'
                
                flt_Over85_H = ((df_H['FT_Goals_H'] + df_H['FT_Goals_A']) > 7)
                df_Over85_H = df_H[flt_Over85_H]
                count_Over85_H = df_Over85_H.Home.count() 
                por_count_Over85_H = round((round((count_Over85_H / len(df_H)),2)*100))
                por_count_Over85_H = str(por_count_Over85_H)+'%'
                
                flt_Over85_A = ((df_A['FT_Goals_H'] + df_A['FT_Goals_A']) > 7)
                df_Over85_A = df_A[flt_Over85_A]
                count_Over85_A = df_Over85_A.Away.count() 
                por_count_Over85_A = round((round((count_Over85_A / len(df_A)),2)*100))
                por_count_Over85_A = str(por_count_Over85_A)+'%'
                
                
                row_names = ['Over 0.5','Over 1.5','Over 2.5','Over 3.5','Over 4.5','Over 5.5','Over 6.5','Over 7.5','Over 8.5']
                df1 = pd.DataFrame([por_count_Over05_H,por_count_Over15_H,por_count_Over25_H,por_count_Over35_H,por_count_Over45_H,por_count_Over55_H,por_count_Over65_H,por_count_Over75_H,por_count_Over85_H], index=row_names, columns=['Home'])
                
                row_names = ['Over 0.5','Over 1.5','Over 2.5','Over 3.5','Over 4.5','Over 5.5','Over 6.5','Over 7.5','Over 8.5']
                df2 = pd.DataFrame([por_count_Over05_A,por_count_Over15_A,por_count_Over25_A,por_count_Over35_A,por_count_Over45_A,por_count_Over55_A,por_count_Over65_A,por_count_Over75_A,por_count_Over85_A], index=row_names, columns=['Away'])
                
                
                df0 = pd.concat([df1,df2], axis=1)
                st.write('Total de Gols')
                st.write(df0)
                st.markdown('---')
            except:
                pass
        except:
            pass












































































































    def lay_goleada():

        st.header("Lay Goleada")

        import datetime
        from datetime import date

        dia = st.date_input(
            "Data de Análise",
            date.today())

        key = "20e2d4aa7479a657c52935c4a743a626941b0a1f41b12156642dd7b62d893145"

    ################################################
    ########## Importando os Jogos do Dia ##########
    ################################################
        # @st.cache
        @st.cache_data
        def load_data_jogos():
            
            url1 = f"https://api.football-data-api.com/todays-matches?key={key}&date={dia}&page=1"
            data1 = requests.get(url1)
            resp = data1.json()['data']
            dados1 = pd.DataFrame.from_dict(resp)

            url2 = f"https://api.football-data-api.com/todays-matches?key={key}&date={dia}&page=2"
            data2 = requests.get(url2)
            resp = data2.json()['data']
            dados2 = pd.DataFrame.from_dict(resp)

            data_jogos = pd.concat([dados1, dados2],ignore_index=True)

            return data_jogos

        df_jogos = load_data_jogos()

        ligas_footystats = ['Argentina Primera División',
                            'Austria 2. Liga', 
                            'Austria Bundesliga',
                            'Belgium Pro League', 
                            'Brazil Serie A',
                            'Brazil Serie B', 
                            'Bulgaria First League',
                            'Chile Primera División', 
                            'China Chinese Super League',
                            'Croatia Prva HNL', 
                            'Czech Republic First League',
                            'Denmark Superliga', 
                            'Egypt Egyptian Premier League',
                            'England Championship', 
                            'England EFL League One',
                            'England EFL League Two', 
                            'England Premier League',
                            'Estonia Meistriliiga', 
                            'Finland Veikkausliiga', 
                            'France Ligue 1', 
                            'France Ligue 2',
                            'Germany 2. Bundesliga', 
                            'Germany Bundesliga',
                            'Greece Super League', 
                            'Iceland Úrvalsdeild', 
                            'Italy Serie A',
                            'Italy Serie B', 
                            'Japan J1 League', 
                            'Japan J2 League',
                            'Netherlands Eerste Divisie', 
                            'Netherlands Eredivisie',
                            'Norway Eliteserien', 
                            'Norway First Division',
                            'Paraguay Division Profesional', 
                            'Poland Ekstraklasa',
                            'Portugal Liga NOS', 
                            'Portugal LigaPro',
                            'Republic of Ireland Premier Division', 
                            'Romania Liga I',
                            'Scotland Premiership',
                            'Serbia SuperLiga', 
                            'Slovakia Super Liga', 
                            'Slovenia PrvaLiga',
                            'South Korea K League 1',
                            'South Korea K League 2', 
                            'Spain La Liga',
                            'Spain Segunda División', 
                            'Sweden Allsvenskan',
                            'Sweden Superettan', 
                            'Switzerland Challenge League',
                            'Switzerland Super League', 
                            'Turkey Süper Lig', 
                            'USA MLS',
                            'Uruguay Primera División', 
                            'Wales Welsh Premier League']
        
        
        
        df_jogos = df_jogos[['competition_id','season','date_unix','game_week','home_name','away_name','odds_ft_1','odds_ft_x','odds_ft_2','odds_ft_over25','odds_btts_yes']]
        df_jogos.columns = ['League','Season','Date','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_BTTS_Yes']
        df_jogos['Date'] = pd.to_datetime(df_jogos['Date'], unit='s') - pd.DateOffset(hours=3)
        df_jogos = df_jogos.dropna()
        df_jogos['Date'] = df_jogos['Date'].astype('str')
        df_jogos[['Date2','Time']] = df_jogos['Date'].str.split(' ',expand=True)
        df_jogos = df_jogos[['League','Season','Date2','Time','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_BTTS_Yes']]
        df_jogos.columns = ['League','Season','Date','Time','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_BTTS_Yes']
        
        rename_leagues(df_jogos)

        df_jogos = df_jogos[df_jogos['League'].isin(ligas_footystats) == True]

        df_jogos.reset_index(inplace=True, drop=True)
        df_jogos.index = df_jogos.index.set_names([''])
        df_jogos = df_jogos.rename(index=lambda x: x + 1)
        # st.write(df_jogos)
        df_rounded = df_jogos.round(2)

        # Filtros de Odds
        Odd_Min_Back_Fav = 1.50
        Odd_Max_Back_Fav = 2.20
        Odd_Min_Over25 = 1.50
        Odd_Max_Over25 = 2.20
        Odd_Min_BTTS = 1.50
        Odd_Max_BTTS = 2.20

        flt = (
                (df_jogos.FT_Odd_H >= Odd_Min_Back_Fav)  
            & (df_jogos.FT_Odd_H <= Odd_Max_Back_Fav) 
            & (df_jogos.FT_Odd_Over25 >= Odd_Min_Over25) 
            & (df_jogos.FT_Odd_Over25 <= Odd_Max_Over25) 
            & (df_jogos.FT_Odd_BTTS_Yes >= Odd_Min_BTTS)
            & (df_jogos.FT_Odd_BTTS_Yes <= Odd_Max_BTTS) 
            )

        df_LGP = df_jogos[flt]
        df_LGP = df_LGP[['Time','League','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_BTTS_Yes']]

        st.subheader("Entradas")

        for a,b,c,d in zip(df_LGP.League, df_LGP.Time, df_LGP.Home, df_LGP.Away):
                    
            liga = a
            hora = b
            mandante = c
            visitante = d

            if liga == "Argentina Primera División":
                id ="8595"
            if liga == "Australia A-League":
                id ="8008"
            if liga == "Austria 2. Liga":
                id ="7584"
            if liga == "Austria Bundesliga":
                id ="7890"
            if liga == "Belgium First Division B":
                id ="7572"
            if liga == "Belgium Pro League":
                id ="7544"
            if liga == "Brazil Serie A":
                id ="9035"
            if liga == "Brazil Serie B":
                id ="9042"
            if liga == "Brazil Serie C":
                id ="9087"
            if liga == "Bulgaria First League":
                id ="7483"
            if liga == "Chile Primera División":
                id ="8833"
            if liga == "China Chinese Super League":
                id ="9186"
            if liga == "Croatia Prva HNL":
                id ="7457"
            if liga == "Czech Republic First League":
                id ="7586"
            if liga == "Denmark Superliga":
                id ="7426"
            if liga == "Egypt Egyptian Premier League":
                id ="8520"
            if liga == "England Championship":
                id ="7593"
            if liga == "England EFL League One":
                id ="7570"
            if liga == "England EFL League Two":
                id ="7574"
            if liga == "England Premier League":
                id ="7704"
            if liga == "Estonia Meistriliiga":
                id ="8898"
            if liga == "Europe UEFA Champions League":
                id ="7455"
            if liga == "Finland Veikkausliiga":
                id ="8935"
            if liga == "France Ligue 1":
                id ="7500"
            if liga == "France Ligue 2":
                id ="7501"
            if liga == "Germany 2. Bundesliga":
                id ="7499"
            if liga == "Germany 3. Liga":
                id ="7591"
            if liga == "Germany Bundesliga":
                id ="7664"
            if liga == "Greece Super League":
                id ="7954"
            if liga == "Iceland Úrvalsdeild":
                id ="8784"
            if liga == "Italy Serie A":
                id ="7608"
            if liga == "Italy Serie B":
                id ="7864"
            if liga == "Japan J1 League":
                id ="8810"
            if liga == "Japan J2 League":
                id ="8811"
            if liga == "Netherlands Eerste Divisie":
                id ="7484"
            if liga == "Netherlands Eredivisie":
                id ="7482"
            if liga == "Norway Eliteserien":
                id ="8739"
            if liga == "Norway First Division":
                id ="8740"
            if liga == "Paraguay Division Profesional":
                id ="8783"
            if liga == "Poland Ekstraklasa":
                id ="7428"
            if liga == "Portugal Liga NOS":
                id ="7731"
            if liga == "Portugal LigaPro":
                id ="7732"
            if liga == "Republic of Ireland Premier Division":
                id ="8741"
            if liga == "Romania Liga I":
                id ="7663"
            if liga == "Russia Russian Premier League":
                id ="7573"
            if liga == "Scotland Premiership":
                id ="7494"
            if liga == "Serbia SuperLiga":
                id ="7492"
            if liga == "Slovakia Super Liga":
                id ="7958"
            if liga == "Slovenia PrvaLiga":
                id ="7526"
            if liga == "South America Copa Libertadores":
                id ="8781"
            if liga == "South Korea K League 1":
                id ="8899"
            if liga == "South Korea K League 2":
                id ="8938"
            if liga == "Spain La Liga":
                id ="7665"
            if liga == "Spain Segunda División":
                id ="7592"
            if liga == "Sweden Allsvenskan":
                id ="8737"
            if liga == "Sweden Superettan":
                id ="8738"
            if liga == "Switzerland Challenge League":
                id ="7496"
            if liga == "Switzerland Super League":
                id ="7504"
            if liga == "Turkey Süper Lig":
                id ="7768"
            if liga == "USA MLS":
                id ="8777"
            if liga == "Uruguay Primera División":
                id ="8937"
            if liga == "Wales Welsh Premier League":
                id ="7620"



            try:
                url = f"https://api.football-data-api.com/league-matches?key={key}&season_id={id}" 
                data = requests.get(url)
                resp = data.json()
                resp = data.json()['data']
                df = pd.DataFrame.from_dict(resp)
                df['League'] = liga 

                df = df[['League','season','status','date_unix','game_week','home_name','away_name','odds_ft_1','odds_ft_x','odds_ft_2','homeGoalCount','awayGoalCount','totalGoalCount','homeGoals','awayGoals','odds_ft_over05','odds_ft_over15','odds_ft_over25','odds_btts_yes','odds_btts_no','odds_1st_half_result_1','odds_1st_half_result_x','odds_1st_half_result_2','odds_1st_half_over05','odds_1st_half_over15','odds_1st_half_over25','ht_goals_team_a','ht_goals_team_b','HTGoalCount','team_a_shotsOnTarget','team_b_shotsOnTarget','team_a_shotsOffTarget','team_b_shotsOffTarget','team_a_shots','team_b_shots','odds_1st_half_under05','odds_1st_half_under15','odds_1st_half_under25','odds_ft_under05','odds_ft_under15','odds_ft_under25']]
                df.columns = ['League','Season','Status','Date','Rodada','Home','Away','FT_Odds_H','FT_Odds_D','FT_Odds_A','FT_Goals_H','FT_Goals_A','FT_TotalGoals','Goals_H_Minutes','Goals_A_Minutes','FT_Odds_Over05','FT_Odds_Over15','FT_Odds_Over25','FT_Odds_BTTS_Yes','FT_Odds_BTTS_No','HT_Odds_H','HT_Odds_D','HT_Odds_A','HT_Odds_Over05','HT_Odds_Over15','HT_Odds_Over25','HT_Goals_H','HT_Goals_A','HT_TotalGoals','ShotsOnTarget_H','ShotsOnTarget_A','ShotsOffTarget_H','ShotsOffTarget_A','Shots_H','Shots_A','HT_Odds_Under05','HT_Odds_Under15','HT_Odds_Under25','FT_Odds_Under05','FT_Odds_Under15','FT_Odds_Under25']
                df = df.dropna()
                df['Date'] = pd.to_datetime(df['Date'], unit='s') - pd.DateOffset(hours=3)
                df = df.sort_values(['Date'])
                flt = df.Status == 'complete'
                df = df[flt]
                df = df[['League','Season','Date','Rodada','Home','Away','HT_Odds_H','HT_Odds_D','HT_Odds_A','HT_Odds_Over05','HT_Odds_Over15','HT_Odds_Over25','HT_Odds_Under05','HT_Odds_Under15','HT_Odds_Under25','HT_Goals_H','HT_Goals_A','HT_TotalGoals','FT_Odds_H','FT_Odds_D','FT_Odds_A','FT_Odds_Over05','FT_Odds_Over15','FT_Odds_Over25','FT_Odds_Under05','FT_Odds_Under15','FT_Odds_Under25','FT_Goals_H','FT_Goals_A','FT_TotalGoals','FT_Odds_BTTS_Yes','FT_Odds_BTTS_No','Goals_H_Minutes','Goals_A_Minutes','ShotsOnTarget_H','ShotsOnTarget_A','ShotsOffTarget_H','ShotsOffTarget_A','Shots_H','Shots_A']]
                df.reset_index(inplace=True, drop=True)
                df.index = df.index.set_names(['Nº'])
                df = df.rename(index=lambda x: x + 1)
                df1 = df           

                Gols_Marcados_Home = df1[['Home','FT_Goals_H']].groupby('Home').sum()
                Gols_Marcados_Away = df1[['Away','FT_Goals_A']].groupby('Away').sum()
                Gols_Marcados = pd.concat([Gols_Marcados_Home, Gols_Marcados_Away],axis=1)
                Gols_Marcados['Gols_Marcados'] = Gols_Marcados.FT_Goals_H + Gols_Marcados.FT_Goals_A
                Gols_Marcados = Gols_Marcados[['Gols_Marcados']]
                Gols_Marcados.index = Gols_Marcados.index.set_names(['Time'])
                Gols_Marcados = Gols_Marcados.sort_values(['Gols_Marcados'], ascending=False)
                Gols_Marcados = Gols_Marcados.rename_axis('index').reset_index()
                Gols_Marcados.reset_index(inplace=True, drop=True)
                Gols_Marcados.index = Gols_Marcados.index.set_names(['Nº'])
                Gols_Marcados = Gols_Marcados.rename(index=lambda x: x + 1)
                Gols_Marcados.columns = ['Time','Gols Marcados']
        
                Gols_Sofridos_Home = df1[['Home','FT_Goals_A']].groupby('Home').sum()
                Gols_Sofridos_Away = df1[['Away','FT_Goals_H']].groupby('Away').sum()
                Gols_Sofridos = pd.concat([Gols_Sofridos_Home, Gols_Sofridos_Away],axis=1)
                Gols_Sofridos['Gols_Sofridos'] = Gols_Sofridos.FT_Goals_H + Gols_Sofridos.FT_Goals_A
                Gols_Sofridos = Gols_Sofridos[['Gols_Sofridos']]
                Gols_Sofridos.index = Gols_Sofridos.index.set_names(['Time'])
                Gols_Sofridos = Gols_Sofridos.sort_values(['Gols_Sofridos'], ascending=True)
                Gols_Sofridos = Gols_Sofridos.rename_axis('index').reset_index()
                Gols_Sofridos.reset_index(inplace=True, drop=True)
                Gols_Sofridos.index = Gols_Sofridos.index.set_names(['Nº'])
                Gols_Sofridos = Gols_Sofridos.rename(index=lambda x: x + 1)
                Gols_Sofridos.columns = ['Time','Gols Sofridos']        
                
                flt_goleada1 = (Gols_Marcados.index > 5) & (Gols_Marcados.index <=15);
                df_gol1 = Gols_Marcados[flt_goleada1]
                lista1 = (sorted(df_gol1['Time'].unique()));
                flt_goleada2 = (Gols_Sofridos.index <=15);
                df_gol2 = Gols_Sofridos[flt_goleada2]
                lista2 = (sorted(df_gol2['Time'].unique()));
                if mandante in lista1 and mandante in lista2 and visitante in lista1 and visitante in lista2:
                    st.text("Liga: " + liga)
                    st.text("Jogo: " + mandante + " x " + visitante)
                    st.text("Horário: " + str(hora))
                    st.text("---")
                else:
                    pass
            except:
                pass
        
            

        st.text("Good Luke!!!")





        





































    def singularidades():

        st.header("Singularidades")

    ################################################
    ########## Importando a Base de Dados ##########
    ################################################
        # @st.cache
        @st.cache_data
        def load_data():

            base_singulares = pd.read_csv("./Bases/x_Singularidades_FootyStats_x.csv")
            
            return base_singulares

       
        df1 = load_data()
        
        dia = st.date_input(
            "Data de Análise",
            date.today())

        key = "20e2d4aa7479a657c52935c4a743a626941b0a1f41b12156642dd7b62d893145"

    ################################################
    ########## Importando os Jogos do Dia ##########
    ################################################
        # @st.cache
        @st.cache_data
        def load_data_jogos():
            
            url1 = f"https://api.football-data-api.com/todays-matches?key={key}&date={dia}&page=1"
            data1 = requests.get(url1)
            resp = data1.json()['data']
            dados1 = pd.DataFrame.from_dict(resp)

            url2 = f"https://api.football-data-api.com/todays-matches?key={key}&date={dia}&page=2"
            data2 = requests.get(url2)
            resp = data2.json()['data']
            dados2 = pd.DataFrame.from_dict(resp)

            data_jogos = pd.concat([dados1, dados2],ignore_index=True)

            return data_jogos

        df_jogos = load_data_jogos()

        ligas_footystats = ['Argentina Primera División',
                            'Austria 2. Liga', 
                            'Austria Bundesliga',
                            'Belgium Pro League', 
                            'Brazil Serie A',
                            'Brazil Serie B', 
                            'Bulgaria First League',
                            'Chile Primera División', 
                            'China Chinese Super League',
                            'Croatia Prva HNL', 
                            'Czech Republic First League',
                            'Denmark Superliga', 
                            'Egypt Egyptian Premier League',
                            'England Championship', 
                            'England EFL League One',
                            'England EFL League Two', 
                            'England Premier League',
                            'Estonia Meistriliiga', 
                            'Finland Veikkausliiga', 
                            'France Ligue 1', 
                            'France Ligue 2',
                            'Germany 2. Bundesliga', 
                            'Germany Bundesliga',
                            'Greece Super League', 
                            'Iceland Úrvalsdeild', 
                            'Italy Serie A',
                            'Italy Serie B', 
                            'Japan J1 League', 
                            'Japan J2 League',
                            'Netherlands Eerste Divisie', 
                            'Netherlands Eredivisie',
                            'Norway Eliteserien', 
                            'Norway First Division',
                            'Paraguay Division Profesional', 
                            'Poland Ekstraklasa',
                            'Portugal Liga NOS', 
                            'Portugal LigaPro',
                            'Republic of Ireland Premier Division', 
                            'Romania Liga I',
                            'Scotland Premiership',
                            'Serbia SuperLiga', 
                            'Slovakia Super Liga', 
                            'Slovenia PrvaLiga',
                            'South Korea K League 1',
                            'South Korea K League 2', 
                            'Spain La Liga',
                            'Spain Segunda División', 
                            'Sweden Allsvenskan',
                            'Sweden Superettan', 
                            'Switzerland Challenge League',
                            'Switzerland Super League', 
                            'Turkey Süper Lig', 
                            'USA MLS',
                            'Uruguay Primera División', 
                            'Wales Welsh Premier League']
        
        
        
        df_jogos = df_jogos[['competition_id','season','date_unix','game_week','home_name','away_name','odds_ft_1','odds_ft_x','odds_ft_2','odds_ft_over25','odds_btts_yes']]
        df_jogos.columns = ['League','Season','Date','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_BTTS_Yes']
        df_jogos['Date'] = pd.to_datetime(df_jogos['Date'], unit='s') - pd.DateOffset(hours=3)
        df_jogos = df_jogos.dropna()
        df_jogos['Date'] = df_jogos['Date'].astype('str')
        df_jogos[['Date2','Time']] = df_jogos['Date'].str.split(' ',expand=True)
        df_jogos = df_jogos[['League','Season','Date2','Time','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_BTTS_Yes']]
        df_jogos.columns = ['League','Season','Date','Time','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_BTTS_Yes']
        
        rename_leagues(df_jogos)

        df_jogos = df_jogos[df_jogos['League'].isin(ligas_footystats) == True]

        df_jogos.reset_index(inplace=True, drop=True)
        df_jogos.index = df_jogos.index.set_names([''])
        df_jogos = df_jogos.rename(index=lambda x: x + 1)
        
        lista = ['0x0','0x1','0x2','0x3','1x0','1x1','1x2','1x3','2x0','2x1','2x2','2x3','3x0','3x1','3x2','3x3','Goleada_H','Goleada_A']

        j1, j2 = st.columns(2)
        selecao1 = j1.selectbox('Escolha o Placar', lista) 

        df_today = df_jogos

        st.subheader("Entradas")

        for a,b in zip(df_today.Home,df_today.Away):
            home = a
            away = b
            
            ########## Placar 0x0 ##########
            # Home
            sing_H = df1[df1.Home == home].copy()
            sing_H = sing_H[sing_H[selecao1] == 1]
            n_sing_H = sing_H[sing_H.columns[0]].count()
            # Away
            sing_A = df1[df1.Away == away].copy()
            sing_A = sing_A[sing_A[selecao1] == 1]
            n_sing_A = sing_A[sing_A.columns[0]].count()
            # Home x Away
            sing_HxA = df1[(df1.Home == home) & (df1.Away == away)].copy()
            sing_HxA = sing_HxA[sing_HxA[selecao1] == 1]
            n_sing_HxA = sing_HxA[sing_HxA.columns[0]].count()
            if (n_sing_A == 0) & (n_sing_H == 0) & (n_sing_HxA == 0):
                st.text('O Placar ' + selecao1 +' no jogo ' + home + ' x ' + away + ' é Singular.')
            else:
                pass

        
            
            #st.text("---")
        
        st.text("Good Luke!!!")




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def sing_odd_1000():

        st.header("Odd 1000")

    ################################################
    ########## Importando a Base de Dados ##########
    ################################################
        # @st.cache
        @st.cache_data
        def load_data():

            base_singulares = pd.read_csv("./Bases/x_Luke_FootyStats_x.csv")
            
            return base_singulares

       
        base = load_data()
        
        dia = st.date_input(
            "Data de Análise",
            date.today())

        key = "20e2d4aa7479a657c52935c4a743a626941b0a1f41b12156642dd7b62d893145"

    ################################################
    ########## Importando os Jogos do Dia ##########
    ################################################
        # @st.cache
        @st.cache_data
        def load_data_jogos():
            
            url1 = f"https://api.football-data-api.com/todays-matches?key={key}&date={dia}&page=1"
            data1 = requests.get(url1)
            resp = data1.json()['data']
            dados1 = pd.DataFrame.from_dict(resp)

            url2 = f"https://api.football-data-api.com/todays-matches?key={key}&date={dia}&page=2"
            data2 = requests.get(url2)
            resp = data2.json()['data']
            dados2 = pd.DataFrame.from_dict(resp)

            data_jogos = pd.concat([dados1, dados2],ignore_index=True)

            return data_jogos

        df_jogos = load_data_jogos()

        ligas_footystats = ['Argentina Primera División',
                            'Austria 2. Liga', 
                            'Austria Bundesliga',
                            'Belgium Pro League', 
                            'Brazil Serie A',
                            'Brazil Serie B', 
                            'Bulgaria First League',
                            'Chile Primera División', 
                            'China Chinese Super League',
                            'Croatia Prva HNL', 
                            'Czech Republic First League',
                            'Denmark Superliga', 
                            'Egypt Egyptian Premier League',
                            'England Championship', 
                            'England EFL League One',
                            'England EFL League Two', 
                            'England Premier League',
                            'Estonia Meistriliiga', 
                            'Finland Veikkausliiga', 
                            'France Ligue 1', 
                            'France Ligue 2',
                            'Germany 2. Bundesliga', 
                            'Germany Bundesliga',
                            'Greece Super League', 
                            'Iceland Úrvalsdeild', 
                            'Italy Serie A',
                            'Italy Serie B', 
                            'Japan J1 League', 
                            'Japan J2 League',
                            'Netherlands Eerste Divisie', 
                            'Netherlands Eredivisie',
                            'Norway Eliteserien', 
                            'Norway First Division',
                            'Paraguay Division Profesional', 
                            'Poland Ekstraklasa',
                            'Portugal Liga NOS', 
                            'Portugal LigaPro',
                            'Republic of Ireland Premier Division', 
                            'Romania Liga I',
                            'Scotland Premiership',
                            'Serbia SuperLiga', 
                            'Slovakia Super Liga', 
                            'Slovenia PrvaLiga',
                            'South Korea K League 1',
                            'South Korea K League 2', 
                            'Spain La Liga',
                            'Spain Segunda División', 
                            'Sweden Allsvenskan',
                            'Sweden Superettan', 
                            'Switzerland Challenge League',
                            'Switzerland Super League', 
                            'Turkey Süper Lig', 
                            'USA MLS',
                            'Uruguay Primera División', 
                            'Wales Welsh Premier League']
        
        
        
        df_jogos = df_jogos[['competition_id','season','date_unix','game_week','home_name','away_name','odds_ft_1','odds_ft_x','odds_ft_2','odds_ft_over25','odds_btts_yes']]
        df_jogos.columns = ['League','Season','Date','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_BTTS_Yes']
        df_jogos['Date'] = pd.to_datetime(df_jogos['Date'], unit='s') - pd.DateOffset(hours=3)
        df_jogos = df_jogos.dropna()
        df_jogos['Date'] = df_jogos['Date'].astype('str')
        df_jogos[['Date2','Time']] = df_jogos['Date'].str.split(' ',expand=True)
        df_jogos = df_jogos[['League','Season','Date2','Time','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_BTTS_Yes']]
        df_jogos.columns = ['League','Season','Date','Time','Rodada','Home','Away','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_BTTS_Yes']
        
        rename_leagues(df_jogos)

        df_jogos = df_jogos[df_jogos['League'].isin(ligas_footystats) == True]

        df_jogos.reset_index(inplace=True, drop=True)
        df_jogos.index = df_jogos.index.set_names([''])
        df_jogos = df_jogos.rename(index=lambda x: x + 1)

        lista = ['0x0','0x1','0x2','0x3','1x0','1x1','1x2','1x3','2x0','2x1','2x2','2x3','3x0','3x1','3x2','3x3','Goleada_H','Goleada_A']
                
        j1, j2 = st.columns(2)
        selecao1 = j1.selectbox('Escolha o Placar', lista) 
        st.markdown('---')



        df_today = df_jogos

        #selecao1 = home
        st.subheader("Placares com Odd 1000")
        
        for a,b,c in zip(df_today.League,df_today.Home,df_today.Away):

            liga = a
            home = b
            away = c

            flt = base.League == liga 
            df = base[flt]

            df_f = df[(df['Home'] == home)]
            df_filtrado = df_f[(df_f[selecao1] == 1)]
            df_filtrado = df_filtrado[['Date','League','Season','Home','Away','FT_Goals_H','FT_Goals_A','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_BTTS_Yes']]
            df_filtrado.columns = ['Date','League','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS']
            df_filtrado.reset_index(inplace=True, drop=True)
            df_filtrado.index = df_filtrado.index.set_names(['Nº'])
            df_filtrado = df_filtrado.rename(index=lambda x: x + 1)

            n_H = df_filtrado[df_filtrado.columns[0]].count()
            df2_H = df[df.Home == home]
            porcentagem_team_H = n_H / len(df2_H)
            odd_team_H = 1 / porcentagem_team_H

            df_f = df[(df['Away'] == away)]
            df_filtrado = df_f[(df_f[selecao1] == 1)]
            df_filtrado = df_filtrado[['Date','League','Season','Home','Away','FT_Goals_H','FT_Goals_A','FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','FT_Odd_BTTS_Yes']]
            df_filtrado.columns = ['Date','League','Season','Home','Away','Goals_H','Goals_A','Odd_H','Odd_D','Odd_A','Odd_Over25','Odd_BTTS']
            df_filtrado.reset_index(inplace=True, drop=True)
            df_filtrado.index = df_filtrado.index.set_names(['Nº'])
            df_filtrado = df_filtrado.rename(index=lambda x: x + 1)

            n_A = df_filtrado[df_filtrado.columns[0]].count()
            df2_A = df[df.Away == away]
            porcentagem_team_A = n_A / len(df2_A)
            odd_team_A = 1 / porcentagem_team_A

            if ((odd_team_H == np.inf) & (odd_team_A == np.inf)):
                st.text("O Placar "+ selecao1 +" no jogo " + home + " x " + away + " é Odd 1000.")
  
        st.text("")
        st.text("Good Luke!!!")



    #################################################
    ################# Jogos do Dia ##################
    #################################################
    
    def h2h():
        
        # st.image('logo.jpg', width=250)
        st.header("Luke")
        st.subheader("Head To Head")

        ########## Importando os Jogos do Dia ##########

        # @st.cache
        @st.cache_data
        def load_data():

            base = pd.read_csv("./Bases/x_Singularidades_x.csv")
            
            return base

        df = load_data()

        flt = ((df.Season == "2022/2023") | (df.Season == "2023"))
        df = df[flt]

        teams = df.sort_values(['Home'])
        teams =  teams['Home'].unique()

        c1, c2 = st.columns(2)
        selecao_H = c1.selectbox('Escolha o Mandante', teams) 
        selecao_A = c2.selectbox('Escolha o Visitante', teams)

        home = selecao_H
        away = selecao_A


        # Média de Gols em Casa
        
        # Gols Marcados   
        Goals_MH = df.groupby(['Home'])['FT_Goals_H'].get_group(home).sum()
        Goals_MH = int(Goals_MH)
        Goals_MH = f'{Goals_MH:.0f}'
        Goals_MA = df.groupby(['Away'])['FT_Goals_A'].get_group(away).sum()
        Goals_MA = int(Goals_MA)
        Goals_MA = f'{Goals_MA:.0f}'

        # Gols Sofridos
        Goals_SH = df.groupby(['Home'])['FT_Goals_A'].get_group(home).sum()
        Goals_SH = int(Goals_SH)
        Goals_SA = df.groupby(['Away'])['FT_Goals_H'].get_group(away).sum()
        Goals_SA = int(Goals_SA)

        # Gols Total
        Goals_TH = int(Goals_MH) + int(Goals_SH)
        Goals_TA = int(Goals_MA) + int(Goals_SA)
        
        # Média de gols marcados    
        mean_Goals_MH = df.groupby(['Home'])['FT_Goals_H'].get_group(home).mean()
        mean_Goals_MH = float(round(mean_Goals_MH,2))
        mean_Goals_MA = df.groupby(['Away'])['FT_Goals_A'].get_group(away).mean()
        mean_Goals_MA = float(round(mean_Goals_MA,2))
        
        # Média de gols sofridos    
        mean_Goals_SH = df.groupby(['Home'])['FT_Goals_A'].get_group(home).mean()
        mean_Goals_SH = float(round(mean_Goals_SH,2))
        mean_Goals_SA = df.groupby(['Away'])['FT_Goals_H'].get_group(away).mean()
        mean_Goals_SA = float(round(mean_Goals_SA,2))

        # Média total de gols 
        mean_Goals_TH = round((mean_Goals_MH + mean_Goals_SH),2)
        #mean_Goals_TH = f'{mean_Goals_TH:.2f}'
        mean_Goals_TA = round((mean_Goals_MA + mean_Goals_SA),2)
        #mean_Goals_TA = f'{mean_Goals_TA:.2f}'

        row_names = ['Gols Marcados','Gols Sofridos','Gols Total','Média Gols Marcados','Média Gols Sofridos','Média Total Gols']
        df1 = pd.DataFrame([Goals_MH,Goals_SH,Goals_TH,mean_Goals_MH,mean_Goals_SH,mean_Goals_TH], index=row_names, columns=['Home'])
        
        row_names = ['Gols Marcados','Gols Sofridos','Gols Total','Média Gols Marcados','Média Gols Sofridos','Média Total Gols']
        df2 = pd.DataFrame([Goals_MA,Goals_SA,Goals_TA,mean_Goals_MA,mean_Goals_SA,mean_Goals_TA], index=row_names, columns=['Away'])
        
        df12 = pd.concat([df1,df2], axis=1)

        col1, col2 = st.columns(2)

        with col1:
            st.write(df1)

        with col2:
            st.write(df2)





        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def backtest():
        
        st.header("Luke")
        st.subheader("Backtesting")

        ########## Importando os Jogos do Dia ##########

        # @st.cache
        @st.cache_data
        def load_data():

            base = pd.read_csv("./Bases/futpythontraderpunter.csv")
            
            return base

        df = load_data()
        df = df[['Date','League','Season','Home','Away','HT_Goals_H','HT_Goals_A','FT_Goals_H','FT_Goals_A',
                'FT_Odd_H','FT_Odd_D','FT_Odd_A',
                'HT_Odd_Over05','HT_Odd_Under05','FT_Odd_Over05','FT_Odd_Under05','FT_Odd_Over15','FT_Odd_Under15',
                'FT_Odd_Over25','FT_Odd_Under25','FT_Odd_Over35','FT_Odd_Under35','FT_Odd_Over45','FT_Odd_Under45',
                'Odd_BTTS_Yes','Odd_BTTS_No','Odd_AH_Neg05_H','Odd_AH_Pos05_A','Odd_AH_Pos05_H','Odd_AH_Neg05_A',
                'CS_0x0','CS_0x1','CS_0x2','CS_0x3',
                'CS_1x0','CS_1x1','CS_1x2','CS_1x3',
                'CS_2x0','CS_2x1','CS_2x2','CS_2x3',
                'CS_3x0','CS_3x1','CS_3x2','CS_3x3','CS_4x4',
                'Goals_Minutes_Home','Goals_Minutes_Away']]

        # Filtro por Temporada (mesmo código da função anterior)
        sorted_seasons = sorted(df['Season'].unique())
        sorted_seasons.insert(0, "Todas as Temporadas")
        selected_seasons = st.multiselect('Filtrar por Temporada:', sorted_seasons, default="Todas as Temporadas")
        
        # Filtro de Liga
        sorted_leagues = sorted(df['League'].unique())
        sorted_leagues.insert(0, "Todas as Ligas")
        selected_leagues = st.multiselect('Filtrar por Liga:', sorted_leagues, default="Todas as Ligas")

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



        
        # temporada = st.selectbox('Temporada', df['Season'].unique())

        # Filtrando os dados da liga e temporada selecionadas
        # df = df[(df['League'] == liga) & (df['Season'] == temporada)]

        # # Adicionando campos para selecionar as variáveis
        # variaveis = st.multiselect('Variáveis', df.columns)

        # # Botão para calcular o lucro acumulado
        # if st.button('Calcular'):
        #     # Filtrando os dados com as variáveis selecionadas
        #     df = df[variaveis]

        #     # Calculando o lucro acumulado
        #     lucro_acumulado = df['lucro'].cumsum()

        #     # Mostrando o resultado do cálculo
        #     st.write(f'Lucro acumulado: {lucro_acumulado.iloc[-1]}')




















   
    


    def bases_de_dados():

        st.header("Luke")
        st.subheader("Bases de Dados")

        # @st.cache
        @st.cache_data
        def load_data():

            base = pd.read_csv('./Bases/futpythontraderpunter.csv')
            
            return base

        df = load_data()
  
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
            base_full = filtered_df[['Date','Time','League','Season','Round','Home','Away','HT_Goals_H','HT_Goals_A','FT_Goals_H','FT_Goals_A',
                                     'FT_Odd_H','FT_Odd_D','FT_Odd_A',
                                     'HT_Odd_Over05','HT_Odd_Under05','FT_Odd_Over05','FT_Odd_Under05','FT_Odd_Over15','FT_Odd_Under15',
                                     'FT_Odd_Over25','FT_Odd_Under25','FT_Odd_Over35','FT_Odd_Under35','FT_Odd_Over45','FT_Odd_Under45',
                                     'Odd_BTTS_Yes','Odd_BTTS_No','Odd_AH_Neg05_H','Odd_AH_Pos05_A','Odd_AH_Pos05_H','Odd_AH_Neg05_A',
                                     'CS_0x0','CS_0x1','CS_0x2','CS_0x3',
                                     'CS_1x0','CS_1x1','CS_1x2','CS_1x3',
                                     'CS_2x0','CS_2x1','CS_2x2','CS_2x3',
                                     'CS_3x0','CS_3x1','CS_3x2','CS_3x3','CS_4x4',
                                     'Goals_Minutes_Home','Goals_Minutes_Away']]
            # Renomear as colunas do DataFrame
            df0 = base_full.copy()
            df0 = df0[['Date','League','Season','Home','Away','FT_Goals_H','FT_Goals_A',
                               'FT_Odd_H','FT_Odd_D','FT_Odd_A']]
            df0.columns = ['Date', 'League', 'Season', 'Home', 'Away', 
                            'Goals_H', 'Goals_A', 'Odd_H', 'Odd_D', 'Odd_A']
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

    def machine_learning():
        
        st.header("Luke")
        st.subheader("Machine Learning")

        # @st.cache
        @st.cache_data
        def load_data():
            
            base = pd.read_csv('./Bases/futpythontraderpunter.csv')
            
            return base

        df = load_data()
     
        
        # Money Finder
        def money_finder(data,columns,target,divisions,min_jogos):
            # Define the main function
            def find_value(data,column,target,divisions):
                interval = (data[column].max() - data[column].min())/ divisions
                list_interval = list(np.arange(data[column].min(),data[column].max() + interval,interval))
                best_value = data[target].sum()
                best_data = data.copy()
                for x_min in list_interval[:-1]:
                    for x_max in list_interval[list_interval.index(x_min)+1:]:
                        some_data = data[data[column].between(x_min,x_max)]
                        value = some_data[target].sum()
                        if value > best_value:
                            best_value = value
                            best_data = some_data
                return (best_value,best_data,best_data.shape[0])
            best_value = data[target].sum()
            best_data = data.copy()
            df_parametros = pd.DataFrame()
            for column in columns:
                parameters = {}
                values = find_value(data = best_data,column=column,target=target,divisions=divisions)
                if (values[0] > best_value) & (values[2]>= min_jogos):
                    best_value = values[0]
                    best_data = values[1]
                    for coluna in columns:
                        parameters[f'{coluna.lower()}_min'] = best_data[coluna].min()
                        parameters[f'{coluna.lower()}_max'] = best_data[coluna].max()
                    parameters['n_games'] = values[2]
                    parameters['value'] = best_value
                    parameters = pd.DataFrame(parameters,index=[0])
                    df_parametros = pd.concat([df_parametros,parameters],ignore_index=True)
                    df_parametros = df_parametros.sort_values('value',ascending=False)
                    df_parametros = df_parametros.iloc[:10]
            return df_parametros
        
        # Dataframe Filtrado
        def retorna_df(dicionario,data):
            data = data.copy()
            list_columns = dicionario.keys()
            for i in data.columns.to_list():
                for x in list_columns:
                    if i.lower() in x:
                        try:
                            x_min = dicionario[f'{i.lower()}_min']
                            x_max = dicionario[f'{i.lower()}_max']
                            data = data[data[i].between(x_min,x_max)]
                        except:
                            pass
            return data
        
        # Gráfico
        def grafico(dataframe,target):
            dataframe = dataframe.copy()
            dataframe.reset_index(drop=True,inplace=True)
            dataframe['Target_Acum'] = dataframe[target].cumsum()
            roi = dataframe[target].sum()/dataframe.shape[0]
            profit = dataframe[target].sum()
            dataframe['Target_Acum'].plot(title=f'ROI = {round(roi*100,2)} % \nProfit = {round(profit,2)} Stakes',xlabel=f'{dataframe.shape[0]} Entradas')
        
        
        
        df['FT_Odd_H'] = df['FT_Odd_H'].astype(float)
        df['FT_Odd_D'] = df['FT_Odd_D'].astype(float)
        df['FT_Odd_A'] = df['FT_Odd_A'].astype(float)
        df['FT_Odd_Over25'] = df['FT_Odd_Over25'].astype(float)
        df['Odd_BTTS_Yes'] = df['Odd_BTTS_Yes'].astype(float)
        df = df[['Date', 'League', 'Season', 'Home', 'Away', 'FT_Goals_H', 'FT_Goals_A', 'FT_Odd_H', 'FT_Odd_D', 'FT_Odd_A', 'FT_Odd_Over25', 'Odd_BTTS_Yes']]

        # Probabilidades
        df['p_H'] = 1 / df.FT_Odd_H
        df['p_D'] = 1 / df.FT_Odd_D
        df['p_A'] = 1 / df.FT_Odd_A
        
        # Pontos
        df.loc[df['FT_Goals_H'] > df['FT_Goals_A'], 'Ptos_H'] = 3
        df.loc[df['FT_Goals_H'] == df['FT_Goals_A'], 'Ptos_H'] = 1
        df.loc[df['FT_Goals_H'] < df['FT_Goals_A'], 'Ptos_H'] = 0

        df.loc[df['FT_Goals_H'] < df['FT_Goals_A'], 'Ptos_A'] = 3
        df.loc[df['FT_Goals_H'] == df['FT_Goals_A'], 'Ptos_A'] = 1
        df.loc[df['FT_Goals_H'] > df['FT_Goals_A'], 'Ptos_A'] = 0

        df["Ptos_H"] = df["Ptos_H"].astype('int64')
        df["Ptos_A"] = df["Ptos_A"].astype('int64')

        df['Media_Ptos_H'] = df.groupby('Home')['Ptos_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
        df['Media_Ptos_A'] = df.groupby('Away')['Ptos_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)

        df['Media_Ptos_H'] = df.groupby('Home')['Media_Ptos_H'].shift(1)
        df['Media_Ptos_A'] = df.groupby('Away')['Media_Ptos_A'].shift(1)

        df['DesvPad_Ptos_H'] = df.groupby('Home')['Ptos_H'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)
        df['DesvPad_Ptos_A'] = df.groupby('Away')['Ptos_A'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)

        df['DesvPad_Ptos_H'] = df.groupby('Home')['DesvPad_Ptos_H'].shift(1)
        df['DesvPad_Ptos_A'] = df.groupby('Away')['DesvPad_Ptos_A'].shift(1)

        df['CV_Media_Ptos_H'] = df['DesvPad_Ptos_H'] / df['Media_Ptos_H']
        df['CV_Media_Ptos_A'] = df['DesvPad_Ptos_A'] / df['Media_Ptos_A']

        # Custo do Gol
        df['CG_H'] = df.FT_Goals_H / df.p_H 
        df['CG_A'] = df.FT_Goals_A / df.p_A

        df['Media_CG_H'] = df.groupby('Home')['CG_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
        df['Media_CG_A'] = df.groupby('Away')['CG_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)

        df['Media_Custo_Gol_H'] = df.groupby('Home')['Media_CG_H'].shift(1)
        df['Media_Custo_Gol_A'] = df.groupby('Away')['Media_CG_A'].shift(1)

        df['DesvPad_CG_H'] = df.groupby('Home')['CG_H'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)
        df['DesvPad_CG_A'] = df.groupby('Away')['CG_A'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)

        df['DesvPad_CG_H'] = df.groupby('Home')['DesvPad_CG_H'].shift(1)
        df['DesvPad_CG_A'] = df.groupby('Away')['DesvPad_CG_A'].shift(1)

        df['CV_Custo_Gol_H'] = df['DesvPad_CG_H'] / df['Media_CG_H']
        df['CV_Custo_Gol_A'] = df['DesvPad_CG_A'] / df['Media_CG_A']

        # Valor do Gol
        df['VG_H'] = df.FT_Goals_H * df.p_A
        df['VG_A'] = df.FT_Goals_A * df.p_H

        df['Media_VG_H'] = df.groupby('Home')['VG_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
        df['Media_VG_A'] = df.groupby('Away')['VG_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)

        df['Media_Valor_Gol_H'] = df.groupby('Home')['Media_VG_H'].shift(1)
        df['Media_Valor_Gol_A'] = df.groupby('Away')['Media_VG_A'].shift(1)

        df['DesvPad_VG_H'] = df.groupby('Home')['VG_H'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)
        df['DesvPad_VG_A'] = df.groupby('Away')['VG_A'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)

        df['DesvPad_VG_H'] = df.groupby('Home')['DesvPad_VG_H'].shift(1)
        df['DesvPad_VG_A'] = df.groupby('Away')['DesvPad_VG_A'].shift(1)

        df['CV_Valor_Gol_H'] = df['DesvPad_VG_H'] / df['Media_VG_H']
        df['CV_Valor_Gol_A'] = df['DesvPad_VG_A'] / df['Media_VG_A']

        # Média de Gols Marcados
        df['Media_GM_H'] = df.groupby('Home')['FT_Goals_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
        df['Media_GM_A'] = df.groupby('Away')['FT_Goals_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)

        df['Media_Gols_Marcados_H'] = df.groupby('Home')['Media_GM_H'].shift(1)
        df['Media_Gols_Marcados_A'] = df.groupby('Away')['Media_GM_A'].shift(1)

        df['DesvPad_GM_H'] = df.groupby('Home')['FT_Goals_H'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)
        df['DesvPad_GM_A'] = df.groupby('Away')['FT_Goals_A'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)

        df['DesvPad_GM_H'] = df.groupby('Home')['DesvPad_GM_H'].shift(1)
        df['DesvPad_GM_A'] = df.groupby('Away')['DesvPad_GM_A'].shift(1)

        df['CV_Gols_Marcados_H'] = df['DesvPad_GM_H'] / df['Media_GM_H']
        df['CV_Gols_Marcados_A'] = df['DesvPad_GM_A'] / df['Media_GM_A']

        # Média de Gols Sofridos
        df['Media_GS_H'] = df.groupby('Home')['FT_Goals_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
        df['Media_GS_A'] = df.groupby('Away')['FT_Goals_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)

        df['Media_Gols_Sofridos_H'] = df.groupby('Home')['Media_GS_H'].shift(1)
        df['Media_Gols_Sofridos_A'] = df.groupby('Away')['Media_GS_A'].shift(1)

        df['DesvPad_GS_H'] = df.groupby('Home')['FT_Goals_A'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)
        df['DesvPad_GS_A'] = df.groupby('Away')['FT_Goals_H'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)

        df['DesvPad_GS_H'] = df.groupby('Home')['DesvPad_GS_H'].shift(1)
        df['DesvPad_GS_A'] = df.groupby('Away')['DesvPad_GS_A'].shift(1)

        df['CV_Gols_Sofridos_H'] = df['DesvPad_GS_H'] / df['Media_GS_H']
        df['CV_Gols_Sofridos_A'] = df['DesvPad_GS_A'] / df['Media_GS_A']

        # Saldo de Gols
        df['SG_H'] = df['FT_Goals_H'] - df['FT_Goals_A']
        df['SG_A'] = df['FT_Goals_A'] - df['FT_Goals_H']

        df['Media_SG_H'] = df.groupby('Home')['SG_H'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)
        df['Media_SG_A'] = df.groupby('Away')['SG_A'].rolling(window=10, min_periods=2).mean().reset_index(0,drop=True)

        df['Media_Saldo_Gols_H'] = df.groupby('Home')['Media_SG_H'].shift(1)
        df['Media_Saldo_Gols_A'] = df.groupby('Away')['Media_SG_A'].shift(1)

        df['DesvPad_SG_H'] = df.groupby('Home')['SG_H'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)
        df['DesvPad_SG_A'] = df.groupby('Away')['SG_A'].rolling(window=10, min_periods=2).std(ddof=0).reset_index(0,drop=True)

        df['DesvPad_SG_H'] = df.groupby('Home')['DesvPad_SG_H'].shift(1)
        df['DesvPad_SG_A'] = df.groupby('Away')['DesvPad_SG_A'].shift(1)

        df['CV_Saldo_Gols_H'] = df['DesvPad_SG_H'] / df['Media_SG_H']
        df['CV_Saldo_Gols_A'] = df['DesvPad_SG_A'] / df['Media_SG_A']

        df.replace(np.inf, 1, inplace=True)

        # Back Home
        df.loc[(df['FT_Goals_H'] >  df['FT_Goals_A']), 'Profit_H'] = df['FT_Odd_H'] - 1
        df.loc[(df['FT_Goals_H'] <= df['FT_Goals_A']), 'Profit_H'] = -1
        # Back Draw
        df.loc[(df['FT_Goals_H'] == df['FT_Goals_A']), 'Profit_D'] = df['FT_Odd_D'] - 1
        df.loc[(df['FT_Goals_H'] != df['FT_Goals_A']), 'Profit_D'] = -1
        # Back Away
        df.loc[(df['FT_Goals_H'] <  df['FT_Goals_A']), 'Profit_A'] = df['FT_Odd_A'] - 1
        df.loc[(df['FT_Goals_H'] >= df['FT_Goals_A']), 'Profit_A'] = -1
        # Back Over25
        df.loc[((df['FT_Goals_H'] + df['FT_Goals_A']) > 2), 'Profit_Over'] = df['FT_Odd_Over25'] - 1
        df.loc[((df['FT_Goals_H'] + df['FT_Goals_A']) < 3), 'Profit_Over'] = -1
        # Back BTTS
        df['BTTS_Yes_No'] = df.apply(lambda row: 1 if (row['FT_Goals_H'] > 0 and row['FT_Goals_A'] > 0) else 0, axis=1)
        df.loc[(df['BTTS_Yes_No'] == 1), 'Profit_BTTS'] = df['Odd_BTTS_Yes'] - 1
        df.loc[(df['BTTS_Yes_No'] == 0), 'Profit_BTTS'] = -1

        ligas = df.sort_values(['League'])
        ligas = ligas['League'].unique()
        ligas = sorted(ligas)

        c1, c2 = st.columns(2)
        toda_liga_selecionada = c1.checkbox("Todas as Ligas", value=True)
        if toda_liga_selecionada:
            ligas_selecionadas = ligas
        else:
            ligas_selecionadas = c1.multiselect('Ligas', ligas)

        # Filtro de colunas
        colunas_selecionadas = c2.multiselect('Variáveis para Análise', 
                                              ['FT_Odd_H','FT_Odd_D','FT_Odd_A','FT_Odd_Over25','Odd_BTTS_Yes',
                                              'Media_Ptos_H','Media_Ptos_A','CV_Media_Ptos_H','CV_Media_Ptos_A',
                                              'Media_Gols_Marcados_H','Media_Gols_Marcados_A','CV_Gols_Marcados_H','CV_Gols_Marcados_A',
                                              'Media_Gols_Sofridos_H','Media_Gols_Sofridos_A','CV_Gols_Sofridos_H','CV_Gols_Sofridos_A',
                                              'Media_Saldo_Gols_H','Media_Saldo_Gols_A','CV_Saldo_Gols_H','CV_Saldo_Gols_A',
                                              'Media_Valor_Gol_H','Media_Valor_Gol_A','CV_Valor_Gol_H','CV_Valor_Gol_A',
                                              'Media_Custo_Gol_H','Media_Custo_Gol_A','CV_Custo_Gol_H','CV_Custo_Gol_A'])

        df0 = df[df['League'].isin(ligas_selecionadas)]

        estrategias = ['Back Home', 'Back Draw', 'Back Away', 'Over25 FT', 'BTTS Sim']

        backtestes = st.selectbox('Escolha a Metodologia', estrategias)

        try:

            if backtestes == 'Back Home':

                columns=colunas_selecionadas
                target = 'Profit_H'
                divisions = 50
                min_jogos = 100
                
                result = money_finder(data=df0,columns=columns,target=target,divisions=divisions,min_jogos=min_jogos)

                df_filtrado = retorna_df(result.iloc[0].to_dict(),df0)
                df_filtrado['Profit_H_acu'] = df_filtrado.Profit_H.cumsum()
                df_filtrado = df_filtrado.dropna()
                df_filtrado = df_filtrado.reset_index(drop=True)
                df_filtrado.index += 1
                lucro = round(df_filtrado.Profit_H_acu.tail(1).item(),2)
                total = len(df_filtrado)
                ROI = round((lucro/total)*100,2)
    
                # Criando o gráfico
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=df_filtrado.index, y=df_filtrado['Profit_H_acu'], mode='lines'))
                # Configurando o layout do gráfico
                fig.update_layout(
                    title="Profit Acumulado",
                    xaxis_title="Entradas",
                    yaxis_title="Stakes"
                )
                # Plotando o gráfico no Streamlit
                st.plotly_chart(fig)

                st.write("Profit:",str(lucro),"stakes em", str(total),"jogos")
                st.write("ROI:",str(ROI),"%")    
                st.write('')

                

            
            elif backtestes == 'Back Draw':

                columns=colunas_selecionadas
                target = 'Profit_D'
                divisions = 50
                min_jogos = 100
                
                result = money_finder(data=df0,columns=columns,target=target,divisions=divisions,min_jogos=min_jogos)

                df_filtrado = retorna_df(result.iloc[0].to_dict(),df0)
                df_filtrado['Profit_D_acu'] = df_filtrado.Profit_D.cumsum()
                df_filtrado = df_filtrado.dropna()
                df_filtrado = df_filtrado.reset_index(drop=True)
                df_filtrado.index += 1
                lucro = round(df_filtrado.Profit_D_acu.tail(1).item(),2)
                total = len(df_filtrado)
                ROI = round((lucro/total)*100,2)
    
                # Criando o gráfico
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=df_filtrado.index, y=df_filtrado['Profit_D_acu'], mode='lines'))
                # Configurando o layout do gráfico
                fig.update_layout(
                    title="Profit Acumulado",
                    xaxis_title="Entradas",
                    yaxis_title="Stakes"
                )
                # Plotando o gráfico no Streamlit
                st.plotly_chart(fig)

                st.write("Profit:",str(lucro),"stakes em", str(total),"jogos")
                st.write("ROI:",str(ROI),"%")    
                st.write('')
            
            elif backtestes == 'Back Away':

                columns=colunas_selecionadas
                target = 'Profit_A'
                divisions = 50
                min_jogos = 100
                
                result = money_finder(data=df0,columns=columns,target=target,divisions=divisions,min_jogos=min_jogos)

                df_filtrado = retorna_df(result.iloc[0].to_dict(),df0)
                df_filtrado['Profit_A_acu'] = df_filtrado.Profit_A.cumsum()
                df_filtrado = df_filtrado.dropna()
                df_filtrado = df_filtrado.reset_index(drop=True)
                df_filtrado.index += 1
                lucro = round(df_filtrado.Profit_A_acu.tail(1).item(),2)
                total = len(df_filtrado)
                ROI = round((lucro/total)*100,2)
    
                # Criando o gráfico
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=df_filtrado.index, y=df_filtrado['Profit_A_acu'], mode='lines'))
                # Configurando o layout do gráfico
                fig.update_layout(
                    title="Profit Acumulado",
                    xaxis_title="Entradas",
                    yaxis_title="Stakes"
                )
                # Plotando o gráfico no Streamlit
                st.plotly_chart(fig)

                st.write("Profit:",str(lucro),"stakes em", str(total),"jogos")
                st.write("ROI:",str(ROI),"%")    
                st.write('')

            elif backtestes == 'Over25 FT':

                columns=colunas_selecionadas
                target = 'Profit_Over'
                divisions = 50
                min_jogos = 100

                result = money_finder(data=df0,columns=columns,target=target,divisions=divisions,min_jogos=min_jogos)

                df_filtrado = retorna_df(result.iloc[0].to_dict(),df0)
                df_filtrado['Profit_Over_acu'] = df_filtrado.Profit_Over.cumsum()
                df_filtrado = df_filtrado.dropna()
                df_filtrado = df_filtrado.reset_index(drop=True)
                df_filtrado.index += 1
                lucro = round(df_filtrado.Profit_Over_acu.tail(1).item(),2)
                total = len(df_filtrado)
                ROI = round((lucro/total)*100,2)
    
                # Criando o gráfico
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=df_filtrado.index, y=df_filtrado['Profit_Over_acu'], mode='lines'))
                # Configurando o layout do gráfico
                fig.update_layout(
                    title="Profit Acumulado",
                    xaxis_title="Entradas",
                    yaxis_title="Stakes"
                )
                # Plotando o gráfico no Streamlit
                st.plotly_chart(fig)

                st.write("Profit:",str(lucro),"stakes em", str(total),"jogos")
                st.write("ROI:",str(ROI),"%")    
                st.write('')

            elif backtestes == 'BTTS Sim':

                columns=colunas_selecionadas
                target = 'Profit_BTTS'
                divisions = 50
                min_jogos = 100

                result = money_finder(data=df0,columns=columns,target=target,divisions=divisions,min_jogos=min_jogos)

                df_filtrado = retorna_df(result.iloc[0].to_dict(),df0)
                df_filtrado['Profit_BTTS_acu'] = df_filtrado.Profit_BTTS.cumsum()
                df_filtrado = df_filtrado.dropna()
                df_filtrado = df_filtrado.reset_index(drop=True)
                df_filtrado.index += 1
                lucro = round(df_filtrado.Profit_BTTS_acu.tail(1).item(),2)
                total = len(df_filtrado)
                ROI = round((lucro/total)*100,2)
    
                # Criando o gráfico
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=df_filtrado.index, y=df_filtrado['Profit_BTTS_acu'], mode='lines'))
                # Configurando o layout do gráfico
                fig.update_layout(
                    title="Profit Acumulado",
                    xaxis_title="Entradas",
                    yaxis_title="Stakes"
                )
                # Plotando o gráfico no Streamlit
                st.plotly_chart(fig)

                st.write("Profit:",str(lucro),"stakes em", str(total),"jogos")
                st.write("ROI:",str(ROI),"%")    
                st.write('')
            
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
                file_name=f'Luke_Backtesting_{backtestes}_Machine_Learning.xlsx',
                mime='application/vnd.ms-excel'
            )


            
            
            
        except:
            st.write("Tente Novamente!")
        
        try:
            # st.dataframe(result.iloc[0])
            result = result.drop(['value', 'n_games'], axis=1)
            filtros = result.iloc[0].to_dict()
            st.write(filtros)
        except:
            pass

    



    
    # st.sidebar.title('Luke \n by @FutPythonTrader & @GetUpTrading')
    st.sidebar.markdown('---')

    paginas = ['Jogos do Dia', 'Favorito Home', 'Favorito Away', 'Lay Goleada', 'Singularidades', 
               'Odd 1000', 'Head To Head', 'Bases de Dados', 'Backtesting', 'Machine Learning']
    escolha = st.sidebar.radio('', paginas)
    

    if escolha == 'Jogos do Dia':
        jogos_do_dia()

    if escolha == 'Favorito Home':
        favorito_home()

    if escolha == 'Favorito Away':
        favorito_away()

    if escolha == 'Lay Goleada':
        lay_goleada()

    if escolha == 'Singularidades':
        singularidades()
    
    if escolha == 'Odd 1000':
        sing_odd_1000()
    
    if escolha == 'Head To Head':
        h2h()

    if escolha == 'Bases de Dados':
        bases_de_dados()
    
    if escolha == 'Backtesting':
        backtest()
    
    if escolha == 'Machine Learning':
        machine_learning()

    st.sidebar.markdown('---')
    
    authenticator.logout("Logout", "sidebar")
    
