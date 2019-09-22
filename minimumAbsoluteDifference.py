class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """


        if (len(arr) < 2):
            return

        arr.sort()
        output = []
        minDiff =  abs(arr[0] - arr[1])
        for i in range(len(arr)-1):
            curDiff = abs(arr[i] - arr[i+1])
            if ( curDiff < minDiff):
                minDiff = curDiff

        for i in range(len(arr)-1):
            curDiff = abs(arr[i] - arr[i + 1])
            if (curDiff == minDiff):
                tmp = [arr[i], arr[i+1]]
                output.append(tmp)

        return output

