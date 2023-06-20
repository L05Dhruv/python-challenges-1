# Write a function that checks whether a given number num is a prime number.
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
#
# RETURNS a boolean

def is_prime_number(num):
    # TODO: Check if num is a prime number
    pass

# Test the function
num = int(input("Enter a number: "))
is_prime = is_prime_number(num)
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
