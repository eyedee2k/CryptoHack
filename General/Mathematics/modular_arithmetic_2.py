def modular_exponentiation(n, e, p):
    """
    Calculate (n^e) % p using modular exponentiation.

    :param n: Base number
    :param e: Exponent
    :param p: Modulus
    :return: Result of (n^e) % p
    """
    result = 1
    n = n % p  # Update n if it is more than or equal to p

    while e > 0:
        # If e is odd, multiply n with the result
        if (e % 2) == 1:
            result = (result * n) % p

        # e must be even now
        e = e >> 1  # e = e // 2
        n = (n * n) % p  # Change n to n^2

    return result

# Example usage:
# n = 2, e = 5, p = 13
# print(modular_exponentiation(2, 5, 13))  # Output: 6

print(modular_exponentiation(3, 17, 17)) # Output: 3
print(modular_exponentiation(5, 17, 17)) # Output: 5
print(modular_exponentiation(7, 16, 17)) # Output: 1
print(modular_exponentiation(273246787654, 65536, 65537)) # Output: 1