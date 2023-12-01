# from collections import deque
# from queue import Queue

# -------- Function File --------------------
'''
  1. Below you will find the function that returns the shortest possible path from a start word to an end word.
  2. Please review the Specifications.md file for more details on the conditions of the function and its parameters.
  3. Thank you and happy searching for the shortest path!
'''

class ShortestPossiblePath:
  def __init__(self, start, end, dictionaryList):
    self.start = start
    self.end = end
    self.dictionaryList = dictionaryList
    # To make look up in the dictionary O(1) time complexity as opposed to O(N), where N is equal to the number of words in dictionaryList
    self.dictionarySet = set(dictionaryList)

  def addLetter(self, wordInfo):
    # return all possible transition words that exist in the dict after adding a letter to the current word
    print("letter added")

  def deleteLetter(self, wordInfo):
    # return all possible transition words that exist in the dict after adding a letter to the current word
    print("letter deleted")

  def changeLetter(self, wordInfo):
    # return all possible transition words that exist in the dict after adding a letter to the current word
    print("switched from the ABC's")

  def shortestPathway(self):
    # Implementing a Breadth First Search:
    # queue = deque([self.start, 1])
    # queue = Queue([self.start, 1])
    # regular array pop(0) is a shift -- can I make this a better time complexity later?
    queue = [[self.start, 1]]

    while queue:
      current = queue.pop(0)
      currentWord = current[0]
      currentLength = current[1]

      self.addLetter(currentWord)




    # print("dictionary is: ", self.dictionarySet, self.dictionaryList)

  # def addLetter(self):
  #   # ------ See if there are any changes that exist in the dictionary




first = "tag"
last = "bowl"
listOfWords = ["tag", "tar", "bar", "boar", "boa", "bow", "bowl"]
# expected ^^^
test = ShortestPossiblePath(first, last, listOfWords)
test.shortestPathway()





