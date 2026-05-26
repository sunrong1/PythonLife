from typing import List

"""
回溯法
1more
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
            # 数字到字母的映射
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        # path is the digits's letter
        n = len(digits)
        ret  = []
        path =[]
        def trackback(i):
            # result collect
            if i== n:
                ret.append("".join(path))
                return 
            for c in mapping[digits[i]]:
                path.append(c)
                trackback(i+1)
                path.pop()
        trackback(0)
        return ret


s = Solution()
print(s.letterCombinations("23"))
