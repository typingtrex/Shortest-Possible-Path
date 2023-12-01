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
  count = 1

  while queue and count < 4:
    current = queue.pop(0)
    currentWord = current[0]

    # our baseline for the return result:
    if currentWord == end:
      return resultList(visitedHashmap)

    addList = addLetter(current)
    deleteList = deleteLetter(current)
    changeList = changeLetter(current)

    # adding all the transitionWords to check from add, delete, and change functions to the queue:
    queue.extend(addList)
    queue.extend(deleteList)
    queue.extend(changeList)
    print("current queue is: ", queue)
    count += 1

#  ---------- SUB FUNCTIONS -------------------------------------------------------
#  ------- ADD A LETTER ----------------
def addLetter(wordInfo, hashmap):
  # return all possible transition words that exist in the dict after adding a letter to the current word
  transitionWords = []
  alphabets = 'abcdefghijklmnopqrstuvwxyz'
  word = wordInfo[0]
  pathLength = wordInfo[1]
  nextPathLength = pathLength + 1

  # adding a letter from (a - z) for each index in word -- will this add to the end of the word as well?
  for i in range(len(word)):
    for char in alphabets:
      nextWord = word[:i] + char + word[i:]
      print("word: ", word)
      print("nextWord", nextWord)
      if nextWord in hashmap:
        transitionWords.append([nextWord, nextPathLength])

  return transitionWords

#  ------- DELETE A LETTER --------------------------------------------------------
def deleteLetter(wordInfo, hashmap):
  # return all possible transition words that exist in the dict after adding a letter to the current word
  transitionWords = [["yellow", 2], ["bye", 2]]
  print("letter deleted")
  return transitionWords

#  ------- CHANGE A LETTER --------------------------------------------------------
def changeLetter(wordInfo, hashmap):
  # return all possible transition words that exist in the dict after adding a letter to the current word
  transitionWords = [["fellow", 2]]
  alphabets = 'abcdefghijklmnopqrstuvwxyz'

  print("switched from the ABC's")
  return transitionWords

#  ------- CREATE LIST FROM START TO END WITH THE SHORTEST PATHWAY ----------------
def resultList(hashmap):
  # use end word to traverse back through the
  print("visted dictionary ", hashmap)



# --------- TEST EXAMPLES ---------------------------------------------------------
first = "tag"
last = "bowl"
listOfWords = ["tag", "tar", "bar", "boar", "boa", "bow", "bowl"]

shortestPossiblePath(first, last, listOfWords)