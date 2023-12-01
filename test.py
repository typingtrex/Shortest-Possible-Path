from shortestPossiblePathFunction import shortestPossiblePath

# --------- TEST EXAMPLES ---------------------------------------------------------

first = "tag"
last = "bowl"

listOfWords1 = ["tag", "tar", "bar", "boar", "boa", "bow", "bowl", "fowl", "rag", "tal", "bal", "bol"]
listOfWords2 = ["tag", "tar", "bar", "boar", "boa", "bow", "bowl", "fowl", "rag"]
listOfWords3 = ["tag", "tar", "bar", "boar", "bow", "bowl", "fowl", "rag"]

print(shortestPossiblePath(first, last, listOfWords1))
print(shortestPossiblePath(first, last, listOfWords2))
print(shortestPossiblePath(first, last, listOfWords3)) # return None

start = "hit"
end = "cog"
dictionary = ["hit", "hot", "dog", "dot", "lot", "log", "cog"]
print(shortestPossiblePath(start, end, dictionary))
