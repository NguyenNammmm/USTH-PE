import math
class Grade:
    def __init__(self,value):
        self.value=value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,value):
        if type(value) not in (int,float) or not math.isfinite(value) or not 0<=value<=10:
            raise ValueError("score")
        self._value=value
    def __str__(self):
        return f"Grade({self.value})"
    def __lt__(self,other):
        if not isinstance(other,Grade):
            return NotImplemented
        return self.value<other.value
