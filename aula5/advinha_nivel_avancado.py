
#Neste exemplo irei fazer um jogo de advinhação em nivel mais acima do fácil:

import random


numero_aleatorio=random.randrange(1,30)
numero_tentativas=4

for i in range(numero_tentativas):
    #solicitando entrada do usuario
    tentativa=int(input("Digite um número: "))
    if(tentativa == numero_aleatorio):
        print('Parabéns! Você acertou o número!')
        break  # Encerra o loop se acertar
    else:
            if tentativa < numero_aleatorio:
                print('Tente um número maior.')
            else:
                print('Tente um número menor.')
else:
     print("Você não acertou, suas tentativas se esgotou , numero correto é : " ,  numero_aleatorio)


# Repare que o for no Python é bem diferente do for no Java em Java é algo como:
"""for (int i = 0; i < numero_tentativa; i++) {
    // código a ser repetido
}"""

# Vamos entender agora detalhe por detalhe neste for diferente em Python:

