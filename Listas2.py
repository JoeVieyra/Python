lista_cursos = ['python','Django','Flask','java','rust','css']
lista_cursos2 = ['c','c++','Docker']
#len cuanta los elementos en las listas
print(len(lista_cursos))
#append agrega elementos a la lista en la posicion final
lista_cursos.append('MongoDB')
lista_cursos.append('c#')
#insert agrega un elemento en la pocision que le digamos
lista_cursos.insert(1, 'Rails')
#.extend agrega los elementos de la lista 1 a la 2
lista_cursos.extend(lista_cursos2)


print(lista_cursos)
print(len(lista_cursos))
#.remove elimina elementos seleccionados0
lista_cursos.remove('MongoDB')
print(lista_cursos)
#del elimina elementos por indice
del lista_cursos[0]
#clear elimina todos los elementos de la lista
lista_cursos.clear()

print(lista_cursos)