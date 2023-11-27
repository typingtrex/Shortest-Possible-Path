from collections import deque
# deque stands for "double-ended queue" and is imported to quickly append and pop elements from both ends of the queue.

# -- Solution for Shortest Possible Path using Breadth First Search with a Queue -------
# returning the shortest possible path changing the starting word to the ending word, in which one path is one letter change, which must be included as a word in the dictionary.


#  ------ BEFORE SUBMITTING NOTES ------------------------
# This solution only takes into consideration if the start word and end word are at the same length
# Need to include a subfunction that will append characters or delete characters and check agains the dictionary
# Need to break up this one function into more subfuctions (inside dictionary ? return boolean)


class Solution: 
    def shortestPossiblePath(self, startWord: str, endWord: str, dictionary: dict):
        # if the end word is not in the dictionary, return 0
        if endWord not in dictionary: 
            return 0
        
        # Utilizing a queue to hold the starting word (later current word) and total path number
        queue = deque([startWord, 1])

        # Breadth-first-search loop
        while queue:
            # FIFO (First In First Out) Dequeue the leftmost element to get word and path number
            # 
            currentWord, length = queue.popleft()
        # print("This is the current word: ", currentWord)
        # print("this is length: ", length)
        # print("This is the QUEUE: ", queue)

        # Check if the current word is the target word
        if currentWord == endWord:
            return length

        # Explore all possible one-character transformations of the current word
        for i in range(len(currentWord)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                # Generate a new word by replacing the current character
                nextWord = currentWord[:i] + char + currentWord[i + 1:]
                # print("current word: ", current_word)
                # print("current_word[:i] ISSS: ", current_word[:i])
                # print("CHAR is: ", char)
                # print("currentWORD current_word[i + 1:]: ", current_word[i + 1:])
                # Check if the new word is in the dictionary
                if nextWord in dictionary:
                # Remove the new word from the dictionary to avoid revisiting it
                    dictionary.remove(nextWord)
                # Enqueue the new state with the updated length
                    queue.append((nextWord, length + 1))
                    print('queue ', queue)
        # If no valid path is found
        return 0


start = "hit"
end = "cog"
dictionary = {
    "hot": True,
    "dot": True,
    "dog": True,
    "lot": True,
    "log": True,
    "cog": True
}

# Creating an instance of the Solution class
solutionInstance = Solution()

# Calling the shortestPossiblePath function on the instance
result = solutionInstance.shortestPossiblePath(start, end, dictionary)

# Printing the result
print(result) # Output: 5

