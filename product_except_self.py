
def productExceptSelf(nums: List[int]) -> List[int]:
    initial = 1
    ans = []
    for n in nums:
        ans.append(initial)
        initial*=n
    initial = 1
    for i in range(len(nums)-1,-1,-1):
        ans[i]*=initial
        initial*=nums[i]
    return ans
