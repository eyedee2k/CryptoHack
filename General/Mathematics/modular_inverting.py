def modular_inverse(a, p):
    """
    Calculate the modular inverse of a under modulo p using the Extended Euclidean Algorithm.

    :param a: Number to find the inverse of
    :param p: Modulus
    :return: Modular inverse of a under modulo p
    """
    t, new_t = 0, 1
    r, new_r = p, a

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        raise ValueError(f"{a} has no modular inverse under modulo {p}")
    if t < 0:
        t = t + p

    return t

# Example usage:
# a = 3, p = 11
# print(modular_inverse(3, 11))  # Output: 4

print(modular_inverse(3, 13))