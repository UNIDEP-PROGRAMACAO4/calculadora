from app.calculadora import Calculadora


def obtem_numero():
    opcao_valida = False
    numero = 0
    while not opcao_valida:
        try:
            numero = float(input('Informe um número: '))
            opcao_valida = True
        except:
            print('Opção inválida')

    return numero

def obtem_opcao_operacao():
    opcao_valida = False
    opcao = 1
    while not opcao_valida:
        try:
            print('Informe uma opção: ')
            opcao = int(input('1 - Soma, 2 - subtração, 3 multiplicação, 4 divisão'))
            if opcao not in (1, 2, 3, 4):
                print('Opção inválida!')
            else:
                opcao_valida = True
        except:
            print('Opção inválida!')

    return opcao


def obtem_operacao(opcao, numero1, numero2):
    calculadora = Calculadora(numero1, numero2)
    if opcao == 1:
        return calculadora.soma
    if opcao == 2:
        return calculadora.subtracao
    if opcao == 3:
        return calculadora.multiplicacao
    return calculadora.divisao
