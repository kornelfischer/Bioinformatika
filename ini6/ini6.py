import sys

inFile = sys.argv[1]

def word_count(my_file="test.txt"):
    #print(inFile)
    counts = dict()
    open_file = open(inFile, "r")
    data = open_file.read()
    data_into_list = data.replace('\n', ' ').split(" ")
    #print(data_into_list)
    for word in data_into_list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    open_file.close()
    for key, value in counts.items():
        print(key,"",value)
        #print(value)

word_count((input))

#pelda futtatas: python dictionary.py rosalind_6.txt