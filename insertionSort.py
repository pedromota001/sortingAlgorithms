def insertionSort(lista):
    tam = len(lista)
    for i in range(1, tam):
        current = lista[i]
        j = i - 1
        while(j >= 0 and lista[j] > current):
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = current

def main():
    listaPrincipal = [15, 3,8,7,1, 2,0, 17, 16, 25, 28, 45, 33]
    insertionSort(listaPrincipal)
    print(listaPrincipal)

if __name__ == "__main__":
    main()