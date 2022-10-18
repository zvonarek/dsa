#Change coin problem DP
def coinChange(n: int) -> list[int]:

    if (n % 25 == 0): return [0,0,int(n/25)]
    if n == 25: return [0,0,1]
    if n == 10: return [0,1,0] 
    if n == 1: return [1,0,0]
    c1 = [0,0,0]
    c2 = [0,0,0]
    c3 = [0,0,0]
    min_c = [0,0,0]
    #case1
    if n > 1:
        c1 = coinChange(n-1)
        c1[0] = c1[0] + 1
        min_s = sum(c1)
        min_c = c1
    #case2
    if n > 10:
        c2 = coinChange(n-10)
        c2[1] = c2[1] + 1
        if min_s > sum(c2):
            min_s=sum(c2)
            min_c=c2
    #case3
    if n > 25:
        c3 = coinChange(n-25)
        c3[2] = c3[2] + 1
        if min_s > sum(c3):
            min_c=c3
    return min_c

print(coinChange(1231))