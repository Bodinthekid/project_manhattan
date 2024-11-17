Existem várias maneiras de renomear as colunas de um DataFrame no pandas. Aqui estão algumas das mais comuns:

1. Usando DataFrame.columns
Atribua diretamente uma lista com os novos nomes para todas as colunas:
    df.columns = ['new_name1', 'new_name2', 'new_name3']
Observação: Certifique-se de que o número de novos nomes seja igual ao número de colunas existentes no DataFrame.

2. Usando o método rename()
A função rename() permite renomear colunas específicas sem precisar mudar todas. Esse método é útil para renomear uma ou algumas colunas de forma seletiva.
    df = df.rename(columns={'old_name1': 'new_name1', 'old_name2': 'new_name2'})
Dica: Use inplace=True para aplicar a mudança diretamente no DataFrame original:
    df.rename(columns={'old_name1': 'new_name1', 'old_name2': 'new_name2'}, inplace=True)


3. Usando uma expressão lambda para renomear todas as colunas
Se precisar fazer uma alteração padronizada em todos os nomes, como colocar em minúsculas ou remover espaços, use DataFrame.columns com uma expressão lambda.
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]







