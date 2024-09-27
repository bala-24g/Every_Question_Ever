from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Create a set for fast look-up and remove duplicates
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # Initialize BFS queue with the beginWord and the initial transformation length as 1
        dq = deque([(beginWord, 1)])
        visited = set([beginWord])
        alphabets = "abcdefghijklmnopqrstuvwxyz"

        # Perform BFS
        while dq:
            word, level = dq.popleft()

            # If we found the endWord, return the current level
            if word == endWord:
                return level

            # Try transforming each letter in the word
            for i in range(len(word)):
                for ch in alphabets:
                    if word[i] != ch:
                        transformedWord = word[:i] + ch + word[i+1:]

                        # If the transformed word is in wordSet and not yet visited
                        if transformedWord in wordSet and transformedWord not in visited:
                            visited.add(transformedWord)
                            dq.append((transformedWord, level + 1))

        # If no transformation sequence is found, return 0
        return 0
#Logic is, change each letter of each word and see if it is in the set of given words, and if it is push that into dq and do the same. Also maintain a visited set to not keep going back and forth.