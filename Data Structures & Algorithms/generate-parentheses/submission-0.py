class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(op, cp, comb):
            if len(comb) == 2 * n:
                ans.append(comb)
                return

            if op < n:
                helper(op+1,cp, comb + '(')

            if cp < op:
                helper(op,cp+1, comb + ')')

        helper(0, 0, '')
        return ans