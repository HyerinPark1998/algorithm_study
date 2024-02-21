# https://school.programmers.co.kr/learn/courses/30/lessons/12951
# JadenCase 문자열 만들기
# 문제 설명
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
# 제한 조건
# s는 길이 1 이상 200 이하인 문자열입니다.
# s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
# 숫자는 단어의 첫 문자로만 나옵니다.
# 숫자로만 이루어진 단어는 없습니다.
# 공백문자가 연속해서 나올 수 있습니다.

from collections import Counter
s = '3abc   c   i'
# 첫글자를 문자인지 숫자인지 판단한 후 숫자면 그대로 두고 문자면 대문자로 바꾼후 나버지는 소문자로 만들어주기.

# 문자열 나누기
arr = s.split()

# 첫글자 확인하기
for i, a in enumerate(arr):
    if a[0].isdigit():
        arr[i] = a.lower()
    else:
        arr[i] = a[0].upper()+a[1:].lower()

print(' '.join(arr))

# 제출을 했더니 몇몇 케이스를 통과하지 못했다. 문제를 보고 생각하는데 공백문자가 연속해서 나올수 있다는 말이 걸렸다.
# 혹시 공백문자가 연속해서 나왔을 때 연속한 그대로 반환이 안되어서 그런건 아닐까.
# 그렇다면 split을 쓰면 안될 것 같다.

# 그래서 for문으로 돌다가 전문자가 공백이면 대문자로 바꿔주게 다시 로직을 작성해보겠다.
for i, a in enumerate(s):
    # 첫글자는 무조건 upper를 해주겠다.
    if i == 0:
        s.replace(a, a.upper(), 1)
    elif s[i-1] == ' ':
        s.replace(a, a.upper(), 1)

# replace로 변환하려다 보니 인덱스값으로 변환이 어려워 리스트로 변환 후 인덱스값으로 바꿔주겠다.
list_s = list(s)

for i, a in enumerate(list_s):
    if i == 0:
        list_s[i] = a.upper()
    elif list_s[i-1] == ' ':
        list_s[i] = a.upper()
    else:
        list_s[i] = a.lower()

print(list_s)
print(''.join(map(str, list_s)))


# 최종 함수
def solution(s):
    list_s = list(s)

    for i, a in enumerate(list_s):
        if i == 0:
            list_s[i] = a.upper()
        elif list_s[i-1] == ' ':
            list_s[i] = a.upper()
        else:
            list_s[i] = a.lower()
    return ''.join(map(str, list_s))

# 제출 후 다른 사람 풀이를 보니 title 내장 함수가 존재했다. title은 문자열의 단어 앞글자를 대문자로 바꿔준다.
# 후에 조건이 바뀌면서 문제를 통과시킬 순 없지만 새로운 함수를 배웠다.


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/12924
# 숫자의 표현
# 문제 설명
# Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.
# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15
# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.
# 제한사항
# n은 10,000 이하의 자연수 입니다.

# 반복문으로 하나씩 더해보자...
n = 15

# 자기 자신의 경우 추가
check = 1
while range(n):
    sum = 0
    for i in range(1, n):
        sum += i
    if sum == n:
        check += 1
        continue
    if sum == n:
        continue

# 역시나 시간이 오래걸린다. 다시 풀어보는 걸로..

# 지금 보니 코드가 뭔가 이상하다 내가 의도한 대로 안된것 같다.
# 반복문으로 하나씩 더해갔을 때 시작점을 매번 달라지게 해야할것 같다.
check = 1
start = 1
while True:
    sum = 0
    for i in range(start, n):
        sum += i
    if sum == n:
        check += 1
        start += 1
        continue
    elif sum > n:
        start += 1
        continue
    if start >= n:
        break

# 시간이 계속 오래걸려서 이중 for문으로 바꿔보겠다.


# if문을 안쪽에 넣었어야했는데 위치를 잘못 했던것 같다.
# 최종함수
def solution(n):
    check = 1
    for j in range(1, n):
        sum = 0
        for i in range(j, n):
            sum += i
            if sum == n:
                check += 1
                continue
            elif sum > n:
                break
    return check


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 귤 고르기
# 문제 설명
# 경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다. 그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.
# 예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 경화가 귤 6개를 판매하고 싶다면, 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.
# 경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
# 제한사항
# 1 ≤ k ≤ tangerine의 길이 ≤ 100,000
# 1 ≤ tangerine의 원소 ≤ 10,000,000


def solution(k, tangerine):
    # 크기 별로 각각 몇개 있는지 파악하기
    sizes = {}
    for s in tangerine:
        if s in sizes:
            sizes[s] += 1
        else:
            sizes[s] = 1
    # 개수가 많은것부터 상자에 담기
    sorted_sizes = dict(
        sorted(sizes.items(), key=lambda item: item[1], reverse=True))
    box = []
    for key, v in sorted_sizes.items():
        box.extend(key for i in range(v))
    box = set(box[:k])
    return len(box)


# counter 활용하기
def solution(k, tangerine):
    # 크기 별로 각각 몇개 있는지 파악하기
    sizes = Counter(tangerine)
    # 개수가 많은것부터 상자에 담기
    sorted_sizes = dict(
        sorted(sizes.items(), key=lambda item: item[1], reverse=True))
    box = []
    for key, v in sorted_sizes.items():
        box.extend(key for i in range(v))
    box = set(box[:k])
    return len(box)

# 어떤 크기의 귤이 담겼는지 중요한게 아니기 때문에 k값에서 많이 가지고 있는 귤 크기의 개수를 빼주면 박스를 채울 수 있다.


def solution(k, tangerine):
    answer = 0
    # 크기 별로 각각 몇개 있는지 파악하기
    sizes = Counter(tangerine)
    for v in sorted(sizes.values(), reverse=True):
        # 개수가 많은 크기부터 한번에 상자에 담기
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer
