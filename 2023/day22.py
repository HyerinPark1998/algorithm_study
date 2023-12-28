# https://www.acmicpc.net/problem/2720
# 세탁소 사장 동혁
# 문제
# 미국으로 유학간 동혁이는 세탁소를 운영하고 있다. 동혁이는 최근에 아르바이트로 고등학생 리암을 채용했다.
# 동혁이는 리암에게 실망했다. 리암은 거스름돈을 주는 것을 자꾸 실수한다. 심지어 $0.5달러를 줘야하는 경우에 거스름돈으로 $5달러를 주는것이다!
# 어쩔수 없이 뛰어난 코딩 실력을 발휘해 리암을 도와주는 프로그램을 작성하려고 하지만, 디아블로를 하느라 코딩할 시간이 없어서 이 문제를 읽고 있는 여러분이 대신 해주어야 한다.
# 거스름돈의 액수가 주어지면 리암이 줘야할 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성하시오.
# 거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다. 예를 들어, $1.24를 거슬러 주어야 한다면, 손님은 4쿼터, 2다임, 0니켈, 4페니를 받게 된다.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 거스름돈 C를 나타내는 정수 하나로 이루어져 있다. C의 단위는 센트이다. (1달러 = 100센트) (1<=C<=500)
# 출력
# 각 테스트케이스에 대해 필요한 쿼터의 개수, 다임의 개수, 니켈의 개수, 페니의 개수를 공백으로 구분하여 출력한다.

# 손님이 받는 동전의 개수를 최소로 거스름돈을 돌려주는 것! 뭔가 개미군단 문제가 떠오른다. 개미군단은 각 계급의 수를 더한 결과를 원했다면 이건 각각의 값만 도출하면 되는 정도의 차이?!
# 쿼터(Quarter, $0.25), 다임(Dime, $0.10), 니켈(Nickel, $0.05), 페니(Penny, $0.01)
# C의 단위는 센트면 쿼터 = 25센트, 다음 = 10센트, 니켈 = 5센트, 페니 = 1센트

# 테스트 개수 입력 받기
T = int(input())

# 결과 리스트
result_list = []

for i in range(T):
    # 거스름돈 입력 받기
    C = int(input())
    # 거스름돈 구하기
    result = [C//25, (C % 25)//10, (C % 25 % 10)//5, (C % 25 % 10 % 5)]
    result_list.append(result)

# 결과 출력
for i in range(T):
    print(' '.join(map(str, result_list[i])))


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/12950
# 행렬의 덧셈
# 문제
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

# 인덱스값 받아서 같은 위치에 있는 값 더해주자
arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]
answer = []

for x in arr1:
    a = [arr1[x][y]+arr2[x][y] for y in range(len(arr1[x]))]
    answer.append(a)


# 최종함수
def solution(arr1, arr2):
    answer = []

    for x in range(len(arr1)):
        a = [arr1[x][y]+arr2[x][y] for y in range(len(arr1[x]))]
        answer.append(a)
    return answer

# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/42748
# k번째 수
# 문제 설명
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면 array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다. 2에서 나온 배열의 3번째 숫자는 5입니다.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
# 제한 사항
# array의 길이는 1 이상 100 이하입니다.
# array의 각 원소는 1 이상 100 이하입니다.
# commands의 길이는 1 이상 50 이하입니다.
# commands의 각 원소는 길이가 3입니다.


# i~j까지 자르고 정렬한 후 k번째 숫자 알아내기
# commands의 원소[i,j,k] 당 숫자 계산 후 리턴하기
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []

for i in commands:
    # i부터 j까지 자르고 정렬하기
    a = sorted(array[i[0]-1:i[1]])
    # k번째 숫자 구하기
    answer.append(a[i[2]-1])
print(answer)


# 최종함수
def solution(array, commands):
    answer = []
    for i in commands:
        a = sorted(array[i[0]-1:i[1]])
        answer.append(a[i[2]-1])
    return answer


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/81301
# 숫자 문자열과 영단어
# 문제
# 네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.
# 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

# 숫자와 그에 대응하는 영어를 딕셔너리 형식으로 정리해 주고 문자열에서 해당 단어를 숫자로 리플레이스 시켜준다.
dic = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}

s = "2three45sixseven"
for num in dic.keys():
    if num in s:
        # 리플레이스는 문자열만 가능
        s = s.replace(num, str(dic[num]))


# 최종함수
def solution(s):
    dic = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }

    for num in dic.keys():
        if num in s:
            s = s.replace(num, str(dic[num]))
    return int(s)
