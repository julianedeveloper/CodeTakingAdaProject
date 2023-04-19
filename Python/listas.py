#Before
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

#With list
notas = [7.9, 9.7, 8.2]

#Creating Lists
lista = [] #a empty list it's correct. There's the later possibility to fill with variables.
lista = list() #same the before here, plus that the lista() method, changes all datas in a list. Can be empty to be filled after.
lista = ["Juliane", True, 1.63, 37]
#lista_de_lista = [10[1,2,3]] #it's possible have a list inside another one.

#Indexing 
lista = ["Fernando", True, 1,75, 37]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-1]) #the negative numbers calls the list from the last one to the first one position. The -2 come the item before the last and 

#Slices
lista = [10,50,30,40,25,60,5]
print(lista[0:3])
print(lista[3:6])
print(lista[3:])
print(lista[2:6:2])

#Iteration with FOR
# 1 > Using the own list elements

for elemento in lista: #to any element in the list, then print the element.
    print(elemento)

#2 > Using the indexes

print(len(lista))

for i in range(len(lista)):
   # print(i) or
    print(lista[i]) 