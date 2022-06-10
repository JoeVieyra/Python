nombre = input('introduce tu nombre: ')
edad = int (input('ingresa tu edad: '))
altura = float (input('introduce tu altura: '))
autorizacion = input('autorizas?') == 'si'

print(nombre, edad, altura,autorizacion)
print(type(nombre),type(edad),type(altura), type(autorizacion))
