
#Utilizando tecnicas de um script de advinhação com a linguagem python

print("Bem vindo ao jogo de advinhação")

numero_correto=43;

chute=input("Informe o número: ")
print("Você digitou ", chute)
conversao=int(chute)

if(conversao == numero_correto):
    print("Você acertou")
else:
    print("VocÊ errou")


# Coisas que podem gerar erro de sintaxe devido a tabs por exemplo
if 5 > 2:
  print("Five is greater than two!")

if 5 > 2:
   print("Condicional para teste de sintaxe")
#print("Five is greater than two!") -> Aqui dará erro

numero1=6;
numero2=8;
if numero1 > numero2:
 print("Sim, numero 1 é maior que número 2 ") 
else:
    print("Não, número 1 não é maior que numero 2") 

    """
    Isso também é um comentário
    """