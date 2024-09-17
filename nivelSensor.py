import time
import random  # Simula dados dos sensores

# Função para simular a leitura dos sensores de nível de estoque
def read_stock_level():
    # Simula o nível de estoque entre 0 e 1000 unidades
    stock_level = random.uniform(0, 100)
    return stock_level

# Função para gravar os dados em um arquivo CSV
def log_stock_data(stock_level):
    with open('stock_level_data.csv', 'a') as file:
        file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')},{stock_level:.2f}\n")

# Loop principal para coletar dados periodicamente
def main():
    while True:
        stock_level = read_stock_level()
        log_stock_data(stock_level)
        time.sleep(60)  # Coleta dados a cada 60 segundos

if __name__ == "__main__":
    main()
