# put your python code here
time_one = abs(int(input()))
time_two = abs(int(input()))
time_three = abs(int(input()))

time_four = abs(int(input()))
time_five = abs(int(input()))
time_six = abs(int(input()))

HOUR = 3600  # 3600 seconds in an hour
MINUTE = 60  # 60 seconds in a minute

input_one = time_one * HOUR + time_two * MINUTE + time_three
input_two = time_four * HOUR + time_five * MINUTE + time_six

print(abs(input_one - input_two))
