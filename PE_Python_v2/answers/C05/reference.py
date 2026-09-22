import math
def arithmetic(a,b):
    return dict(add=a+b, sub=a-b, mul=a*b, div=a/b,
                quot=a//b, rem=a%b, power=a**b)
def floor_tenth(x):
    return math.floor(x*10)/10
