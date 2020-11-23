import math

class SearchGrid():
    grid = ""
    ROW_LENGTH = 0
    GRID_LENGTH = 0
    TRIE_DEPTH = 2
    trieDict = {}

    def __init__(self, gridString):
        self.grid = gridString
        self.ROW_LENGTH = int(math.sqrt(len(gridString))) # Assuming grid is square i.e. (GRID_LENGTH = ROW_LENGTH*ROW_LENGTH)
        self.GRID_LENGTH = len(gridString)
        self.populateTrie()

    # Pre-processing method to generate flattened "trie" from gridString
    def populateTrie(self):
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
                    

    # Create new key,value pair if string is new, otherwise only add index
    # to existing index list if string length equals trie depth (as could prefix longer word)
    def addStringValue(self, str, index):
        if (not(str in self.trieDict)):
            self.trieDict.update({str:[index]})
        else:
            if (len(str) == self.TRIE_DEPTH):
                self.trieDict[str].append(index)

    # Given index in the grid, returns character that is stepRight chars horizontally right of index
    # Only returns character if it's on same row as index
    def getAdjacentCharRight(self, index, stepRight):
        charPosition = (index + stepRight)
        rowRemaining = (int(round(index/self.ROW_LENGTH)+1)*self.ROW_LENGTH-index-1)

        if ((index >= 0) and (charPosition < self.GRID_LENGTH) and (rowRemaining >= stepRight) and (stepRight >= 0)):
            return self.grid[charPosition]
        else:
            return ''

    def getAdjacentCharDown(self, index, stepDown):
        charPosition = (index + (stepDown*self.ROW_LENGTH))

        if ((index >= 0) and (charPosition < self.GRID_LENGTH) and (index < self.GRID_LENGTH) and (stepDown >= 0)):
            return self.grid[charPosition]
        else:
            return ''


class WordSearch():
    trieGrid = {}

    def __init__(self, grid):
        self.trieGrid = SearchGrid(grid)

    # Returns true if word exists in grid horizontally right or vertically down, else returns false
    def is_present(self, word):
        prefixPositions = []
        trieDepth = self.trieGrid.TRIE_DEPTH

        # If word length is less than trie depth, entire word will exist in trie
        if (len(word) <= trieDepth):
            try:
                found = self.trieGrid.trieDict[word]
                return True
            except: # Exception thrown if word doesn't exist in trie (i.e. doesn't exist in grid)
                return False
        else:
            try:
                # At every position in the grid where the word's prefix string exists
                prefixPositions = self.trieGrid.trieDict[word[:trieDepth]]
                for pos in range (0, len(prefixPositions)):
                    if (self.existsRight(word, prefixPositions[pos]) or self.existsDown(word, prefixPositions[pos])):
                        return True
                return False  
            except:

                return False
    
    # Compares word against all words in the grid that are prefixed the same horizontally right
    # Returns True if word horizontally right is same as word
    def existsRight(self, word, pos):
        for i in range (0, len(word)):
            if (word[i] != self.trieGrid.getAdjacentCharRight(pos, i)):
                return False
        return True

    def existsDown(self, word, pos):
        for i in range (0, len(word)):
            if (word[i] != self.trieGrid.getAdjacentCharDown(pos, i)):
                return False
        return True