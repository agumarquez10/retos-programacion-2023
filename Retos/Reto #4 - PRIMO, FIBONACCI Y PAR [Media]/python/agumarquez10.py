import math

def check_prime_fibo_even(number):

    result = f"{number} "

    # Primo
    if number > 1:
        for index in range(2, number):
            if number % index == 0:
                result += "no es primo, "
                break
        else:
            result += "es primo, "

    else:
        result += "no es primo, "

    # Fibonacci
    if is_perfect_square(5 * number * number + 4) or is_perfect_square(5 * number * number -4):
        result += "es fibonacci "
    else:
        result += "no es fibonacci "

    # Par
    if number % 2 == 0:
        result += "y es par"
    else:
        result += "y es impar"

    print(result)

def is_perfect_square(number):
    sqrt = int(math.sqrt(number))
    return sqrt * sqrt == number

check_prime_fibo_even(6)