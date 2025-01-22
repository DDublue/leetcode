class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # space: O(1)
        # time: O(n)

        # simply checking each stone if it's a jewel
        total_jewels = 0
        for stone in stones:
            if stone in jewels:
                total_jewels += 1
        return total_jewels
