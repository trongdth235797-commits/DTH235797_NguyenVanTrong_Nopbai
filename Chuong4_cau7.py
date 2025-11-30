# tính độ dài AB
import math
def do_dai_AB(xA, yA, xB, yB):
    return math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
xA = float(input("Nhập hoành độ điểm A: "))
yA = float(input("Nhập tung độ điểm A: "))
xB = float(input("Nhập hoành độ điểm B: "))
yB = float(input("Nhập tung độ điểm B: "))
print("Độ dài đoạn AB là:", round(do_dai_AB(xA, yA, xB, yB), 2))