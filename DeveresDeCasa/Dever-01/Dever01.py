import time
import random

def bubble_sort(arr):
    """
    Implementação do Bubble Sort.
    Ordena uma lista de números em ordem crescente.
    """
    n = len(arr)
    for i in range(n - 1):
        troca = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                troca = True
        if not troca:
            break
    return arr

def medir_tempo_execucao(tamanho):
    """
    Mede o tempo de execução do Bubble Sort para uma lista aleatória de determinado tamanho.
    """
    arr = [random.randint(0, 1000000) for _ in range(tamanho)]  # Gera lista aleatória

    inicio = time.time()  # Marca o tempo inicial
    bubble_sort(arr)  # Executa o algoritmo
    fim = time.time()  # Marca o tempo final

    tempo_execucao = fim - inicio  # Calcula o tempo total
    print(f"Tamanho: {tamanho} | Tempo de execução: {tempo_execucao:.6f} segundos")

# Executa para diferentes tamanhos de entrada
tamanhos = [100, 1_000, 10_000, 100_000]

for tamanho in tamanhos:
    medir_tempo_execucao(tamanho)