
#reads mapping file, each line is read, each mapping is made,
#and then sorted to create a canonical list to compare

import sys, os

def readMappings(inputFile):
    
    file = open(inputFile, 'r')
    
    mappings = []
    
    for line in file:
        line = line.rstrip('\n')
        line = line.split()
        mappings.append(line)
    
    return mappings

def readNodes(inputFile):
    
    file = open(inputFile, 'r')
    
    mappings = []
    
    for line in file:
        line = line.rstrip('\n')
        mappings.append(line)
    
    return mappings

#For now this is command line, will be a function?


def findMatches(gene, mapList):
    matches = []
    for i in range(len(mapList)):
        if (mapList[i][0] == gene):
            matches = mapList[i]
            del matches[0]
    return matches

#intersection could be sets
def findMatchesPresent(list1, list2):
    matchesPresent = []
    for i in range(len(list1)):
     
        if (list1[i] in list2):
            matchesPresent.append(list1[i])

    return matchesPresent




def main():

    mappingsFile = sys.argv[1]
    list2convertFile = sys.argv[2]
    rangeFile = sys.argv[3]
    outputFile = sys.argv[4]
    
    #mappings many to many from domain D1
    # to range R1 in species S1
    mappings = readMappings(mappingsFile)
   
    list2Convert = readNodes(list2convertFile)
  
    
    #rangeS1 is subset of possible
    #genes in S1 in format R1 that
    #exist as possible matches (in the network)
    range = readNodes(rangeFile)
    

    
    convertedList = []
    controversialList = []
    notMatchedList = []
    
    outputConvertedFile = open(outputFile, 'w')
    
    for i in range(len(list2Convert)):
        
        matches = findMatchesPresent(findMatches(list2Convert[i], mappings), range)

        lenMatches = len(matches)
       
        if (lenMatches == 0):
            notMatchedList.append(list2Convert[i])
        elif (lenS1matches == 1):
            convertedPair.append(matches[0])
            outputConvertedFile.write("{}\n".format(matches[0]))
        else:
            controversialList.append(matches)




if __name__ == "__main__":
    main()
