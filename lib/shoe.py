#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand):
        self.brand = brand

    def cobble(self):
        self._condition = "New"
        print("Your shoe is as good as new!")

    def get_condition(self):
        return self._condition
    
    def set_condition(self, condition):
        self._condition = condition

    condition = property(get_condition, set_condition)