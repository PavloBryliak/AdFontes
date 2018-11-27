with open('weight.txt') as file:
    file_contents = file.read()
    product_weight_list = list(map(int, file_contents.split()))
print(product_weight_list)


