<!-- For my thoughts and clarifications/approach to the problem -->

# My Approach

## Interview Prompt:

**Technical Exercise**

- "Design and implement a function in Python that takes two words and a dictionary of words as input. Your function should return the shortest possible path between the two words by changing one letter at a time. Each change is one path step."

- **Coding exercise is to be completed before Friday, December 1st EOD**

- **Use this exercise to show:**

  - Technical skills
  - DevRel skills:
    - Organized repository with intstructions on how to run your code as though this were a demo being created.

## The Problem Details:

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
   a) return an error message OR null (_note to self choose one_)
6. Return a list of words for the changes from start to end (i.e. ["bat", "cat", "cab"])
   --- edge case?? -----
7. In the case of multiple solutions of the same shortest path length, return any one of them **_ point this out to Fokke _**

## Ji's Follow Up Questions and Breaking Down of the Problem:

### Clarifying Questions:

1.  For the assumption of _"Only one letter can be changed, added, or deleted at a time"_, is a letter being changed a swap of letters?
    Example: "hat" -> "cat" - "hat" -> change/swap "h" to "c" -> "cat" - _change_ is **one path step** by swapping "h" and "c".

        **OR**

        - The only possible paths are addition and deletion?
            - "hat" -> deletion (and check dictionary that "at" exists) -> "at" -> addition of "h" -> "hat"
            - Total of **two path steps**.

2.  Does the dictionary hold both starting and ending strings?

3.  Will there always be a solution?

    1. Dictionary will hold enough intermediate strings for a path to be formed?
    2. If there is no path available, what should the function return? (Null? 0?)

4.  Can we assume that both strings being lowercase means that there will be no symbols or numbers in the starting and ending words?

5.  The function is required to return _"the shortest possible path"_
    1. What format would you want the shortest possible path to be returned as?
       - Should I return the shortest possible path as an array that holds all the paths necessary to change from start string to end string?
         - Example: "cat" -> "bag"
           - Path1: "cat" -> change "a" to "b" -> "bat"
           - Path2: "bat" -> change "t" to "g" and check that "bag" exists in dictionary -> "bag"
           - return: ["change", "change"]
6.  What format will the dictionary provided hold the intermediate words?
    - key = "intermediate word string"
    - value = (?)

### Edge Cases

1. Can start and end words be empty strings?

### Solution Thoughts:

#### Prioritizing Time Complexity:

Assuming that the start and end strings are all the english alphabets in lowercase.

1.
