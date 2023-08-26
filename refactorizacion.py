def primer_caso():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        if point.isdigit():
            point = int(point)
            if 1 <= point <= 5:
                comment = input('Introduzca sus comentarios.\n')
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
            else:
                print('Indíquelo en una escala de 1 a 5')
        else:
            print('Por favor, ingresa el punto de evaluación como un número')


def segundo_caso():
    print('Resultados hasta la fecha.')
    with open("data.txt", "r") as read_file:
        print(read_file.read())


def tercer_caso():
    print('Terminación.')


while True:
    print('''Seleccione el proceso que desea aplicar
    1:Ingresa el punto de evaluación y el comentario
    2: Comprueba los resultados obtenidos hasta ahora
    3: Terminación.''')
    num = input()

    if num.isdigit():
        num = int(num)
        if num == 1:
            primer_caso()
        elif num == 2:
            segundo_caso()
        elif num == 3:
            tercer_caso()
            break
        else:
            print('Introduzca de 1 a 3')
    else:
        print('Introduzca de 1 a 3')
