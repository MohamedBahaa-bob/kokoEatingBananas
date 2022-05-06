# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        sum = 0
        for i in range(len(piles)):
            sum += piles[i]
        left = max(math.floor(sum / h), 1)
        right = max(piles)
        res = right

        while left <= right:
            mid = ((left + right) // 2)
            sum = 0
            for i in range(0, len(piles)):
                sum += math.ceil(piles[i] / mid)
            if sum <= h:
                res = min(mid, res)
                right = mid - 1
            else:
                left = mid + 1
        return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
