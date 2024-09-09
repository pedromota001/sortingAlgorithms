from max_heapfy import max_heapify

def build_maxHeap(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(lista, i, n)



def main():
    lista = [4,1,3,2,16,9,10,14,8,7]
    build_maxHeap(lista)
    print(lista)

if __name__ == "__main__":
    main()