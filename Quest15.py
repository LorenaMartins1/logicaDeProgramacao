frequencia = int(input("Digite a frequência do aluno: "))
total = int(input("Digite o total de aula: "))
n1 = int(input("Digite nota1: "))
n2 = int(input("Digite nota2: "))
n3 = int(input("Digite nota3: "))
n4 = int(input("Digite nota4: "))

media = n1 + n2 + (n3*2) + (n4*2)
calcularFre = (frequencia * 1)/total

if media >= 7 and calcularFre > 0.75:
    print("Aprovado")
elif media < 7 and media >= 2.5:
    print("Prova final")
elif media < 2.5:
    print("Reprovado por nota")
if calcularFre < 0.75:
    print("Reprovado por falta")
