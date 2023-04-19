#DICIONÁRIO
#Criando Dicionários

lista = []
dicionario = {}
dicionario = dict()

dicionario = {'Nome:':'Juliane','Idade:': 34,'Altura:':1.63 }
print(dicionario)
print(dicionario['Nome:'])

#Adicionando e Alterando elementos

dicionario['Programador:\\\                                                                                          s'] = True
dicionario['Altura:'] = 1.77
print(dicionario)

#Iterando sobre um dicionário
for chave in dicionario:
    print(chave, dicionario[chave])

#Testando a existência de uma chave 

print('Peso' in dicionario)
print('Altura' in dicionario)
print('Nome' in dicionario)