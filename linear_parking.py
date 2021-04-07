def linear_parking(
    number_of_cars,
    parking_capacity,
    arrival_times,
    departure_times
):
    """
    Problem: https://www.urionlinejudge.com.br/judge/pt/problems/view/1523
    """
    if number_of_cars == 0 and parking_capacity == 0:
        return "Não"

    parking = []

    for i in range(number_of_cars):
        if not parking or departure_times[i] < parking[-1]:
            if len(parking) == parking_capacity:
                return "Não"
            else:
                parking.append(departure_times[i])

        else:
            while parking and parking[-1] <= arrival_times[i]:
                parking.pop()

            if parking and departure_times[i] >= parking[-1]:
                return "Não"
            else:
                parking.append(departure_times[i])

    return "Sim"
