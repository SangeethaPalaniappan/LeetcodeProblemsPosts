# 1701. Average Waiting Time

class Solution:
    def averageWaitingTime(self, customers):
        add_to_time = 0
        tot_sum = 0
        for arr in customers:
            if arr[0] >= add_to_time: 
                add_to_time = arr[0] + arr[1] 
                tot_sum += (add_to_time - arr[0])
            else:
                add_to_time += arr[1] 
                tot_sum += add_to_time - arr[0] 
                
        return tot_sum / len(customers)    


