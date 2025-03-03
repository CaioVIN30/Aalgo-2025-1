
# Importar os módulos do sistema operacional
import os
import locale

# Definições e funções para todos os exemplos
# encoding: iso-8859-1

from datetime import datetime
import random

# Ajustando a localização para o Brasil
import os
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')
from datetime import datetime
import pytz

# Define o fuso horário para o Brasil (Brasília)
con_fuso_horario = pytz.timezone("America/Sao_Paulo")

conSeparador= "\nXXXXXXXXXXXXX---XXXXXXXXXXXXX\n"

# Função formatar tempo de execução (dado tempo de inicio e fim, retorna h:m:milisegundos formatado)
def formata_tempo_execucao (dttInicio, dttfim):
    strTempo = dttfim - dttInicio
    str_tempo_execucao_formatado = "{:02d}:{:02d}.{:06d}".format(
    strTempo.seconds // 60,  # Minutos
    strTempo.seconds % 60,  # Segundos
    strTempo.microseconds  # Microsegundos
    )
    return str_tempo_execucao_formatado

def formata_data(dttParametro):
  return dttParametro.strftime("%d/%m/%Y - %H:%M:%S.%f")

def formata_numero(numero):
    return locale.format_string("%d", numero, grouping=True)

# Cria um array do tamanho intElementosArray, valores inteiros entre intMin e intMax)
def montar_array (intElementosArray,intMin, intMax):
  x = 0
  array = []
  while x < intTamArray:
    intElementosArray = random.randint(intMin,intMax)
    array.append (intElementosArray)
    x += 1
  return (array)

def ler_inteiro (strMensagem):
  while True:
    try:      # Se nenhuma exceção ocorrer, a cláusula except é ignorada e a execução da instrução try é finalizada
      tamanho = int(input(strMensagem))
      break  # Se a entrada for válida, sai do loop e finaliza o programa
    except ValueError:
      print("Erro: Por favor, digite um número inteiro valido.")
  return tamanho


def carregar_array():
    arrMeuArray = []
    while True:
        entrada = input("Digite um número inteiro para o array (-1 para sair): ")
        try:
            numero = int(entrada)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue
        if numero == -1:
            break
        arrMeuArray.append(numero)
        print (f"O array atual tem {str(len(arrMeuArray))}. Seu conteúdo é \n")
        print (arrMeuArray)
    return arrMeuArray

def marcar_inicio (strMensagem):
  dttInicio = datetime.now(con_fuso_horario)
  dttInicioFormatado = formata_data(dttInicio)
  print(f"Iniciando {strMensagem} as : " + str(dttInicioFormatado))
  return dttInicio

def marcar_fim (strMensagem):
  dttFim = datetime.now(con_fuso_horario)
  dttFimFormatado = formata_data (dttFim)
  print(f"Finalizando {strMensagem} as : " + str(dttFimFormatado))
  return dttFim

"""# Aula 01

**Exemplo 01 - O(1)**
"""

arrMeuArray = []

# Data impressa não formatada e com timezone errado. PROPOSITAL PARA DEMONSTRAR ERROS.

print("Data impressa não formatada e com timezone errado. PROPOSITAL PARA DEMONSTRAR ERROS.\n")

dttInicio = datetime.now()
print("Iniciando a adição de um elemento ao array as : " + str(dttInicio))

intElementoArray = random.randint(0,10000000)
arrMeuArray.append (intElementoArray)

dttFim = datetime.now()
print("Finalizando a adição de um elemento ao array as : " + str(dttFim))
print("Tempo de execucao foi de: : " + (str(dttFim - dttInicio)))

print (f"O array é: {arrMeuArray}")

"""**Exemplo 2 - O(N)**"""

# Exemplo 2 - O(N) - tempor de execução cresce conforme tamanho da entrada de dados

print ("EXEMPLO 2 - incluir N elementos em um array - O(N)")

intTamArray = ler_inteiro("Digite o tamanho do array que deseja montar (>0)")
strTamArrayFormatado = formata_numero (intTamArray)

strMensagem = "incluir " + strTamArrayFormatado + " elementos em um array"

dttInicio = marcar_inicio (strMensagem)

arrMeuArray = montar_array (intTamArray,0,1000)

dttFim = marcar_fim (strMensagem)

strTempoExecucaoFormatado = formata_tempo_execucao(dttInicio, dttFim)

print(f"Tempo de execucao foi de: {strTempoExecucaoFormatado}")

"""**Exemplo 3 - O(log(N))**"""

# Exemplo 3 - Ordenar o Array através do Quicksort

print ("EXEMPLO 3 - Ordenar o Array com QuickSort - O(log (N))")

