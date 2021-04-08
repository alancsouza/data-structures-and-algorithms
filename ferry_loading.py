def ferry_loading(
    ferry_length,
    left_queue,
    right_queue
):
    """
    Problem: https://open.kattis.com/problems/ferryloading4
    """
    # converting from meters to centimeters
    ferry_length = ferry_length * 100

    number_of_trips = 0

    ferry_is_on_left_side = True

    while left_queue or right_queue:
        should_add_cars_to_ferry = True

        queue = left_queue if ferry_is_on_left_side else right_queue

        sum_of_cars_sizes = 0

        while should_add_cars_to_ferry:
            if not queue:
                should_add_cars_to_ferry = False
            else:
                current_car_size = queue[0]

                sum_of_cars_sizes += current_car_size

                if sum_of_cars_sizes <= ferry_length:
                    should_add_cars_to_ferry = True
                    left_queue.pop(0) if ferry_is_on_left_side else right_queue.pop(0)
                else:
                    should_add_cars_to_ferry = False

        ferry_is_on_left_side = not ferry_is_on_left_side

        number_of_trips += 1

    return number_of_trips
