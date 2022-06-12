class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #2022/06/12
        answer = []
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in nums:
                idx = nums.index(ans)
                if i == idx:
                    continue
                answer.append(i)
                answer.append(idx)
                return answer
        '''
        #2022/05/22
        answer = []
        for i in range(len(nums)):
            #print "i={}".format(i)
            if len(answer) > 0:
                break
            for j in range(len(nums)):
                #print "j={}".format(j)
                if i == j:
                    continue
                #print "sum={}".format(nums[i] + nums[j])
                if (nums[i] + nums[j]) == target:
                    answer.append(i)
                    answer.append(j)
                    break
                    
        return answer
        '''
                
