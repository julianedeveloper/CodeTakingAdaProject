#Comentário de uma linha.

"""
Comentário multilinha.
"""
idade = 34 #declarando uma variável no Python.
nome = "Juliane"
altura = 1,63
estudando = True
linguagem = input("Linguagem de programação atualmente estudada: ")

"""
1.int: números inteiros, sem decimal. Ex: 0, -10, 34.
2.float: números decimais, números reais. Ex: 0,77, 4,57, -7,27.
3.str:cadeia de caracteres.
4.boolean: valores lógicos. True ou false. Sempre um dos dois.
"""

print(type(idade)) # o type me mostra de forma declarado no código, o tipo da variável.
print (type(nome))
print(type(altura))
print(type(estudando))
print("A linguagem estudada atualmente por ", nome, " é ", linguagem, ".")

