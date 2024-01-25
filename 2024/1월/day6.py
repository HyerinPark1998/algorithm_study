# https://school.programmers.co.kr/learn/courses/30/lessons/131128
# 숫자 짝꿍
# 문제 설명
# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.
# 예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
# 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.
# 제한사항
# 3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
# X, Y는 0으로 시작하지 않습니다.
# X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.

# 같은 자리에 같은 숫자들을 찾아낸다.
# 숫자들을 조합해 가장 큰 정수를 만든다.
# 짝꿍이 없다면 -1, 짝꿍이 0으로만 구성되어 있다면 짝궁은 0.
# 문자열로 반환하기.

# X와 Y의 길이는 다를 수 있다. 다르다면 길이가 작은 수를 기준으로 비교를 하면 될것 같다.
X = "100"
Y = "203045"

# 짧은 길이를 기준으로 반복문 돌리기
# 뒤에서부터 자리를 비교하는게 편할 것 같아. 뒤에서부터 비교를 해보겠다.
# 인덱스를 기준으로 같은 인덱스에 해당하는 숫자를 비교후에 저장해두기
common = []
for i in range(-1, -len(min(X, Y))-1, -1):
    # 같은 자리에 있는 숫자 비교하기
    if X[i] == Y[i]:
        common.append(X[i])


# 가장 큰 정수 만들기 값이 없다면 -1 반환하기
answer = ''.join(common) if common else "-1"

# 풀고 있는 중에 문제의 이해를 제대로 못한걸 깨달았다. 같은자리에 같은 숫자가 있어야 하는게 아닌 갯수로 따졌을 때 하나씩 가지고 있으면 되는 거였다.
# 즉 X와 Y가 어떤 숫자들을 몇개 갖고 있는 지 파악하고 짝지으면 되는거였다.
# X의 개수를 딕셔너리로 정리하고 Y의 숫자와 비교해보겠다.
cnt_x = {}
for n in X:
    if n in cnt_x:
        cnt_x[n] += 1
    else:
        cnt_x[n] = 1

# Y의 숫자와 공통 숫자 찾기
couple = []
for n in Y:
    if n in cnt_x:
        # 짝 지을 수 있는 수가 남아 있다면 짝 짓고 리스트에 넣기.
        if cnt_x[n] > 0:
            cnt_x[n] -= 1
            couple.append(n)

# 리스트에 작성된 숫자로 가장 큰 정수 만들기
# 큰 순서로 정렬한 다음 join을 이용해 문자열로 합쳐주기
print(''.join(sorted(couple, reverse=True)) if couple else "-1")

# 0으로만 이루어진 경우는 "0"을 반환해야한다.
# 저번에 배운 all()을 이용하여 0으로만 이루어졌는지 판별해주겠다
if all(n == "0" for n in couple):
    print("0")

# 위의 두 조건을 합치면
if all(n == "0" for n in couple):
    print("0")
else:
    print(''.join(sorted(couple, reverse=True)) if couple else "-1")

# all을 이용하면 리스트가 비어있는 경우도 True가 되어버린다.
# 조건문을 좀 더 섬세하게 할 필요가 있다.
if couple:
    if all(n == "0" for n in couple):
        print("0")
    else:
        print(''.join(sorted(couple, reverse=True)))
else:
    print("-1")


# 최종 함수
def solution(X, Y):
    couple = []
    cnt_x = {}
    for n in X:
        if n in cnt_x:
            cnt_x[n] += 1
        else:
            cnt_x[n] = 1
    for n in Y:
        if n in cnt_x:
            if cnt_x[n] > 0:
                cnt_x[n] -= 1
                couple.append(n)
    if couple:
        if all(n == "0" for n in couple):
            return "0"
        else:
            return ''.join(sorted(couple, reverse=True))
    else:
        return "-1"

# 여담이지만 숫자를 셀 때 딕셔너리 외에도 collection 모듈의 Counter를 이용하여 셀 수도 있다.
# from collections import Counter
# arr = ['a','b','c','dd','b','g','zz','k','k']
# print(Counter(arr))
# Counter({'b': 2, 'k': 2, 'a': 1, 'c': 1, 'dd': 1, 'g': 1, 'zz': 1})
# 이 때 타입은 <class 'collections.Counter'> 이다.
