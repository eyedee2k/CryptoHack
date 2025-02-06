def modular_arithmetic():
    x = 11 % 6
    y = 8146798528947 % 17
    return x, y

if __name__ == "__main__":
    x, y = modular_arithmetic()
    print(f"11 ≡ {x} (mod 6)")
    print(f"8146798528947 ≡ {y} (mod 17)")