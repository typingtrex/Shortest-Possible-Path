<!-- For the Users of this Function -->

# Shortest-Possible-Path

Welcome! Shortest-Possible-Path is a repository that holds a Python3 function that takes three parameters:

- start word
- end word
- dictionary (list)

and returns the shortest possible pathway from the start word to the end word by changing one letter at a time. Each intermediate word must exist in the given dictionary. Result is in a list format containing the start word, all intermediates, and the end word. Return _None_ if no possible path exists.

## Description Overview:

- Both the start and end words are lowercase alphabetic strings.
- The start and end words can be different lengths.
- Only one letter can be changed, added, or deleted at a time.

  1. Change: change a letter in the word to another letter in the alphabet
     - (i.e. "bat" -> change "a" for "e" -> "bet")
  2. Add: add a letter to the start string
     - (i.e. "bat" -> add "i" at index 2 -> "bait")
  3. Delete: delete a letter from the start string
     - (i.e. "hate" -> delete "e" at index 3 -> "hat")

- Each intermediate word must exist in the dictionary of words.
- The solution is returned as a list

  - ["bet", "bat", "bad"]

  OR

  _None_ if there is no possible path.

## Prerequisites:
