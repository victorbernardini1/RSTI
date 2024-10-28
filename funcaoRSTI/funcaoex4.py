#foi feita uma pesquisa no SENACRS. foram coletados idade e sexo(m/f) dos alinos e nota.  
#faça um programa em python que calcule e mostre a idade e o sexo do aluno que possui a menor nota

def main():
    # Lista para armazenar os dados dos alunos
    alunos = []
    
    # Quantidade de alunos que você deseja inserir
    n = int(input("Digite o número de alunos: "))
    
    # Coletando dados dos alunos
    for i in range(n):
        idade = int(input(f"Digite a idade do aluno {i + 1}: "))
        sexo = input(f"Digite o sexo do aluno {i + 1} (m/f): ").lower()
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        
        alunos.append((idade, sexo, nota))

    # Verificando o aluno com a menor nota
    if alunos:
        menor_nota_aluno = min(alunos, key=lambda aluno: aluno[2])
        idade_menor_nota, sexo_menor_nota, _ = menor_nota_aluno

        # Exibindo os resultados
        print(f"A idade do aluno com a menor nota é: {idade_menor_nota}")
        print(f"O sexo do aluno com a menor nota é: {sexo_menor_nota}")
    else:
        print("Nenhum aluno registrado.")

if __name__ == "__main__":
    main()
