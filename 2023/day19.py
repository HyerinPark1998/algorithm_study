# https://www.acmicpc.net/problem/25206
# 너의 평점은
# 문제
# 인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!
# 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.
# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
# 인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.
# P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다. 과연 치훈이는 무사히 졸업할 수 있을까?
# 입력
# 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.
# 출력
# 치훈이의 전공평점을 출력한다.
# 정답과의 절대오차 또는 상대오차가 10^{-4} 이하이면 정답으로 인정한다.

# 전공평점 = (과목별 (학점 x 과목평점)의 합) / (학점의 총합)
# 입력마다 과목, 학점, 등급으로 분류 -> 등급에 따른 과목평점은 딕셔너리로 정의해서 가져오기
score = {'A+': 4.5,
         'A0': 4.0,
         'B+': 3.5,
         'B0': 3.0,
         'C+': 2.5,
         'C0': 2.0,
         'D+': 1.5,
         'D0': 1.0,
         'F': 0.0
         }
points = []
grades = []
# 학점과 등급을 과목별로 같은 인덱스를 가진 다른 리스트에 넣기
for i in range(20):
    subject, point, grade = input().split()
    if grade == 'P':
        pass
    else:
        points.append(float(point))
        grades.append(score[grade])

# 계산하기! 아 그냥 리스트를 계산한 리스트로 정리해 보자!
# 리스트는 (과목별 (학점 x 과목평점)), (학점)으로 총 두개를 만들겠다.
point_grade = []
point_list = []
for i in range(20):
    subject, point, grade = input().split()
    # 등급이 P인 과목은 계산에서 제외
    if grade == 'P':
        pass
    else:
        # 각각 계산 후 리스트에 추가
        point_grade.append(score[grade]*float(point))
        point_list.append(float(point))
# 전공평점 = (과목별 (학점 x 과목평점)의 합) / (학점의 총합) 구하기
avg = sum(point_grade)/sum(point_list)
print(avg)


# ----------------------------------
# https://www.acmicpc.net/problem/2738
# 행렬 덧셈
# 문제
# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
# 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
# 출력
# 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

# N*M 크기의 행렬 input 값 받기/ N개의 줄에 원소 개수가 M
N, M = map(int, input().split())
# 각각의 행렬 리스트를 만든 다음 같은 인덱스끼리 더해주자
A = []
B = []

# 두개의 행렬 받기
for i in range(2):
    if i == 0:
        # M만큼의 리스트 받기
        for y in range(N):
            x_list = list(map(int, input().split()))
            A.append(x_list)
    else:
        for y in range(N):
            x_list = list(map(int, input().split()))
            B.append(x_list)

# 행렬이 만들어졌으면 더해주자
sum_list = []
for i in range(N):
    x_list = []
    for n in range(M):
        x = A[i][n] + B[i][n]
        x_list.append(x)
    sum_list.append(x_list)

# 이제 행렬에 맞춰서 프린트해주자
for i in range(N):
    print(' '.join(map(str, sum_list[i])))
