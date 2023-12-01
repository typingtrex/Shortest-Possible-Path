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
    self.visitedHashmap = dict()

# refactoring -- can I change transitionWords to be a list in my init to push to as I find them in all of my subfunctions??
  def addLetter(self, wordInfo):
    # return all possible transition words that exist in the dict after adding a letter to the current word
    transitionWords = []
    print("letter added")
    return transitionWords

  def deleteLetter(self, wordInfo):
    # return all possible transition words that exist in the dict after adding a letter to the current word
    transitionWords = [["yellow", 2], ["bye", 2]]
    print("letter deleted")
    return transitionWords

  def changeLetter(self, wordInfo):
    # return all possible transition words that exist in the dict after adding a letter to the current word
    transitionWords = [["fellow", 2]]
    print("switched from the ABC's")
    return transitionWords

  def resultList(self):
    # use end word to traverse back through the
    print("visted dictionary ", self.visitedHashmap)

  def shortestPathway(self):
    # Implementing a Breadth First Search:
    # queue = deque([self.start, 1])
    # queue = Queue([self.start, 1])
    # regular array pop(0) is a shift -- can I make this a better time complexity later?
    queue = [[self.start, 1]]
    count = 1

    while queue and count < 4:
      current = queue.pop(0)
      currentWord = current[0]

      # our baseline for the return result:
      if currentWord == self.end:
        return self.resultList()

      addList = self.addLetter(current)
      deleteList = self.deleteLetter(current)
      changeList = self.changeLetter(current)

      # adding all the transitionWords to check from add, delete, and change functions to the queue:
      queue.extend(addList)
      queue.extend(deleteList)
      queue.extend(changeList)
      print("current queue is: ", queue)
      count += 1




    # print("dictionary is: ", self.dictionarySet, self.dictionaryList)

  # def addLetter(self):
  #   # ------ See if there are any changes that exist in the dictionary




first = "tag"
last = "bowl"
listOfWords = ["tag", "tar", "bar", "boar", "boa", "bow", "bowl"]
# expected ^^^
test = ShortestPossiblePath(first, last, listOfWords)
test.shortestPathway()





