from particioneQuickSort import particione


def quickSort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = particione(lista, inicio, fim)
        quickSort(lista, inicio, p-1)
        quickSort(lista, p+1, fim)



def main():
    lista = [99, 33,55,77,11,22,88,66, 33, 44]
    n = len(lista) - 1
    quickSort(lista)
    print(lista)

if __name__ == "__main__":
    main()