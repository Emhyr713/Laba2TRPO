# prime_utils.py

def is_prime(n):
    """Оптимизированная проверка, (!(!)) является ли число простым."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0: 
        return False
    # Проверяем делители от 5 до √n, пропуская чётные числа
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True  
