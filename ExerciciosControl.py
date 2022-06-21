import this
import ExerciciosModel
this.opcao = -1


def Menu():
    print('Menu\n\n' +
          '\n1. Exercicio 01' +
          '\n2. Exercicio 02' +
          '\n3. exercicio 03' +
          '\n4. exercicio 04' +
          '\n5. exercicio 05' +
          '\n6. exercício 06' +
          '\n7. exercício 07' +
          '\n8. exercício 08' +
          '\n9. exercício 09' +
          '\n10.exercicio 10' +
          '\n11.exercicio 11' +
          '\n12 exercicio 12' +
          '\n13.exercicio 13' +
          '\n0. Sair'         +
          '\nEscolha uma das opções acima:')
    this.opcao = int(input())

def Executar():
    while(this.opcao != 0):
        Menu()
        if this.opcao == 0:
            print('Obrigado!')
        elif this.opcao == 1:
            print(ExerciciosModel.exercicios01())
        elif this.opcao == 2:
            print('Escreva aqui a solução para o exercício 02')
            num1 = int(input())
            print(ExerciciosModel.exercicios02(num1))
        elif this.opcao == 3:
            print('informe a base do retângulo')
            bas = float(input())
            print('informe a altura do retângulo')
            altura = float(input())
            print(ExerciciosModel.exercicios03(bas, altura))
        elif this.opcao == 4:
             print('informe a ano de uma pessoa')
             anos = int(input())
             print('informe o meses')
             meses = int(input())
             print('informe os dias')
             dias = int(input())
             print(ExerciciosModel.exercicios04(anos,meses,dias))
        elif this.opcao == 5:
             print('número de eleitores')
             eleitores = int(input())
             print('números de votos brancos')
             brancos = int(input())
             print('votos nulos')
             nulos = int(input())
        elif this.opcao == 6:
             print('informe o salário mensal')
             A = int(input())
             print('informe o salário atual')
             B = int(input())
             print(ExerciciosModel.exercicio06())
        elif this.opcao == 7:
             print('informe o custo de fábrica de um carro')





        else:
            print('Opção informada não é válida!')









