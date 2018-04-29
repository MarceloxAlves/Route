import random

x = 16
mapa = (x * x) * [0]

def main():
    montar_mapa()
    mostrar_mapa()

def montar_mapa():
    for i in range(0, len(mapa)):
        if is_borda(i):
            mapa[i] = "x"
        else:
            mapa[i] = tipo()
            caminho_valido(i)

def mostrar_mapa():
    for i in range(0, len(mapa)):
        print("%2s" % mapa[i], end=" ")
        if (i + 1) % x == 0:
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

def tipo():
    return random.randint(1, 5)

def caminho_valido(index):
    if index < prox_num(index-x):
        mapa[index] = 0
    return mapa[index]

#seleciona o tamanho da plataforma
def bloco():
    return random.randint(3,4)

def prox_num(index):
    if mapa[index] != 1:
        return index+x

if __name__ == '__main__':
    main()