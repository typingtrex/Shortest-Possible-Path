from shortestPossiblePathFunction import shortestPossiblePath

# --------- TEST EXAMPLES ---------------------------------------------------------

first = "tag"
last = "bowl"

listOfWords1 = ["tag", "tar", "bar", "boar", "boa", "bow", "bowl", "fowl", "rag", "tal", "bal", "bol"]
listOfWords2 = ["tag", "tar", "bar", "boar", "boa", "bow", "bowl", "fowl", "rag"]
listOfWords3 = ["tag", "tar", "bar", "boar", "bow", "bowl", "fowl", "rag"]
listOfWords4 = ["tag", "tar", "bar", "boar", "boa", "bow", "bowl", "fowl", "rag", "tal", "bal", "bol", "taw", "baw"]

print("list1: ", shortestPossiblePath(first, last, listOfWords1))
print("list2: ", shortestPossiblePath(first, last, listOfWords2))
print("list3: ", shortestPossiblePath(first, last, listOfWords3)) # return None
print("list4: ", shortestPossiblePath(first, last, listOfWords4)) # 2 possible options
  # path length  5
  # ['tag', 'tal', 'bal', 'bol', 'bowl']
  # ['tag', 'taw', 'baw', 'bow', 'bowl']
  # BUT only returns the first instance when end word == current word
start = "hit"
end = "cog"
dictionary = ["hit", "hot", "dog", "dot", "lot", "log", "cog"]
print(shortestPossiblePath(start, end, dictionary))
