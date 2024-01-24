# https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 두 개 뽑아서 더하기
# 문제 설명
# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# numbers의 길이는 2 이상 100 이하입니다.
# numbers의 모든 수는 0 이상 100 이하입니다.

import itertools
numbers = [2, 1, 3, 4, 1]
answer = []
# 서로 다른 두개의 수를 뽑아 더하기
ncr = list(itertools.combinations(numbers, 2))
for n in ncr:
    answer.append(sum(n))

# 중복 제거하기
answer = list(set(answer))

# 오름차순
answer.sort()


# 최종 함수
def solution(numbers):
    answer = []
    ncr = list(itertools.combinations(numbers, 2))
    for n in ncr:
        answer.append(sum(n))
    answer = list(set(answer))
    answer.sort()
    return answer


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/17682
# [1차] 다트 게임
# 문제 설명
# 다트 게임은 총 3번의 기회로 구성된다.
# 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
# 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.
# 입력 형식
# "점수|보너스|[옵션]"으로 이루어진 문자열 3세트.
# 예) 1S2D*3T
# 제한사항
# 점수는 0에서 10 사이의 정수이다.
# 보너스는 S, D, T 중 하나이다.
# 옵선은 *이나 # 중 하나이며, 없을 수도 있다.

# 3번의 기회로 구성, 한 기회당 0~10점을 얻음.
# S = n**1, D = n**2, T = n**3
# 스타상(*) = i-1*2, i*2, 중첩 될 수 있다.
# 아차상(#) = n*-1

# 세개의 점수를 담은 리스트를 만든 후 총점수 반환하기
dartResult = '1S*2T*3S'

# 숫자를 기준으로 각각의 기회를 구분하기
heart = 0
score = []
bonus = {'S': 1, 'D': 2, 'T': 3}
for n in dartResult:
    # n이 숫자일시 스코어에 기록하기, 기회 체크
    if n.isdigit():
        score.append(int(n))
        heart += 1
    # 숫자가 아닐 경우 보너스인지, 옵션인지 구분하기
    else:
        # 보너스이면 해당하는 값을 찾아 계산하기
        if n in bonus:
            score[-1] **= bonus[n]
        # 옵션일때 스타상, 아차상에 따라 계산해주기
        else:
            # 스타상일 때 점수 계산
            if n == '*':
                # 해당점수 2배
                score[heart-1] *= 2
                # 이전 인덱스 존재한다면 2배
                if len(score) > 1:
                    score[heart-2] *= 2
            else:
                score[heart-1] *= -1

# 문제가 발생하였다. 숫자를 한글자 한글자 떼다 보니 10을 인식 못하는 경우가 발생하였다. 처음에 숫자를 분리하는 작업을 다시해야할까. 지금 이 코드에서 보완해서 구분할 순 없을까?
# 인덱스를 이용하여 바로 앞 인덱스의 문자도 숫자일시 10으로 기록되게 코드를 바꿔보겠다.

for i, n in enumerate(dartResult):
    # n이 숫자일시 스코어에 기록하기, 기회 체크
    if n.isdigit():
        # 만약 바로 앞의 문자가 숫자면 10이므로 확인 후 기록하기
        if dartResult[i-1].isdigit():
            score[-1] = 10
        score.append(int(n))
        heart += 1
    # 숫자가 아닐 경우 보너스인지, 옵션인지 구분하기
    else:
        # 보너스이면 해당하는 값을 찾아 계산하기
        if n in bonus:
            score[-1] **= bonus[n]
        # 옵션일때 스타상, 아차상에 따라 계산해주기
        else:
            # 스타상일 때 점수 계산
            if n == '*':
                # 해당점수 2배
                score[heart-1] *= 2
                # 이전 인덱스 존재한다면 2배
                if len(score) > 1:
                    score[heart-2] *= 2
            else:
                score[heart-1] *= -1

# 10을 인식하게 제출했을 때 몇몇 문제가 실패했다. 어떤 부분을 놓쳤는지 문제를 다시 읽어봐야겠다.
# 옵션도 딕셔너리로 추가해서 코드를 조금 간결하게 바꿔보겠다.


# 최종 함수
def solution(dartResult):
    score = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'*': 2, '#': -1}
    for i, n in enumerate(dartResult):
        if n.isdigit():
            if dartResult[i-1].isdigit():
                score[-1] = 10
            else:
                score.append(int(n))
        else:
            if n in bonus:
                score[-1] **= bonus[n]

            else:
                if n == '*' and len(score) > 1:
                    score[-2] *= 2
                score[-1] *= option[n]
    return sum(score)


# ----------------------------------
