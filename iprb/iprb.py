import sys

inFile = sys.argv[1]

def iprb(my_file="test.txt"):
    open_file = open(inFile, "r")
    data = open_file.read().split()
    k,m,n = int(data[0]),int(data[1]),int(data[2])
    #print("k:{}, m:{}, n:{}".format(k,m,n))
    p = k+m+n
    out_prob= (4*k*(k-1)+3*m*(m-1)+4*(2*k*m+2*k*n+m*n))/(4*p*(p-1))
    print(out_prob)

iprb(inFile)
