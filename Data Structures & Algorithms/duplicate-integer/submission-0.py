class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        answer = []
        for i in nums:
            if i not in answer:
                answer.append(i)
        if nums == answer:
            return False
        else:
            return True      


