# 方法一 时间复杂度n*log(n)
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        sum = 0
        for i in range(1, n + 1):
            x = i
            while x != 0:
                if x % 10 == 1:
                    sum += 1
                x = int(x / 10)
        return sum

# 方法二 时间复杂度log(n)
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n == 0:
            return 0
        s = str(n)
        length = len(s)
        if length == 1:
            return 1
        res = pow(10, length - 1)  # 获取当前n的幂级
        firstNumber = int(n / res)
        firstBit = (n % res) + 1 if firstNumber == 1 else res
        otherBit = (length - 1) * firstNumber * int(res / 10)
        return firstBit + otherBit + self.NumberOf1Between1AndN_Solution(n % res)




