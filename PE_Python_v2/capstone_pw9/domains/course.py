from dataclasses import dataclass
from datetime import date
import math
import numpy as np

@dataclass(frozen=True)
class Course:
    cid:str; name:str; credits:int
    def __post_init__(self):
        if not self.cid.strip() or not self.name.strip() or type(self.credits) is not int or self.credits<=0: raise ValueError("course")
    @classmethod
    def input(cls,ask): return cls(ask("Ma: "),ask("Ten: "),int(ask("Tin chi: ")))
    def list(self): return (self.cid,self.name,self.credits)
