class Solution:
    def isPalindrome(self, x: int) -> bool:
        ex = str(x)
        first = 0
        last = len(ex) - 1
        while last >= first:
            if ex[last] == ex[first]:
                last -= 1
                first += 1
            else:
                return False
        return True
