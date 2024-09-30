import time
from cProfile import label

import numpy as np

from heapSort import heapSort
from insertionSort import insertionSort
from mergeSort import mergeSort
from quickSort import quickSort
from selectionSort import selectionSort
import matplotlib.pyplot as plt

def generate_random_array(size):
    return np.random.randint(0, 1000000, size)

def measure_time(algorithm, arr):
    start_time = time.perf_counter()
    algorithm(arr.copy())
    end_time = time.perf_counter()

    return end_time - start_time

def analise_execucao():
    array_sizes = [10 ** i for i in range(1, 6)]
    execution_times = {
        "InsertionSort": [],
        "QuickSort": [],
        "SelectionSort": [],
        "MergeSort": [],
        "HeapSort": []
    }

    for size in array_sizes:
        arr = generate_random_array(size)

        time_insertion_sort = measure_time(insertionSort, arr)
        execution_times["InsertionSort"].append(time_insertion_sort)

        time_quick_sort = measure_time(quickSort, arr)
        execution_times["QuickSort"].append(time_quick_sort)

        time_selection_sort = measure_time(selectionSort, arr)
        execution_times["SelectionSort"].append(time_selection_sort)

        time_merge_sort = measure_time(mergeSort, arr)
        execution_times["MergeSort"].append(time_merge_sort)

        time_heap_sort = measure_time(heapSort, arr)
        execution_times["HeapSort"].append(time_heap_sort)

    x_values = array_sizes

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, execution_times["InsertionSort"], label='InsertionSort', marker='o')
    plt.plot(x_values, execution_times["QuickSort"], label='QuickSort', marker='s')
    plt.plot(x_values, execution_times["SelectionSort"], label='SelectionSort', marker='x')
    plt.plot(x_values, execution_times["MergeSort"], label='MergeSort', marker = 'D')
    plt.plot(x_values, execution_times["HeapSort"], label='HeapSort', marker = '^')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Tamanho do Array (log)')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Comparação de Algoritmos de Ordenação')
    plt.legend()
    plt.grid(True)


    plt.show()

if __name__ == "__main__":
    analise_execucao()
