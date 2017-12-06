import sys
a = []
for line in sys.stdin:
    line = line.split()
    for i in line:
        if i.isdigit():
            a.append(i)
            