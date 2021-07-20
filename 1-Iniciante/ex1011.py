#entrada
raio = float(input())
pi = float(3.14159)

#processamento
volume = (4/3.0) * pi * pow(raio, 3)

#saída
print("\033[32;44mVOLUME = {:.3f}\033[m".format(volume))
