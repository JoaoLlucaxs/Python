
#Vamos entender os tipos de dados em python
## Já entendemos que a tipagem do python é dinamica ou seja não preciso dizer seu tipo ao declarar uma variavel

x = 5
print(type(x)) # ela é um int e o python sabe 

x = "Hello World" #str
x = 20 # int
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

# Se você quiser manualmente informar especificar o tipo de dado especifico poderá (Só não necessário ao meu ver , já que estamos tratando de uma linguagem de tipagem dinamica)
x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview

# Observação -> Float também pode ser um número científico com um "e" para indicar a potência de 10. : 
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))