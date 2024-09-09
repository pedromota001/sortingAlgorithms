def max_heapify(A, i):
    l = 2 * i + 1
    r = 2 * i + 2
    if (l < len(A) and A[l] > A[i]):
        largest = l
    else:
        largest = i
    if (r < len(A) and A[r] > A[largest]):
        largest = r
    if (largest != i):
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def main():
    listaPrincipal = [16, 14, 8, 10, 7, 9, 3, 2, 4, 1]
    print(listaPrincipal)
    max_heapify(listaPrincipal, 2)
    print(listaPrincipal)


if __name__ == "__main__":
    main()

