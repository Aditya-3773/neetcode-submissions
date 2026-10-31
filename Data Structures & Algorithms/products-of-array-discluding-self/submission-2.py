class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r= [1]* len(nums)
        prefix= 1
        for i in range(len(nums)):
            r[i]= prefix
            prefix*= nums[i]

        suffix= 1
        for i in range(len(nums)- 1, - 1, - 1):
            r[i]*= suffix
            suffix*= nums[i]
           
        return r


        