

def sum_to_2020(file):
    a = open(file)
    a = a.read()
    a = a.split()
    set_nums = set(a)

    for num in a:
        n_needed = 2020 - int(num)
        if str(n_needed) in set_nums:
            answer = int(num) * n_needed

    return answer

print(sum_to_2020("advent1.txt"))

def sum_3_2020(file):
    a = open(file)
    a = a.read()
    a = a.split()
    set_nums = set(a)

    for num in a:
        for n in a:
            if int(num) + int(n) < 2020:
                needed = 2020 - int(num) - int(n)
                if str(needed) in set_nums:
                    answer = int(num) * int(n) * needed
    return answer

print(sum_3_2020("advent1.txt"))
    
    