Instalação
    pip install requests


1. Realizando Requisições para APIs
Para consumir dados de uma API, geralmente usamos o método GET para recuperar dados ou POST para enviar dados.
Exemplo de Requisição GET

    import requests

    url = "https://api.exemplo.com/dados"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()  # Converte a resposta em JSON
    else:
        print("Erro na requisição:", response.status_code)


2. Trabalhando com PDFs
Para baixar arquivos PDF com requests, basta fazer uma requisição GET e salvar o conteúdo.

    url = "https://www.exemplo.com/arquivo.pdf"
    response = requests.get(url)

    with open("arquivo.pdf", "wb") as f:
        f.write(response.content)


Para manipular o conteúdo de PDFs, bibliotecas como PyPDF2 ou pdfplumber são recomendadas.

3. Trabalhando com CSVs
Para baixar e salvar dados em CSV, você pode usar requests para obter o conteúdo e a biblioteca csv ou pandas para salvar ou processar.

    import csv
    import requests

    url = "https://www.exemplo.com/dados.csv"
    response = requests.get(url)

    with open("dados.csv", "w", newline="") as csvfile:
        csvfile.write(response.text)  # Salva o CSV diretamente

Para manipulação de CSVs com mais controle, pandas pode ser útil.

import pandas as pd

# Lê o CSV diretamente de uma URL
url = "https://www.exemplo.com/dados.csv"
df = pd.read_csv(url)

4. Salvando em Diferentes Formatos
Salvando em JSON
python
Copiar código
import json

dados = {"chave": "valor"}
with open("dados.json", "w") as f:
    json.dump(dados, f)

5. Abrindo Arquivos JSON, PDF e CSV
Abrindo JSON

    import json

    with open("dados.json", "r") as f:
        dados = json.load(f)


Abrindo PDF

Para leitura de PDF, use bibliotecas como pdftotext


Abrindo CSV

    import pandas as pd

    df = pd.read_csv("dados.csv")