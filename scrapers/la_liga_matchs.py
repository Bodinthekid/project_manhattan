# # https://www.skysports.com/la-liga-table
# # https://www.espn.com/soccer/standings/_/league/esp.1
# # https://www.bbc.com/sport/football/spanish-la-liga/table
# # https://www.soccerstats.com/latest.asp?league=spain
# https://onefootball.com/en/competition/laliga-10/table
# https://www.whoscored.com/Regions/206/Tournaments/4/Seasons/10317/Stages/23401/Show/Spain-LaLiga-2024-2025


from operators.dev_library import get_driver, get_soup
from selenium.webdriver.common.by import By
import time
import requests
# import numpy as np



# Teste do Selenium
URL = "https://onefootball.com/en/competition/laliga-10/results"
driver = get_driver(url=URL,headless=False)  # Defina headless=True para não abrir a interface gráfica

print("Título da página:", driver.title)
time.sleep(3)

all_matches = driver.find_element(By.XPATH,'//div[@class="MatchCardsListsAppender_container__y5ame"]')
print(all_matches.text)


time.sleep(3)
try:
    driver.dispose()
except Exception as e:
    print(e)