#ESTRUTURAS CONDICIONAIS

idade = 30

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

"""
Imagine que você queira imprimir "Aprovado", caso o estudante tenha uma média superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7.
"""
media = float(input("Por favor, informe a média do estudante:"))

if media >= 7:
    print("Aprovado.")
elif media == 5:
    print("Recuperação.")
else:
    print("Reprovado.")

#Composto

media = 10
presenca = 100

if media >= 8 and presenca >=70:
    print("Aprovado.")
else:
    print("Reprovado.")