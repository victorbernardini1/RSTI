#foi feita uma pesquisa no SENACRS. foram coletados idade e sexo(m/f) dos alinos e nota.  
#faça um programa em python que calcule e mostre a maior e a menor idade dos alunos

def main():
    # Lista para armazenar as idades dos alunos
    idades = []
    
    # Quantidade de alunos que você deseja inserir
    n = int(input("Digite o número de alunos: "))
    
    # Coletando dados dos alunos
    for i in range(n):
        idade = int(input(f"Digite a idade do aluno {i + 1}: "))
        sexo = input(f"Digite o sexo do aluno {i + 1} (m/f): ").lower()
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        
        idades.append(idade)

    # Verificando a maior e a menor idade
    maior_idade = max(idades) if idades else None
    menor_idade = min(idades) if idades else None

    # Exibindo os resultados
    if maior_idade is not None and menor_idade is not None:
        print(f"A maior idade dos alunos é: {maior_idade}")
        print(f"A menor idade dos alunos é: {menor_idade}")
    else:
        print("Nenhuma idade foi registrada.")

if __name__ == "__main__":
    main()
