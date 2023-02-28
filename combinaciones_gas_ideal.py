import itertools
from itertools import product

"Conviene mencionar que N es el número de casillas posibles que pueden tomar"
"valores V= 1,2,3, los cuales corresponden a los numeros cuánticos. "
N = 9
V = ['1','2','3']

combinaciones = itertools.product(V, repeat=N)

print(list(combinaciones))
