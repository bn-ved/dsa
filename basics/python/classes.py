class MyClass:
    # Constructor
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)

    # "self" keyword is required in params
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()


myObj = MyClass([1, 2, 4])
print(myObj.getLength())
print(myObj.getDoubleLength())
