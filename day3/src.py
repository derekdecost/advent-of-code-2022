def get_compartments(rucksack):
    mid_pt = int(len(rucksack) / 2)
    l, r = rucksack[0:mid_pt], rucksack[mid_pt:len(rucksack)]
    return l, r

def get_item_priority(item):
    unicode_val = ord(item)
    if item.isupper():
        return (unicode_val - 38)
    else:
        return (unicode_val - 96)

def get_group_badge(group):
    group.sort(key=len)
    for item in group[0]:
        if (group[1].find(item) != -1) and (group[2].find(item) != -1):
            return (item)
    return (0)

def main_p2():
    priority_sum = 0
    groups = []
    rucksacks = open("input.txt", 'r').readlines()

    for i in range(0, len(rucksacks), 3):
        groups.append([rucksacks[i].replace("\n", ""), rucksacks[i + 1].replace("\n", ""), rucksacks[i + 2].replace("\n", "")])

    for group in groups:
        priority_sum += get_item_priority(get_group_badge(group))

    print(priority_sum)
        
    return

if __name__ == "__main__":
    main_p2()