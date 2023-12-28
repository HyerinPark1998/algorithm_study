# https://school.programmers.co.kr/learn/courses/30/lessons/12943
# 콜라츠 추측
# 문제
# 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.
# 1-1. 입력된 수가 짝수라면 2로 나눕니다.
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
# 예를 들어, 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다. 위 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성해 주세요.
# 단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.

# 재귀함수 이용? 와일문 이용? 작업 카운트 세기
# 빠져나갈 조건문으로 num값이 1 혹은 작업을 500번 수행했을 때로 설정

# 콜라츠 추측
num = 6
# 짝수일 경우
if num % 2 == 0:
    num = num // 2
# 홀수일 경우
else:
    num = (num * 3)+1


# 재귀함수 이용하기
def collatz(num):
    # num ==1일 때 빠져나가기
    if num == 1:
        return num
    # 짝수일 경우
    if num % 2 == 0:
        num = num // 2
    # 홀수일 경우
    else:
        num = (num * 3)+1
    return collatz(num)


# 몇번 반복하는지 갯수 세기
def collatz(num, count=0):
    # num ==1일 때 빠져나가기
    if num == 1:
        return count
    # 작업을 500번 수행했을 때 빠져나가기
    if count == 500:
        return -1
    # 짝수일 경우
    if num % 2 == 0:
        count += 1
        num = num // 2
    # 홀수일 경우
    else:
        num = (num * 3)+1
        count += 1
    return collatz(num, count)


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/82612
# 부족한 금액 계산하기
# 문제 설명
# 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요. 단, 금액이 부족하지 않으면 0을 return 하세요.
# 제한사항
# 놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
# 처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
# 놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수

# price = 이용료, count = 놀이기구 이용 횟수 및 이용료 배수, money = 소지 금액
# 처음 이용료가 100(price)이었다면 2(count)번째에는 200, 3(count)번째에는 300으로 요금이 인상

# 먼저 놀이기구를 count번 탔을 때 이용료 계산하기
total = 0
for i in range(1, count+1):
    total += price*i

# 금액 비교하기
# 이용금액이 소지 금액보다 클때
if total > money:
    result = total - money
# 금액이 부족하지 않을 때
else:
    result = 0


# 최종함수
def solution(price, money, count):
    total = 0
    for i in range(1, count+1):
        total += price*i
    if total > money:
        return total - money
    else:
        return 0
