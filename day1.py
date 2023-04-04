# https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 머쓱이보다 키 큰 사람

# 문제설명
# 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다.
# 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때,
# 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 1 ≤ array의 길이 ≤ 100
# 1 ≤ height ≤ 200
# 1 ≤ array의 원소 ≤ 200

# 먼저 친구들의 키와 머쓱이의 키 비교하기

def solution(array, height):
    answer = 0
    for a in array:
        a > height
    return answer

# 머쓱이보다 키 큰 사람 수 세기


def solution(array, height):
    answer = 0
    for a in array:
        if a > height:
            answer += 1
    return answer


# ---------------------------------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 삼각형의 완성조건 (1)

# 문제 설명
# 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.
# - 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# 삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다.
# 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# sides의 원소는 자연수입니다.
# sides의 길이는 3입니다.
# 1 ≤ sides의 원소 ≤ 1,000

# 가장 긴 변의 길이 구하기
def solution(sides):
    answer = 0
    a = max(sides)
    return answer

# 다른 두 변의 길이의 합구하기


def solution(sides):
    answer = 0
    a = max(sides)
    sides.remove(a)
    sum_list = sum(sides)
    return answer

# 삼각형 조건 비교하기


def solution(sides):
    answer = 0
    a = max(sides)
    sides.remove(a)
    sum_list = sum(sides)
    if a < sum_list:
        answer = 1
    else:
        answer = 2
    return answer


# ---------------------------------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/120887
# k의 개수

# 문제 설명
# 1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다.
# 정수 i, j, k가 매개변수로 주어질 때,
# i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.

# 제한 사항
# 1 ≤ i < j ≤ 100,000
# 0 ≤ k ≤ 9

# i부터 j까지의 숫자 만들기
range(i, j+1)

# 숫자 내의 k 개수 확인하기
answer = 0
for a in range(i. j+1):
    if str(k) in str(a):
        answer += 1
# 이렇게 하면 11과 같은 수의 개수가 세어지지 않는다.

# 반복문을 한번 더 사용하여 숫자를 나눠서 확인하기
answer = 0
for a in range(i, j+1):
    for b in str(a):
        if str(k) == b:
            answer += 1

# 최종 함수


def solution(i, j, k):
    answer = 0
    for a in range(i, j+1):
        for b in str(a):
            if str(k) == b:
                answer += 1
    return answer


# ---------------------------------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/120910
# 세균 증식

# 문제 설명
# 어떤 세균은 1시간에 두배만큼 증식한다고 합니다.
# 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때
# t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

# 제한 사항
# 1 ≤ n ≤ 10
# 1 ≤ t ≤ 15

# 곱하자
def solution(n, t):
    answer = n*2**t
    return answer


# ---------------------------------------------------------
