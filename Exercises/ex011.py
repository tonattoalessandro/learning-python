height_wall = float(input('What\'s the wall\'s height in meters? '))
width_wall = float(input('What\'s the wall\'s width in meters? '))

area_wall = height_wall * width_wall

print(f'The wall\'s area is {area_wall:.2f}m, and is necessary {area_wall / 2} ink liters.')
