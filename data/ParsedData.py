class Data:
    warehouses = dict ()
    weight = list ()
    orders = dict ()

    def __init__(self):

        self.setWarehouses()
        self.setOrders()
        self.setWeight()
    def setWarehouses(self):
        with open ('warehouse.txt') as fp:
            # number_of_warehouses =
            line = fp.readline ()
            for i in range (int (line)):
                line = fp.readline ()
                cord = tuple (map (int, line.split ()))
                line = fp.readline ()
                quantity = list (map (int, line.split ()))
                Data.warehouses[cord] = quantity

    def setWeight(self):
        with open ('weight.txt') as file:
            file_contents = file.read ()
            Data.weight = list (map (int, file_contents.split ()))

    def setOrders(self):
        with open ('orders.txt') as fp:
            line = fp.readline ()
            for i in range (int (line)):
                line = fp.readline ()
                cord = tuple (map (int, line.split ()))
                line = fp.readline ()
                line = fp.readline ()
                products = list (map (int, line.split ()))
                Data.orders[cord] = products


