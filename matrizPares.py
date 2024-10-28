#fazer uma matriz 4x4 e imprimir no arquivo txt os numeros pares em python

# Criação da matriz 4x4
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Caminho do arquivo onde os números pares serão salvos
caminho_arquivo = 'numeros_pares.txt'

# Abrindo o arquivo para escrita
with open(caminho_arquivo, 'w') as arquivo:
    # Escrevendo os números pares no arquivo
    for linha in matriz:
        for numero in linha:
            if numero % 2 == 0:  # Verifica se o número é par
                arquivo.write(f'{numero}\n')

print(f'Números pares da matriz salvos em {caminho_arquivo}')
