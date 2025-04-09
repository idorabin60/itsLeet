from typing import List


def carFleet(target: int, positions: List[int], speed: List[int]) -> int:
    position_and_speed = list(zip(positions, speed))
    position_and_speed = sorted(position_and_speed)
    position_and_speed = list(reversed(position_and_speed))
    print(position_and_speed)
    result = []
    pair_to_compare_to = position_and_speed[0]
    result.append(pair_to_compare_to)
    for pair in position_and_speed[1:]:
        if if_two_pairs_will_not_become_a_fleet(target, pair_to_compare_to, pair):
            result.append(pair)
            pair_to_compare_to = pair

    return len(result)


def if_two_pairs_will_not_become_a_fleet(target, pair1, pair2):
    time_to_get_to_target_for_car1 = (target-pair1[0])/pair1[1]
    time_to_get_to_target_for_car2 = (target-pair2[0])/pair2[1]
    print(time_to_get_to_target_for_car1)
    print(time_to_get_to_target_for_car2)
    return time_to_get_to_target_for_car1 < time_to_get_to_target_for_car2


target = 10
position = [4, 1, 0, 7]
speed = [2, 2, 1, 1]

print(carFleet(target, positions=position, speed=speed))
