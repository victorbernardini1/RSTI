#fazer uma matriz 4x4 e imprimir no arquivo txt a soma da Diagonal principal em python

# Criação da matriz 4x4
matriz = [[j + i * 4 for j in range(1, 5)] for i in range(4)]

# Cálculo da soma da diagonal principal
soma_diagonal = sum(matriz[i][i] for i in range(4))

# Caminho do arquivo onde a matriz e a soma serão salvas
caminho_arquivo = 'matriz_diagonal_soma.txt'

# Abrindo o arquivo para escrita
with open(caminho_arquivo, 'w') as arquivo:
    # Escrevendo a matriz no arquivo
    for linha in matriz:
        arquivo.write(' '.join(map(str, linha)) + '\n')
    
    # Escrevendo a soma da diagonal no arquivo
    arquivo.write(f'Soma da Diagonal Principal: {soma_diagonal}\n')

print(f'Matriz 4x4 e soma da diagonal principal salva em {caminho_arquivo}')
