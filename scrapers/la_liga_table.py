from operators.dev_library import get_driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import pandas as pd
from io import StringIO

URL = 'https://www.whoscored.com/Regions/206/Tournaments/4/Seasons/10317/Stages/23401/Show/Spain-LaLiga-2024-2025'

driver = get_driver(url=URL,headless=False)

def df_from_website(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'))
        ).click()
        # Espera até que o elemento esteja presente (aguarda 10 segundos)
        
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="tournament-tables-23401"]'))
        ).get_attribute('outerHTML')

        # FutureWarning: Passing literal html to 'read_html' is deprecated and will be removed in a future version. 
        # To read from a literal string, wrap it in a 'StringIO' object.
        table_io = StringIO(table)
        dfs = pd.read_html(table_io)

        df = dfs[0]

    except Exception as e:
        # Captura qualquer exceção, mas não fecha o driver
        print(f"Erro ocorreu: {e}")
        # Você pode adicionar lógica aqui para continuar o fluxo ou logar o erro sem fechar o driver

    # O driver continua aberto aqui, independentemente do erro
    driver.close()

    return df

df = df_from_website(driver)

print(df)