black = (0,0,0)
file_png =[[(255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(255, 0, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 0), (0, 255, 0)]]
buildings = []
dictmap = {}
y_number = 0

for line in file_png:
    x_number = 0
    for pixel in line:
        dictmap[y_number] = dictmap.get(y_number, {})
        dictmap[y_number][x_number] = pixel
        x_number += 1
    y_number += 1
print(dictmap)
print(dictmap[0])
def get_colored(file_png):
    # !TODO should filter from dictmap not the list of lists again...
    dict_colored = {}
    y = 0
    for line in file_png:
        x = 0
        for pixel in line:
            if pixel != black:
                dict_colored[(x,y)] = pixel
            x += 1
        y += 1
    return dict_colored
#checking dict order

def get_rectangle(x, y, color, png_array):
    """get rectangle top(xs) and left(ys) points.
        then saves the spotted rectangle in a list "buildings
        returns y_points and width" """
    source = x,y
    X = x
    Y = y
    width = 0
    height = 0
    try:
        while png_array[Y][x] == color:
            # print(f'Xs finder, analyzing "{x,Y}"')
            width += 1
            x += 1
    except KeyError:
        pass

    try:
        while png_array[y][X] == color:
            print(y,X)
            # print(f'Ys finder, analyzing "{X, y}"')
            height += 1
            y += 1
    except KeyError:
        pass

    # appending spotted rectangle as spotted building
    building = source, color, width, height  # position,color,width,height
    buildings.append(building)
    return width, height
#x_to, y_to = x_from + width, y_from + height
def is_rectangle(position,source,x_to,y_to):
    """#returns True if pixel is in the same rectangle
        as the rectangle that start at position"""
    x,y = position
    x_from, y_from = source
    if x_from <= x <= x_to and y_from <= y < y_to:
        return False
    else:
        return True
##tryin to remove 1st rectangle
#starting_point = (0,0)
#x_to = 2
#y_to = 2
#new_dict = {pixel_xy:pixel for pixel_xy,pixel in d.items() if is_rectangle(pixel_xy,starting_point,x_to,y_to) }
#print(new_dict)
d = get_colored(file_png)
while d:
    print(d)
    #need to get source,width and height
    source = next(iter(d))
    source_x, source_y = source
    width, height = get_rectangle(source_x,source_y,d[source],dictmap)
    x_to, y_to = source_x + width, source_y + height
    d = {position:color for position,color in d.items() if is_rectangle(position,source,x_to,y_to)}
#print(d)
#source = next(iter(d))
#print(source)
#source_x, source_y = source
#width, height = get_rectangle(source_x,source_y,d[source],dictmap)
#print(width,height)
#x_to, y_to = source_x + width, source_y + height
#print(x_to,y_to)
#d = {position:color for position,color in d.items() if is_rectangle(position,source,x_to,y_to)}
#print(d)
#
print(buildings)
