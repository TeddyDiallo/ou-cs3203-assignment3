# This function returns the sum of a list 
def sum_list(data):
    sum = 0
    for i in range(len(data)):
        sum += data[i]


# This function returns the product of elements of a list 

def product_list(data):
    product = 0
    for i in range(len(data)):
        product *= data[i]
    return product 