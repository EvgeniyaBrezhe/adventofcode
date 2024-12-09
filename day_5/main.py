list_of_rules = []
with open("rules.txt", "r") as file:
    for line in file:
        list_of_rules.append(list(map(int, line.strip().split('|'))))

set_of_rules = set()
for rule in list_of_rules:
    set_of_rules.update(rule)

list_of_updates = []
with open("updates.txt", "r") as file:
    for line in file:
        list_of_updates.append(list(map(int, line.strip().split(','))))


def check_list(my_graph, sequence):
    for a in my_graph:
        if a in sequence:
            for b in graph[a]:
                if b in sequence:
                    if sequence.index(a) < sequence.index(b):
                        return False
    return True


def fix_incorrect_list(my_graph, sequence):
    print(sequence)
    ordered = []
    added = set()
    newly_created = []
    for num in sequence:
        for dependency in my_graph[num]:
            print(f"dependency: {dependency}")
            for i in my_graph[dependency]:
                print(f"i: {i}")
                if i not in added:
                    ordered.append(dependency)
                    added.add(dependency)
            if dependency not in added:
                ordered.append(dependency)
                added.add(dependency)
        if num not in added:
            ordered.append(num)
            added.add(num)

    for i in ordered:
        if i in sequence and i not in newly_created:
            newly_created.append(i)
            print(newly_created)
    print(f"newly_created: {newly_created}")

    return newly_created


graph = {}
for rule in list_of_rules:
    if rule[1] not in graph:
        graph[rule[1]] = set()
    graph[rule[1]].add(rule[0])

positions = {num: idx for idx, num in enumerate(list_of_updates[0])}

my_sum = 0
for list in list_of_updates:
    answer = check_list(graph, list)
    if answer:
        middle_element_index = len(list) // 2
        middle_element = list[middle_element_index]
        my_sum += middle_element

print(f"Result #1: {my_sum}")
