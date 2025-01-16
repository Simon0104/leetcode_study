from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    tmp = {}
    for s in strs:
        sorted_s = sorted(s)
        key = ''.join(sorted_s)
        if key in tmp:
            tmp[key].append(s)
        else:
            tmp[key] = [s]
    print(tmp.values())

groupAnagrams(["eat","tea","tan","ate","nat","bat"])