intTamArray = ler_inteiro("Digite o tamanho do array que deseja montar (>0)")
strTamArrayFormatado = formata_numero (intTamArray)
arrMeuArray = montar_array (intElementoArray,0,100000)
strTamArrayFormatado = formata_numero (intTamArray)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arrBubble = arrMeuArray.copy() # usar o método copy, caso contrário será criada uma referência e não um novo array.
arrQuick = arrMeuArray.copy()

strMensagem = "ordenar com Quick Sort " + strTamArrayFormatado + " elementos em um array"
dttInicio = marcar_inicio (strMensagem)

arrQuick = quick_sort(arrQuick)

dttFim = marcar_fim (strMensagem)

strTempoExecucaoFormatado = formata_tempo_execucao(dttInicio, dttFim)

print("Tempo de execucao do Quick Sort foi de: " + strTempoExecucaoFormatado)

"""**Exemplo 4 - O(N2) - N ao quadrado**"""

# Exemplo 4 - Ordenar o Array através do Bubblesort
print ("EXEMPLO 4 - Ordenar o Array com Bubble Sort - O(N2)")

intTamArray = ler_inteiro("Digite o tamanho do array que deseja montar (>0)")
strTamArrayFormatado = formata_numero (intTamArray)
arrMeuArray = montar_array (intElementoArray,0,100000)
strTamArrayFormatado = formata_numero (intTamArray)

strMensagem = "ordenar com Bubble Sort " + strTamArrayFormatado + " elementos em um array"
dttInicio = marcar_inicio (strMensagem)

def bubble_sort(arr):

    # Loop externo
    for n in range(len(arr) - 1, 0, -1):

        bolTrocou = False

        # Loop Interno
        for i in range(n):
            if arr[i] > arr[i + 1]:


                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                bolTrocou = True

        if not bolTrocou:
            break

dttFim = marcar_fim (strMensagem)

strTempoExecucaoFormatado = formata_tempo_execucao(dttInicio, dttFim)

print("Tempo de execucao foi de: " + strTempoExecucaoFormatado)

"""**Exemplo 5 - O(2n) - 2 elevado a n**"""

# Exemplo 5 - Determinar se existe um subconjunto de um conjunto dado de números que soma a um determinado valor
print ("EXEMPLO 5 - Ver se um número é a soma de dois elementos de um array - O(2n)")

def subset_soma(arrTeste, intAlvo, parcial=[]):
    s = sum(parcial)

    # Caso base: se a soma parcial é igual ao alvo, retorna True
    if s == intAlvo:
        return True

    # Se a soma parcial exceder o alvo, retorna False
    if s > intAlvo:
        return False

    # Tenta incluir cada número do conjunto em turnos
    for i, n in enumerate(arrTeste):
        arrRestante = arrTeste[i + 1:]
        if subset_soma(arrRestante, intAlvo, parcial + [n]):
            return True

    return False

# Carregar o array
intTamArray = ler_inteiro ("Digite tamanho do array: ")

arrNumeros = montar_array (intTamArray,0,10)

print (f"O array é: {arrNumeros}")

intNumeroAlvo = ler_inteiro ("Digite o número a ser procurado: ")

strMensagem = "ver se número é soma de elementos de um dado array"
dttInicio = marcar_inicio (strMensagem)


if subset_soma(arrNumeros, intNumeroAlvo):
    print("Existe um subconjunto que soma ao alvo.")
else:
    print("Não existe um subconjunto que soma ao alvo.")

dttFim = marcar_fim (strMensagem)

strTempoExecucaoFormatado = formata_tempo_execucao(dttInicio, dttFim)

print("Tempo de execucao foi de: " + strTempoExecucaoFormatado)

"""**Exemplo 6 - O(N!)**"""

def permutacoes(lista):
    # Caso base: se a lista tem um único elemento, retorna a lista com ele mesmo
    if len(lista) == 1:
        return [lista]

    # Lista para armazenar as permutações
    resultado = []

    # Itera sobre todos os elementos da lista
    for i in range(len(lista)):
        # Elemento atual
        atual = lista[i]
        # Restante da lista sem o elemento atual
        restante = lista[:i] + lista[i+1:]
        # Gera todas as permutações do restante da lista
        for p in permutacoes(restante):
            # Adiciona o elemento atual no início de cada permutação do restante
            resultado.append([atual] + p)

    return resultado

# Exemplo de uso
intTamArray = ler_inteiro ("Digite tamanho do array: ")

arrNumeros = montar_array (intTamArray,0,9)
print (f"O array é: {arrNumeros}")


strMensagem = "criando as permutações entre os números"
dttInicio = marcar_inicio (strMensagem)

todas_permutacoes = permutacoes(arrNumeros)

dttFim = marcar_fim (strMensagem)

strTempoExecucaoFormatado = formata_tempo_execucao(dttInicio, dttFim)

for p in todas_permutacoes:
    print(p)

print("Tempo de execucao foi de: " + strTempoExecucaoFormatado + "\n")