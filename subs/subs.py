#id: subs
import sys

inFile = sys.argv[1]

def subs(my_file="test.txt"):
    open_file = open(inFile, "r")
    data = open_file.read()
    data=data.split("\n")
    s = data[0]
    S=len(s)
    t = data[1]
    T = len(t)
    starting_points=[]
    for i in range(S-T):
        if s[i:i+T] == t:
            starting_points.append(i+1)
    print(*starting_points)

subs(inFile)
