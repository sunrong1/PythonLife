class Solution():
    def mySqrt(self, x: int) -> int:
        """
        
        :param x:
        :return:
        """
        s1 = 0
        s2 = x
        while s2 > s1:
            if s2 - s1 == 1:
                if s2 ** 2 == x:
                    return s2
                else:
                    return s1
            if (s1 + (s2 - s1) // 2) ** 2 == x:
                return s1 + (s2 - s1) // 2
            elif (s1 + (s2 - s1) // 2) ** 2 > x:
                s2 = s1 + (s2 - s1) // 2
            else:
                s1 = s1 + (s2 - s1) // 2
        return s1


s = Solution()
print(s.mySqrt(8))
