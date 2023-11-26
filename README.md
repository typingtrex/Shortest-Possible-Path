# Shortest-Possible-Path
Seaplane's Technical Interview Application
Technical was provided: 11/21/2023 4:40 PM EST

## Interview Prompt: 

- **Coding exercise is to be completed before Friday, December 1st EOD**

- **Use this exercise to show:**
    - Technical skills
    - DevRel skills: 
        - Organized repository with intstructions on how to run your code as though this were a demo being created.

- **Technical Exercise**
    - "Design and implement a function in Python that takes two words and a dictionary of words as input. Your function should return the shortest possible path between the two words by changing one letter at a time. Each change is one path step."
    - *Assumptions:*
        - Both the start and end words are lowercase strings of varying lengths.
        - The start and end words can be different lengths.
        - Only one letter can be changed, added, or deleted at a time.
        - Each intermediate word must exist in the dictionary of words.


## Ji's Follow Up Questions and Breaking Down of the Problem: 

### Clarifying Questions: 

1. For the assumption of *"Only one letter can be changed, added, or deleted at a time"*, is a letter being changed a swap of letters?     
Example: "hat" -> "cat" 
    - "hat" -> change/swap "h" to "c" -> "cat" 
    - *change* is **one path step** by swapping "h" and "c".
    
    **OR**
        
    - The only possible paths are addition and deletion?
        - "hat" -> deletion (and check dictionary that "at" exists) -> "at" -> addition of "h" -> "hat"
        - Total of **two path steps**.

2. Dictionary holds both starting and ending strings?

3. Will there always be a solution? 
    1. Dictionary will hold enough intermediate strings for a path to be formed?
    2. If there is no path available, what should the function return? (Null? 0?)

3. Can we assume that both strings being lowercase means that there will be no symbols or numbers in the starting and ending words?

4. The function is required to return *"the shortest possible path"* 
    1. What format would you want the shortest possible path to be returned as?
        - Should I return this shortest possible path as an array that holds all the paths necessary to change from start string to end string? 
            - Example: "cat" -> "catch"
                - Path1: "cat" -> add "c", check that "catc" exists in dictionary -> "catc"
                - Path2: "catc" -> add "h" check that "catch" exists in dictionary -> "catch"
                - return: ["addition", "addition"]

### Edge Cases
    1. 
    2. 

### Solution Thoughts: 
#### Prioritizing Time Complexity:
Assuming that the start and end strings are all the english alphabets in lowercase.

1. Create a dictionary that holds the alphabets as keys, and the values are the end word's indices when the letter occurs. 
    
    1. Example: "hat" 
        dictionary = {
        
        "a" : 1,

        .

        .

        .

        "h" : 0,

        .

        .

        .

        "t" : 2
        
        .
        
        .
        
        .
        
        "z" = null
        
        } 
2. Use dictionary of instances in end word to determine whether to keep a letter in starting word or to add a letter or to delete a letter. 

    1. The instances dictionary will tell us: 
        - If the same letter exists in starting and ending words.
        - If the order of the letters matches (?) // - write this part clearer 