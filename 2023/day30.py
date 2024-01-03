# https://school.programmers.co.kr/learn/courses/30/lessons/135808
# 과일 장수
# 문제 설명
# 과일 장수가 사과 상자를 포장하고 있습니다. 사과는 상태에 따라 1점부터 k점까지의 점수로 분류하며, k점이 최상품의 사과이고 1점이 최하품의 사과입니다. 사과 한 상자의 가격은 다음과 같이 결정됩니다.
# 한 상자에 사과를 m개씩 담아 포장합니다.
# 상자에 담긴 사과 중 가장 낮은 점수가 p (1 ≤ p ≤ k)점인 경우, 사과 한 상자의 가격은 p * m 입니다.
# 과일 장수가 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익을 계산하고자 합니다.(사과는 상자 단위로만 판매하며, 남는 사과는 버립니다)
# 예를 들어, k = 3, m = 4, 사과 7개의 점수가 [1, 2, 3, 1, 2, 3, 1]이라면, 다음과 같이 [2, 3, 2, 3]으로 구성된 사과 상자 1개를 만들어 판매하여 최대 이익을 얻을 수 있습니다.
# (최저 사과 점수) x (한 상자에 담긴 사과 개수) x (상자의 개수) = 2 x 4 x 1 = 8
# 사과의 최대 점수 k, 한 상자에 들어가는 사과의 수 m, 사과들의 점수 score가 주어졌을 때, 과일 장수가 얻을 수 있는 최대 이익을 return하는 solution 함수를 완성해주세요.
# 제한사항
# 3 ≤ k ≤ 9
# 3 ≤ m ≤ 10
# 7 ≤ score의 길이 ≤ 1,000,000
# 1 ≤ score[i] ≤ k
# 이익이 발생하지 않는 경우에는 0을 return 해주세요.

# m = 한 상자에 담긴 사과 개수
# k = 사과 최대 점수
# 상자의 가격 = 가장 낮은 점수 * m
# score = 사과들의 점수
k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]

# 최대 이익
price = 0
# 상자에 가장 높은 사과들 우선으로 채워보자
# 사과들 품질 내림차순으로 변경
score.sort(reverse=True)
# 만들 수 있는 상자 개수
for i in range(len(score)//m):
    # 상자에 사과 담기
    box = score[:m]
    # 담은 사과 없애기
    score = score[m:]
    # 상자 가격 더하기
    price += min(box)*m

# 시간 초과가 발행하였다. 어디서 시간을 많이 잡아먹는 걸까.
# 슬라이싱이 인덱스를 돌면서 자르기 때문에 시간을 잡아먹는다고 한다. 두번이나 실행하니 문제가 생긴 듯 하다.
# 그래서 슬라이싱이 아닌 range를 활용하여 건너뛰어 숫자를 세기로 했다. 담은 사과를 없애는게 아니라 건너뛰어서 박스에 담을 첫 숫자가 i로 오게 하였다.


# 최종 함수
def solution(k, m, score):
    price = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        box = score[i:i+m]
        if len(box) == m:
            price += min(box)*m
    return price

# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/132267
# 콜라 문제
# 문제 설명
# 이 문제는 빈 병 a개를 가져다주면 콜라 b병을 주는 마트가 있을 때, 빈 병 n개를 가져다주면 몇 병을 받을 수 있는지 계산하는 문제입니다.
# 기존 콜라 문제와 마찬가지로, 보유 중인 빈 병이 a개 미만이면, 추가적으로 빈 병을 받을 순 없습니다. 상빈이는 열심히 고심했지만, 일반화된 콜라 문제의 답을 찾을 수 없었습니다. 상빈이를 도와, 일반화된 콜라 문제를 해결하는 프로그램을 만들어 주세요.
# 제한사항
# 1 ≤ b < a ≤ n ≤ 1,000,000
# 정답은 항상 int 범위를 넘지 않게 주어집니다.


a = 2
b = 1
n = 20

# 재귀함수를 이용하면 되지 않을까?


def Cola(a, b, n, left_cola=0):
    # 빈병 n개 있을 때 받는 병의 개수
    cola = n//a
    # 나머지가 있을 경우 저장하기.
    left_cola += n % 1
    # 만약 남은 콜라가 a개수라면
    if left_cola % a == 0:
        cola += left_cola//a
    return Cola(a, b, cola, left_cola)+cola


# 시간이 너무 오래걸린다 재귀함수말고 while문으로 돌려보자.
dic = {'cola': n, 'left_cola': 0, 'total': 0}

while True:
    # 빈병 n개 있을 때 받는 병의 개수
    dic['cola'] = n//a
    # 나머지가 있을 경우
    dic['left_cola'] += n % 1
    # 만약 남은 콜라가 a개수라면
    if dic['left_cola'] % a == 0:
        dic['cola'] += dic['left_cola']//a
    # 받은 콜라 총개수
    dic['total'] += dic['cola']

    if dic['cola'] < a:
        break

# 이것도 시간이 오래걸린다 아예 다른 방향으로 알아봐야겠다. 딕셔너리를 사용하지 말아보자. 조금만 더 간결하게 도전.
total = 0
# a병을 바꾸기 위한 n의 최소 개수
while n >= a:
    # 빈병 n개 있을 때 받는 병의 개수
    new_cola = n//a*b
    # 나머지가 있을 경우
    left_cola = n % a
    # 받은 병의 총 개수
    total += new_cola
    # 현재 가지고 있는 콜라의 개수
    n = new_cola + left_cola


# 최종 함수
def solution(a, b, n):
    total = 0
    while n >= a:
        new_cola = n//a*b
        left_cola = n % a
        total += new_cola
        n = new_cola + left_cola
    return total


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/12922
# 수박수박수박수박수박수?
# 문제 설명
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
# 제한 조건
# n은 길이 10,000이하인 자연수입니다.

# 최종 함수
def solution(n):
    if n % 2 == 0:
        return '수박'*(n//2)
    else:
        return '수'+'박수'*(n//2)
