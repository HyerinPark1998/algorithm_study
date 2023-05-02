# https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 하샤드 수
# 문제 설명
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
# 제한 조건
# x는 1 이상, 10000 이하인 정수입니다.

# 하샤드 수인지 분별하는 식
# 자릿수를 다 더해야하니까 스트링으로 바꿔서 인자를 다 더해보자
x = 12
sum_num = 0
for i in str(x):
    sum_num += int(i)

# 자릿수 합을 구했으면 x를 합으로 나누었을 때 나누어떨어지는 지 확인하자
print(x % sum_num == 0)

# 최종함수


def solution(x):
    sum_num = 0
    for i in str(x):
        sum_num += int(i)
    return x % sum_num == 0


# 번외) for문을 한줄로 정리할 순 없을까 싶어서 이것저것 도전해봤다
# sum_num += int(i) for i in str(x)
# sum_num += (int(i) for i in str(x))

# 하지만 이렇게 되면 더하기가 되지 않는다
# 그러다 발견한게 sum() 이 함수를 이용해 모든 i들을 더해줄 수 있다.
sum(int(i) for i in str(x))

# 그리고 이걸 return 값에 대입하면


def solution(x):
    return x % sum(int(i) for i in str(x)) == 0

# 나머지가 0이 나오면 True 0이 아니면 False로 반환된다.


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/12910
# 나누어 떨어지는 숫자 배열
# 문제설명
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
# 제한사항
# arr은 자연수를 담은 배열입니다.
# 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
# divisor는 자연수입니다.
# array는 길이 1 이상인 배열입니다.

arr = [2, 36, 1, 3]
divisor = 1
div_list = []

# 먼저 나누어 떨어지는 값을 골라내고 오름차순으로 정렬하자.
for i in arr:
    if i % divisor == 0:
        div_list.append(i)
div_list.sort()

# 그런데 만약 div_list가 비었다면 -1을 반환해야한다.
if not div_list:
    print(-1)

# 최종함수


def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if not answer:
        answer.append(-1)
    return answer


# 번외 리스트 한줄로 표현하기
answer = [i for i in arr if i % divisor == 0]
answer.sort()
if not answer:
    answer.append(-1)

# 새로운 발견
# a or b가 있을 때 or의 앞부분이 참이면 앞부분만, 앞부분이 거짓이면 뒷부분이 나온다.
# 조건문을 사용 할 때는 써봤지만 다른 문법에서도 적용되는 지 처음 알았다.
print(answer or [-1])


# ----------------------------------
# https://www.acmicpc.net/problem/25083
# 새싹
# 아래 예제와 같이 새싹을 출력하시오.

# 따옴표를 출력하고 싶을때는 따옴표 앞에 \를 붙여줘야 한다.
print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \. \". L_r'")
print("   `~\/")
print("      |")
print("      |")


# ----------------------------------
# https://www.acmicpc.net/problem/3003
# 킹, 퀸, 룩, 비숍, 나이트, 폰
# # 문제
# 동혁이는 오래된 창고를 뒤지다가 낡은 체스판과 피스를 발견했다.
# 체스판의 먼지를 털어내고 걸레로 닦으니 그럭저럭 쓸만한 체스판이 되었다. 하지만, 검정색 피스는 모두 있었으나, 흰색 피스는 개수가 올바르지 않았다.
# 체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.
# 동혁이가 발견한 흰색 피스의 개수가 주어졌을 때, 몇 개를 더하거나 빼야 올바른 세트가 되는지 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 동혁이가 찾은 흰색 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수가 주어진다. 이 값은 0보다 크거나 같고 10보다 작거나 같은 정수이다.
# 출력
# 첫째 줄에 입력에서 주어진 순서대로 몇 개의 피스를 더하거나 빼야 되는지를 출력한다. 만약 수가 양수라면 동혁이는 그 개수 만큼 피스를 더해야 하는 것이고, 음수라면 제거해야 하는 것이다.

# 총 16개로 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
# 부족하거나 많은 피스의 개수를 세면 된다.

# 흠 리스트를 이용해서 값들을 비교해볼까?
found = list(map(int, input().split()))
piece = [1, 1, 2, 2, 2, 8]

# 처음엔 크기를 비교한 뒤 더하기빼기를 할까 했지만 더해야할 때는 양수값으로 빼야할 때는 음수로 표현해야했기에 기존 값에서 찾은 값을 빼주었다.
for i in range(len(found)):
    found[i] = piece[i] - found[i]

print(' '.join(map(str, found)))
