def fatorial(n):

    if n <= 0:
        return 1
    else:
        return n * fatorial(n-1)

numero = ler_inteiro("Calcular o fatorial do número: ")
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")