# https://school.programmers.co.kr/learn/courses/30/lessons/159994
# 카드 뭉치
# 문제 설명
# 코니는 영어 단어가 적힌 카드 뭉치 두 개를 선물로 받았습니다. 코니는 다음과 같은 규칙으로 카드에 적힌 단어들을 사용해 원하는 순서의 단어 배열을 만들 수 있는지 알고 싶습니다.
# 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용합니다.
# 한 번 사용한 카드는 다시 사용할 수 없습니다.
# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.
# 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없습니다.
# 예를 들어 첫 번째 카드 뭉치에 순서대로 ["i", "drink", "water"], 두 번째 카드 뭉치에 순서대로 ["want", "to"]가 적혀있을 때 ["i", "want", "to", "drink", "water"] 순서의 단어 배열을 만들려고 한다면 첫 번째 카드 뭉치에서 "i"를 사용한 후 두 번째 카드 뭉치에서 "want"와 "to"를 사용하고 첫 번째 카드뭉치에 "drink"와 "water"를 차례대로 사용하면 원하는 순서의 단어 배열을 만들 수 있습니다.
# 문자열로 이루어진 배열 cards1, cards2와 원하는 단어 배열 goal이 매개변수로 주어질 때, cards1과 cards2에 적힌 단어들로 goal를 만들 있다면 "Yes"를, 만들 수 없다면 "No"를 return하는 solution 함수를 완성해주세요.
# 제한사항
# 1 ≤ cards1의 길이, cards2의 길이 ≤ 10
# 1 ≤ cards1[i]의 길이, cards2[i]의 길이 ≤ 10
# cards1과 cards2에는 서로 다른 단어만 존재합니다.
# 2 ≤ goal의 길이 ≤ cards1의 길이 + cards2의 길이
# 1 ≤ goal[i]의 길이 ≤ 10
# goal의 원소는 cards1과 cards2의 원소들로만 이루어져 있습니다.
# cards1, cards2, goal의 문자열들은 모두 알파벳 소문자로만 이루어져 있습니다.

# goal에서 각각의 인덱스를 파악한 다음, 카드1,카드2에서 해당하는 단어의 goal 인덱스를 확인 했을 때 오름차순 정렬이면 yes, 아니면 no이지 않을까?
goal = ["i", "want", "to", "drink", "water"]
cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]

# goal의 인덱스 정의하기
goal = {w: i for i, w in enumerate(goal)}
# 카드1, 카드2 인덱스 확인하기
cards1 = [goal[i] for i in cards1]
cards2 = [goal[i] for i in cards2]
if sorted(cards1) == cards1 and sorted(cards2) == cards2:
    print("yes")
else:
    print("no")

# 런타임 에러를 만났다. 인덱스 문제일까..
# 다시 제한 사항을 살펴보니 goal의 길이는 카드1+카드2의 길이를 더한것보다 작을 수 있다고 한다. 그 말은 카드1,2에는 goal에 없는 단어를 포함할 수도 있다는 거 아닐까.
# 카드 1,2를 확인할 때 goal에 없는 경우를 예외처리해서 리스트를 만들어주자
cards1 = [goal[i] if i in goal else 100 for i in cards1]
cards2 = [goal[i] if i in goal else 100 for i in cards2]

# 최종 함수


def solution(cards1, cards2, goal):
    goal = {w: i for i, w in enumerate(goal)}
    cards1 = [goal[i] if i in goal else 100 for i in cards1]
    cards2 = [goal[i] if i in goal else 100 for i in cards2]
    if sorted(cards1) == cards1 and sorted(cards2) == cards2:
        return "Yes"
    else:
        return "No"


# ----------------------------------
# 기초문제 day1 풀기

# 대소문자 바꿔서 출력하기
str = input()
str = [a.upper() if a.islower() else a.lower() for a in str]
print(''.join(str))

# 하지만 이미 대소문자를 상호전환해주는 함수가 있었으니..
input().swapcase()
# swapcase()는 알아서 대문자는 소문자로, 소문자는 대문자로 전환하여 문자열을 반환한다.


# 특수문자 출력
# 일반 스트링을 입력하듯 특수문자를 출력하면 오류가 발생한다. 백슬래시를 특수문자 앞에 붙여 사용할수도 있지만 문장에 특수문자가 많을 땐 스트링값 앞에 r을 붙여주면 된다.
# Raw String은 이스케이프 문자열을 그대로 출력하거나, json, html과 같은 문서에서 특수문자나 태그등을 변환하지 않고 그대로 사용할 때 사용된다.
print(r'!@#$%^&*(\'"<>?:;')
