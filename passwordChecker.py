# Write a function that takes a password as input and checks its strength based on the following criteria:
#
# At least 8 characters long
# Contains both uppercase and lowercase letters
# Includes at least one digit
#
# The function should RETURN a boolean value indicating whether the password meets the criteria.

def check_password_strength(password):
    # TODO: Implement the password strength checking logic
    pass

# Test the function
password = input("Enter a password: ")
is_strong = check_password_strength(password)
print("Is the password strong?", is_strong)
