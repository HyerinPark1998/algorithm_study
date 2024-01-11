# 기초문제 공부
# 리스트 모든 원소들의 곱을 구하는 법

import math
from functools import reduce
num_list = [3, 4, 5, 2, 1]


# 기본적인 구현
def multiply(num_list):
    ans = 1
    for n in num_list:
        if n == 0:
            return 0
        ans *= n
    return ans


# reduce를 통한 방법
# 함수형 프로그래밍(functional programming)에는 fold라는 개념이 있다. fold는 재귀적인 자료구조를 원소들을 반복적으로 처리해 하나의 결과값으로 반환하는 기능이다.
# 파이썬에서는 이 기능을 functools모듈의 reduce라는 함수로 지원하고 있다.
# 사용 예시, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
# 람다식을 이용하여 계산식을 수정할 수 있다.


def reduce_multiply(num_list):
    return reduce(lambda x, y: x*y, num_list)  # ((((1*2)*3)*4)*5)


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/136798
# 기사단원의 무기
# 문제 설명
# 숫자나라 기사단의 각 기사에게는 1번부터 number까지 번호가 지정되어 있습니다. 기사들은 무기점에서 무기를 구매하려고 합니다.
# 각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매하려 합니다. 단, 이웃나라와의 협약에 의해 공격력의 제한수치를 정하고, 제한수치보다 큰 공격력을 가진 무기를 구매해야 하는 기사는 협약기관에서 정한 공격력을 가지는 무기를 구매해야 합니다.
# 예를 들어, 15번으로 지정된 기사단원은 15의 약수가 1, 3, 5, 15로 4개 이므로, 공격력이 4인 무기를 구매합니다. 만약, 이웃나라와의 협약으로 정해진 공격력의 제한수치가 3이고 제한수치를 초과한 기사가 사용할 무기의 공격력이 2라면, 15번으로 지정된 기사단원은 무기점에서 공격력이 2인 무기를 구매합니다. 무기를 만들 때, 무기의 공격력 1당 1kg의 철이 필요합니다. 그래서 무기점에서 무기를 모두 만들기 위해 필요한 철의 무게를 미리 계산하려 합니다.
# 기사단원의 수를 나타내는 정수 number와 이웃나라와 협약으로 정해진 공격력의 제한수치를 나타내는 정수 limit와 제한수치를 초과한 기사가 사용할 무기의 공격력을 나타내는 정수 power가 주어졌을 때, 무기점의 주인이 무기를 모두 만들기 위해 필요한 철의 무게를 return 하는 solution 함수를 완성하시오.

# 제한사항
# 1 ≤ number ≤ 100,000
# 2 ≤ limit ≤ 100
# 1 ≤ power ≤ limit

# 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기 구매 하지만 제한수치보다 큰 무기는 구매불가하고 대신 정해진 공격력을 가진 무기를 구매.
# 공격력 1 = 1kg
# number = 기사단원 수
# limit = 공격력 제한 수치
# power = 제한 수치 초과한 기사가 사용할 무기의 공격력
# return 기사단원들의 무기를 만들기 위한 철의 무게

number = 5
limit = 3
power = 2

# 1. 각 기사단원의 약수 구하기
# 2. 약수 개수를 토대로 제한수치와 비교하며 구매할 수 있는 공격력 확인

# 계속해서 풀어왔지만 약수는 짝수로 이루어져 있다. 그렇기에 제곱근까지의 숫자로 약수 개수를 파악할 수 있다.
# 총 철의 무게
total = 1
# 각 기사단원들의 약수 판별하기
# number가 1일 때는 늘 약수가 1개 이므로 1이후로 약수 개수 파악하기
if number != 1:
    for num in range(2, number+1):
        # 한 기사단원의 약수 개수 파악하기
        count = 0
        for n in range(1, int(math.sqrt(num) + 1)):
            # n이 num의 약수일 때
            if num % n == 0:
                count += 1
                # n이 제곱근이 아니라면 n의 짝도 세주기
                if n**2 != num:
                    count += 1
        # 기사단원의 공격력이 제한수치를 넘지 않는 지 확인하기
        total += count if count <= limit else power


# 최종 함수


def solution(number, limit, power):
    total = 1
    if number != 1:
        for num in range(2, number+1):
            count = 0
            for n in range(1, int(math.sqrt(num) + 1)):
                if num % n == 0:
                    count += 1
                    if n**2 != num:
                        count += 1
            total += count if count <= limit else power
    return total
