import re

with open('input.txt', 'r') as file:
    content = file.read()


def mul(int1, int2):
    return int1 * int2


list_of_muls = re.findall("mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)", content)

counter = 0
for i in list_of_muls:
    func = "".join(re.findall("[a-z]", i))
    list_of_int = re.findall("[1-9][0-9]{0,2}", i)
    result = locals()[func](int(list_of_int[0]), int(list_of_int[1]))
    counter += result

print(f"Result #1: {counter}")

counter = 0

does_and_donts = re.findall("do[n't()]*|mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)", content)

flag = True
for i in does_and_donts:
    func = "".join(re.findall("[a-z']", i))
    if flag:
        if func == "mul":
            list_of_int = re.findall("[1-9][0-9]{0,2}", i)
            result = locals()[func](int(list_of_int[0]), int(list_of_int[1]))
            counter += result
    if func == "don't":
        flag = False
    if func == "do":
        flag = True

print(f"Result #2: {counter}")
