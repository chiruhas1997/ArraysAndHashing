#bad memory complexity
def longestConsecutive1(nums: List[int]) -> int:
    if nums==[]:return 0
    max_val = max(nums)
    min_val = min(nums)
    min_val*=-1

    hashm = [ 0 for _ in range(max_val+1+min_val)]
    for n in nums:
        hashm[n+min_val] = 1

    cons, temp = 0, 0
    for i in hashm:
        if i==1:
            temp+=1
        else:
            if cons<temp:
                cons=temp
            temp=0
    if cons<temp:
        cons=temp
    return cons


def longestConsecutive( nums: List[int]) -> int:
    num_set = set(nums)
    seq,temp = 0,0
    for i in num_set:
        j = i
        if i-1 not in num_set:
            temp=1
            while j+1 in num_set:
                temp+=1
                j+=1
            if seq<temp:seq=temp
    return seq