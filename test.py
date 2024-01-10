def sign(num):
    if(num>0):
        print("Positive")

print(r'Cup\'s Question')

def add_numbers(a, b):
    # Iterate until there is no carry
    while b != 0:
        # XOR to get the sum of bits without considering the carry
        sum_bits = a ^ b
        print(a,b)
        # AND to get the carry bits
        carry = (a & b) << 1
        
        # Update a with the sum of bits
        a = sum_bits
        # Update b with the carry bits for the next iteration
        b = carry

    return a

# Example usage
num1 = 5
num2 = 7
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")
