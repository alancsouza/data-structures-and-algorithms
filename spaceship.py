"""
Problem: https://codeforces.com/problemset/problem/1184/B1

usage:

Given a list of spaceship power, base defense power and base gold


>>> solve_spaceship([1,3,5,2,4], [0,4,2,9], [1,2,8,4])
output: [1, 9, 11, 9, 11]
"""

def solve_spaceship(
    spaceship_power: list,
    base_defense: list,
    base_gold: list
):
    base_defense_gold = list(zip(base_defense, base_gold))

    total_gold_per_ship = []

    for ship in spaceship_power:
        total_gold = sum(
            [gold for defense_power, gold in base_defense_gold if ship >= defense_power]
        )

        total_gold_per_ship.append(total_gold)

    return total_gold_per_ship
