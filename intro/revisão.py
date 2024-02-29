#var sempre sugestivas e em snake case

idade_aluno="Luiza"

# Python não tem constantes. Na declaração de uma variável devemos indicar que su valor não deve ser alterado colocando tudo em letras maiúsculas.

GRAVIDADE_DA_TERRA= "9.8 m/s"

print (GRAVIDADE_DA_TERRA)


#conversão
#reserva valor inteiro

preco = 5.4

preco=int(preco)
print(preco)

#duas barras preserva o valor inteiro
print(preco//2)

#converter string
print(str(preco))


idade=22
nome='Luiza'

texto = f'meu nome é {nome} e tenho {idade} anos'
print(texto)


#imput

nome = input('informe seu nome: ')
print (nome)



#operadores
# aritméticos. 

print(10+2)

print(10-2)

print(10/2)

print(10*2)

print(10//2)

print(10%2)

print(10**2)


# comparação

#igualdade 
saldo=400
saque=50

print(saldo==saque)

#diferença
print(saldo!=saque)

#maior ou igual ou maior
print(saldo>saque)
print(saldo>=saque)

#menor ou igual ou menor
print(saldo<saque)
print(saldo<=saque)


# Atribuiçaõ

#adiçaõ, sub, div, mult, etc = só adicionar seu simbolo junto ao sinal de igualdade
saldo=500
saldo +=200

print(saldo)


#lógicos

limite=1000

print (saldo>= saque and saque <= limite)
print (saldo>= saque or saque <= limite)
print (not saldo>= saque and saque <= limite)


#identidade

curso='Python'
nome_curso = curso

print (curso is nome_curso)

print(curso is not nome_curso)

print(curso is saldo)


#condicional/repeticão

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:

    if numero % 2 == 0:  
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
        
        
#while

numero = int(input("Digite um número inteiro positivo: "))

if numero <= 0:
    print("Número inválido. Por favor, digite um número inteiro positivo.")
else:
    
    print("Contagem regressiva iniciada:")
    while numero > 0:
        print(numero)
        numero -= 1  
    print("Contagem regressiva concluída!")