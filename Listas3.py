lista = [8, 9, 7, 5, 4, 1, 45, 110, 21]
#el metodo .sort() ordena la lista en forma asendente
#el parametro .sort(reverse=True) ordena de forma desendente

lista.sort()
#min -max conocer el manor elemento y le mayor
print(min(lista))
print(max(lista))
#in nos permite conocer si un elemento se encentra en la lista
print(4 in lista)
print(11 not in lista) 
print(lista[0],lista[-1])

print(8 in lista)
print(lista.index(8))
