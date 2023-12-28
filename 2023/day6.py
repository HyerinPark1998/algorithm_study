# 백준
import sys

# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

T = int(sys.stdin.readline())

for i in range(1,T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {A+B}')

# --------------------------------
# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

T = int(sys.stdin.readline())

for i in range(1, T+1):
    A,B = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {A} + {B} = {A+B}')

# --------------------------------
# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

N = int(sys.stdin.readline())

for i in range(1, N+1):
    print('*'*i)

# --------------------------------
# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

N = int(input())
for i in range(1, N+1):
    print(' '*(N-i),'*'*i, sep='')

# --------------------------------
# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 입력의 마지막에는 0 두 개가 들어온다.
# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

while True :
    A, B = map(int, input().split())
    if A==0 and B == 0:
        break
    else:
        print(A+B)

# --------------------------------
# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except EOFError:
        break



# 프로그래머스

# OX퀴즈
# 문제 설명
# 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다.
# 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
# 제한사항
# 연산 기호와 숫자 사이는 항상 하나의 공백이 존재합니다. 단 음수를 표시하는 마이너스 기호와 숫자 사이에는 공백이 존재하지 않습니다.
# 1 ≤ quiz의 길이 ≤ 10
# X, Y, Z는 각각 0부터 9까지 숫자로 이루어진 정수를 의미하며, 각 숫자의 맨 앞에 마이너스 기호가 하나 있을 수 있고 이는 음수를 의미합니다.
# X, Y, Z는 0을 제외하고는 0으로 시작하지 않습니다.
# -10,000 ≤ X, Y ≤ 10,000
# -20,000 ≤ Z ≤ 20,000
# [연산자]는 + 와 - 중 하나입니다.


# 문자열을 분리해보자
a = '100 x -100 = 4'
quizs = a.split()

# 분리된 리스트의 0번째, 2번째는 계산해야하는 수, 4번째는 답이다.
# 연산자는 +와 -중 하나이므로 연산자를 구분한 뒤 계산을 해주자.
answer = []
if quizs[1] == '+':
    if int(quizs[0])+int(quizs[2])==int(quizs[4]):
        answer.append('O')
    else:
        answer.append('X')
else:
    if int(quizs[0]) - int(quizs[2]) == int(quizs[4]):
        answer.append('O')
    else:
        answer.append('X')

# 최종함수
def solution(quiz):
    answer = []
    for a in quiz:
        quizs = a.split()
        if quizs[1] == '+':
            if int(quizs[0])+int(quizs[2])==int(quizs[4]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(quizs[0]) - int(quizs[2]) == int(quizs[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer

# --------------------------------
# 문자열 내 마음대로 정렬하기
# 문제 설명
# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
# 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.
# 제한 조건
# strings는 길이 1 이상, 50이하인 배열입니다.
# strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
# strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
# 모든 strings의 원소의 길이는 n보다 큽니다.
# 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.

# 정렬하면 sort, sorted key값을 주어 정렬 기준을 주자
strings.sort(key=lambda x:x[n]) #key에는 정렬을 목적으로 하는 함수를 값으로 넣는다.

# 음 이렇게 돌려보니까 인덱스 n번째 문자가 같을 때 정렬이 제대로 이루어지지 않았다.
# 그럼 먼저 리스트를 사전순으로 정렬한다음에 인덱스n을 기준으로 정렬하면 괜찮지 않을까?
strings.sort()
string.sort(key=lambda x:x[n])

# 테스트 통과~
# 최종함수
def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x:x[n])
    return strings