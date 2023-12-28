# https://school.programmers.co.kr/learn/courses/30/lessons/120585
# n의 배수 고르기

#문제 설명
# 정수 n과 정수 배열 numlist가 매개변수로 주어질 때,
# numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

# 제한 사항
# 1 ≤ n ≤ 10,000
# 1 ≤ numlist의 크기 ≤ 100
# 1 ≤ numlist의 원소 ≤ 100,000

# n의 배수를 먼저 구하자
num % n == 0

# numlist에서 n의 배수 판별 후 리스트화
answer = []
for num in numlist:
    if num % n == 0:
        answer.append(num)



# 최종 함수
def solution(n, numlist):
    answer = []
    for num in numlist:
        if num % n == 0:
            answer.append(num)
    return answer



# ---------------------------------------------------------
# 2차원으로 만들기

# 문제 설명
# 정수 배열 num_list와 정수 n이 매개변수로 주어집니다.
# num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.
# num_list가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 n이 2이므로
# num_list를 2 * 4 배열로 다음과 같이 변경합니다.
# 2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.
# num_list  [1, 2, 3, 4, 5, 6, 7, 8]
# num  2
# result  [[1, 2], [3, 4], [5, 6], [7, 8]]

# 제한 사항
# num_list의 길이는 n의 배 수개입니다.
# 0 ≤ num_list의 길이 ≤ 150
# 2 ≤ n < num_list의 길이

# 최종 함수
def solution(num_list, n):
    answer = []                 # 빈 리스트 생성
    for i in range(len(num_list)):      # 생성할 안쪽 리스트의 개수(반복문을 한번 돌때마다 한개의 안쪽 리스트가 만들어진다)
        if i % n == 0:                  # 조건문으로 안쪽 리스트가 n의 배수만큼 생기도록 한다.
            n_list = []                 # 안쪽 리스트로 사용할 빈 리스트 생성
            for a in range(n):          # n만큼의 요소를 갖는 안쪽 리스트 생성
                n_list.append(num_list[i+a]) # 인덱스와 반복문을 이용하여 리스트의 순서대로 요소가 될 수 있도록 한다.
            answer.append(n_list)       # 안쪽 리스트에 n만큼의 요소를 다 채웠으면 전체 리스트에 추가



# ---------------------------------------------------------
# 캐릭터의 좌표

# 문제 설명
# 머쓱이는 RPG게임을 하고 있습니다. 게임에는 up, down, left, right 방향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다.
# 예를 들어 [0,0]에서 up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다.
# 머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다.
# 캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.
# [0, 0]은 board의 정 중앙에 위치합니다. 예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지 오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.

# 제한 사항
# board은 [가로 크기, 세로 크기] 형태로 주어집니다.
# board의 가로 크기와 세로 크기는 홀수입니다.
# board의 크기를 벗어난 방향키 입력은 무시합니다.
# 0 ≤ keyinput의 길이 ≤ 50
# 1 ≤ board[0] ≤ 99
# 1 ≤ board[1] ≤ 99
# keyinput은 항상 up, down, left, right만 주어집니다.

# 방향키 설정하기
senter = [0,0]
if keyinput == 'up':
    senter[1] += 1
if keyinput == 'down':
    senter[1] -= 1
if keyinput == 'left':
    senter[0] -= 1
if keyinput == 'right':
    senter[0] += 1

# 보드 크기 설정하기
senter = [0,0]
if keyinput == 'up':
    senter[1] = min(senter[1] + 1, board[1]//2)
if keyinput == 'down':
    senter[1] = max(senter[1] - 1, -(board[1]//2))
if keyinput == 'left':
    senter[0] = max(senter[0] - 1, -(board[0]//2))
if keyinput == 'right':
    senter[0] = min(senter[0] + 1, board[0]//2)

# 최종 함수
def solution(keyinput, board):
    senter = [0, 0]
    for a in keyinput:
        if a == 'up':
            senter[1] = min(senter[1] + 1, board[1]//2)
        if a == 'down':
            senter[1] = max(senter[1] - 1, -(board[1]//2))
        if a == 'left':
            senter[0] = max(senter[0] - 1, -(board[0]//2))
        if a == 'right':
            senter[0] = min(senter[0] + 1, board[0]//2)
    return senter



# ---------------------------------------------------------\
# 영어가 싫어요

# 문제 설명
# 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다.
# 문자열 numbers가 매개변수로 주어질 때,
# numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.

# 제한 사항
# numbers는 소문자로만 구성되어 있습니다.
# numbers는 "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" 들이 공백 없이 조합되어 있습니다.
# 1 ≤ numbers의 길이 ≤ 50
# "zero"는 numbers의 맨 앞에 올 수 없습니다.

# 숫자의 영어와 그에 대응하는 숫자를 딕셔너리로 짝짓는다.

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

# 딕셔너리를 반복문을 돌려서 숫자 단어가 포함되어 있으면 그에 대응하는 숫자로 교체해준다.
for num in dic.keys():
    if num in numbers:
        numbers.replace(num,dic[num])


# 최종 함수
def solution(numbers):
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
        if num in numbers:
            numbers.replace(num, dic[num])
    return numbers
