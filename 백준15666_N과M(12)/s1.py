import sys
sys.stdin = open('input.txt')

def dfs(k, j):
    global n, m, nlist, check, total, temp
    if k == m:
        total.append(temp[:])
        return
    for i in range(j, n):
        temp.append(nlist[i])
        dfs(k + 1, i)
        temp.pop()



n, m = map(int, sys.stdin.readline().split())
nlist = sorted(list(map(int, sys.stdin.readline().split())))
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
