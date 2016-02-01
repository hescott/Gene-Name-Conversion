

import sys, os

def readNodes(inputFile):
    
    file = open(inputFile, 'r')
    
    mappings = []
    
    for line in file:
        line = line.rstrip('\r\n')
        mappings.append(line)
    
    return mappings



def main():

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]


   
    list2Convert = readNodes(inputFile)
 
    listWithoutDupes = list(set(list2Convert))
   
    outputFile = open(outputFile, 'w')
    
    for i in range(len(listWithoutDupes)):
        outputFile.write("{}\n".format(listWithoutDupes[i]) )




if __name__ == "__main__":
    main()
