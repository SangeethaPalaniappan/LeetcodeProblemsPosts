# 2379. Minimum Recolors to Get K Consecutive Black Blocks

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = blocks[:k].count('W')
        mini = count

        for i in range(1, len(blocks) - k + 1):
            if blocks[i - 1] == 'W':
                count -= 1
            if blocks[i + k - 1] == 'W':
                count += 1

            mini = min(mini, count)

        return mini
