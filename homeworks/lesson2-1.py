# -*- condig: windows-1251 -*-

with open('lesson2-1.txt', 'r') as f:
    for index, line in enumerate(f):
        line = line.strip()
        # print(index+1)
        print(line)