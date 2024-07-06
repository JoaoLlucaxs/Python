# é NECESSÁRIO ESSA CONVERSÃO (INT)? -> NÃO , POIS ELE ENTENDERÁ
#Qual é o método para imprimir Hello World ou qualquer mensagem?
#Você pode usar os seguintes métodos –

#método print()
#Método sys.stdout.write() importando o módulo sys
#Usando string python-f

a=int(input('Digite um numero'));
b=int((input('Digite outro numero')));

total=a + b;
print('A soma é : ' , total);
print('Valor do a = ' , a);
print('Valor do b = ' , b);

# Em python para saber o tipo dessa variavel basta utilizar:
nome="Brasil";
print(type(nome))

quantidade=5
print(type(quantidade))

# O python muda sua variavel dinamicamente diferente do Java que é tipagem forte estatica e não muda sua variavel para outro tipo
#Variáveis ​​não precisam ser declaradas com nenhum tipo específico e podem até mesmo mudar de tipo depois de serem definidas
pais="Brasil"
pais=655
pais=4.5

# Se quiser converter variaveis logo de cara basta fazer o seguinte
x = str(3)    # x irá ser '3' -> str signfica STRING
y = int(3)    # y irá ser 3
z = float(3)  # z irá ser 3.0

# Muitos valores para múltiplas variáveis
x, y, z = "Laranja", "Banana", "Maça"
print(x)
print(y)
print(z)

# Testando uma função básica
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Lidando com escopo -> vamos ver uma função com variavel que morre após seu escopo
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# Utilizando GLOBAL -> a variável pertence ao escopo global: (Não acredito que seja muito util de se utilizar a depender do tamanho do projeto)
# Diferente dos testes acima que a variavel morre após a função acabar vou demonstrar utilizando GLOBAL que não morrerá e é atribuida recebendo um novo valor mesmo depois da função ser chamada
def myfunc():
  global y
  y = "que fantastico"

myfunc()

print("Python é diferente " + y)

z = "Testando"

def myfunc():
  global z # estou dizendo que essa varialve agora será global podendo ser chamada e atribuida em qualquer lugar
  z = "teste de python" # sendo global agora o z=testanto será trocado por essa string, e chamando após termino da função ocorrerá a troca devido a variavel agora ser global

myfunc()

print("Entendendo global " + z)