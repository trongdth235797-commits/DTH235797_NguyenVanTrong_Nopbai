import math
n=int(input("nhập n:"))
s=0
for i in range(n):
    s =math.sqrt(2+s)
print("kết quả là:",round(s,2))