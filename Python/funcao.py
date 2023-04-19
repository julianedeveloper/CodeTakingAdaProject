#FUNÇÕES

"""
1 -  O que são funções e por que usar?
Função é quando abstraio uma lógica, que será usada repetidamente.

Funções já usadas anteriormente:
print() = Imprimi uma msg (seja str, boo, float, etc...) no console (terminal ou cmd).
input() = Retorna um dado informado pelo user.
len() = Recebe uma lista e retorna o tamanho da lista.
max() = Retorna o maior valor de uma lista.

"""

#2 - Criação de Funções
#Função Inicial 
def saudacao():
    print("Olá! Seja bem vindo(a)!")
    print("É um prazer ter você em nosso curso!")

    saudacao()

#Função com parâmetros
def saudacao(nome, curso):
    print(f"Olá! Seja bem vindo(a) {nome}!")
    print(f"É um prazer ter você em nosso curso {curso}!")

    saudacao('Juliane', 'Data Science')
    saudacao('Fernando', 'Arquitetura')

#Função com parâmetros default
def saudacao(nome, curso = 'Python'):
    print(f"Olá! Seja bem vindo(a) {nome}!")
    print(f"É um prazer ter você em nosso curso {curso}!")

    saudacao('Juliane', 'Data Science')
    saudacao('Fernando', 'Arquitetura')

#Função com retorno
def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1*num2
    

    resultado = calculadora(10, 20, '-')
    print(resultado)
    print("Fim do código.")



