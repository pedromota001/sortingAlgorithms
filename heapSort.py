from buildMaxHeap import build_maxHeap
from max_heapfy import max_heapify


def heapSort(lista):
    n = len(lista)
    heap_size = n
    build_maxHeap(lista)
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heap_size -= 1
        max_heapify(lista, 0, heap_size)

def main():
    lista = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heapSort(lista)
    print(lista)

if __name__ == "__main__":
    main()