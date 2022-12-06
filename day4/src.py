def get_pairs(data):
    entry = data.replace("\n", "")
    l, r = entry.split(",")
    l, r = l.split("-"), r.split("-")
    l, r = list(range(int(l[0]), (int(l[1]) + 1))), list(range(int(r[0]), (int(r[1]) + 1)))
    return set(l), set(r)

def main_p1():
    cnt = 0
    pairs = []
    data = open("input.txt", 'r').readlines()
    for entry in data:
        pairs.append(get_pairs(entry))
    
    for pair in pairs:
        if pair[0] <= pair[1]:
            cnt += 1
            continue
        elif pair[1] <= pair[0]:
            cnt += 1
    print(f"Part 1 Answer: {cnt}")

def main_p2():
    cnt = 0
    pairs = []
    data = open("input.txt", 'r').readlines()
    for entry in data:
        pairs.append(get_pairs(entry))
    
    for pair in pairs:
        if not pair[0].isdisjoint(pair[1]):
            cnt += 1
            continue
    print(f"Part 2 Answer: {cnt}")
    

if __name__ == "__main__":
    main_p1()
    main_p2()