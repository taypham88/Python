# Design a Class that:
# insert values no duplicates
# delete value
# get random

import random

class Data:

    def __init__(self):
        self.data = []
        self.map = {}

    def insert(self, data):
        if data in self.map.values():
            return
        else:
            self.data.append(data)
            self.map[data] = len(self.data) - 1

    def delete(self, data):
        if data not in self.map: return
        else:
            self.data.pop(self.map[data])
            for k,v in self.map.items():
                if self.map[data] < v:
                    self.map[k] -= 1
            del self.map[data]

    def get_random(self):
        if self.data:
            return print(random.choice(self.data))

    def printing(self): return print(self.data),print(self.map)



deleted_items = [1,5,2]
add_items = [1,2,3,3,3,4,5,5]
test = Data()

for add in add_items:
    test.insert(add)

test.printing()

for item in deleted_items:
    test.delete(item)

test.printing()

test.get_random()