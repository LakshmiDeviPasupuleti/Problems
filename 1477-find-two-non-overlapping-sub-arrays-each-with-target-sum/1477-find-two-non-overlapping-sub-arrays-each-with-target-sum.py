class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)

        # best[i] = shortest valid subarray
        # ending at or before index i
        best = [float('inf')] * n

        left = 0
        curr_sum = 0
        ans = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            # Sum ekkuva ayithe left nunchi elements remove cheyyali
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # Current window sum = target
            if curr_sum == target:
                length = right - left + 1

                # Previous non-overlapping subarray undha?
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])

                # Current position varaku shortest subarray
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)

            else:
                # Current index varaku previous best carry forward
                if right > 0:
                    best[right] = best[right - 1]

        return -1 if ans == float('inf') else ans
        