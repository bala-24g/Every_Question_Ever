from collections import deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset = set(wordList)
        if endWord not in wordset:
            return []

        alphabets = "abcdefghijklmnopqrstuvwxyz"
        dq = deque()
        dq.append([beginWord, [beginWord]])  # Queue stores word and the path to it
        visited = set([beginWord])  # Visited set to track global visited words
        level_visited = set()  # To track visited words in each BFS level
        ans = []  # To store final answers
        found = False  # To indicate when the shortest paths are found
        min_level = float('inf')  # Track the minimum level where the endWord is found

        while dq and not found:
            level_size = len(dq)
            
            for _ in range(level_size):
                word, lst = dq.popleft()

                # If the word is the endWord, we store the path
                if word == endWord:
                    found = True
                    ans.append(lst)
                
                # Explore all possible one-letter transformations
                for i in range(len(word)):
                    for j in alphabets:
                        trans = word[:i] + j + word[i+1:]
                        if trans in wordset and trans not in visited:
                            level_visited.add(trans)
                            dq.append([trans, lst + [trans]])

            # Add level-specific visited words to the global visited set
            visited.update(level_visited)
            level_visited.clear()

            # If we've found at least one path to the endWord, stop searching
            if found:
                break

        return ans
#This you've to return all possible shortest paths. 
#This gives TLE
#However, the way this is done is through checking level wise.
#You traverse for the length of the dq by popping out stuff drom the btm and marking the possible paths out as the prev problem did
#But the updating the visited one is done level wise, not immediately.