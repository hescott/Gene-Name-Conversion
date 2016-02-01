
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

    mappingsFile1 = sys.argv[1]
    mappingsFile2 = sys.argv[2]
    homologFile = sys.argv[3]
    rangeS1File = sys.argv[4]
    rangeS2File = sys.argv[5]
    
    #mappings many to many from domain D1
    # to range R1 in species S1
    mappingsS1 = readMappings(mappingsFile1)
   
    
    
    #mappings many to many from domain D2
    # to range R2 in species S2
    mappingsS2 = readMappings(mappingsFile2)

    
    #most likely D1 and D2 are the same as
    #are R1 and R2
    
    #homologs is a pair of genes
    #from species S1 in D1 mapped to S2
    #of type D2
    homologs = readMappings(homologFile)
  
    
    #rangeS1 is subset of possible
    #genes in S1 in format R1 that
    #exist as possible matches (in the network)
    rangeS1 = readNodes(rangeS1File)
    
    
    #same as above
    rangeS2 = readNodes(rangeS2File)



    
    convertedList = []
    controversialList = []
    notMatchedList = []
    
    outputConvertedFile = open(sys.argv[6], 'w')
    
    for i in range(len(homologs)):
        convertedPair = []
        s1matches = findMatchesPresent(findMatches(homologs[i][0], mappingsS1), rangeS1)
        
       
        
        s2matches = findMatchesPresent(findMatches(homologs[i][1], mappingsS2), rangeS2)



        lenS1matches = len(s1matches)
        lenS2matches = len(s2matches)
        
        if (lenS1matches == 0 or lenS2matches == 0):
            notMatchedList.append(homologs[i])
        elif (lenS1matches == 1 and lenS2matches == 1):
            convertedPair.append(s1matches[0])
            convertedPair.append(s2matches[0])
            convertedList.append(convertedPair)
            outputConvertedFile.write("{}\t{}\n".format(s1matches[0], s2matches[0]) )
            
        
        else :
            convertedPair.append(s1matches)
            convertedPair.append(s2matches)
            controversialList.append(convertedPair)




#print mappings1
#    print " "
#   print " "
#    print len(mappings1)
#   print " "
#   print " "
#   print mappings2
#   print " "
#   print " "
#    print len(mappings2)

#    same = True

#   for index in range(len(mappings1)):
#        if (mappings1[index][0] != mappings2[index][0]):
#            same = False
#        if (mappings1[index][1] != mappings2[index][1]):
#            same = False

#    print same







if __name__ == "__main__":
    main()
