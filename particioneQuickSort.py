def particione(lista, inicio, fim):
    x = lista[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if(lista[j] <= x):
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i+1], lista[fim] = lista[fim], lista[i+1]
    return i+1

def main():
    lista = [99, 33,55,77,11,22,88,66, 33, 44]
    n = len(lista) - 1
    particione(lista, 0, n)
    print(lista)


if __name__ == "__main__":
    main()
