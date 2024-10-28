#faça um algoritmo para cadastrar veículos para uma seguradora. o veículo deve ter cadastrado a placa, a marca,
# o modelo, o valor e o ano. a partir disso, em python fazer uma função principal.

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
        # Retorna uma representação em string do veículo para fácil visualização
        return f'Veículo(Placa: {self.placa}, Marca: {self.marca}, Modelo: {self.modelo}, Valor: R${self.valor:.2f}, Ano: {self.ano})'

# Função para cadastrar um veículo
def cadastrar_veiculo():
    # Coleta os dados do veículo a partir da entrada do usuário
    placa = input("Digite a placa do veículo: ")
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    valor = float(input("Digite o valor do veículo: R$ "))  # Converte a entrada para float
    ano = int(input("Digite o ano do veículo: "))  # Converte a entrada para int
    
    # Retorna uma nova instância de Veiculo com os dados coletados
    return Veiculo(placa, marca, modelo, valor, ano)

# Função para exibir todos os veículos cadastrados
def exibir_veiculos(veiculos):
    if not veiculos:  # Verifica se a lista de veículos está vazia
        print("Nenhum veículo cadastrado.")
    else:
        # Itera sobre a lista de veículos e imprime cada um
        for veiculo in veiculos:
            print(veiculo)

# Função principal que gerencia o fluxo do programa
def main():
    veiculos = []  # Lista para armazenar os veículos cadastrados
    
    while True:  # Loop que continua até o usuário decidir sair
        print("\n=== Cadastrador de Veículos ===")
        print("1. Cadastrar veículo")  # Opção para cadastrar um veículo
        print("2. Exibir veículos cadastrados")  # Opção para exibir veículos
        print("3. Sair")  # Opção para sair do programa
        
        opcao = input("Escolha uma opção: ")  # Coleta a escolha do usuário
        
        if opcao == '1':
            veiculo = cadastrar_veiculo()  # Chama a função para cadastrar veículo
            veiculos.append(veiculo)  # Adiciona o veículo à lista
            print("Veículo cadastrado com sucesso!")
        
        elif opcao == '2':
            exibir_veiculos(veiculos)  # Chama a função para exibir veículos
        
        elif opcao == '3':
            print("Saindo do sistema.")  # Mensagem de saída
            break  # Encerra o loop e o programa
        
        else:
            print("Opção inválida! Tente novamente.")  # Mensagem de erro para opções inválidas

# Ponto de entrada do programa
if __name__ == "__main__":
    main()  # Chama a função principal