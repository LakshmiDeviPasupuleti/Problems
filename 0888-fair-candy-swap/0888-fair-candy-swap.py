class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        alicetotal=sum(aliceSizes)
        bobtotal=sum(bobSizes)
        differnce=(alicetotal - bobtotal)//2
        for a in aliceSizes:
            for b in bobSizes:
                if a-b== differnce :
                    return [a,b]