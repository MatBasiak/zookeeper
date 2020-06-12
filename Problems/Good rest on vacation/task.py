# put your python code here
duration = int(input())
food_per_day = int(input())
one_way_fly_cost = int(input())
one_night_in_hotel = int(input())

total = duration * food_per_day + (duration - 1) * (one_night_in_hotel) + 2 * one_way_fly_cost
print(total)
