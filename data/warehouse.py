with open('warehouse.txt') as fp:
    number_of_warehouses =
    line = fp.readline()
    cnt = 1
    while line:
        print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1


    #warehouse = list(map(int, file_contents.split()))


#print(warehouse)