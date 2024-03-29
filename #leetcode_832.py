# 832. Flipping an Image

class Solution:
    def flipAndInvertImage(self, image):
        for nums in image:
            nums.reverse()
        
        for arr in image:
            for i in range(len(arr)):

                if arr[i] == 0:
                    arr[i] = 1
                elif arr[i] == 1:
                    arr[i] = 0

        return image                
