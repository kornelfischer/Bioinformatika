import sys

inFile = sys.argv[1]
with open(inFile,"r") as file:
    U,A,B = file.readlines()
    U = set([i for i in range(1,int(U.strip())+1)])
    A = set(map(int, A.strip().rstrip('}').lstrip('{').replace(' ', '').split(',')))
    B = set(map(int, B.strip().rstrip('}').lstrip('{').replace(' ', '').split(',')))

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(U.difference(A))
print(U.difference(B))    