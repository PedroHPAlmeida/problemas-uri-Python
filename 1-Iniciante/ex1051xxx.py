def taxa(valor=0, op=0):
    if valor <= 2000:
        return 0
    elif valor <= 3000:
        return 0.8
    elif valor <= 4500:
        return 0.8 
    else:
        return 0.28
    

#entrada
salario = float(input())
baseCalc = (salario - 2000) - (salario % 1000)
rest = (salario - 2000) % 1000 

#processamento
taxaSal = taxa(salario)
taxaBas = taxa(baseCalc, 1)

if taxaSal == 0:
    print('Isento')
else:
    irpf = (taxaSal * rest) + (taxaBas * baseCalc)
    print(f'R$ {irpf:.2f}')
