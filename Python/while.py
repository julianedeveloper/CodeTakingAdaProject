numero_sorteado = 15
numero_escolhido = int(input("Escolha um número entre 1 e 20."))

while numero_escolhido != numero_sorteado:
    print('Você errou, tente novamente.')

    numero_escolhido = int(input('Escolha um número entre 1 e 20.'))
    print('Parabéns, você acertou.')



