# https://school.programmers.co.kr/learn/courses/30/lessons/142086
# 가장 가까운 같은 글자
# 문제 설명
# 문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알고 싶습니다.
# 예를 들어, s="banana"라고 할 때,  각 글자들을 왼쪽부터 오른쪽으로 읽어 나가면서 다음과 같이 진행할 수 있습니다.
# b는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
# a는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
# n은 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
# a는 자신보다 두 칸 앞에 a가 있습니다. 이는 2로 표현합니다.
# n도 자신보다 두 칸 앞에 n이 있습니다. 이는 2로 표현합니다.
# a는 자신보다 두 칸, 네 칸 앞에 a가 있습니다. 이 중 가까운 것은 두 칸 앞이고, 이는 2로 표현합니다.
# 따라서 최종 결과물은 [-1, -1, -1, 2, 2, 2]가 됩니다.
# 문자열 s이 주어질 때, 위와 같이 정의된 연산을 수행하는 함수 solution을 완성해주세요.
# 제한사항
# 1 ≤ s의 길이 ≤ 10,000
# s은 영어 소문자로만 이루어져 있습니다.

# s = 문자열
# 앞에 같은 글자가 없으면 -1로 표시, 있으면 가장 가까운 글자와의 거리로 표시

# 각 글자의 인덱스를 기록해야할까?
# 앞에서부터 글자의 인덱스를 기록하면서 같은 글자면 가장 최신 인덱스로 업데이트 하고 기록한 딕셔너리에서 비교하기?

# 예시
s = "foobar"
# 각 문자들의 인덱스를 기록할 딕셔너리
ind = {}
# 결과값 리스트
result = []
# 한글자씩 뜯어보기, 이때 인덱스 정보도 함께
for i, l in enumerate(s):
    # 앞에서 해당 문자가 존재했는지 확인
    if l in ind:
        # 존재한다면 인덱스 비교
        result.append(i-ind[l])
    else:
        # 앞에 같은 글자가 없으면 -1
        result.append(-1)
    # 해당 글자의 가장 가까운 인덱스로 업데이트
    ind[l] = i


def solution(s):
    ind = {}
    answer = []
    for i, l in enumerate(s):
        if l in ind:
            answer.append(i-ind[l])
        else:
            answer.append(-1)
        ind[l] = i
    return answer
