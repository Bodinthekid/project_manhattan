
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from io import StringIO

from operators.dev_library import get_driver
from operators.manipulate_library import ManipulateDF

manipulator = ManipulateDF() 

#################### VARIABLES ##################
# new_columns = {
#     'Team': 'team_name',
#     'P': 'played',
#     'W': 'wins',
#     'D': 'draws',
#     'L': 'losses',
#     'GF': 'goals_for',
#     'GA': 'goals_against',
#     'GD': 'goal_difference',
#     'Pts': 'points',
#     'Form': 'recent_form'
# }

file_name = '/Users/matheusborges/Documents/futbol_general_api/spain_table.csv'
URL = 'https://www.whoscored.com/'
league = 'LaLiga'
################################################


def df_from_website(table):

    # FutureWarning: Passing literal html to 'read_html' is deprecated and will be removed in a future version. 
    # To read from a literal string, wrap it in a 'StringIO' object.
    table_io = StringIO(table)
    dfs = pd.read_html(table_io)
    
    df = dfs[0]

    return df


# OPEN THE DRIVER SHOWING THE BROWSER
driver = get_driver(url=URL,headless=False)

# Get the total screen size
screen_width = driver.execute_script("return window.screen.width;")
screen_height = driver.execute_script("return window.screen.height;")
# Set the window size to half of the screen width and full height
driver.set_window_size(screen_width // 2, screen_height)
# Moves the window to the left side
driver.set_window_position(0, 0)  


try:
    # TRY TO FIND COOKIES IN THE WEBPAGE
    try:  
        WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'))
            ).click()
            # Espera até que o elemento esteja presente (aguarda 10 segundos)
        print("cookies was found")
        time.sleep(4)
    except:
        print("no cookies")

    # FIND SEARCH BAR IN THE WEBPAGE
    search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search"]'))
        )
    print('search bar was found')
    time.sleep(2)

    # SEND league(LaLiga) AS INPUT ON search_bar AND PRESS 'ENTER' TO SEE THE RESULTS
    search_bar.send_keys(league)
    time.sleep(2)
    search_bar.send_keys(Keys.RETURN) 

    # CLICK ON league(LaLiga) TO SEE ALL INFORMATION ABOUT THE SPAIN LEAGUE 
    try: 
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//*[text()='{league}']"))
            ).click()
        time.sleep(2)
        league_flag = True
        print(f'information about {league} was found')
    except:
        league_flag = False
        print('no league was found')

    # GET THE TABLEOF THE LEAGUE THAT WAS SEARCHED
    if league_flag == True:

        print("finding the table 🔎 ")
        time.sleep(5)

        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="tournament-tables-23401"]'))
        ).get_attribute('outerHTML')

        # Scroll to the element
        # driver.execute_script("arguments[0].scrollIntoView();", table)

        # USE THIS DEF TO CONVERT THE HTML TO DATAFRAME FORMAT
        df = df_from_website(table)
        print(df)

        df.to_csv(file_name, index=False)

        print(f"your file was save on {file_name}")

        # df.rename(columns = new_columns, inplace=True)

        # df = manipulator.remove_nr_from_column(df=df,column_name='team_name')ß

        # print(df)

except:
    print('error')

driver.quit()

print('done')