class Solution:
    def missingRange(self, arr, low, high):
        # The code below used to remove elements which are there in arr from arr1. Too much time complexity.
        
        """arr1 = list(range(low, high + 1))
        for i in range(len(arr)):
            if arr1 == []:
                break
            if arr[i] >= low and arr[i] <= high:
                if arr[i] in arr1:
                    arr1.remove(arr[i])
        
        return arr1 """
        
        # Now this removed duplicate elements from arr and added missing elements from range into another array.
        
        arr1 = set(arr)
        missing = []
        for num in range(low, high + 1):
            if num not in arr1:
                missing.append(num)
                
        return missing