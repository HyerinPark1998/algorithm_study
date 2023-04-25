import string

# https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 베열의 유사도
# 문제 설명
# 두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.
# 제한사항
# 1 ≤ s1, s2의 길이 ≤ 100
# 1 ≤ s1, s2의 원소의 길이 ≤ 10
# s1과 s2의 원소는 알파벳 소문자로만 이루어져 있습니다
# s1과 s2는 각각 중복된 원소를 갖지 않습니다.

# 교집합을 만들고 수 세기


def solution(s1, s2):
    a = set(s1)
    b = set(s2)
    return len(a & b)

# add(값) - 집합에 새로운 값을 추가한다. (중복된 값은 무시)
# remove(값) - 전달받은 값을 삭제 (없을 때 에러 메시지를 출력)
# discard(값) - 전달받은 값을 삭제 (없을 때 그냥 무시)
# pop() - 임의의 값을 리턴하고 삭제
# clear() - 집한에 있는 모든 값을 삭제
# copy() - 집합을 복제하여 리턴
# union() - 합집합을 만들어 리턴
# update() - 합집합을 만들어 원본 데이터를 갱신(수정)
# difference() - 차집합을 만들어 리턴
# difference_update() - 차집합을 만들어 원본 데이터를 갱신
# intersection() - 교집합을 만들어 리턴
# intersection_update() - 교집합을 만들어 원본 데이터를 갱신

# intersection() - 교집합을 만들어 리턴


def solution(s1, s2):
    a = set(s1)
    b = set(s2)
    answer = a.intersection(b)
    return len(answer)


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 숫자 찾기
# 문제 설명
# 정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고
# 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 0 < num < 1,000,000
# 0 ≤ k < 10
# num에 k가 여러 개 있으면 가장 처음 나타나는 자리를 return 합니다.


# 1번째 문자열로 변환 후 포함되어있는지 확인, 포함되어 있다면 인덱스값 반환
def solution(num, k):
    answer = -1
    a = str(num)
    b = str(k)
    if b in a:
        answer = a.index(b)+1
    return answer


# 2번째
def solution(num, k):
    for i, n in enumerate(str(num)):  # 문자열의 각 문자와 해당 문자의 인덱스를 함께 가져옵니다
        if str(k) == n:  # 문자열과 문자열을 비교해야 하기 때문
            return i + 1
    return -1


# ----------------------------------
# https://www.acmicpc.net/problem/1546
# 평균
# 문제
# 세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다.
# 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
# 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다. 둘째 줄에 세준이의 현재 성적이 주어진다.
# 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
# 출력
# 첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.
# 점수 최댓값 = M
# 모든 점수 = 점수/M*100
# 시험 본 과목의 개수 = N
N = int(input())
score = list(map(int, input().split()))
M = max(score)

# 모든 점수를 바꿔주기
for i, s in enumerate(score):
    score[i] = s/M*100

# 평균 구하기
avg = sum(score)/N
print(avg)


# ----------------------------------
# https://www.acmicpc.net/problem/27866
# 문자와 문자열
# 문제
# 단어 S와 정수 i가 주어졌을 때, S의 i번째 글자를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 영어 소문자와 대문자로만 이루어진 단어 S가 주어진다. 단어의 길이는 최대 1000이다.
# 둘째 줄에 정수 i가 주어진다.(1 =< i =< |S|)
# 출력
# S의 i번째 글자를 출력한다.

S = input()
i = int(input())
print(S[i-1])


# ----------------------------------
# https://www.acmicpc.net/problem/2743
# 단어 길이 재기
# 문제
# 알파벳으로만 이루어진 단어를 입력받아, 그 길이를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 영어 소문자와 대문자로만 이루어진 단어가 주어진다. 단어의 길이는 최대 100이다.
# 출력
# 첫째 줄에 입력으로 주어진 단어의 길이를 출력한다.

word = input()
print(len(word))


# ----------------------------------
#
# 문제
# 문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다. 각 테스트 케이스는 한 줄에 하나의 문자열이 주어진다.
# 문자열은 알파벳 A~Z 대문자로 이루어지며 알파벳 사이에 공백은 없으며 문자열의 길이는 1000보다 작다.
# 출력
# 각 테스트 케이스에 대해서 주어진 문자열의 첫 글자와 마지막 글자를 연속하여 출력한다.

T = int(input())

for i in range(T):
    word = input()
    print(word[0:1]+word[-1:])


# ----------------------------------
# https://www.acmicpc.net/problem/9086
# 아스키 코드
# 문제
# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.
# 입력
# 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.
# 출력
# 입력으로 주어진 글자의 아스키 코드 값을 출력한다.

a = input()
print(ord(a))

# ord(str)은 str을 아스키코드값으로 변환
# chr(int)은 아스키 코드값을 알파벳으로 변환


# ----------------------------------
# https://www.acmicpc.net/problem/11720
# 숫자의 합
# 문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
# 출력
# 입력으로 주어진 숫자 N개의 합을 출력한다.

N = int(input())
num = input()
sum_num = 0
for i in num:
    sum_num += int(i)

print(sum_num)


# ----------------------------------
# https://www.acmicpc.net/problem/10809
# 알파벳 찾기
# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

# 알파벳 리스트를 만들고 하나씩 돌면서 인덱스를 넣어주자
# 일일이 만들기 번거로울 때 string 함수를 이용해서 만들어주자 import 필수
# ascii_lowercase=소문자, ascii_uppercase=대문자, ascii_letters=대문자+소문자
lower = [i for i in string.ascii_lowercase]
S = input()

for i in range(len(lower)):  # 리스트의 인덱스로 값을 불러와서 값을 바꿔주자
    if lower[i] in S:
        lower[i] = S.index(lower[i])
    else:
        lower[i] = -1

print(' '.join(map(str, lower)))


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/12948
# 핸드폰 번호 가리기
# 문제 설명
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한
# 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
# 제한 조건
# phone_number는 길이 4 이상, 20이하인 문자열입니다.

# 뒷 4자리를 제외한 모든숫자는 전부*
# 폰넘버 길이에 4를 빼고 나머지는 모두 *로 바꿔주자
phone_number = "01033334444"

# 별로 바꿔야하는 길이
a = len(phone_number)-4

# 바꿔야하는 길이를 잘라 바꿔주기
b = phone_number.replace(phone_number[:a], "*"*a)

# 다른버전으로 바꿔야하는만큼 별을 만든다음에 숫자로 보일부분 붙여주기
answer = "*"*a + phone_number[-4:]
