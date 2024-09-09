def max_heapify(A, i, heap_size):
    l = 2 * i + 1
    r = 2 * i + 2
    if (l < heap_size and A[l] > A[i]):
        largest = l
    else:
        largest = i
    if (r < heap_size and A[r] > A[largest]):
        largest = r
    if (largest != i):
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)


def main():
    listaPrincipal = [16, 14, 8, 10, 7, 9, 3, 2, 4, 1]
    print(listaPrincipal)
    n = len(listaPrincipal)
    max_heapify(listaPrincipal, 2, n)
    print(listaPrincipal)


if __name__ == "__main__":
    main()

