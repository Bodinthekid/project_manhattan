from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup

def get_driver(headless=False):
    """
    Configura o Chrome WebDriver.

    Parâmetros:
        headless (bool): Se True, executa o Chrome em modo headless (sem interface gráfica).

    Retorna:
        WebDriver: Instância do WebDriver para controle do navegador.
    """
    options = webdriver.ChromeOptions()
    
    if headless:
        options.add_argument('--headless')  # Executa em modo headless
    
    # Adiciona outras opções se necessário
    options.add_argument('--no-sandbox')  # Para evitar problemas em ambientes isolados
    options.add_argument('--disable-dev-shm-usage')  # Para evitar problemas em contêineres

    # Cria a instância do WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    return driver

def get_soup(url):
    """
    Obtém o conteúdo HTML de uma URL e cria um objeto Beautiful Soup.

    Parâmetros:
        url (str): URL da página da qual obter o HTML.

    Retorna:
        BeautifulSoup: Instância do BeautifulSoup com o conteúdo HTML da página.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        raise Exception(f"Failed to retrieve page: {response.status_code}")
