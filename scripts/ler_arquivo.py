import pandas as pd
import os

# Defina o caminho correto para o diretório
directory_path = "../data/raw_data/"


# Verifique se o diretório existe
if not os.path.isdir(directory_path):
    raise FileNotFoundError(f"O diretório '{directory_path}' não foi encontrado.")

# Inicialize um DataFrame vazio para armazenar os dados combinados
combined_data = pd.DataFrame()

# Itere sobre todos os arquivos no diretório
for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory_path, filename)
        try:
            data = pd.read_csv(file_path)
            print(f"Lendo: {filename} ({len(data)} linhas)")  # Log do progresso
            combined_data = pd.concat([combined_data, data], ignore_index=True)
        except Exception as e:
            print(f"Erro ao ler {filename}: {e}")

# Verifique se há dados antes de prosseguir
if combined_data.empty:
    print("Nenhum dado foi carregado.")
else:
    if 'delivery_country' in combined_data.columns and 'total_price' in combined_data.columns:
        # Agrupe os dados por país e some as vendas
        sales_summary = combined_data.groupby('delivery_country')['total_price'].sum().reset_index()
        print(sales_summary)
    else:
        print("As colunas necessárias ('delivery_country' e 'total_price') não foram encontradas.")
