# https://school.programmers.co.kr/learn/courses/30/lessons/120875
# 평행
# 문제 설명
# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.
# 제한사항
# dots의 길이 = 4
# dots의 원소는 [x, y] 형태이며 x, y는 정수입니다.
# 0 ≤ x, y ≤ 100
# 서로 다른 두개 이상의 점이 겹치는 경우는 없습니다.
# 두 직선이 겹치는 경우(일치하는 경우)에도 1을 return 해주세요.
# 임의의 두 점을 이은 직선이 x축 또는 y축과 평행한 경우는 주어지지 않습니다.


dots = [[3, 5], [4, 1], [2, 4], [5, 10]]

'''
1. 평행하다를 어떻게 알수있을까요?
평행은 무한한 선이 안만나는것
기울기가 같다면 평행하다는것!
'''

# 기울기 구하는 방법
# test1 = [1, 4]
# test2 = [9, 2]
# print((test1[1]-test2[1])/(test1[0]-test2[0]))
'''모든선에서 기울기가 같은것 1값 return 없으면 0 return'''

answer = 0
list_a = []
# dots 2개씩 뽑는 모든 경우의 수
for i in range(len(dots)):
    if answer == 1:
        break
    for a in range(i+1, len(dots)):  # i를 제외한 점들과 짝만들기
        # 모든 경우의 수를 통한 기울기 list 만들기
        dy = dots[i][1]-dots[a][1]
        dx = dots[i][0]-dots[a][0]
        if dx == 0:  # 분모가 0일때는 나누기를 할 수 없다
            a = '존재하지않음'
            if a in list_a:
                answer = 1
                break
            else:
                list_a.append(a)
        else:
            a = dy/dx  # 기울기 구하기
            if a in list_a:
                answer = 1
                break
            else:
                list_a.append(a)


# list값에서 겹친거 있는지 확인하여 1혹은 0 return (answer)
if len(list_a) > len(set(list_a)):
    answer = 1
else:
    answer = 0

print(answer)


# 최종함수
def solution(dots):
    answer = 0
    list_a = []
    for i in range(len(dots)):
        for a in range(i+1, len(dots)):
            dy = dots[i][1]-dots[a][1]
            dx = dots[i][0]-dots[a][0]
            if dx == 0:
                a = '존재하지않음'
                if a in list_a:
                    answer = 1
                    return answer
                else:
                    list_a.append(a)
            else:
                a = dy/dx
                if a in list_a:
                    answer = 1
                    return answer
                else:
                    list_a.append(a)
    return answer


# 하지만 테스트 12번부터 통과를 못했다. 왜그럴까 왤까 검색해보니 경우의 수가 각각 한번씩 짝지어지는게 아니라 총 세가지의 경라고 한다.
# 점 A, 점 B, 점 C, 점 D가 있으면 [A-B, A-C, A-D, B-C, B-D, C-D]가 아니라
# [A-B,C-D],[A-C,B-D],[A-D,B-C]이렇게 세가지경우로 각 경우에서 각자 비교해야한다는것이다.
# 다 짝지어서 한번에 비교하는게 아니라. 그래서 다시 경우의 수를 만들어보았다.


answer = 0
# 한가지 점만 돌아가면서 짝지으면 세가지 경우의 수가 나오기에 한 점을 빼고 반복문을 돌린다.
for i in range(len(dots)-1):
    list_a = []  # 반복문이 돌때마다 비교할 수 있는 리스틀 만들어준다
    dy = dots[i][1] - dots[-1][1]  # 첫번째 선분의 기울기를 계산한다
    dx = dots[i][0] - dots[-1][0]
    if dx == 0:
        list_a.append('X')
    else:
        b = dy/dx
        list_a.append(b)
    a = dots[:]  # 첫번째 선분의 점들을 제외한 후 두번째 선분의 기울기를 구한다.
    a.remove(dots[i])
    a.remove(dots[-1])
    a_dy = a[0][1] - a[-1][1]
    a_dx = a[0][0] - a[-1][0]
    if a_dx == 0:
        X = 'X'
        if X in list_a:  # 리스트 안에 이미 같은 값이 존재한다면 1을 리턴한다.
            answer = 1
            print('1', answer)
            # return answer
    else:
        b = a_dy/a_dx
        if b in list_a:
            answer = 1
            print('1', answer)
            # return answer


