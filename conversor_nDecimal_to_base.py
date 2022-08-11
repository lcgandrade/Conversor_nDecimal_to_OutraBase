import numpy as np
import math

def conversor_nDecimal():

    valor=int(input('Digite o valor no Sistema Decimal: '))
    base=int(input('Digite a base para qual se deseja converter: '))
    quociente=abs(valor)
    restos=""

    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    f = 'f'

    while quociente > 0:
        if quociente%base == 10:
            restos+=str(a)
            quociente=quociente // base
        if quociente%base == 11:
            restos+=str(b)
            quociente=quociente // base
        if quociente%base == 12:
            restos+=str(c)
            quociente=quociente // base
        if quociente%base == 13:
            restos+=str(d)
            quociente=quociente // base
        if quociente%base == 14:
            restos+=str(e)
            quociente=quociente // base
        if quociente%base == 15:
            restos+=str(f)
            quociente=quociente // base
        else:
            restos+=str(quociente%base)
            quociente=quociente // base

    if (valor > 0):
        print('({}) 10 = ({}) {}'.format(valor, restos[::-1], base))
    else:
        print('({}) 10 = (-{}) {}'.format(valor, restos[::-1], base))

conversor_nDecimal()