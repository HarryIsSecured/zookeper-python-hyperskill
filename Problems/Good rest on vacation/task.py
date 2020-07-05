# put your python code here

days_of_holiday = abs(int(input()))
daily_food_cost = abs(int(input()))
one_flight_cost = abs(int(input()))
daily_hotel_cost = abs(int(input()))
total_cost = days_of_holiday * daily_food_cost + (days_of_holiday - 1) * daily_hotel_cost + one_flight_cost * 2
print(total_cost)
