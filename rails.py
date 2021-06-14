"""
problem: https://www.urionlinejudge.com.br/repository/UOJ_1062.html

Test cases:

>>> solve_rails(5, [5, 4, 3, 2, 1])
output: "Yes"

>>> solve_rails(5, [1, 2, 3, 4, 5])
output: "Yes"

>>> solve_rails(5, [5, 4, 1, 2, 3])
output: "No"
"""


def solve_rails(size: int, output: list) -> None:
    A = list(range(1,size+1))
    B = []
    station = []

    current_expected_index = 0

    for value in A:
        expected_value = output[current_expected_index]

        if value == expected_value:
            B.append(value)
            print(f"Adding input value {value} to B: {B}")

            current_expected_index += 1
        elif station and station[-1] == expected_value:
            station_value = station.pop()
            B.append(station_value)
            print(f"Adding station value {station_value} to B: {B}")
            station.append(value)
            print(f"Adding input value {value} to station: {station}")

            current_expected_index += 1
        else:
            station.append(value)
            print(f"Adding input value {value} to station: {station}")

    # need to reverse station before merge with B
    station.reverse()
    B.extend(station)

    if B == output:
        print("Yes")
    else:
        print("No")
