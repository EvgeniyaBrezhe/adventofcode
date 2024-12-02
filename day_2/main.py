with open('input.csv', 'r') as file:
    lines = file.readlines()

all_lists = [list(map(int, line.split())) for line in lines if line.strip()]

print(all_lists)


def is_increasing(my_list):
    return all(i < j and j - i <= 3 for i, j in zip(my_list, my_list[1:]))

def is_decreasing(my_list):
    return all(i > j and i - j <= 3 for i, j in zip(my_list, my_list[1:]))

def check_possibilities_increase(my_list):
    for index in range(len(my_list)):
        new_list = my_list[:index] + my_list[index+1:]
        if is_increasing(new_list):
            return True
    return False


def check_possibilities_decrease(my_list):
    for index in range(len(my_list)):
        new_list = my_list[:index] + my_list[index+1:]
        if is_decreasing(new_list):
            return True
    return False


safe = 0

for i in all_lists:
    print(f"Checking list: {i}")
    if is_increasing(i) or is_decreasing(i):
        print("List is SAFE")
        safe += 1
    else:
        print("List is not SAFE")
        if check_possibilities_increase(i):
            print("List is SAFE after modifying for increasing")
            safe += 1
        elif check_possibilities_decrease(i):
            print("List is SAFE after modifying for decreasing")
            safe += 1
        else:
            print("List is not SAFE :( ")

print(f"Final safe score: {safe}")
