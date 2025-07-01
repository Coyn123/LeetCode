class Solution:
    def possibleStringCount(self, word: str) -> int:
        left = 0
        right = 1
        toList = list(word)
        res = 1
        if len(toList) > 1:
            while right < len(toList):
                if toList[left] == toList[right]:
                    right += 1
                    res += 1
                else:
                    right += 1
                    left = right - 1
        else:
            return res
        return res


        #simple two pointer solution:
        #problems fleshing out indexing problems, should have started with while loop
        #overall good technical problem solving, figured out the algo and put it to use efficiently.
