import math

def resultados_num():
    try:
        num = int(input("Ingrese un número: "))

        raiz_cuadrada = math.sqrt(num)
        valor_absoluto = abs(num)
        valor_e = math.pow(math.e, num)

        # Resultados
        print("\nResultados")
        print(f"Número: {num}")
        print(f"Raíz cuadrada: {raiz_cuadrada:.2f}")
        print(f"Valor absoluto: {valor_absoluto}")
        print(f"e elevado a {num}: {valor_e:.2f}")

    except ValueError:
        print("Error: Debes ingresar un número entero válido.")

def main():
    resultados_num()

main()
