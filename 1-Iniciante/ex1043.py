#entrada
a, b, c = str(input()).split()
a = float(a)
b = float(b)
c = float(c)

#processamento/saída
if (a + b) > c and (a + c) > b and (c + b) > a:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")
