from math import tan
#entrada
pi = 3.141592654
while True:
   try:
      angulo, distanciaArvore, alturaElfo = str(input()).split()
      angulo = float(angulo)
      distanciaArvore = float(distanciaArvore)
      alturaElfo = float(alturaElfo)

      #processamento
      alturaArvore = tan(angulo * (pi/180)) * distanciaArvore + alturaElfo
      qntdCordao = alturaArvore * 5

      #saida
      print('{:.2f}'.format(qntdCordao))
   except EOFError:
      break
