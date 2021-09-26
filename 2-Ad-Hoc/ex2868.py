#entrada
n = int(input())
for i in range(0, n):
    expressao = str(input()).split()

    #processamento
    v1 = int(expressao[0])
    operacao = expressao[1]
    v2 = int(expressao[2])
    respErrada = int(expressao[4])

    if operacao == '+':
        respCerta = v1 + v2
    elif operacao == '-':
        respCerta = v1 - v2
    else:
        respCerta = v1 * v2

    diferenca = abs(respCerta - respErrada)

    errou = 'E'
    for j in range(0, diferenca):
        errou += 'r'

    errou += 'ou!'

    #saida
    print(errou)
