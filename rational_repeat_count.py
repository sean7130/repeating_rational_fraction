def repeating_decimal_length(d, n):
    # Simplify the fraction
    from math import gcd
    g = gcd(d, n)
    n //= g

    # Simplify n by removing factors of 2 and 5
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5

    # If n becomes 1, the decimal is terminating
    if n == 1:
        return 0

    # Find the multiplicative order of 10 modulo n
    length = 1
    remainder = 10 % n

    while remainder != 1:
        remainder = (remainder * 10) % n
        length += 1

    return length

# Example usage
d = int(input("Enter the numerator: "))
n = int(input("Enter the denominator: "))
result = repeating_decimal_length(d, n)
print(f"The length of the repeating decimal is: {result}")

