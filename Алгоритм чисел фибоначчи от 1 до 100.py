def fibonacci_iterative(n):
    """
    Вычисляет n-е число Фибоначчи итеративным методом.

    Args:
        n: Номер элемента в последовательности Фибоначчи (начиная с 1).

    Returns:
        n-е число Фибоначчи.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def print_fibonacci_sequence(limit):
    """
    Выводит последовательность чисел Фибоначчи до заданного элемента.

    Args:
        limit: Максимальный номер элемента для вывода.
    """
    for i in range(1, limit + 1):
        print(f"Элемент {i}: {fibonacci_iterative(i)}")


# Вычисление и вывод последовательности от 1 до 100
print_fibonacci_sequence(100)