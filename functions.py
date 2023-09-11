# This function returns the sum of a list 
def sum_list(data):
    sum = 0
    for i in data:
        sum += i
    return sum


# This function returns the product of elements of a list 
def product_list(data):
    product = 1
    for i in data:
        product *= i
    return product 

# This function reverses a list 
def reverse_list(data):
    reversed_list = []
    for i in range(1,len(data)+1):
        reversed_list.append(data[-i])
    return reversed_list