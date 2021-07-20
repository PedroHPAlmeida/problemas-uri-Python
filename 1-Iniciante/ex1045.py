#entrada
l1, l2, l3 = str(input()).split()
l1 = float(l1)
l2 = float(l2)
l3 = float(l3)

#processamento
#ordem descrescente
if l1 >= l2 >= l3:
    a = l1
    b = l2
    c = l3
elif l1 >= l3 > l2:
    a = l1
    b = l3
    c = l2
elif l2 > l1 >= l3:
    a = l2
    b = l1
    c = l3
elif l2 > l3 > l1:
    a = l2
    b = l3
    c = l1
elif l3 > l1 >= l2:
    a = l3
    b = l1
    c = l2
else:
    a = l3
    b = l2
    c = l1


#processamento/saída
if a >= (b + c): #forma um triangulo?
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == (b**2 + c**2):
        print("TRIANGULO RETANGULO") #triangulo retangulo
    if a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO") #triangulo obtu
    if a**2 < (b**2 + c**2):
        print("TRIANGULO ACUTANGULO") #triangulo acutan
    if a == b == c:
        print("TRIANGULO EQUILATERO") #triangulo equilatero
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES") #triangulo isosceles
