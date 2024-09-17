import pandas as pd
import matplotlib.pyplot as plt

# Função para carregar e analisar dados
def analyze_stock_data(filename):
    data = pd.read_csv(filename, names=['Timestamp', 'Stock Level'])
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    data.set_index('Timestamp', inplace=True)
    
    # Exibindo estatísticas básicas
    print(data.describe())
    
    # Plotando dados
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Stock Level'], label='Stock Level')
    plt.xlabel('Time')
    plt.ylabel('Stock Level (units)')
    plt.title('Stock Level Over Time')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    analyze_stock_data('stock_level_data.csv')
