from math import inf

from data.Drone import Drone
from data.dataParser import Data
from data.makePacks import *
from data.scoreCalculator import *

drone_list = [Drone() for i in range (30)]
global_turn = 0
all_turns = 112993
global_score = 0

#we use here greedy algorithm, which choose the closest drone
#to the given shelter
def greedy_algorithm(packs, order):
    global drone_list
    best_result = inf
    commands = []

    while packs:
        for shelter in packs:
            for drone in drone_list:
                if drone.busy == False:
                    if (length(shelter[0], drone.location) + length(drone.location, order)) < best_result:
                        best_option = (drone, shelter)
        best_option[0].setBusy()
        commands.append(best_option)
        packs = [i for i in packs if i != best_option[1]]

    return commands


if __name__=='__main__':
    a = Data ()

    order_counter = 0
    for order in Data.orders.keys():

        packs = splitToPacks (order)
        if packs == None: continue

        while True:
            if global_turn >= all_turns: break
            free_drones = []
            for drone in drone_list:
                if drone.turns < global_turn:
                    drone.setFree ()
                if drone.busy == False:
                    free_drones.append (drone)
            if len(free_drones) < len(packs):
                global_turn += 1
            else: break
        order_counter+=1

        if global_turn >= all_turns: break

        commands = greedy_algorithm(packs, order)
        for pack in commands:
            pack[0].upload(pack[1][1], pack[1][0])
            pack[0].deliver(pack[1][1], order)
        global_score += calculateScore([i[0] for i in commands], all_turns)
        global_turn += 1
    print("the global score is ", round(global_score, 0), " points")


