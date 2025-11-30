# viết chương trinh logxa
import math
def logxa(a, b):
    return math.log(b, a)
a = float(input("Nhập cơ số a: "))
b = float(input("Nhập số b: "))
if a>0 and a!=1 and b>0:
    print("Kết quả loga(b) là:", round(logxa(a, b), 2))
else:
    print("Dữ liệu không hợp lệ")