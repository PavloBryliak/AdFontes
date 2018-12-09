from data.main import *
def calculateScore(drones, all_turns):
    score = 0
    for drone in drones:
        score += (all_turns-drone.score)*100/all_turns
        drone.score = 0
    return score