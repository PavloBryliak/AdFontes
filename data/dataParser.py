from cmath import sqrt


class Data:
    warehouses = dict ()
    weight = list ()
    orders = dict ()

    def __init__(self):

        self.setWarehouses()
        self.setOrders()
        self.setWeight()
    def setWarehouses(self):
        with open ('dataToParse/motherOfAll_1.txt') as fp:
            # number_of_warehouses =
            line = fp.readline ()
            for i in range (int (line)):
                line = fp.readline ()
                cord = tuple (map (int, line.split ()))
                line = fp.readline ()
                quantity = list (map (int, line.split ()))
                Data.warehouses[cord] = quantity

    def setWeight(self):
        with open ('dataToParse/weight.txt') as file:
            file_contents = file.read ()
            Data.weight = list (map (int, file_contents.split ()))

    def setOrders(self):
        with open ('dataToParse/orders.txt') as fp:
            line = fp.readline ()
            for i in range (int (line)):
                line = fp.readline ()
                cord = tuple (map (int, line.split ()))
                line = fp.readline ()
                line = fp.readline ()
                products = list (map (int, line.split ()))
                Data.orders[cord] = products

def path_lenght(self, B):
    return sqrt((self.A[0] - B[0])**2 + (self.A[1] - B[1])**2)
