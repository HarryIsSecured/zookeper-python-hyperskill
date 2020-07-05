# put your python code here

number_of_halls = abs(int(input()))
capacity = abs(int(input()))
number_of_viewers = abs(int(input()))

if number_of_halls * capacity >= number_of_viewers:
	print("True")
else:
	print("False")
