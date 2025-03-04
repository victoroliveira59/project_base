# Script em Python para Processar Arquivos CSV

Crie um script em Python que processe os meus dados CSV de arquivos distintos, verifique as colunas de **Pais** e **Vendas**, e some todas essas vendas. Preciso que a sua saída seja como uma tabela com o seu respectivo **ID**.

## Descrição

O script a seguir realiza as seguintes operações:
- Lê todos os arquivos CSV dentro da pasta especificada.
- Filtra apenas as colunas **Pais** e **Vendas**.
- Soma as vendas agrupadas por país.
- Adiciona um ID único para cada país.
- Exibe os resultados em formato de tabela.

## Código

```python
import pandas as pd
import glob

def process_csv_files(folder_path):
    # Encontrar todos os arquivos CSV no diretório
    csv_files = glob.glob(f"{folder_path}/*.csv")

    # Lista para armazenar os DataFrames
    dataframes = []

    for file in csv_files:
        try:
            df = pd.read_csv(file)
            if 'Pais' in df.columns and 'Vendas' in df.columns:
                dataframes.append(df[['Pais', 'Vendas']])
        except Exception as e:
            print(f"Erro ao processar {file}: {e}")

    # Concatenar todos os DataFrames
    if dataframes:
        combined_df = pd.concat(dataframes)

        # Somar as vendas por país
        result = combined_df.groupby('Pais', as_index=False)['Vendas'].sum()

        # Adicionar coluna de ID
        result.insert(0, 'ID', range(1, len(result) + 1))

        # Exibir a tabela final
        print(result.to_string(index=False))
    else:
        print("Nenhum arquivo válido encontrado.")

# Defina o caminho da pasta onde estão os arquivos CSV
folder_path = "caminho/para/seus/arquivos"
process_csv_files(folder_path)
