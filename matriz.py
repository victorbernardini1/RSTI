#fazer uma matriz 4x4 e imprimir no arquivo txt(imprimir a matriz)

# Criação da matriz 4x4
matriz = [[j + i * 4 for j in range(1, 5)] for i in range(4)]

# Caminho do arquivo onde a matriz será salva
caminho_arquivo = 'matriz.txt'

# Abrindo o arquivo para escrita
with open(caminho_arquivo, 'w') as arquivo:
    for linha in matriz:
        # Convertendo cada linha em uma string e escrevendo no arquivo
        arquivo.write(' '.join(map(str, linha)) + '\n')

print(f'Matriz 4x4 salva em {caminho_arquivo}')
