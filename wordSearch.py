import math

class SearchGrid():
    grid = ""
    ROW_LENGTH = 0
    GRID_LENGTH = 0
    TRIE_DEPTH = 3
    trieDict = {}

    def __init__(self, gridString):
        self.grid = gridString
        self.ROW_LENGTH = int(math.sqrt(len(gridString))) # Assuming grid is square i.e. (GRID_LENGTH = ROW_LENGTH*ROW_LENGTH)
        self.GRID_LENGTH = len(gridString)
        self.populateTrie()

    # Pre-processing method to generate flattened "trie" from gridString
    def populateTrie(self):
        print("Hello World")

        for i in range (0, self.GRID_LENGTH):
            horizontalString = verticalString = ""
            currentChar = self.grid[i]
            horizontalString += self.grid[i]
            verticalString += self.grid[i]
            self.addStringValue(currentChar, i)

            # Add string,index key,value pairing to trie for every substring up to length of trie depth
            for trieCount in range(1, self.TRIE_DEPTH):
                rowRemaining = (int(round(i/self.ROW_LENGTH)+1)*self.ROW_LENGTH-i-1) # Number of chars left on row in right direction
                columnPosition = int(i + (trieCount*self.ROW_LENGTH))

                # Only append to horizontal substring if in space of row
                if ((trieCount <= rowRemaining) and ((i+trieCount) < self.GRID_LENGTH) and (rowRemaining != self.ROW_LENGTH)):
                    horizontalString += self.grid[i+trieCount]
                    self.addStringValue(horizontalString, i)

                # Only append to vertical substring if in space of column
                if(columnPosition < self.GRID_LENGTH):
                    verticalString += self.grid[columnPosition]
                    self.addStringValue(verticalString, i)
                    

    def addStringValue(self, str, index):
        
        # Create new key,value pair if string is new, otherwise only add index
        # to existing index list if string length equals trie depth (as could prefix longer word)
        if (not(str in self.trieDict)):
            self.trieDict.update({str:[index]})
        else:
            if (len(str) == self.TRIE_DEPTH):
                self.trieDict[str].append(index)



class WordSearch():
    def __init__(self, grid):
        trieGrid = SearchGrid(grid)
        print(trieGrid.trieDict)

    def is_present(self, word):
        return True