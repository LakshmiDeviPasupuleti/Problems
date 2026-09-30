class Solution:
    def hammingWeight(self, n: int) -> int:
        #x=bin(n)
        return n.bit_count()