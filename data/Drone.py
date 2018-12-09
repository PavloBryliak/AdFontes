from math import sqrt

from data.dataParser import Data
from data.Warehouses import Warehouses

def length(a, b):
    return sqrt((a[1] - b[1]) ** 2 + (a[0] - b[0]) ** 2)

class Drone:
    capacity = 200
    id = 0
    def __init__(self):
        self.location = [0,0]
        self.busy = False
        self.cargoList = []
        self.turns = 0
        self.score = 0
        self.id = Drone.id
        Drone.id += 1


    def upload(self,items, ware_coordinates):
        # self.setBusy()
        print("drone ",self.id," travels  to ", ware_coordinates, " and uploads item/s", items)
        for i in items:
            self.score += 1
        self.score += length(self.location, ware_coordinates)
        self.location = ware_coordinates
        self.turns += self.score

    def deliver(self, items, order_coordinates):
        print("drone ",self.id," travels  to order", order_coordinates, " and delivers item/s", items)
        for i in items:
            self.score += 1
        self.score += length (self.location, order_coordinates)
        self.location = order_coordinates
        self.turns += self.score



    def setBusy(self):
        self.busy = True
    def setFree(self):
        self.busy = False






