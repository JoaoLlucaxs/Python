nome=input('Informe seu nome');
print("Bem vindo ao mundo Python " + nome);

dia=input('Informe o dia');
mes=input('Informe o mes');
ano=input('Informe o ano');

pergunta=print('VocÊ nasceu no dia ' , dia , mes , ano ,  ' correto? digite 0 para SIM e 1 para NÃO');

if pergunta == 0:
    print("Uhuull seja muito bem vindo!");
elif pergunta == 1:
    print("Ué , verifique por gentileza as informações que você nos passou")
else:
    print("Favor digitar corretamente as opções passadas a você");


numero1=3;
numero2=6;
total=numero1 + numero2;

print('A soma é ' , total);

