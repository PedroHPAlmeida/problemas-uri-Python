#entrada
n1, n2, n3 = str(input()).split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

#processamento
digitado = [n1, n2, n3]
crescente = [0, 0, 0]

if n1 == n2 and n2 == n3:
    crescente = [n1, n2, n3]
else:
    if n1 < n2 and n2 < n3:
        crescente = [n1, n2, n3]
    elif n1 < n2 and n1 < n3:
        crescente = [n1, n3, n2]
    elif n2 < n1 and n1 < n3:
        crescente = [n2, n1, n3]
    elif n2 < n1 and n2 < n3:
        crescente = [n2, n3, n1]
    elif n3 < n1 and n1 < n2:
        crescente = [n3, n1, n2]
    else:
        crescente = [n3, n2, n1]

#saída 
for cont in range(0,3):
    print(f"{crescente[cont]}")

print("")

for cont in range(0,3):
    print(f"{digitado[cont]}")
