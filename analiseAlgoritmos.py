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
    """Gera um array de inteiros aleatórios de tamanho especificado."""
    return np.random.randint(0, 1000000, size)

def measure_time(algorithm, arr):
    """Mede o tempo de execução de um algoritmo."""
    start_time = time.perf_counter()  # Marca o tempo de início
    algorithm(arr.copy())  # Executa o algoritmo, usando uma cópia do array para evitar modificações
    end_time = time.perf_counter()  # Marca o tempo de término

    return end_time - start_time  # Retorna a diferença de tempo (tempo de execução)

def analise_execucao():
    """Função para analisar e comparar o tempo de execução dos algoritmos."""
    # Tamanhos dos arrays
    array_sizes = [10 ** i for i in range(1, 5)]  # De 10^1 a 10^6

    # Dicionário para armazenar os tempos de execução
    execution_times = {
        "InsertionSort": [],
        "QuickSort": [],
        "SelectionSort": [],
        "MergeSort": [],
        "HeapSort": []
    }

    # Medição de tempo para cada tamanho de array
    for size in array_sizes:
        arr = generate_random_array(size)  # Gera um array aleatório para o tamanho atual

        # Medir tempo para InsertionSort
        time_insertion_sort = measure_time(insertionSort, arr)
        execution_times["InsertionSort"].append(time_insertion_sort)

        # Medir tempo para QuickSort
        time_quick_sort = measure_time(quickSort, arr)
        execution_times["QuickSort"].append(time_quick_sort)

        # Medir tempo para SelectionSort
        time_selection_sort = measure_time(selectionSort, arr)
        execution_times["SelectionSort"].append(time_selection_sort)

        time_merge_sort = measure_time(mergeSort, arr)
        execution_times["MergeSort"].append(time_merge_sort)

        time_heap_sort = measure_time(heapSort, arr)
        execution_times["HeapSort"].append(time_heap_sort)

    # Plotando os resultados
    x_values = array_sizes

    plt.figure(figsize=(10, 6))  # Define o tamanho da figura
    plt.plot(x_values, execution_times["InsertionSort"], label='InsertionSort', marker='o')
    plt.plot(x_values, execution_times["QuickSort"], label='QuickSort', marker='s')
    plt.plot(x_values, execution_times["SelectionSort"], label='SelectionSort', marker='x')
    plt.plot(x_values, execution_times["MergeSort"], label='MergeSort', marker = 'D')
    plt.plot(x_values, execution_times["HeapSort"], label='HeapSort', marker = '^')

    # Configurações do gráfico
    plt.xscale('log')  # Escala logarítmica no eixo X
    plt.yscale('log')  # Escala logarítmica no eixo Y
    plt.xlabel('Tamanho do Array (log)')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Comparação de Algoritmos de Ordenação')
    plt.legend()
    plt.grid(True)  # Adiciona uma grade ao gráfico

    # Mostrando o gráfico
    plt.show()

if __name__ == "__main__":
    analise_execucao()  # Executa a função de análise
