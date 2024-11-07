import pandas as pd
from operators.dev_library import upload_data_in_batches_simple

# Criando um DataFrame simples com os dados que você deseja inserir
data = {
    'id': [1, 2, 3, 4],
    'nome': ['João', 'Maria', 'Carlos', 'Ana'],
    'idade': [25, 30, 22, 28],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}

df_test = pd.DataFrame(data)

# Agora vamos chamar a função de upload
table_name = 'pessoas'  # Nome da tabela onde os dados serão inseridos
upload_data_in_batches_simple(df_test, table_name)

print('done')