Salvando Diferentes Tipos de Arquivos em 
Este guia traz exemplos de como salvar diferentes tipos de arquivos em : texto, JSON, CSV (com pandas), binário e imagens.

1. Salvando Arquivo de Texto
Para salvar conteúdo em um arquivo de texto, você pode usar o modo "w" para sobrescrever ou "a" para acrescentar

text_content = "Este é um exemplo de conteúdo de texto."

with open("arquivo.txt", "w") as f:
    f.write(text_content)

2. Salvando Arquivo JSON
Arquivos JSON são úteis para armazenar dados estruturados em formato de dicionário ou lista. Use o módulo json para salvar um dicionário em um arquivo JSON.

import json

data = {
    "nome": "Matheus",
    "idade": 22,
    "cidade": "São Paulo"
}

with open("arquivo.json", "w") as f:
    json.dump(data, f, indent=4)  # 'indent=4' adiciona formatação

3. Salvando Arquivo CSV (com Pandas)
Para salvar dados em formato CSV usando pandas, você pode criar um DataFrame e usar o método .to_csv().

import pandas as pd

# Dados para o DataFrame
dados = {
    "nome": ["Matheus", "Ana", "Carlos"],
    "idade": [22, 25, 28]
}

# Cria o DataFrame
df = pd.DataFrame(dados)
# Salva o DataFrame em um arquivo CSV
df.to_csv("arquivo.csv", index=False)  # 'index=False' remove a coluna de índice


4. Salvando Arquivo Binário
Para salvar dados em formato binário (útil para dados não textuais), abra o arquivo com "wb".

binary_data = b"Exemplo de dados binários"
with open("arquivo.bin", "wb") as f:
    f.write(binary_data)






