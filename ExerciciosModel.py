def exercicios01():
    A = 10
    B = 20
    msg = "Antes da Troca: A = {} , B = {}".format(A,B)
    aux = A
    A = B
    B = aux
    msg = msg + " \nDepois da Troca: A = {} , B = {}" .format(A,B)
    return msg


def exercicios02(num1):
    num1 - 1

def exercicios03(bas,altura):
    if bas <= 0:
        return  'Por favor,digite um número positivo!'
    elif altura <= 0:
        return  'Por favor,digite um número positivo!'
    else:
        return bas * altura

def exercicios04(anos,meses,dias):
    return (anos * 365) + (meses * 30) + dias

def exercicios05(eleitores,votosbrancos,votosnulos,total):
    eleitores = 5000
    votosbrancos = 2000

def exercicios06():
    A = 1500
    B = 15000
    msg = 'Salário mensal: A = {} , B = {}.format'(A, B)
    aux = A
    A = B
    B = aux
    msg = msg + " \nDepois salário atual: A = {} , B = {}".format(A, B)
    return msg
