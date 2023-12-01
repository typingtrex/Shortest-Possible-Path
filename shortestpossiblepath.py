from collections import deque

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

  def shortestPathway(self):
    #  --- To make look up in the dictionary O(1) time complexity as opposed to O(N), where N is equal to the number of words in dictionaryList
    dictionarySet = set(self.dictionaryList)
    print("dictionary is: ", dictionarySet, self.dictionaryList)




first = "tag"
last = "bowl"
listOfWords = ["tag", "tar", "bar", "boar", "boa", "bow", "bowl"]
# expected ^^^
test = ShortestPossiblePath(first, last, listOfWords)
test.shortestPathway()





