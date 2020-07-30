# Use sorted, lambda counting 1s of binary of x and storing it with x
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))
