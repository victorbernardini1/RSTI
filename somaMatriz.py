#fazer uma matriz 4x4 e imprimir no arquivo txt a soma da matriz em python

# Criação da matriz 4x4
matriz = [[j + i * 4 for j in range(1, 5)] for i in range(4)]

# Cálculo da soma da matriz
soma_matriz = sum(sum(linha) for linha in matriz)

# Caminho do arquivo onde a matriz e a soma serão salvas
caminho_arquivo = 'matriz_soma.txt'

# Abrindo o arquivo para escrita
with open(caminho_arquivo, 'w') as arquivo:
    # Escrevendo a matriz no arquivo
    for linha in matriz:
        arquivo.write(' '.join(map(str, linha)) + '\n')
    
    # Escrevendo a soma no arquivo
    arquivo.write(f'Soma da matriz: {soma_matriz}\n')

print(f'Matriz 4x4 e soma salva em {caminho_arquivo}')