# 최종함수
def solution(dots):
    answer = 0
    for i in range(len(dots)-1):
        list_a = []
        dy = dots[i][1] - dots[-1][1]
        dx = dots[i][0] - dots[-1][0]
        if dx == 0:
            list_a.append('X')
        else:
            b = dy/dx
            list_a.append(b)
        a = dots[:]
        a.remove(dots[i])
        a.remove(dots[-1])
        a_dy = a[0][1] - a[-1][1]
        a_dx = a[0][0] - a[-1][0]
        if a_dx == 0:
            X = 'X'
            if X in list_a:
                answer = 1
                return answer
        else:
            b = a_dy/a_dx
            if b in list_a:
                answer = 1
                return answer
    return answer


# dots는 리스트다. 다른 풀이들을 살펴보면서 리스트를 순서대로 변수에 집어넣을 수 있다는 것을 알았다.
a = [1, 2]
A, B = a
# A=1, B=2 가 된다. 리스트안의 리스트가 있어도 마찬가지이다.
b = [[1, 2], [3, 4]]
C, D = b
# C=[1,2],D=[3,4]가 된다 C,D뿐 아니라 [a1,b1],[a2,b2]형식으로 값을 지정할 수도 있다.


# ----------------------------------
# https://www.acmicpc.net/problem/2675
# 문자열 반복
# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다.
# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

T = int(input())
for i in range(T):
    R, S = input().split()
    result = ''
    for i in S:  # 반복문으로 각각의 문자들을 뽑아
        result += i*int(R)  # R만큼 반복해서 result에 넣어준다

    print(result)


# ----------------------------------
# https://www.acmicpc.net/problem/1152
# 단어의 개수
# 문제
# 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
# 입력
# 첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열은 공백으로 시작하거나 끝날 수 있다.
# 출력
# 첫째 줄에 단어의 개수를 출력한다.

S = list(input().split())
print(len(S))


# ----------------------------------
# https://www.acmicpc.net/problem/2908
# 상수
# 문제
# 상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다.
# 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.
# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
# 출력
# 첫째 줄에 상수의 대답을 출력한다.

# 상수는 수를 거꾸로 읽는다.
A, B = input().split()
# 먼저 거꾸로 읽어보자
a = A[::-1]
b = B[::-1]
# 슬라이싱은 int 타입은 받지 않으므로 str타입인 채로 거꾸로 읽어주자
# 큰 수를 비교할 때는 int로 바꿔주자
max_num = max(int(a), int(b))
print(max_num)


# ----------------------------------
# https://www.acmicpc.net/problem/5622
# 다이얼
# 문제
# 상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다.
# 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.
# 출력
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

# 가장가까운 숫자 1을 걸려면 총 2초, 1보다 큰수들은 한 칸마다 +1
# 영어를 키값으로 숫자를 밸류값으로 가진 딕셔너리를 만든 다음

dic_a = {' ': '1',
         'A': '2', 'B': '2', 'C': '2',
         'D': '3', 'E': '3', 'F': '3',
         'G': '4', 'H': '4', 'I': '4',
         'J': '5', 'K': '5', 'L': '5',
         'M': '6', 'N': '6', 'O': '6',
         'P': '7', 'Q': '7', 'R': '7', 'S': '7',
         'T': '8', 'U': '8', 'V': '8',
         'W': '9', 'X': '9', 'Y': '9', 'Z': '9',
         'OPERATOR': '0',
         }

S = input()
time = 0
for a in S:  # 입력된 영어에 해당하는 번호를 가지고 온 후 걸리는 시간을 측정하자
    num = dic_a[a]
    time += (int(num)+1)

print(time)


# ----------------------------------
# https://www.acmicpc.net/problem/11718
# 그대로 출력하기
# 문제
# 입력 받은 대로 출력하는 프로그램을 작성하시오.
# 입력
# 입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다.
# 각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.
# 출력
# 입력받은 그대로 출력한다.

while True:
    try:
        S = input()
        print(S)
    except:
        break
