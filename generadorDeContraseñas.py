import random

print('*** Generador de Contrasenas ***')
sistemaAT=True
# Solicitar al usuario la cantidad de contraseñas que quiere generar
while sistemaAT:
    try:
        numeroDeContrasenias = int(input('Indica cuántas contraseñas deseas generar: '))
        largoDeContrasenia = 15 #cantidad ideal de caracteres para tener una contraseña fuerte
        sistemaAT = False #Sale del bucle
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")
        
#caracteres utilizados para generar la contraseña
char='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()-_.,?'

print('\n Aqui tienes tus contrasenas: ')
for i in range(numeroDeContrasenias):
    contrasenia=''
    for j in range(largoDeContrasenia):
        contrasenia+=random.choice(char)
    print(contrasenia)



