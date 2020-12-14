def check_tobaggan_route(file):
    map = open(file)
    x = 0
    trees = 0

    for line in map:
        line.rstrip()
        if line[x % 31] == "#":
            trees += 1
        x += 3
    
    return trees

print(check_tobaggan_route("advent3.txt"))

def check_more_routes(file):
    map = open(file)
    x = 0
    trees= 0
    y = [1, 3, 5, 7]
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
    for line in map:
        line.rstrip()
        if line [x % 31]
        