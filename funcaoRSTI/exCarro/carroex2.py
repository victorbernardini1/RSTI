#faça um algoritmo para cadastrar veículos para uma seguradora. o veículo deve ter cadastrado a placa, a marca,
#o modelo, o valor e o ano. a partir disso, função com a média dos valores dos veículos

# Classe que representa um veículo
class Veiculo:
    def __init__(self, placa, marca, modelo, valor, ano):
        # Inicializa os atributos do veículo
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        self.ano = ano

    def __str__(self):
        # Retorna uma representação em string do veículo
        return f'Veículo(Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}, Valor: R${self.valor:.2f}, Ano: {self.ano})'

# Função para cadastrar um veículo
def cadastrar_veiculo():
    placa = input("Digite a placa do veículo: ")
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    valor = float(input("Digite o valor do veículo: R$ "))  # Converte a entrada para float
    ano = int(input("Digite o ano do veículo: "))  # Converte a entrada para int
    
    return Veiculo(placa, marca, modelo, valor, ano)

# Função para calcular a média dos valores dos veículos
def calcular_media_valores(veiculos):
    if not veiculos:  # Verifica se a lista de veículos está vazia
        return 0  # Retorna 0 se não houver veículos
    
    total_valores = sum(veiculo.valor for veiculo in veiculos)  # Soma os valores dos veículos
    media = total_valores / len(veiculos)  # Calcula a média
    return media

# Função para exibir todos os veículos cadastrados
def exibir_veiculos(veiculos):
    if not veiculos:
        print("Nenhum veículo cadastrado.")
    else:
        for veiculo in veiculos:
            print(veiculo)

# Função principal que gerencia o fluxo do programa
def main():
    veiculos = []  # Lista para armazenar os veículos cadastrados
    
    while True:  # Loop que continua até o usuário decidir sair
        print("\n=== Cadastrador de Veículos ===")
        print("1. Cadastrar veículo")
        print("2. Exibir veículos cadastrados")
        print("3. Calcular média dos valores dos veículos")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            veiculo = cadastrar_veiculo()  # Chama a função para cadastrar veículo
            veiculos.append(veiculo)  # Adiciona o veículo à lista
            print("Veículo cadastrado com sucesso!")
        
        elif opcao == '2':
            exibir_veiculos(veiculos)  # Chama a função para exibir veículos
        
        elif opcao == '3':
            media = calcular_media_valores(veiculos)  # Chama a função para calcular a média
            print(f'A média dos valores dos veículos cadastrados é: R$ {media:.2f}')
        
        elif opcao == '4':
            print("Saindo do sistema.")
            break  # Encerra o loop e o programa
        
        else:
            print("Opção inválida! Tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()  
# Chama a função principal