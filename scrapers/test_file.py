from operators.dev_library import get_driver, get_soup
import time
import requests

# Teste do Selenium
driver = get_driver(headless=False)  # Defina headless=True para não abrir a interface gráfica
driver.get("https://www.google.com")
print("Título da página:", driver.title)
time.sleep(3)
driver.quit()

# Teste do Beautiful Soup
soup = get_soup("https://stackoverflow.com/questions/62131724/use-pipenv-to-build-and-publish-a-python-package")
print("Título da página obtido pelo Beautiful Soup:", soup.title.string)

# URL de uma API pública de exemplo
url = "https://jsonplaceholder.typicode.com/todos/1"

# Faz a requisição GET
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Converte a resposta para JSON
    data = response.json()
    print("Resposta:", data)
else:
    print("Erro:", response.status_code)