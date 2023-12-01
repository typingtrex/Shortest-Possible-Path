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

#  ------- ADD A LETTER -----------------------------------------------------------
def addLetter(wordInfo, hashmap, visitedHashmap):
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

      if nextWord in hashmap:
        # list of next words to add to the queue
        transitionWords.append([nextWord, nextPathLength])

        # adding to visited to back trace for result list
        if nextWord not in visitedHashmap:
          visitedHashmap[nextWord] = word


  return transitionWords


#  ------- DELETE A LETTER --------------------------------------------------------
def deleteLetter(wordInfo, hashmap, visitedHashmap):
  # return all possible transition words that exist in the dict after adding a letter to the current word
  transitionWords = []
  word = wordInfo[0]
  pathLength = wordInfo[1]
  nextPathLength = pathLength + 1

  # delete one letter at a time and check if the word exists in dict
  for i in range(len(word)):
    nextWord = word[:i] + word[i + 1:]

    if nextWord in hashmap:
      # list of next words to add to the queue
      transitionWords.append([nextWord, nextPathLength])

      # adding to visited to back trace for result list
      if nextWord not in visitedHashmap:
        visitedHashmap[nextWord] = word
  print("letter deleted")
  return transitionWords


#  ------- CHANGE A LETTER --------------------------------------------------------
def changeLetter(wordInfo, hashmap, visitedHashmap):
  # return all possible transition words that exist in the dict after adding a letter to the current word
  transitionWords = [["fellow", 2]]
  alphabets = 'abcdefghijklmnopqrstuvwxyz'
  word = wordInfo[0]
  pathLength = wordInfo[1]
  nextPathLength = pathLength + 1

  # changing a letter with (a - z) for each index in word
  for i in range(len(word)):
    for char in alphabets:
      nextWord = word[:i] + char + word[i+1:]

      if nextWord in hashmap:
        # list of next words to add to the queue
        transitionWords.append([nextWord, nextPathLength])

        # adding to visited to back trace for result list
        if nextWord not in visitedHashmap:
          visitedHashmap[nextWord] = word

  print("switched from the ABC's")
  return transitionWords


#  ------- CREATE LIST FROM START TO END WITH THE SHORTEST PATHWAY ----------------
def resultList(visitedHashmap):
  # use end word to traverse back through the
  print("visted dictionary ", visitedHashmap)



# --------- TEST EXAMPLES ---------------------------------------------------------
first = "tag"
last = "bowl"
listOfWords = ["tag", "tar", "bar", "boar", "boa", "bow", "bowl"]

shortestPossiblePath(first, last, listOfWords)
