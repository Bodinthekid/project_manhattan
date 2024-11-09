
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


import json
import pandas as pd
from operators.dev_library import upload_data_in_batches_simple


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
print(team_df.columns.values)
