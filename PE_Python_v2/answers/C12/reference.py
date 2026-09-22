import math
def classify(text):
    try:
        score=float(text)
    except ValueError:
        return "Invalid"
    if math.isfinite(score) and 0<=score<=10:
        if score>=8:
            return "Gioi"
        elif score>=5:
            return "Dat"
        else:
            return "Chua dat"
    return "Invalid"
def main():
    print(classify(input("Diem: ")))
if __name__=="__main__":
    main()
