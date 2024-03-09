
def topKFrequent( nums: List[int], k: int) -> List[int]:
    ans=[]
    carCount = {}
    hashm = [[] for _ in range(len(nums)+1)]

    for n in nums:
        carCount[n] = 1+carCount.get(n, 0) 
    for key, val in carCount.items():
        hashm[val].append(key)
    for i in range(len(nums), 0, -1):
        for j in hashm[i]:
            ans.append(j)
            k-=1
            if k == 0:
                return ans

        