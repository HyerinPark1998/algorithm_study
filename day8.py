# https://school.programmers.co.kr/learn/courses/30/lessons/120866
# 안전지대

# 먼저 폭탄을 찾아보자
# 폭탄은 1인다. 그러므로 1을 찾자
# for문을 돌려서 그 안에 1이 있는지 확인해보자
# 폭탄을 위치를 기준으로 상하좌우대각선은 안전지역이 아니다.

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


bomb = [(1, 1), (-1, -1), (1, -1), (-1, 1),
        (1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]
answer = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 1:
            # 폭탄의 위치는 (i,j)
            # bomb에 폭탄 위치를 넣었을때?더했을때. 보드를 넘어가지 않는 애들만 세자
            for a in bomb:
                # 위험지역 위치를 구했으면 보드안에 존재하는지 확인 후 보드에 표시
                if -1 < a[0]+i < len(board) and -1 < a[1]+j < len(board):
                    if board[a[0]+i][a[1]+j] != 1:
                        board[a[0]+i][a[1]+j] = 2
    # 안전지대 칸 수 확인

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 0:
            answer += 1


# https://www.acmicpc.net/problem/10807
# 백준
# 개수 세기
# 문제
# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다.
# 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.
# 출력
# 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.

# 입력된 값들을 하나씩 돌려 같으면 카운트해보자
N = int(input())
a = list(map(int, input().split()))
v = int(input())
count = 0
for i in a:
    if i == v:
        count += 1

print(count)

# 번외, 카운트 메소드를 써보자!
N = int(input())
a = list(map(int, input().split()))
v = int(input())
a.count(v)
