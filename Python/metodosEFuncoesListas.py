# LIST METHODS AND FUCTIONS
lista = [1,3,12,8,2]

#APPEND, is a method to add a item in the end.
print("Antes do append:", lista)
 
#INSERT
lista.insert(2,10)
print("Depois do insert:" , lista)

#EXTEND
lista2 = [1, 2, 3]
lista.extend(lista2)
print("Depois do extend: ", lista)

#POP
print("Depois do pop:", lista.pop(0))

#REMOVE 
print("Depois do remove:", lista.remove(3))

#COUNT
print("Quantidade de 2 na lista:", lista.count(2))

#INDEX
print("Índice do elemento 12: ", lista.index(12))

#SORT 
lista.sort()
print("Lista ordenada: ")
lista.sort(reverse=True)
print("Lista ordenada em ordem decrescente: ")

#FUNCTION TO LIST
#len
print("Aqui vai o tamanho da lista (por itens): ", len(lista))
#sum
print("Aqui é somando todos os itens", sum(lista))
#max
print("Qual o maior elemento da lista?", max(lista))
#min
print("Qual o menor elemento da lista:", min(lista))