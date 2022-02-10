from tkinter import N


class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        if len(nums) > 0:
            for n in nums:
                self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        if len(nums) > 0:
            for n in nums:
                self.result -= n
        return self

md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)

md.result = 0

y = md.add(2).add(2,5,1).add(4,2,3,6).subtract(3,2).subtract(5,2,1).subtract(9,4,3,1).result
print(y)


