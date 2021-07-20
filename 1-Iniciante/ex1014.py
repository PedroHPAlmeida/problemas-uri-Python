#layout
cores = {"limpa":"\033[m", 
        "verde":"\033[4;32m"}
#entrada
km = int(input())
litros = float(input())

#processamento
kmPorLitro = km / litros

#saída
print("{}{:.3f}{} km/l".format(cores["verde"], kmPorLitro, cores["limpa"]))
