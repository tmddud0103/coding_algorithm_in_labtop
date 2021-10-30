import sys
sys.stdin = open('input.txt')

def dfs(k, j):
    global n, m, nlist, check, total, temp
    if k == m:
        total.append(temp[:])
        return
    for i in range(0, n):
        if check[i] == 0:
            check[i] = 1
            temp.append(nlist[i])
            dfs(k + 1, i)
            temp.pop()
            check[i] = 0


n, m = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))
check = [0]*n
total = []
temp = []
kk = []

dfs(0, 0)
total = sorted(list(set(list(map(tuple, total)))))
for i in range(len(total)):
    for j in range(m):
        print(total[i][j], end=" ")
    print()
