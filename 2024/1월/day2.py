# https://school.programmers.co.kr/learn/courses/30/lessons/12977
# 소수 만들기
# 문제 설명
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

# 먼저 주어진 숫자 중 3개를 뽑아서 더한다.
# - 주어진 리스트에서 3개의 원소로 구성된 리스트가 몇개 나올지 구한다음 안겹치게 3개씩 랜덤으로 뽑으면 될까?
# - 그렇게 되면 리스트 중에 중복된 리스트가 존재할 것 같다. 다른 방법은 없을까?
# 소수인지 판별한다.
# 약수는 대칭으로 존재한다. 그렇기에 자기 자신의 숫자에 도달할 때까지 반복문을 실행할 필요가 없다.
# 해당 수의 제곱근까지만 확인하면 된다. 제곱근이 정수로 존재한다면 소수가 아니다. 그러면 확인하는 대상이 적어지면서 시간도 단축시킬 수 있다.
# 제곱근은 math.sqrt로 구할 수 있다.

import math
import itertools
nums = [1, 2, 7, 6, 4]

# intertools의 combinations()를 활용하면 간단하게 조합을 구성할 수 있다.

# 주어진 숫자 중 3개를 뽑아서 더하기
ncr = list(itertools.combinations(nums, 3))
# 소수 개수 확인
count = 0
for n in ncr:
    num = sum(n)
    # 소수 판별하기
    check = True
    # 제곱근이 정수라면 소수가 아니기에 정수가 아닌 숫자만 판별한다.
    if math.sqrt(num) != int:
        # 제곱근까지의 숫자 중 약수가 존재하는지 확인하기.
        for number in range(2, int(math.sqrt(num) + 1)):
            if num % number == 0:
                check = False
                break
        if check:
            count += 1


# 최종 함수
def solution(nums):
    ncr = list(itertools.combinations(nums, 3))
    count = 0
    for n in ncr:
        num = sum(n)
        check = True
        if math.sqrt(num) != int:
            for number in range(2, int(math.sqrt(num) + 1)):
                if num % number == 0:
                    check = False
                    break
            if check:
                count += 1
    return count
