import math

def Funcao_recursiva(n):

    if n == 1:
        return 2
    return 2 * Funcao_recursiva(n - 1) + n**2

n = int(input("Digite um número: "))
resultado = Funcao_recursiva(n)

print(f"F(n)) = {resultado}" )