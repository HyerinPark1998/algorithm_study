# https://school.programmers.co.kr/learn/courses/30/lessons/68935
# 3진법 뒤집기
# 문제 설명
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.

# 3진법 구하기
import math


def base_3(N):
    n = N//3
    num = N % 3
    if n == 0:
        return str(num)
    return base_3(n)+str(num)

# 3진법을 십진법으로 바꾸기


def base_10(N):
    num = N[::-1]
    result = 0
    for i, n in enumerate(num):
        result += int(n)*(3**i)
    return result

# 위 두 함수를 합쳐보자! 앞뒤 반전을 하게 되면 두번이다 돌리는 꼴이 되므로 그 부분도 수정하자


def solution(n):
    num = base_3(n)
    result = 0
    for i, n in enumerate(num):
        result += int(n)*(3**i)
    return result


# ----------------------------------
# 소수 찾기
# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다. (1은 소수가 아닙니다.)
# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.

# 1과 자기 자신으로만 나누어지는 수 이므로 for문으로 돌려서 하나씩 나누어지는지 테스트 하고 다른 숫자로 나누어진다면 패스, 아니라면 카운트
def solution(n):
    count = 0
    # n까지의 숫자 불러오기
    for num in range(2, n+1):
        # 2부터 num까지 나누어지는 숫자 찾기
        for number in range(2, num):
            # 만약 1과 자신을 제외하고 나누어 떨어지는 숫자가 있다면 이 숫자는 제외
            if num % number == 0:
                break
            # 다 돌았는데 나누어 떨어지는 숫자가 없다면 카운트하기
            if number+1 == num:
                count += 1
    # 2는 무조건 소수임으로 추가하기
    return count+1

# 이렇게 풀었는데 시간초과로 실패했다. 좀 더 시간을 단축 시킬 수는 없을까?
# 이 문제는 1과 자신을 제외한 약수의 존재를 판별해야한다. 여기서 간과한 점이 약수는 대칭으로 존재한다. 그렇기에 자기 자신의 숫자에 도달할 때까지 반복문을 실행할 필요가 없다.
# 그럼 어디까지만 확인할 것인가. 해당 수의 제곱근까지만 확인하면 된다. 제곱근이 정수로 존재한다면 소수가 아니다. 그러면 확인하는 대상이 적어지면서 시간도 단축시킬 수 있다.
# 제곱근은 math.sqrt로 구할 수 있다.


def solution(n):
    count = 0
    for num in range(2, n+1):
        # 약수 존재 확인
        check = True
        for number in range(2, int(math.sqrt(num) + 1)):
            if num % number == 0:
                check = False
                break
        if check:
            count += 1
    return count
