
# APÓS ENTENDERMOS SOBRE VARIAVEIS LOCAIS ESTANDO FORA E SENDO CHAMADA DENTRO DE UMA FUNÇAÕ FUNCIONA VEJA:

nome="João Lucas" 

def minhafuncao():
    print("Olá " + nome)


minhafuncao()


# PORÉM APÓS DECLARARMOS UMA VARIAVEL GLOBAL CHAMADA "nomeCompleto" FORA DA FUNÇÃO E OUTRA VARIAVEL COM O MESMO NOME VEJA O QUE ACONTECE

nomeCompleto="Lucas"

def testeVariavel():
    nomeCompleto="Joao"
    print("Olá " + nomeCompleto)

testeVariavel() # Sairá Joao , a variavel com mesmo nome vai sempre sobresair a variavel LOCAL

# CHAMANDO A VARIAVEL QUE ESTÁ DENTRO DA FUNÇÃO DEPOIS (FORA DA FUNÇÃO) 

def chamaVariavel():
    ola="Opa python tudo bem?"

chamaVariavel()

# -> print(ola) # Dirá que não foi definida, pois é uma variavel LOCAL

def chamarVariavel2():
    global ola  # definindo a variavel que está dentro da função como global ela se torna variavel global (use raramente isso)
    ola="Opa python"

chamarVariavel2()

print(ola);

