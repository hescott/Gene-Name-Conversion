

import sys, os

def readMappings(inputFile):
    
    file = open(inputFile, 'r')
    
    mappings = []
    
    for line in file:
        line = line.rstrip('\n')
        line = line.split()
        for i in range(1, len(line)):
            pair = []
            pair.append(line[i])
            pair.append(line[0])
            mappings.append(pair)

    mappings.sort(key = lambda col: col[0])
    

    previous = ""
    reversedMap = []

    currentMatches = []

    for i in range(len(mappings)):
        if(previous == mappings[i][0]):
            currentMatches.append(mappings[i][1])
        elif(previous == ""):
            previous = mappings[i][0]
            currentMatches.append(mappings[i][0])
            currentMatches.append(mappings[i][1])

        else:
            reversedMap.append(currentMatches)
            currentMatches = []
            previous = mappings[i][0]
            currentMatches.append(mappings[i][0])
            currentMatches.append(mappings[i][1])



    return reversedMap

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
                #print matches
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
    rangeX = readNodes(rangeFile)
    

    
    convertedList = []
    controversialList = []
    notMatchedList = []
    

    outputConvertedFile = open(outputFile, 'w')
    
    
    for i in range(len(list2Convert)):
  
        matches = findMatchesPresent(findMatches(list2Convert[i],  mappings), rangeX)

        lenMatches = len(matches)
       
        if (lenMatches == 0):
            notMatchedList.append(list2Convert[i])
        elif (lenMatches == 1):
            convertedList.append(matches[0])
            outputConvertedFile.write("{}\n".format(matches[0]))
        else:
            controversialList.append(matches)




if __name__ == "__main__":
    main()
