# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length =0
        last_seen ={}

        for right, n in enumerate(s):
            if n in last_seen and last_seen[n] >= left:
                left = last_seen[n] +1

            max_length = max(max_length, right-left +1)
            last_seen[n] = right

        return max_length

# 438. Find All Anagrams in a String
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcounter, scounter = defaultdict(int), defaultdict(int)
        res= []
        for i in range(len(p)):
            pcounter[p[i]] +=1

        for j in range(len(s)):
            scounter[s[j]] +=1
            if j >=len(p):
                if scounter[s[j - len(p)]] ==1:
                    del scounter[s[j -len(p)]]
                else:
                    scounter[s[j -len(p)]] -= 1
            if scounter == pcounter:
                res.append(j - len(p) +1)
        return res

567. Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = defaultdict(int)
        mp2 = defaultdict(int)

        for n in s1:
            mp2[n] += 1

        i, j = 0, 0
        while j <len(s2):
            mp[s2[j]] += 1
            j += 1
            if j - i == len(s1):
                if mp == mp2:
                    return True
                mp[s2[i]] -= 1
                if mp[s2[i]] == 0:
                    del mp[s2[i]]
                i += 1

        return False
