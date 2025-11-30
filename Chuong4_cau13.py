def tong_uoc(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong
def so_hoan_thien(n):
    if n<=0:
        return False
    return tong_uoc(n) == n
def so_thịnhvong(n):
    if n<=0:
        return False
    return tong_uoc(tong_uoc(n)) > n 
n=int(input("Nhập n: "))
if so_hoan_thien(n):
    print(f"{n} là số hoàn thiện")
elif so_thịnhvong(n):
    print(f"{n} là số thịnh vượng")
else:
    print(f"{n} không phải số hoàn thiện và không phải số thịnh vượng")
