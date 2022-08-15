class TwoSum:

    def __init__(self):
        self.hashMap = {}
        

    def add(self, number: int) -> None:
        if number in self.hashMap:
            self.hashMap[number] += 1
        else:
            self.hashMap[number] = 1
        

    def find(self, value: int) -> bool:
        for val in self.hashMap.keys():
            diff = value - val
            
            if diff in self.hashMap:
                if diff == val:
                    if self.hashMap[diff] > 1:
                        return True
                    
                else:
                    return True
            
        
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)