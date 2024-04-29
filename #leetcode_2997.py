# 2997. Minimum Number of Operations to Make Array XOR Equal to K

class Solution:
    def minOperations(self, nums, k):
        arr_xor = 0
        for i in nums:
            arr_xor ^= i
        flip_count = 0
        while k != 0 or arr_xor != 0:
            rem_k = k % 2
            rem_arr_xor = arr_xor % 2
            if rem_k != rem_arr_xor:
                flip_count += 1
            k //= 2
            arr_xor //= 2
        return flip_count        