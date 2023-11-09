import pandas as pd
import matplotlib.pyplot as plt

# Carregar os resultados do modelo
results = pd.read_csv('../../data/processed_data/model_results.csv')  # Exemplo fictício

# Visualização de características relevantes
plt.figure(figsize=(8, 6))
plt.scatter(results['avg_packet_size'], results['total_packets'], c=results['anomaly_flag'], cmap='viridis')
plt.title('Detecção de Anomalias - Resultados')
plt.xlabel('Tamanho Médio do Pacote')
plt.ylabel('Total de Pacotes')
plt.colorbar(label='Anomalia')
plt.show()