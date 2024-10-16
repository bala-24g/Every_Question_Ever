class Solution:
    def isPossible(self, a, b):
        if a==2 or b==2 :
            if a==b:
                return 0
            else:
                return 1
        return 0
#Need to have inorder for sure then either pre order or post.