# https://school.programmers.co.kr/learn/courses/30/lessons/12953?language=python3
# N개의 최소공배수
# 문제 설명
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
# 제한 사항
# arr은 길이 1이상, 15이하인 배열입니다.
# arr의 원소는 100 이하인 자연수입니다.

# 각각 두원소씩 짝지어서 최소공배수를 구해나가면 되지 않을까?
# 최소공배수는 두수의 곱//최대공약수와 같다.

# 최대공약수 구하는 함수
from itertools import combinations
import math


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


arr = [2, 6, 8, 14]


# 최소공배수 구하는 함수
def lcd(a, b):
    return (a*b)//gcd(a, b)


# arr의 두 원소의 최소공배수를 토너먼트 형식으로 구해나가면 되지 않을까?
gcd_arr = []
for i in range(1, len(arr)):
    gcd_arr.append(lcd(arr[i], arr[i-1]))

# 기존 arr의 최소공배수를 담은 gcd_arr을 계속 이용해서 최소공배수를 구하고 싶다.
# 최소공배수를 구한 수는 없애주고 새로운 최소 공배수를 넣어주는 형식으로 리스트를 사용하려고 한다.
while True:
    if len(arr) == 1:
        break
    for i in range(1, len(arr)):
        arr.append(lcd(arr[1], arr[0]))
        arr.pop(0)
    arr.pop(0)


# 최종 함수
def solution(arr):
    while True:
        if len(arr) == 1:
            break
        for i in range(1, len(arr)):
            arr.append(lcd(arr[1], arr[0]))
            arr.pop(0)
        arr.pop(0)
    return arr[0]

# 그런데 다른 풀이를 살펴 보니 앞에서 최대 공배수를 구하고 나온 최대 공배수에 남은 원소들 차례로 구해나가도 되었다. 토너먼트 형식이라면 원소들이 부전승인 형식.


# 수정한 함수
def solution(arr):
    answer = arr[0]
    for i in arr:
        answer = lcd(i, answer)
    return answer


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 짝지어 제거하기
# 문제 설명
# 짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.
# 예를 들어, 문자열 S = baabaa 라면
# b aa baa → bb aa → aa →
# 의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.
# 제한사항
# 문자열의 길이 : 1,000,000이하의 자연수
# 문자열은 모두 소문자로 이루어져 있습니다.

s = 'sbaabaa'
temp = ''
# 2개 붙어있는 문자 자르기
# while True:
#     for i in range(1, len(s)):
#         if s[i] == s[i-1]:
#             s = s[:i-1]+s[i+1:]
#             break
#     if len(s) == 0:
#         print('1')
#         break
#     else:
#         print('2')
#         break


# while문을 돌리면 모두 제거할 수 없는 경우를 어떻게 빼야할지 고민이 된다.
# while문 말고 재귀함수?
def remove_couple(s):
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return remove_couple(s[:i-1]+s[i+1:])
    if len(s) == 0:
        return 1
    else:
        return 0


# 재귀함수는 런타임 에러가 발생한다.

# 리스트를 이용하여 치환해주겠다.
abc = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm',
       'nn', 'oo', 'pp', 'qq', 'rr', 'ss', 'tt', 'uu', 'vv', 'ww', 'xx', 'yy', 'zz']
for w in abc:
    s = s.replace(w, '')

# 정확성 테스트 3,4,5,10, 효율성 테스트 3,4,5를 실패하였다. 왜일까.
# 'stbaabtaas' 이 경우 ss가 남는 상황이 발생했다. 한번 돌고 넘어간 문자는 다시 없애주지 않는다.
for i in range(len(abc)):
    for w in abc:
        s = s.replace(w, '')


# 효율성, 정확성 모두 3,4,5, 실패
# 새로운 코드로 도전하겠다.
temp = []
for w in s:
    if not temp:
        temp.append(w)
    elif temp[-1] == w:
        print(w)
        temp.pop()
    else:
        temp.append(w)
print(temp)
print(0) if temp else print(1)


# 최종함수
def solution(s):
    temp = []
    for w in s:
        if not temp:
            temp.append(w)
        elif temp[-1] == w:
            temp.pop()
        else:
            temp.append(w)
    return 0 if temp else 1
