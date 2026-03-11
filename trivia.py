nombre_usuario = input('ingrese su nombre')
contador = 0
respuesta_1 = 'perro'
respuesta_2 = 'pajaro'
respuesta_3 = 'leon'
respuesta_4 = 'elefante'

print('Bienvenido esta es una trivia')

pregunta1 = input('que animal tiene 4 patas y una cola?')
if pregunta1 == respuesta_1:
    contador += 1
    print('haz ganado un punto')
else:
    print('incorrecto')

pregunta2 = input('que animal puede volar?')
if pregunta2 == respuesta_2:
    contador += 1
    print('haz ganado un punto')
else:
    print('incorrecto')

pregunta3 = input('que animal tiene 4 patas y una cola?')
if pregunta3 == respuesta_3:
    contador += 1
    print('haz ganado un punto')
else:
    print('incorrecto')

pregunta4 = input('que animal tiene 4 patas y una cola?')
if pregunta4 == respuesta_4:
    contador += 1
    print('haz ganado un punto')
else:
    print('incorrecto')

print(f'fin, haz obtenido {contador} puntos')
