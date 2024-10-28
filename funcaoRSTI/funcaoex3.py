#foi feita uma pesquisa no SENACRS. foram coletados idade e sexo(m/f) dos alinos e nota.  
#faça um programa em python que calcule e mostre a quantidade de alunos no SENACRS

def main():
    # Inicializando a contagem de alunos
    alunos_count = 0
    
    # Quantidade de alunos que você deseja inserir
    n = int(input("Digite o número de alunos: "))
    
    # Coletando dados dos alunos
    for i in range(n):
        idade = int(input(f"Digite a idade do aluno {i + 1}: "))
        sexo = input(f"Digite o sexo do aluno {i + 1} (m/f): ").lower()
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        
        # Incrementando a contagem de alunos
        alunos_count += 1

    # Exibindo a quantidade total de alunos
    print(f"A quantidade total de alunos no SENACRS é: {alunos_count}")

if __name__ == "__main__":
    main()
