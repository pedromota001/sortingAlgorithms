def selectionSort(lista):
    tam = len(lista)
    for i in range(0, tam-1):
        menor = i
        for j in range(i+1, tam):
            if(lista[j] < lista[menor]):
                menor = j
        temp = lista[menor]
        lista[menor] = lista[i]
        lista[i] = temp

def main():
    listaPrincipal = [15, 3,8,7,1, 2,0, 17, 16, 25, 28, 45, 33]
    selectionSort(listaPrincipal)
    print(listaPrincipal)


if __name__ == "__main__":
    main()