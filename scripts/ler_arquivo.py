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
            if 'delivery_country' in df.columns and 'total_price' in df.columns:
                dataframes.append(df[['delivery_country', 'total_price']])
        except Exception as e:
            print(f"Erro ao processar {file}: {e}")

    # Concatenar todos os DataFrames
    if dataframes:
        combined_df = pd.concat(dataframes)

        # Somar as vendas por país
        result = combined_df.groupby('delivery_country', as_index=False)['total_price'].sum()

        # Adicionar coluna de ID
        result.insert(0, 'ID', range(1, len(result) + 1))

        # Exibir a tabela final
        print(result.to_string(index=False))
    else:
        print("Nenhum arquivo válido encontrado.")

# Defina o caminho da pasta onde estão os arquivos CSV
folder_path = "../data/raw_data"
process_csv_files(folder_path)
