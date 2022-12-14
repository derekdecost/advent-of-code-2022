from collections import deque

def is_unique(buffer):
    for i in range(len(buffer)):
        for j in range((i + 1), len(buffer)):
            if buffer[i] == buffer[j]:
                return False
    return True

def find_sop(packet):
    processed_chars = 0
    buffer          = deque([])

    for data in packet: # Simulates receiving data one at a time.
        processed_chars += 1
        buffer.append(data)
        if len(buffer) < 4:
            continue
        if len(buffer) > 4:
            buffer.popleft()

        if is_unique(buffer):
            return processed_chars

def find_som(packet):
    processed_chars = 0
    buffer          = deque([])

    for data in packet: # Simulates receiving data one at a time.
        processed_chars += 1
        buffer.append(data)
        if len(buffer) < 14:
            continue
        if len(buffer) > 14:
            buffer.popleft()

        if is_unique(buffer):
            return processed_chars

def main_p1():
    data = open("input.txt", 'r').readline()
    print(find_sop(data))

def main_p2():
    data = open("input.txt", 'r').readline()
    print(find_som(data))

if __name__ == "__main__":
    main_p1()
    main_p2()