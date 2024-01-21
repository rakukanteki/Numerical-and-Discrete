# Addition function
def addition(x1, x2):
    # Converting numbers to integers
    num1 = int(x1, 2)    
    num2 = int(x2, 2)
    
    # Performing
    result = num1 + num2

    # Convert the integer result to binary 
    return bin(result)[2:]


# Subtraction function
def subtract(x1, x2):
    # Converting numbers to integers
    num1 = int(x1, 2)    
    num2 = int(x2, 2)
    
    # Performing
    result = num1 - num2

    # Convert the integer result to binary 
    return bin(result)[2:]


# Taking 2 binary numbers
x1 = input()
x2 = input()

binary_sum = addition(x1, x2)
binary_sub = subtract(x1, x2)

print(f"{x1} + {x2} = {binary_sum}")
print(f"{x1} - {x2} = {binary_sub}")