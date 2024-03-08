from collections import defaultdict

def fastGroupAnagrams(strs: List[str]) -> List[List[str]]:
    d=defaultdict(list)
    for i, s in enumerate(strs):
        d[tuple(sorted(s))].append(s)
    return d.values()

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    if len(strs)<2: return [strs]
    temp = {}
    for s in strs:
        words = [0]*26

        for i in s:
            words[ ord(i) - ord('a')]+=1
        if tuple(words) not in temp:
            temp[tuple(words)] = [s]
        else:
            temp[tuple(words)].append(s)
    return temp.values()