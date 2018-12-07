from data.ParsedData import Data
from data.Warehouses import Warehouses
from math import sqrt

class Drone:
    def __init__(self):
        self.capacity = 0
        self.A = [0,0]
        self.cargoList = []
        self.turns = 0

    def upload(self, items, warehouse):
        W = self.capacity
        n = len(items)
        s = Data.weight


        m = [[0 for i in range(W)] for j in range(n)]
        for i in range(1, n):
            for j in range(0, W):
                if s[items[i]-1] > j:
                    m[i][j] = m[i - 1][j]
                else:
                    m[i][j] = max (m[i - 1][j], m[i - 1][j - s[items[i]-1]] + s[items[i]-1])
        # [print(i) for i in m]

        results = []
        final = m[n-1][W-1]
        res = m[n-1][W-1]
        w = W-1
        for i in range (n - 1, 0, -1):
            if res <= 0:
                break
            if res == m[i - 1][w]:
                continue
            else:
                results.append (items[i])
                res = res - items[i]
                w = w - items[i]
        self.cargoList = results
        self.capacity = final
        for i in results:
            Warehouses.warehouses[warehouse][i] -= 1
        print(results)
        return results


    def deliver(self,items, order_coordinates):
        while items:
            items_on_drone = self.upload(items, 0)
            for i in items_on_drone:
                items.delete(i)
                self.turns += 1
            self.turns += abs(self.path_lenght(order_coordinates)*2)
            #self.A = order_coordinates


    def path_lenght(self, B):
        return sqrt((self.A[0] - B[0])**2 + (self.A[1] - B[1])**2)



if __name__ == "__main__":
    b = Data()
    a = Drone()
    a.upload([226,183,6,220,299,280,12,42])
