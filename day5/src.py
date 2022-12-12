from dataclasses import dataclass

@dataclass
class Instruction:
    qty: int
    src: int
    dst: int

def parse_moves():
    instructions = []
    data = open("input.txt", 'r').readlines()
    for line in data:
        move = line.split(" ")
        instructions.append(Instruction(int(move[1]), int(move[3]) - 1, int(move[5]) - 1))
    return instructions

def main_p1():
    stacks = [
        ["N", "S", "D", "C", "V", "Q", "T"],
        ["M", "F", "V"],
        ["F", "Q", "W", "D", "P", "N", "H", "M"],
        ["D", "Q", "R", "T", "F"],
        ["R", "F", "M", "N", "Q", "H", "V", "B"],
        ["C", "F", "G", "N", "P", "W", "Q"],
        ["W", "F", "R", "L", "C", "T"],
        ["T", "Z", "N", "S"],
        ["M", "S", "D", "J", "R", "Q", "H", "N"]
    ]

    instructions = parse_moves()
    for instruction in instructions:
        for i in range(instruction.qty):
            crate = stacks[instruction.src].pop()
            stacks[instruction.dst].append(crate)

    print("Results Part 1:")
    for stack in stacks:
        print(stack[-1], end=" ")
    print()

def main_p2():
    stacks = [
        ["N", "S", "D", "C", "V", "Q", "T"],
        ["M", "F", "V"],
        ["F", "Q", "W", "D", "P", "N", "H", "M"],
        ["D", "Q", "R", "T", "F"],
        ["R", "F", "M", "N", "Q", "H", "V", "B"],
        ["C", "F", "G", "N", "P", "W", "Q"],
        ["W", "F", "R", "L", "C", "T"],
        ["T", "Z", "N", "S"],
        ["M", "S", "D", "J", "R", "Q", "H", "N"]
    ]

    instructions = parse_moves()
    for instruction in instructions:
        crates = stacks[instruction.src][-instruction.qty::]
        stacks[instruction.src][-instruction.qty::] = []
        for crate in crates:
            stacks[instruction.dst].append(crate)

    print("Results Part 2:")
    for stack in stacks:
        print(stack[-1], end=" ")
    print()

if __name__ == "__main__":
    main_p1()
    main_p2()
