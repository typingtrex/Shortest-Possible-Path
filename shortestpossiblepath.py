from collections import deque

# -------- Function File ----------------------------------------------------------
'''
  1. Below you will find the function that returns the shortest possible path from a start word to an end word.
  2. Please review the Specifications.md file for more details on the conditions of the function and its parameters.
  3. Thank you and happy searching for the shortest path!
'''
#  ---------- MAIN FUNCTION -------------------------------------------------------
def shortestPossiblePath(start, end, dictionaryList):
  dictionarySet = set(dictionaryList)
  visitedHashmap = dict()

  queue = [[start, 1]]

  while queue:
    current = queue.pop(0)
    currentWord = current[0]

    # our baseline for the return result:
    if currentWord == end:
      # print("path length is: ", current[1])
      return resultList(start, end, visitedHashmap)

    addList = addLetter(current, dictionarySet, visitedHashmap)
    deleteList = deleteLetter(current, dictionarySet, visitedHashmap)
    changeList = changeLetter(current, dictionarySet, visitedHashmap)

    # adding all the transitionWords to check from add, delete, and change functions to the queue:
    queue.extend(addList)
    queue.extend(deleteList)
    queue.extend(changeList)


#  ---------- SUB FUNCTIONS -------------------------------------------------------

#  ------- ADD A LETTER -----------------------------------------------------------
def addLetter(wordInfo, dictionary, visitedHashmap):
  # return all possible transition words that exist in the dict after adding a letter to the current word
  transitionWords = []
  alphabets = 'abcdefghijklmnopqrstuvwxyz'
  word = wordInfo[0]
  pathLength = wordInfo[1]
  nextPathLength = pathLength + 1

  # adding a letter from (a - z) to each index in word
  # Will this add to the end of the word as well? YES! because of the len(word) + 1
  for i in range(len(word) + 1):
    for char in alphabets:
      nextWord = word[:i] + char + word[i:]

      if nextWord in dictionary and nextWord not in visitedHashmap:
        # list of next words to add to the queue
        transitionWords.append([nextWord, nextPathLength])

        # adding to visited to back trace for result list
        visitedHashmap[nextWord] = word

  return transitionWords


#  ------- DELETE A LETTER --------------------------------------------------------
def deleteLetter(wordInfo, dictionary, visitedHashmap):
  # return all possible transition words that exist in the dict after adding a letter to the current word
  transitionWords = []
  word = wordInfo[0]
  pathLength = wordInfo[1]
  nextPathLength = pathLength + 1

  # delete one letter at a time and check if the word exists in dict
  for i in range(len(word)):
    nextWord = word[:i] + word[i + 1:]

    if nextWord in dictionary and nextWord not in visitedHashmap:
      # list of next words to add to the queue
      transitionWords.append([nextWord, nextPathLength])

      # adding to visited to back trace for result list
      visitedHashmap[nextWord] = word

  return transitionWords


#  ------- CHANGE A LETTER --------------------------------------------------------
def changeLetter(wordInfo, dictionary, visitedHashmap):
  # return all possible transition words that exist in the dict after adding a letter to the current word
  transitionWords = []
  alphabets = 'abcdefghijklmnopqrstuvwxyz'
  word = wordInfo[0]
  pathLength = wordInfo[1]
  nextPathLength = pathLength + 1

  # changing a letter with (a - z) for each index in word
  for i in range(len(word)):
    for char in alphabets:
      nextWord = word[:i] + char + word[i+1:]

      if nextWord in dictionary and nextWord not in visitedHashmap:
        # list of next words to add to the queue
        transitionWords.append([nextWord, nextPathLength])

        # adding to visited to back trace for result list
        visitedHashmap[nextWord] = word

  return transitionWords


#  ------- CREATE LIST FROM START TO END WITH THE SHORTEST PATHWAY ----------------
def resultList(start, end, visitedHashmap):
  # use end word to traverse back through the
  shortestPathway = [end]

  # use deque to make adding to the left an O(1) Time Complexity
  shortestPathway = deque(shortestPathway)

  word = end

  while (word != start):
    previousWord = visitedHashmap[word]
    shortestPathway.appendleft(previousWord)
    word = previousWord

  # change back format from deque to a list
  resultingPath = [*shortestPathway]
  return resultingPath



# --------- TEST EXAMPLES ---------------------------------------------------------
first = "tag"
last = "bowl"
listOfWords1 = ["tag", "tar", "bar", "boar", "boa", "bow", "bowl", "fowl", "rag", "tal", "bal", "bol"]
listOfWords2 = ["tag", "tar", "bar", "boar", "boa", "bow", "bowl", "fowl", "rag"]


print(shortestPossiblePath(first, last, listOfWords1))
print(shortestPossiblePath(first, last, listOfWords2))
