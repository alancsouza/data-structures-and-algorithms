"""Solves the postman problem:

Given a list of houses that belong to the street
and the order of houses numbers that should receive a package,
Returns the time that takes to the postman to deliver all packages
following the houses numbers' order, considering that,
each house passed is 1 unit of time.
Problem: https://www.urionlinejudge.com.br/judge/pt/problems/view/2448
"""

number_of_houses_and_packages = list(map(int,input().split()))
houses_numbers = list(map(int,input().split()))
houses_numbers_to_receive_package = list(map(int,input().split()))

time_counter = 0
current_house_idx = 0

houses_indexes = dict(zip(houses_numbers,list(range(number_of_houses_and_packages[0]))))

for package in houses_numbers_to_receive_package:
    package_idx = houses_indexes[package]

    # computes the distance between the current house (index)
    # and the target house to deliver the package
    time_counter += abs(package_idx - current_house_idx)

    current_house_idx = package_idx

print(time_counter)
