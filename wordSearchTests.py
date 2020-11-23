import unittest
import math
from random import choice, randint
from string import ascii_lowercase
from wordSearch import SearchGrid, WordSearch


class WordSearchTests(unittest.TestCase):

    # Generates grid of random characters in range a-z, of length size^2
    def generateLargeGrid(self, size):
        largeGridString = ''.join(choice(ascii_lowercase) for i in range(size**2))
        return largeGridString

    # Generates horizontal word from substring of grid
    # Grid must be at least 26x26
    def generateHorizontalWord(self, grid):
        row_length = int(math.sqrt(len(grid)))
        randomWordLength = randint(1, 26)
        randomRow = randint(0, row_length-1)
        randomColumn = randint(0, row_length-randomWordLength)
        wordIndex = (randomRow * row_length) + randomColumn
        return grid[wordIndex:wordIndex+randomWordLength]

    def generateVerticalWord(self, grid):
        row_length = int(math.sqrt(len(grid)))
        verticalWord = ""
        randomWordLength = randint(1, 26)
        randomColumn = randint(0, row_length-1)
        randomRow = randint(0, row_length-randomWordLength)
        wordIndex = (randomRow * row_length) + randomColumn
        for i in range(0, randomWordLength):
            verticalWord += grid[wordIndex + (i*row_length)]
        return verticalWord

    # Generates list of words, half horizontal, half vertical
    # Grid must be at least 26x26
    def generateWords(self, noOfWords, grid):
        wordsList = []
        for i in range (0, math.floor(noOfWords/2)):
            wordsList.append(self.generateHorizontalWord(grid))
        for i in range (math.floor(noOfWords/2)):
            wordsList.append(self.generateVerticalWord(grid))
        return wordsList

    # Testing general and edge cases on small grid
    def test_smallGrid(self):
        ws = WordSearch("abcdaeaghijalaaa")
        self.assertTrue(ws.is_present("a"))
        self.assertTrue(ws.is_present("ab"))
        self.assertTrue(ws.is_present("dg"))
        self.assertTrue(ws.is_present("abc"))
        self.assertTrue(ws.is_present("abcd"))
        self.assertTrue(ws.is_present("aahl"))
        self.assertTrue(ws.is_present("dgaa"))
        self.assertTrue(ws.is_present("aaa"))
        self.assertTrue(ws.is_present("aeag"))
        self.assertFalse(ws.is_present("gh"))
        self.assertFalse(ws.is_present("ijal"))
        self.assertFalse(ws.is_present("DG"))
        self.assertFalse(ws.is_present("abcda"))

    # Testing searching for 1,000 words in 500x500 char grid
    def test_someWordsMediumGrid(self):
        largeGrid = self.generateLargeGrid(500)
        ws = WordSearch(largeGrid)
        wordsToFind = self.generateWords(1000, largeGrid)
        for word in wordsToFind:
            self.assertTrue(ws.is_present(word))

    # Testing searching for 100,000 words in 1000x1000 char grid
    def test_manyWordsLargeGrid(self):
        largeGrid = self.generateLargeGrid(1000)
        ws = WordSearch(largeGrid)
        wordsToFind = self.generateWords(100000, largeGrid)
        for word in wordsToFind:
            self.assertTrue(ws.is_present(word))


if __name__ == '__main__':
    unittest.main()