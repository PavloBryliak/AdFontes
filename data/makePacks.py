from collections import OrderedDict
from data.Drone import *
from data.Warehouses import *
from data.ParsedData import *
from math import sqrt


def length(a, b):
    return sqrt((a[1] - b[1]) ** 2 + (a[0] - b[0]) ** 2)

def splitToPacks(order):
    order = Data.orders[order]
    splited_order = dict()
    for shelter in Warehouses.warehouses:
        for item in order:
            if Warehouses.warehouses[shelter][item] > 0:
                if shelter not in splited_order: splited_order[shelter] = [item]
                else: splited_order[shelter].append(item)
    sorted_shelters = sorted(splited_order, key=lambda x: length(x, shelter))
    pre_packs = dict()
    pack = 0
    while order != []:
        prev_order = order
        order = [i for i in order if i not in splited_order[sorted_shelters[pack]]]
        pre_packs[sorted_shelters[pack]] = list(set(prev_order) - set(order))
        pack += 1

    final_packs = []
    for shelter in pre_packs:
        if pre_packs[shelter] == []: continue
        if sum([Data.weight[i] for i in pre_packs[shelter]]) > Drone.capacity:
            final_packs.append((shelter, pre_packs[shelter][len(pre_packs[shelter])//2:]))
            final_packs.append ((shelter, pre_packs[shelter][:len (pre_packs[shelter]) // 2]))
        else:
            final_packs.append ((shelter, pre_packs[shelter]))
    return final_packs


if __name__=='__main__':
    a = Data()

    splitToPacks((340, 371))
