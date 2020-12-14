# 4-5 l: rllllj
# 4-10 s: ssskssphrlpscsxrfsr
# 14-18 p: ppppppppppppppppppp
# 1-6 z: zzlzvmqbzzclrz

def check_passwords(file):    
    a = open(file)
    a = a.readlines()
    correct = 0

    for line in a:
        line = line.split()
        nums = line[0].split("-")
        letter = line[1].split(":")
        letter = letter[0]
        password = line[2]
         
        
        count = 0
        for c in password:
            if c == letter:
                count += 1
                  
        if int(nums[0]) <= count <= int(nums[1]):
            correct += 1
            
    
    return correct

# print(check_passwords("advent2.txt"))

def check_passwords_2(file):
    a = open(file)
    a = a.readlines()
    correct = 0

    for line in a:
        line = line.split()
        nums = line[0].split("-")
        num1 = int(nums[0]) - 1
        num2 = int(nums[1]) - 1
        letter = line[1].split(":")
        letter = letter[0]
        password = line[2]

        if letter == password[num1] and letter != password[num2]:
            correct += 1
        if letter != password[num1] and letter == password[num2]:
            correct += 1

    return correct

print(check_passwords_2("advent2.txt"))



