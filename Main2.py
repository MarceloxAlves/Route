import random

import Segundo

x = 16
mapa = (x * x) * [0]


def main():
    for i in range(0, len(mapa)):
      # print("%3d" % i,end=" ")
        if is_borda(i):
            mapa[i] =  "x"
            print("%2s" % mapa[i], end=" ")
        else:
            mapa[i] = random.randint(0, 1)
            caminho_valido(i)
            print("%2s" % mapa[i], end=" ")
        if (i+1) % x == 0:
            print("")

def is_borda(index):
    if(index < x):
        return True
    if index % x == 0:
        return True
    if (index+1) % x  == 0:
        return  True
    if index > (len(mapa)- x):
        return True
    return False

def caminho_valido(index):
    # if mapa[index-1] == 1:
    #     mapa[index] =  "s"

    if mapa[index-x+1] == 1:
        mapa[index] =  "0"
    if mapa[index-x-1] == 1:
        mapa[index] =  "0"



if __name__ == '__main__':
    main()