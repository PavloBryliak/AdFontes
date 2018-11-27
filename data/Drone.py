from data.ParsedData import Data

class Drone:
    def __init__(self):
        self.capacity = 200
        self.state = [0,0]
        self.cargoList = []

    def upload(self, items):
        W = self.capacity
        n = len(items)
        s = Data.weight

        m = [[0 for i in range(W)] for j in range(n)]


        for i in range(1, n):
            for j in range(0, W):
                if s[items[i]] > j:
                    m[i][j] = m[i - 1][j]
                else:
                    m[i][j] = max (m[i - 1][j], m[i - 1][j - s[items[i]]] + s[items[i]])
        [print(i) for i in m]



if __name__ == "__main__":
    b = Data()
    a = Drone()
    a.upload([226,183,6,220,299,280,12,42])