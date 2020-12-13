from collections import Counter
from copy import deepcopy
from pprint import pprint
import math


def get_instructions(filename):
    with open(filename) as data:
        earliest_timestamp = int(data.readline().strip())
        bus_ids = data.readline().strip().split(",")
        return earliest_timestamp, bus_ids


def first_part(instructions):
    earliest_timestamp, bus_ids = instructions
    number_of_minute = 0
    correct_bus = None
    all_timetable = []
    for bus in bus_ids:
        if bus == "x":
            continue
        bus = int(bus)
        if earliest_timestamp % bus == 0:
            correct_bus = bus
            break
        after = math.ceil(earliest_timestamp / bus) * bus
        all_timetable.append((after, bus))

    mini = min([i[0] for i in all_timetable])
    number_of_minute = mini - earliest_timestamp
    for i in all_timetable:
        if i[0] == mini:
            correct_bus = i[1]
    print(number_of_minute * correct_bus)


def second_part(instructions):
    earliest_timestamp, bus_ids = instructions
    all_bus_cycles = {
        int(bus): -i % int(bus) for i, bus in enumerate(bus_ids) if bus != "x"
    }
    # un bus a une vitesse (son numéro) et une vitesse de cycle son numéro -i (le temps de départ)... mais comme on veux un cycle c'est un modulo : -i%int(bus)
    sorted_bus_by_relative_speed = list(reversed(sorted(all_bus_cycles)))
    print(sorted_bus_by_relative_speed)
    bus_synchro_cycle = all_bus_cycles[
        sorted_bus_by_relative_speed[0]
    ]  # optim on choisi le bus au cycle le plus rapide
    lcm = math.lcm(sorted_bus_by_relative_speed[0])
    for bus_index, bus_cycle in enumerate(sorted_bus_by_relative_speed[1:]):
        while (
            bus_synchro_cycle % bus_cycle != all_bus_cycles[bus_cycle]
        ):  # on s'attend a ce que le temps de sychro / cycle du bus/superbus courrant soit égale au temps de syncro du bus vis à vis de l'ensemble des bus
            bus_synchro_cycle += lcm  # on bouge a la vitesse la plus "rapide" de l'ensemble des bus (superbus) déjà traité , hormis celui à sychroniser
        # at the end of this loop n bus are in sync at bus_synchro_cycle according to their cycle
        # for loop 1 :
        # bus_synchro_cycle % bus_1_relative_speed == bus_1_cycle
        # bus_synchro_cycle % bus_2_relavive_speed == bus_2_cycle
        # so each bus is at the start point at bus_synchro_cycle
        # let's move faster using the lcm! PPCM en francais didious!
        lcm = math.lcm(
            lcm, bus_cycle
        )  # on recalcul la vitesse la plus "rapide" de l'ensemble des bus avec le bus courrant pour le suivant

    print(bus_synchro_cycle)


if __name__ == "__main__":
    instructions = get_instructions("input")
    # instructions = get_instructions("input")
    first_part(instructions)
    second_part(instructions)

    # t -= -72 % 557 = 485
    # t % 557 = -72 % 557
    # t -= -41 %379 = 338
    # t % 379 = -41%379
    # t % lcm(379,557) = t%379 = -41%379

    # (X(-72%557)*(379))%379 = -41 % 379
    # pprint(instructions)
