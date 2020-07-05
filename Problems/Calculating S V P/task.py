# put your python code here
length = abs(int(input()))
width = abs(int(input()))
height = abs(int(input()))

all_edge_lengths = 4 * (length + width + height)
surface_area = 2 * (length * width + width * height + length * height)
volume_of_shape = length * width * height

print(all_edge_lengths)
print(surface_area)
print(volume_of_shape)
