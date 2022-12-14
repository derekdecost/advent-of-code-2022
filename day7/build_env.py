import os

i       = 0
fs      = open("input.txt", 'r').readlines()
fs = [ln.replace("\n", "") for ln in fs]
home    = os.getcwd()
os.mkdir("day7_fs")

while i < len(fs):
    if fs[i].startswith("$ cd"):
        fldr = fs[i].split(" ")[-1]
        if fldr == "/":
            os.chdir(home + "/day7_fs")
        else:
            os.chdir(fldr)
        i += 1
        continue
    
    if fs[i].startswith("$ ls"):
        i += 1
        while not fs[i].startswith("$"):
            if fs[i].startswith("dir"):
                os.mkdir(fs[i].split(" ")[-1])
                i += 1
                if i >= len(fs): 
                    break
                continue
            elif (fs[i].split(" ")[0]).isdigit():
                sz, fn = fs[i].split(" ")
                open(f"{fn},{sz}", "w")
                i += 1
                if i >= len(fs): 
                    break
                continue
            else:
                break

