class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + '`'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        curr = ""

        while i < len(s):
            if s[i] == '`':
                res.append(curr)
                curr = ""
                i += 1
            else:
                curr += s[i]
                i += 1
        return res