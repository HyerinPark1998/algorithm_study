# https://school.programmers.co.kr/learn/courses/30/lessons/12912
# 두 정수 사이의 합
# 문제 설명
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
# 제한 조건
# a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
# a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
# a와 b의 대소관계는 정해져있지 않습니다.

# a~b 사이의 합을 구하자
a = 3
b = 5

list_a = [i for i in range(a, b+1)]
sum_list = sum(list_a)

# 어라 제한 조건을 다시보니 a와 b의 대소관계는 정해져 있지 않다고 한다.
# 그럼 먼저 둘의 대소관계를 구분해줘야 겠다.

# a와 b가 같은 경우도 있으니 조건문으로 구분해주겠다.
if a == b:
    print(a)
else:
    # 대소관계를 구분한 후 리스트를 만들고 더하자
    max_num = max(a, b)
    min_num = min(a, b)
    num_list = [i for i in range(min_num, max_num+1)]
    sum_list = sum(num_list)
    print(sum_list)

# 최종함수


def solution(a, b):
    if a == b:
        return a
    else:
        max_num = max(a, b)
        min_num = min(a, b)
        num_list = [i for i in range(min_num, max_num+1)]
        sum_list = sum(num_list)
        return sum_list


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 문자열 다루기 기본
# 문제설명
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
# 제한 사항
# s는 길이 1 이상, 길이 8 이하인 문자열입니다.
# s는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.

# 숫자로만 구성되어있다면 int로 변환할 때 오류가 안 뜨니까 try,exept문을 이용하면 되지않을까

try:
    int(s)
    answer = True
except:
    answer = False

# 흠 그런데 테스트 몇몇개가 실패했다 왜그럴까..
# 문제를 다시보는데 숫자로만 구성돼있는지 확인하는게 아니라 길이가 4 혹은 6으로 숫자로만 구성되어있는 지 확인해야하는건가?

# 그럼 먼저 문자열 길이를 판단해 보겠다

if len(s) == 4 or len(s) == 6:
    try:
        int(s)
        answer = True
    except:
        answer = False
else:
    answer = False

# 길이 판단 후에 try문을 돌리니 모든 테스트를 통과하였다.
# 최종함수


def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            return True
        except:
            return False
    else:
        return False


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/86051
# 없는 숫자 더하기
# 문제 설명
# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# 1 ≤ numbers의 길이 ≤ 9
# 0 ≤ numbers의 모든 원소 ≤ 9
# numbers의 모든 원소는 서로 다릅니다.

# 0부터 9까지의 리스트를 만든 후 차집합을 구해 남은 수를 더해주자
num_list = list(range(10))
sum_list = sum(set(num_list)-set(numbers))
