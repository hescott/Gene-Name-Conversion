
#reads mapping file, each line is read, each mapping is made,
#and then sorted to create a canonical list to compare

import sys, os

def readMappings(inputFile):
    
    file = open(inputFile, 'r')
    
    mappings = []
    
    for line in file:
        line = line.rstrip('\n')
        line = line.split()
        for i in range(1,len(line)):
            pair = []
            pair.append(line[0])
            pair.append(line[i])
            pair.sort()
            mappings.append(pair)

    return mappings


def main():

    input_f1 = sys.argv[1]
    input_f2 = sys.argv[2]

    mappings1 = readMappings(input_f1)
    mappings2 = readMappings(input_f2)

    mappings1.sort()
    mappings2.sort()

    same = True

    for index in range(len(mappings1)):
        if (mappings1[index][0] != mappings2[index][0]):
            same = False
        if (mappings1[index][1] != mappings2[index][1]):
            same = False

    print same







if __name__ == "__main__":
    main()
