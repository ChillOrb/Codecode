
# https://leetcode.com/problems/n-th-tribonacci-number/
# using DP , hash map


class Solution:
    def tribonacci(self, n: int) -> int:
        hmap = {0: 0, 1: 1, 2: 1}
        def trib(n):
            if n in hmap:
                return hmap.get(n)
            else:
                value = trib(n-1) + trib(n-2) + trib(n-3)
                hmap[n] = value
                return value
        return trib(n)
