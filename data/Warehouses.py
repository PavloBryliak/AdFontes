from data.dataParser import Data

class Warehouses:
    warehouses = Data.warehouses
    items = Data.weight
    def storagesWithItem(self, item):
        storages = []
        for i in self.warehouses:
            if self.warehouses[i][item]>0:
                storages.append(i)
        return storages
