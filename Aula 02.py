# TIPOS DE DADOS
# 4 TIPOS DE DADOS
# INTEIRO: NUMEROS INTEIROS(1,2,-5,-10....)
# VIRGULA : NÚMERO COM PONTO FLUTUANTE: (1.2 - 5.4...)
# TEXTUAIS : STRINGS (A, AULA, HOJE É DIA 3)
# BOOLEANOS: VERDADEIRO OU FALSO
# EXEMPLOS DE NÚMEROS INTEIROS : "int" (integer) = INTEIRO ( 1,2,-4...)
# EXEMPLOS DE NÚMEROS COM VÍRGULA: "float" (7.4 , 3.2 , -1.8...)
# EXEMPLOS DE DADOS TEXTUAIS: (entre aspas) "str" ( "a" , "Escola" , "Aprendendo Python")
# EXEMPLOS DE DADOS BOOLEANOS: "bool" (True, False)

# VARIÁVEIS
# Colocar um nome que seja intuitivo. Que represente a realiadade.
# Exemplos:
# numero1 = 5
# numero2 = 2
# soma = numero1 + numero2
# nome_completo = "Jeniffer Schwengber"
# nome = "João"

# OPERAÇÕES MATEMÁTICAS
# SOMA: + (2+3)
# SUBTRAÇÃO: - (6-4)
# MULTIPLICAÇÃO: * (6*2)
# DIVISÃO: / (7/4)


# numero1 = 58
# print(numero1)
# numero2 = 87
#soma = numero1+numero2
# print(soma)
#divisao = numero1/numero2
# print(divisao)
#subtraçao = numero1-numero2
# print(subtraçao)
#multiplicação = numero1*numero2
# print(multiplicação)

# ORDEM DE PRECEDÊNCIA
# 1) Potenciação
# 2) Multiplicação (ou divisão): o que aparecer 1°
# 3) Subtração (adição) : o que aparecer 1°

#calculo = 2+45*23/3-29
# print(calculo)
#calculo2 = ((2+45)*23)/3-29
# print(calculo2)

# RECEBER INFORMAÇÃO DE ALGUEM (usuario informar) (input)

# numero1 = int(input("Digite um número:"))
# numero2 = int(input("Digite outro número:"))
# soma= numero1 + numero2
# print("A soma é:", soma)

# divisao = numero1/numero2
# print("Resultado da divisão", divisao)

# EXEMPLO DE PROGRAMA (CALCULADORA 04 OPERAÇÕES)

#primeiro_numero= int(input("Informe um número:"))
#segundo_numero= int(input("Informe outro número:"))
#soma=primeiro_numero+segundo_numero
#subtraçao=primeiro_numero-segundo_numero
#multiplicação=primeiro_numero*segundo_numero
#divisão=primeiro_numero/segundo_numero
#print("A soma é:", soma)
#print("A subtração é:", subtraçao)
#print("A multiplicação é:", multiplicação)
#print("A Divisão é:", divisão)

# Criem um programa que solicite ao usuario o dia de nascimento,mês de nasciemnto e ano de nascimento:
# imprimir " Olá, fulano. Você nasceu dia  xx de xx de xxxx."

nome = str(input("Qual é o seu nome?"))
dia = int(input("Que dia você nasceu?"))
mes = str(input("Qual mês você nasceu?"))
ano = int(input("Qual ano você nasceu?"))

print("Olá",nome
