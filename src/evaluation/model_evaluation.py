import pandas as pd
from sklearn.metrics import classification_report
import joblib

# Carregar os dados de teste (ou conjunto de validação)
test_data = pd.read_csv('../../data/processed_data/test_data.csv')  # Exemplo fictício

# Carregar o modelo treinado
model = joblib.load('../../models/anomaly_detection_model.pkl')

# Selecionar características relevantes para teste
test_features = test_data[['avg_packet_size', 'total_packets']]

# Previsões do modelo
predictions = model.predict(test_features)

# Relatório de classificação (pode variar dependendo do tipo de modelo)
print(classification_report(predictions, test_data['anomaly_flag']))