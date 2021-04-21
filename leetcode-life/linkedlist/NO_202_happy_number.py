class Solution:

    def isHappy(self, n: int) -> bool:
        """
        方法1：辅助循环链表，典型的数学证明题，需要证明，他不会无线扩大，要么到1，要么在其他的数上循环
        快乐数：每个位置的平方和=1
        :param n:
        :return: 是否快乐数
        """
        # 关键确定Set集合，判断是否出现了重复数字
        numset = set()
        while n != 1 and n not in numset:
            numset.add(n)
            n = self.getNext(n)

        return n == 1

    def getNext(self, num):
        sum = 0
        while num > 0:
            num, mod = divmod(num, 10)
            sum += mod ** 2
        # print(sum)
        return sum


s = Solution()
s.isHappy(19)
