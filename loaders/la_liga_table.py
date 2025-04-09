# Open the CSV file that was downloaded on la_liga_table.py
# convert it to Dataframe, clean and transform data 
# then upload it on sql 

import pandas as pd
from operators.dev_library import upload_data_in_batches_simple
from operators.dev_library import get_driver
from operators.manipulate_library import ManipulateDF

manipulator = ManipulateDF() 

################### VARIABLES ##################
sql_table = 'la_liga_table'
new_columns_names = {
    'Team': 'team_name',
    'P': 'played',
    'W': 'wins',
    'D': 'draws',
    'L': 'losses',
    'GF': 'goals_for',
    'GA': 'goals_against',
    'GD': 'goal_difference',
    'Pts': 'points',
    'Form': 'recent_form'
}

# open csv using pandas
df = pd.read_csv('/Users/matheusborges/Documents/futbol_general_api/spain_table.csv')

# change column names
df2 = manipulator.change_column_name(df=df,new_columns=new_columns_names)

table_df = manipulator.remove_nr_from_column(df=df2,column_name='team_name')
print(table_df)

upload_data_in_batches_simple(table_df,sql_table)
print('upload complete')





