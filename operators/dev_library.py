from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
from operators.db_connection import create_connection 
import pandas as pd 

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

def upload_data_in_batches_simple(df, table_name, batch_size=10):
    conn = create_connection()
    
    cursor = conn.cursor()

    # Preparando a query de inserção
    query = f"""
    INSERT IGNORE INTO {table_name} ({', '.join(df.columns)}) 
    VALUES ({', '.join(['%s'] * len(df.columns))})
    """

    # Inserir dados em lotes
    for i in range(0, len(df), batch_size):
        # Seleciona o lote de dados
        batch = df.iloc[i:i + batch_size].values.tolist()
        
        # Executa a inserção em lote
        cursor.executemany(query, batch)
        conn.commit()

    # Fechar conexão
    cursor.close()
    conn.close()

def get_columns_as_dataframe(table_name, columns):
    """
    Obtém colunas específicas de uma tabela no banco de dados e retorna os resultados em um DataFrame.

    Parâmetros:
        table_name (str): Nome da tabela do banco de dados.
        columns (list): Lista dos nomes das colunas que deseja buscar.

    Retorna:
        DataFrame: DataFrame com as colunas solicitadas.
    """
    conn = create_connection()  # Conecta ao banco de dados
    
    try:
        # Formata a query de seleção
        query = f"SELECT {', '.join(columns)} FROM {table_name}"
        
        # Executa a query e carrega o resultado em um DataFrame
        df = pd.read_sql(query, conn)
    except Exception as e:
        print(f"Erro ao obter colunas da tabela: {e}")
        df = pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro
    finally:
        conn.close()
    
    return df