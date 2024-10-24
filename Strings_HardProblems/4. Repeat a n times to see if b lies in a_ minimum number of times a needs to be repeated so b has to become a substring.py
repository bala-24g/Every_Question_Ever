class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat=(len(b)//len(a)) #maximum number of times it can repeat
        count=1
        while count<=repeat+2:
            if b in a*count:
                return count #i.e after repeating a for count number of times if b is a part of a, then return it
            count+=1
        return -1



        