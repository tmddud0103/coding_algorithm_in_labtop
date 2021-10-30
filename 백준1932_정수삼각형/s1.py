import sys
sys.stdin = open('input.txt')

def solution(lentri, triangle):
    for i in range(1, len(triangle)):
        for j in range(0, i+1):
            if j==0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i - 1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j],triangle[i - 1][j-1])
    return max(triangle[-1])

lentri = int(sys.stdin.readline().lstrip())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(lentri)]
print(solution(lentri, triangle))