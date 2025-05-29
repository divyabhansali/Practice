class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        overall, current = 0, 0
        for i in nums:
            if i==1:
                current +=1
            else:
                overall = max(current, overall)
                current = 0
        overall = max(current, overall)
        return overall
    

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                even = even +1
                
        return even
                
        

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(len(nums)):
            nums[i]= nums[i]*nums[i]
        # if l != 0:
        #     for j  in 
        
#         for k in range(l):
#             min_index = k
#             for j in range(k+1 , l):
#                if nums[j]<nums[min_index]:
                
                
                
        
        
        return sorted(nums)
        


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        p = len(arr)
        k=0
        for i in range(len(arr)):
            l=i+k
            if arr[l] == 0:
                arr.insert(l+1,0)
                k=k+1
        
        while(len(arr) > p):
            arr.pop()
  
        return 1
        

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        # for i in nums2:
        #     nums1.append(i)
        #print(nums1)
        
        for i in range(n):
            nums1.remove(0)
        
        nums1.sort()
#         nums1.remove(0)
#         print(nums1)
        


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for i in nums:
            if i == val:
                count= count+1
        for i in range(count):
            nums.remove(val)
        
        k= len(nums)
        return k
        

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while(i < len(nums)):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
    
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        #arr= [3,1,7,11]
        n= len(arr)
        for i in range(n):
            for j in range(n):
                if (arr[i] == 2*arr[j] and arr[i]!=arr[j]!=0) or (arr[i]/2 == arr[j] and arr[i]!=arr[j]!=0):
                    print("i",arr[i])
                    print("j",arr[j])
                    return True
        return False
            
        
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #[3,5,5]
        up=0
        down = 0
        if len(arr)<3:
            return False
        else:
            for i in range(len(arr)-1):
                if arr[i]>arr[i+1]:
                    down +=1
                elif arr[i]<arr[i+1]:
                    up +=1
                else:
                    return False
        if (len(arr) == (down+up+1)) and (down!=0 and up !=0) and arr[0]<arr[1]:
            return True
        return False
    
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #arr = [17,18,5,4,6,1]
        n = len(arr)
        for i in range(n-1):
            #print(arr[i])
            for j in range(i+1,n-1):
                max = arr[i+1]
                if max < arr[j+1]:
                    max = arr[j+1]
                    print("max",max)
            arr[i] = max
            print(max)
            print(arr)
        arr[n-1] = -1
        #print(arr)
        return arr
        
            #Input: nums = [0,0,1]
        i=0
        while(i <(len(nums)):
            #print(nums[i])
            if nums[i] ==0:
                nums.append(0) #[0,0,1,]
                del nums[i]   #[0,1,0]
                i = i+1
                

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        r=0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
                nums[r]=nums[i]
                r+=1
        k=d.keys()
        
        return len(k)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #[0,1,2,2,3,0,4,2]
        count=0
        for i in nums:
            if i == val:
                count=count+1
               
                
        for j in range(count):
            nums.remove(val)
        k=len(nums)        
        return k
        