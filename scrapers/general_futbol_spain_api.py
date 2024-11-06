############## api to futebol teams data ################
# I NEED TO MAKE 2 REQUESTS AND CONCAT THE JSONS 
# BECAUSE THEY MAY NOT BE IN THE GENERAL JSON FILE
# COULD HAPPEN WITH OTHERS TEAMS NEEDS TO BE CHECKED#


import requests
import json
import numpy as np
import pandas as pd

url_list = ["https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?s=Soccer&c=Spain", # general spain futbol teams
            "https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t=Real_Madrid"] # real madrid team

file_name = '/Users/matheusborges/Documents/futbol_general_api/general_futbol_spain_data.json'

def get_response(url):
    data = np.nan
    # Faz a requisição GET
    response = requests.get(url)

    # get general json
    if response.status_code == 200:
        # Converte a resposta para JSON
        data = response.json()
    else:
        print("Error:", response.status_code)  
    return data

general_data_list = []
for url in url_list:
    team_data_raw = get_response(url)
    team_data = team_data_raw.get('teams')
    general_data_list.extend(team_data)
    
# df_teams = pd.DataFrame(general_data_list)
# print(df_teams)


with open(file_name, "w", encoding="utf-8") as f:
    json.dump(general_data_list, f, ensure_ascii=False, indent=4)


print('done')