# https://school.programmers.co.kr/learn/courses/30/lessons/12945
# 피보나치 수
# 문제 설명
# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
# 예를들어
# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
# 와 같이 이어집니다.
# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
# 제한 사항
# n은 2 이상 100,000 이하인 자연수입니다.

# 재귀함수 이용해서 풀어보기
def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return F(n-1) + F(n-2)


# 메모이제이션: 자꾸만 반복되지만 그 결과값은 변하지 않는 작은 문제들의 결과값을 저장하는 것
dic = {}  # n이 0과 1일 때의 결과값은 정해져 있으니 미리 dic에 저장


def F(n):
    if n in dic:  # 이미 결과값이 존재한다면 불러오기
        return dic[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        dic[n] = F(n-1)+F(n-2)  # n의 값을 저장
        return dic[n]


# 오잉 안된다 지금 생각해보면 결국 또 함수를 동작시키니까 위랑 똑같은건가...
# +위의 피드백을 받은 결과 dic을 인자로 넣어줘서 dic이 뭔지 인식되게 해주어야한다고 한다.
dic = {}


def F(n, dic):
    if n in dic:  # 이미 결과값이 존재한다면 불러오기
        return dic[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        dic[n] = F(n-1, dic)+F(n-2, dic)  # n의 값을 저장
        return dic[n]


# 최대한 함수안에서 함수가 실행이 안되도록 해보자


def F(n):
    dic = {0: 0, 1: 1}
    for i in range(2, n+1):
        dic[i] = dic[i-1]+dic[i-2]
    return dic[n]

# 왜 틀렸는지 알겠다..문제를 똑바로 안본 죄 n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수를 만들어야한다.

# 최종함수


def solution(n):
    dic = {0: 0, 1: 1}
    for i in range(2, n+1):
        dic[i] = dic[i-1]+dic[i-2]
    return dic[n] % 1234567
