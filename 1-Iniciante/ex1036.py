from math import sqrt
#entrada
a, b, c = str(input()).split()
a = float(a)
b = float(b)
c = float(c)

#processamento
delta = b**2 - 4 * a * c

if delta < 0:
    print("Impossivel calcular")
elif a == 0:
    print("Impossivel calcular")
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)

    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
