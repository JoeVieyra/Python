#otra forma de crear listas
lista = list()
#posision en la lista
#           0       1    2     3
lista2 =['String', 10, 15.5, True]
#recomencion listas con un mismo tipo de dato

#posision en la lista
#                   0       1         2      3 
lista_cursos = ['python','Django','Flask','java','rust','css']
#para generar sub listas se colocan el indice inicial y el 
#indice final

#[start:end]
#[start:]->Obtenemos los últimos elementos de la lista
#[:end]->Obtenemos los primeros elementos de la lista
sub_lista = lista_cursos[1:6:2]
#[start:end:skip]
primer_curso = lista_cursos[0]
ultimo_curso = lista_cursos[3]
print(primer_curso,ultimo_curso,sub_lista)
 
 
