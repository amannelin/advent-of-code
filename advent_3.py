def check_tobaggan_route(file, x_increment, y_increment):
    map = open(file)
    map = map.readlines()
    x = 0
    y = 0
    trees = 0

    while y < len(map):
        if map[y][x % 31] == "#":
            trees += 1
        x += x_increment
        y += y_increment
    
    return trees

print(check_tobaggan_route("advent3.txt", 3, 1) *
        check_tobaggan_route("advent3.txt", 1, 1) *
        check_tobaggan_route("advent3.txt", 5, 1) *
        check_tobaggan_route("advent3.txt", 7, 1) *
        check_tobaggan_route("advent3.txt", 1, 2))

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
        