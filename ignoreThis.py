from random import choice, randint
import math
from string import ascii_lowercase

#def generateWords(noOfWords, grid):
#    wordsList = []
#    row_length = int(math.sqrt(len(grid)))

#    # Generate half horizontal, half vertical words
#    for i in range (0, math.floor(noOfWords/2)):
#        randomIndex = randint(0, len(grid))
#        rowRemaining = int(round(randomIndex/row_length)+1)*row_length-randomIndex-1
#        randomWordLength = randint(0, rowRemaining)

#        # Never test an empty word for occurence in search grid
#        while(randomWordLength == 0):
#            randomIndex = randint(0, len(grid))
#            rowRemaining = int(round(randomIndex/row_length)+1)*row_length-randomIndex-1
#            randomWordLength = randint(0, rowRemaining)

#        newWord = ""
#        print("rowRemaining=",rowRemaining)
#        for j in range (randomIndex, (randomIndex+rowRemaining+1-randint(0, rowRemaining))):
#            print(j)
#            newWord += grid[j]

#        print("hey")
#        print(newWord)
#        wordsList.append(newWord)
           


#    return wordsList                        

# Generates horizontal word from substring of grid
# Grid must be at least 26x26
def generateHorizontalWord(grid):
    row_length = int(math.sqrt(len(grid)))
    randomWordLength = randint(1, 4) # change to 26
    randomRow = randint(0, row_length-1)
    randomColumn = randint(0, row_length-randomWordLength)
    wordIndex = (randomRow * row_length) + randomColumn
    return grid[wordIndex:wordIndex+randomWordLength]

def generateVerticalWord(grid):
    row_length = int(math.sqrt(len(grid)))
    verticalWord = ""
    randomWordLength = randint(1, 4) # change to 26
    randomColumn = randint(0, row_length-1)
    randomRow = randint(0, row_length-randomWordLength)
    wordIndex = (randomRow * row_length) + randomColumn
    for i in range(0, randomWordLength):
        verticalWord += grid[wordIndex + (i*row_length)]
    return verticalWord


print(generateVerticalWord("abcdaeaghijalaaa"))