from dataclasses import dataclass
from datetime import date
import math
import numpy as np

@dataclass(frozen=True)
class Student:
    sid:str; name:str; dob:str
    def __post_init__(self):
        if not self.sid.strip() or not self.name.strip(): raise ValueError("student")
        date.fromisoformat(self.dob)
    @classmethod
    def input(cls,ask): return cls(ask("ID: "),ask("Ten: "),ask("DoB: "))
    def list(self): return (self.sid,self.name,self.dob)
