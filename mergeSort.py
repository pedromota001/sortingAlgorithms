def mergeSort(lista, inicio=0, fim = None):
    if fim is None:
        fim = len(lista) - 1
    if(fim - inicio > 0):
        meio = (inicio + fim) // 2
        mergeSort(lista, inicio, meio)
        mergeSort(lista, meio+1, fim)
        merge(lista, inicio,meio,fim)

def merge(lista, inicio, meio, fim):
    listaB = [0] * (fim + 1)
    for i in range(inicio, meio+1):
        listaB[i] = lista[i]
    for k in range(meio+1, fim+1):
        listaB[fim + ((meio + 1) - k)] = lista[k]
    i = inicio
    k = fim
    for j in range(inicio, fim+1):
        if(listaB[i] < listaB[k] and i <= meio):
            lista[j] = listaB[i]
            i = i + 1
        else:
            lista[j] = listaB[k]
            k = k - 1

def main():
    listaPrincipal = [15, 3,8,7,1, 2,0, 17, 16, 25, 28, 45, 33]
    mergeSort(listaPrincipal, 0, len(listaPrincipal) - 1)
    print(listaPrincipal)


if __name__ == "__main__":
    main()
