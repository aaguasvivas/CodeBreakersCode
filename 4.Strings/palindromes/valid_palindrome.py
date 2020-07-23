class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        return new_s == new_s[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        start = 0
        end = len(new_s) - 1

        while start <= end:
            if new_s[start] != new_s[end]:
                return False
            start += 1
            end -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()

        if len(new_s) == 0:
            return True

        n = len(new_s)

        if n % 2:
            lo = n // 2 - 1
            hi = n // 2 + 1

        else:
            lo, hi = n // 2 - 1, n // 2
            if new_s[lo] != new_s[hi]:
                return False
            lo -= 1
            hi += 1

        while lo >= 0 and hi < n:
            if new_s[lo] != new_s[hi]:
                return False
            lo -= 1
            hi += 1
        return True
