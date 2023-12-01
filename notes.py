# Understanding the problem details - response from Fokke included:

'''
Premise:

Given three parameters of start word, end word, and a dictionary, which is a list of words (i.e. ['cog', 'bog', 'dog', 'dot']), return the shortest path for a starting word to become the ending word.

There are three options for a path:
  1. Swap: change a letter (i.e. "bat" -> swap "a" for "e" -> "bet")
  2. Add: add a letter to the start string (i.e. "bat" -> add "i" at index 2 -> "bait")
  3. Delete: delete a letter from the start string (i.e. "hate" -> delete "e" at index 3 -> "hat")

Assumptions and Clarifications:
  1. Both start and end strings are lowercase alphabets only.
  2. Both start and end strings can be varying lenghts.
  3. Only 1 letter can be altered at a time, and the new changed word MUST exist in the dictionary.
  4. Both start and end strings exist in the dictionary.
  5. Solution does not always exist:
      a) return an error message OR null (*note to self choose one*)
  6. Return a list of words for the changes from start to end (i.e. ["bat", "cat", "cab"])
  --- edge case?? -----
  1. In the case of multiple solutions of the same shortest path length, return any one of them *** point this out to Fokke ***

'''

'''

The team has this code, and those outside of the team need instructions on how to use it

-- format good

'''




# ----- Creating subfunctions: ----------------
# 1. Swap
def swap(word, dictionaryMap, queue):
  alphabets = 'abcdefghijklmnopqrstuvwxyz'
  for i in range(len(word)):
    for char in alphabets:
      # all letters before i (index) + char + all letters after i
      nextWord = word[:i] + char + word[i + 1:]

      if nextWord in dictionaryMap & next in dictionaryMap != "seen":
        dictionaryMap[nextWord] = "seen"
        queue.append(nextWord, length + 1)

  return queue

# Add

def add(word, endWord) {
  if len(word) < len(endWord):

}

# testWord = "hello"
# testIdx = 1

# swap(testWord, testIdx, {})
