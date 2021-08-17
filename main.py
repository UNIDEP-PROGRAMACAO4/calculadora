from app.calculadora import Calculadora
from app.telas import obtem_numero, obtem_operacao, obtem_opcao_operacao

continuar_calculando = True
while continuar_calculando:
    numero1 = obtem_numero()
    numero2 = obtem_numero()
    opcao = obtem_opcao_operacao()
    operacao = obtem_operacao(opcao, numero1, numero2)
    resultado = operacao()
    print(resultado)

    decisao = input('Deseja continuar calculando? S/N')
    if decisao in 'Nn':
        continuar_calculando = False




