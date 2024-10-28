#fazer uma matriz 4x4 e imprimir no arquivo txt os números maior que 17

# Criação da matriz 4x4
matriz = [
    [16, 18, 20, 22],
    [14, 19, 23, 25],
    [12, 21, 17, 30],
    [11, 15, 29, 35]
]

# Caminho do arquivo onde os números maiores que 17 serão salvos
caminho_arquivo = 'numeros_maiores_que_17.txt'

# Abrindo o arquivo para escrita
with open(caminho_arquivo, 'w') as arquivo:
    # Escrevendo os números maiores que 17 no arquivo
    for linha in matriz:
        for numero in linha:
            if numero > 17:  # Verifica se o número é maior que 17
                arquivo.write(f'{numero}\n')

print(f'Números maiores que 17 da matriz salvos em {caminho_arquivo}')
