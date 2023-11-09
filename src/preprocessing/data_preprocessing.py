import pandas as pd

# Carregar os dados brutos
raw_data = pd.read_csv('data/raw_data/network_traffic.csv')

# Remover duplicatas, se houver
raw_data = raw_data.drop_duplicates()

# Tratamento de valores ausentes
raw_data = raw_data.dropna()

# Conversão de tipos de dados, se necessário
raw_data['timestamp'] = pd.to_datetime(raw_data['timestamp'])

# Engenharia de recursos (feature engineering)
# Por exemplo, extrair informações temporais adicionais do timestamp, se relevante
raw_data['hour'] = raw_data['timestamp'].dt.hour

# Salvar os dados processados
raw_data.to_csv('data/processed_data/processed_network_traffic.csv', index=False)