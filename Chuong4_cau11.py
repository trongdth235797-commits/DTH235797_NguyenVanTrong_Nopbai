# trường hợp 1 : sum1 5,sum2 5,sum3 0
# trường hợp 2 : sum1 5,sum2 5,sum3 5
# trường hợp 3 : sum1 5,sum2 5,sum3 0
def  sum1(n):
    s=0
    while n>0:
        s+=1
        n-=1
    return s
def sum2():
    global Val
    s=0
    while Val>0:
        s+=1
        Val-=1
    return s
def sum3():
    s=0
    for i in range(Val,0,-1,):
        s+=1
    return s
def main():
    global Val
    Val=5
    print(sum1(5))
    print(sum3())
    print(sum2())
main()