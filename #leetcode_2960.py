# 2960. Count Tested Devices After Test Operations

class Solution:
    def countTestedDevices(self, batteryPercentages): 
        count = 0
        for bat_per in range(len(batteryPercentages)):
            batteryPercentages[bat_per] -= count
            if batteryPercentages[bat_per] > 0:
                count += 1
        return count     
