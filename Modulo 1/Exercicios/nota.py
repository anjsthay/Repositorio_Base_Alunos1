nome = input("Digite o seu nome:")
numero1 = float(input("Digite a primeira nota do aluno:"))
numero2 = float(input("Digite a segunda nota do aluno:"))
numero3 = float(input("digite a terceira nota do aluno:"))

resultado = (numero1 + numero2 + numero3) /3
print("A média do aluno é", resultado)

if resultado >= 7:
    print("O aluno esta aprovado!")
elif resultado > 4:
    print("O aluno está de recuperação!")
else:
    print("O aluno está reprovado.")