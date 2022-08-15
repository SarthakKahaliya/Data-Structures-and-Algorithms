class TwoSum:

    def __init__(self):
        self.array = []
        self.hashMap = {}
        

    def add(self, number: int) -> None:
        self.array.append(number)
        self.hashMap[number] = len(self.array) - 1
        

    def find(self, value: int) -> bool:
        for i, val in enumerate(self.array):
            diff = value - val
            
            if diff in self.hashMap and self.hashMap[diff] != i:
                
                return True
            
        
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)