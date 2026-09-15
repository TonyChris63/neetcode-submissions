class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        ans = []
        for i in range(k):
            mk = max(freq, key = freq.get)
            ans.append(mk)
            del freq[mk]
        return ans
