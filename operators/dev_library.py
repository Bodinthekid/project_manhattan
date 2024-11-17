from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
from operators.db_connection import create_connection 
import pandas as pd 

def get_driver(url,headless=True):
    """
    Configures the Chrome WebDriver.

    Parameters:
        headless (bool): If True, runs Chrome in headless mode (no GUI).

    Returns:
        WebDriver: An instance of WebDriver to control the browser.
    """
    options = webdriver.ChromeOptions()

    # Specify the download directory
    download_directory = '/Users/matheusborges/Documents/Downloads_selenium'

    # Set download preferences
    prefs = {
        "download.default_directory": download_directory,  # Set the default download location
        "download.prompt_for_download": False,             # Disable download prompt
        "download.directory_upgrade": True,                # Automatically replace the old download directory
        "safebrowsing.enabled": True                       # Enable safe browsing for downloads
    }
    
    options.add_experimental_option("prefs", prefs)
    
    if headless:
        options.add_argument('--headless')  # Run in headless mode
    
    # Additional options as needed
    options.add_argument('--no-sandbox')  # Avoid issues in sandboxed environments
    options.add_argument('--disable-dev-shm-usage')  # Avoid shared memory usage issues in containers
    # options.add_argument("--disable-gpu")
    # options.add_argument("--disable-software-rasterizer")   

    # Create WebDriver instance
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    driver.get(url)

    return driver

def get_soup(url):
    """
    Retrieves the HTML content of a URL and creates a BeautifulSoup object.

    Parameters:
        url (str): The URL of the page to retrieve HTML from.

    Returns:
        BeautifulSoup: An instance of BeautifulSoup with the page's HTML content.
    
    Raises:
        Exception: If the page retrieval fails with a non-200 status code.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        raise Exception(f"Failed to retrieve page: {response.status_code}")

def upload_data_in_batches_simple(df, table_name, batch_size=10):
    """
    Uploads data from a DataFrame to a database table in batches.

    Parameters:
        df (DataFrame): The DataFrame containing the data to upload.
        table_name (str): The name of the table to insert data into.
        batch_size (int): The number of rows to upload in each batch.

    """
    conn = create_connection()  # Establishes database connection
    cursor = conn.cursor()

    # Prepare the insert query
    query = f"""
    INSERT IGNORE INTO {table_name} ({', '.join(df.columns)}) 
    VALUES ({', '.join(['%s'] * len(df.columns))})
    """

    # Insert data in batches
    for i in range(0, len(df), batch_size):
        # Select the batch of data
        batch = df.iloc[i:i + batch_size].values.tolist()
        
        # Execute the batch insert
        cursor.executemany(query, batch)
        conn.commit()

    # Close the connection
    cursor.close()
    conn.close()


def get_columns_as_dataframe(table_name, columns):
    """
    Retrieves specific columns from a database table and returns the results in a DataFrame.

    Parameters:
        table_name (str): The name of the database table.
        columns (list): A list of column names to retrieve.

    Returns:
        DataFrame: A DataFrame containing the requested columns.
    """
    conn = create_connection()  # Connects to the database
    
    try:
        # Format the select query
        query = f"SELECT {', '.join(columns)} FROM {table_name}"
        
        # Execute the query and load the result into a DataFrame
        df = pd.read_sql(query, conn)
    except Exception as e:
        print(f"Error retrieving columns from table: {e}")
        df = pd.DataFrame()  # Returns an empty DataFrame in case of error
    finally:
        conn.close()
    
    return df
