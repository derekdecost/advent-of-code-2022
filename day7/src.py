import os
home    = os.getcwd()
day7_fs = [directory[0] for directory in os.walk("day7_fs", False)]

for directory in day7_fs:
    print(directory)