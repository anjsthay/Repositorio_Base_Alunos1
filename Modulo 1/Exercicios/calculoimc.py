peso_usuario = float(input("Digite o seu peso em kg:"))
altura_usuario = float(input("Digite sua altura em metros:"))

imc = peso_usuario / (altura_usuario * altura_usuario)
print("o seu imc é de", imc)

if imc <= 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("peso normal")
elif imc <= 29.9:
    print("sobrepeso")
elif imc <= 34.9:
    print("obesidade grau 1")
elif imc <= 39.9:
    print("obesidade grau 2")
else:
    print("obesidade grau 3 (mórbida)")

