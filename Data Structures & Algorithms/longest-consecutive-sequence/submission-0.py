class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        seen= set(nums)
        l= 0
        for num in seen:
            if(num- 1) not in seen:
                len= 1
                while (num+ len) in seen:
                    len+= 1
                l= max(len, l)

        return l
            

            