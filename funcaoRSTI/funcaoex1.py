#foi feita uma pesquisa no SENACRS. foram coletados idade e sexo(m/f) dos alunos e nota.
#faça um programa em python que calcule e mostre a média das notas dos alunos

def main():
    # Lista para armazenar os dados dos alunos
    alunos = []
    
    # Quantidade de alunos que você deseja inserir
    n = int(input("Digite o número de alunos(as): "))
    
    # Coletando dados dos alunos
    for i in range(n):
        idade = int(input(f"Digite a idade do aluno(a) {i + 1}: "))
        sexo = input(f"Digite o sexo do aluno(a) {i + 1} (m/f): ").lower()
        nota = float(input(f"Digite a nota do aluno(a) {i + 1}: "))
        
        alunos.append((idade, sexo, nota))

    # Calculando a média das notas
    total_notas = sum(nota for _, _, nota in alunos)
    media_notas = total_notas / n if n > 0 else 0

    # Exibindo a média
    print(f"A média das notas dos alunos(as) é: {media_notas:.2f}")

if __name__ == "__main__":
    main()
