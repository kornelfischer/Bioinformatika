#id: fib
import sys

inFile = sys.argv[1]

def fib(my_file="test.txt"):
    open_file = open(inFile, "r")
    data = open_file.read()
    data=data.split(" ")
    n = int(data[0])
    k = int(data[1])
    fib_list=[0,1]
    for i in range(2,n+1):
        fib_list.append(fib_list[-1]+k*fib_list[-2])

    print(fib_list[n])

fib((input))