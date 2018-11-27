storage_dict = dict()
with open('warehouse.txt') as fp:
    # number_of_warehouses =
    line = fp.readline()
    for i in range(int(line)):
        line = fp.readline()
        cord = tuple(map(int, line.split()))
        line = fp.readline()
        quantity = list(map(int, line.split()))
        storage_dict[cord] = quantity
print(storage_dict)




    #warehouse = list(map(int, file_contents.split()))


#print(warehouse)