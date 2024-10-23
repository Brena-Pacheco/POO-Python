def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero."
    except Exception as e:
        return f"Erro: {str(e)}"

# Testando a função dividir
print(dividir(10, 2))  # Saída: 5.0
print(dividir(10, 0))  # Saída: Erro: Divisão por zero.
print(dividir(10, "a"))  # Saída: Erro: invalid literal for int() with base 10: 'a'
