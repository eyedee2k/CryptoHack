def generate_padded_numbers(start, end, min_length):
    """Generates numbers from start to end, padded to a minimum length."""
    numbers = []
    max_num_digits = len(str(end))  # Get the maximum number of digits

    for i in range(start, end + 1):
        num_str = str(i)
        if len(num_str) < min_length:
            padded_num = num_str.zfill(min_length)
        else:
            padded_num = num_str.zfill(max_num_digits) # pad to maximum length if longer than minimum length.
        numbers.append(padded_num)
    return numbers

# Generate numbers from 1 to 9999999, padded to a minimum of 5 characters
number_list = generate_padded_numbers(1, 9999999, 5)

# To print the first 10 numbers for demonstration:
print(number_list[:10])

# To save to file:
with open("padded_numbers.txt", "w") as f:
    for number in number_list:
        f.write(number + "\n")

print("padded_numbers.txt has been created")

# Generator version.
def generate_padded_numbers_generator(start, end, min_length):
    max_num_digits = len(str(end))
    for i in range(start, end + 1):
        num_str = str(i)
        if len(num_str) < min_length:
            yield num_str.zfill(min_length)
        else:
            yield num_str.zfill(max_num_digits)

with open("padded_numbers_generator.txt", "w") as f:
    for number in generate_padded_numbers_generator(1,9999999,5):
        f.write(number + "\n")

print("padded_numbers_generator.txt has been created")