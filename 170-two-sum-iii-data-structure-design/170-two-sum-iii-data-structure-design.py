class TwoSum:

    def __init__(self):
        self.array = []
        

    def add(self, number: int) -> None:
        self.array.append(number)
        

    def find(self, value: int) -> bool:
        hashMap = {}
        for i, val in enumerate(self.array):
            diff = value - val
            
            if diff in hashMap:
                return True
            else:
                hashMap[val] = True
            
        
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)