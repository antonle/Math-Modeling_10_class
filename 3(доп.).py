def image(typel, focus, length):
    """функция, определяющая параметры изображения"""
    if (typel == 'собирающая'):
        if (length<focus):
            print('увеличенное, мнимое, прямое')
        elif (length == focus):
            print('бесконечное изображение')
        elif (length > focus) and (length<2*focus):
            print('увеличенное, действительное, перевернутое')
        elif (length == 2*focus):
            print('уменьшенное, действительное, перевернутое')
        else:
            print('уменьшенное, действительное, перевернутое')
    else:
        print ('уменьшенное, мнимое, прямое')

typel = 'собирающая'
focus = 2
length = 1
image(typel, focus, length)
            