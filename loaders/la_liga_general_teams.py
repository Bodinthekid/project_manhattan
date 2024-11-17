
# this is columns of the data frame after we convert json to a dataframe

    # ['idTeam' 'idSoccerXML' 'idAPIfootball' 'intLoved' 'strTeam'
    #  'strTeamAlternate' 'strTeamShort' 'intFormedYear' 'strSport' 'strLeague'
    #  'idLeague' 'strLeague2' 'idLeague2' 'strLeague3' 'idLeague3' 'strLeague4'
    #  'idLeague4' 'strLeague5' 'idLeague5' 'strLeague6' 'idLeague6'
    #  'strLeague7' 'idLeague7' 'strDivision' 'idVenue' 'strStadium'
    #  'strKeywords' 'strRSS' 'strLocation' 'intStadiumCapacity' 'strWebsite'
    #  'strFacebook' 'strTwitter' 'strInstagram' 'strDescriptionEN'
    #  'strDescriptionDE' 'strDescriptionFR' 'strDescriptionCN'
    #  'strDescriptionIT' 'strDescriptionJP' 'strDescriptionRU'
    #  'strDescriptionES' 'strDescriptionPT' 'strDescriptionSE'
    #  'strDescriptionNL' 'strDescriptionHU' 'strDescriptionNO'
    #  'strDescriptionIL' 'strDescriptionPL' 'strColour1' 'strColour2'
    #  'strColour3' 'strGender' 'strCountry' 'strBadge' 'strLogo' 'strFanart1'
    #  'strFanart2' 'strFanart3' 'strFanart4' 'strBanner' 'strEquipment'
    #  'strYoutube' 'strLocked']

# we will just use the columns that define the futebol team
    # ['idTeam',
    # 'idAPIfootball',
    # 'strTeam',
    # 'strTeamAlternate',
    # 'strTeamShort',
    # 'intFormedYear',
    # 'strSport',
    # 'strDescriptionEN',
    # 'strGender',
    # 'strCountry',
    # 'strBadge',
    # 'strLogo']

# sql table, change the column names on sql and before upload_data_in_batches_simple

# CREATE TABLE la_liga_teams (
#     "team_id" VARCHAR(20) PRIMARY KEY NOT NULL,       -- Identificador único para cada time
#     "idAPIfootball" VARCHAR(10) NULL,                 -- ID do time na API de futebol
#     "strTeam" VARCHAR(80) NOT NULL,                   -- Nome do time
#     "strTeamShort" VARCHAR(7) NULL,                   -- Nome curto do time
#     "intFormedYear" VARCHAR(4) NULL,                  -- Ano de fundação do time
#     "strSport" VARCHAR(10) NULL,                      -- Tipo de esporte
#     "strLocation" VARCHAR(30) NULL,                   -- Localização do time
#     "strStadium" VARCHAR(30) NULL,                    -- Nome do estádio
#     "strDescriptionEN" VARCHAR(250) NULL,             -- Descrição do time em inglês
#     "strGender" VARCHAR(10) NULL,                     -- Gênero do time (masculino, feminino, etc.)
#     "strCountry" VARCHAR(10) NULL,                    -- País do time
#     "strBadge" VARCHAR(250) NULL,                     -- URL do escudo do time
#     "strLogo" VARCHAR(250) NULL                       -- URL do logo do time
# );





import json
import pandas as pd
from operators.dev_library import upload_data_in_batches_simple

sql_table = 'la_liga_teams'
file_name = '/Users/matheusborges/Documents/futbol_general_api/general_futbol_spain_data.json'
used_columns = ['idTeam',
                'idAPIfootball',
                'strTeam',
                'strTeamAlternate',
                'strTeamShort',
                'intFormedYear',
                'strSport',
                'strLocation',
                'strStadium',
                'strDescriptionEN',
                'strGender',
                'strCountry',
                'strBadge',
                'strLogo']

with open(file_name, "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

team_df = df[used_columns]

team_df = team_df.rename(columns={'idTeam':'team_id',
                        'idAPIfootball':'api_id',
                        'strTeam':'team_name',
                        'strTeamAlternate':'alternative_team_name',
                        'strTeamShort':'short_team_name',
                        'intFormedYear':'formed_year',
                        'strSport':'sport',
                        'strLocation':'location_team',
                        'strStadium':'stadium_team',
                        'strDescriptionEN':'description_team',
                        'strGender':'gender',
                        'strCountry':'country_team',
                        'strBadge':'badge_team',
                        'strLogo':'logo_team'
                        })


upload_data_in_batches_simple(team_df,sql_table)
print('upload complete')

