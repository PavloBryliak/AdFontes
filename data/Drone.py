from data.ParsedData import Data
from data.Warehouses import Warehouses

class Drone:
    def __init__(self):
        self.capacity = 0
        self.state = [0,0]
        self.cargoList = []

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


if __name__ == "__main__":
    b = Data()
    a = Drone()
    a.upload([226,183,6,220,299,280,12,42])
