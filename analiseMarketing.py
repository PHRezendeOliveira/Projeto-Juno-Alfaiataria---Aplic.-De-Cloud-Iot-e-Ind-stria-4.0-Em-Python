import pandas as pd

# Função para analisar dados de campanhas de marketing
def analyze_marketing_data(filename):
    data = pd.read_csv(filename, names=['Date', 'Clicks', 'Conversions'])
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Exibindo estatísticas básicas
    print(data.describe())
    
    # Análise de conversões e cliques
    data.plot(x='Date', y=['Clicks', 'Conversions'], kind='line', figsize=(10, 5))
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('Marketing Campaign Performance')
    plt.show()

if __name__ == "__main__":
    analyze_marketing_data('marketing_data.csv')
