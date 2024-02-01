# https://school.programmers.co.kr/learn/courses/30/lessons/160586
# 대충 만든 자판
# 문제 설명
# 휴대폰의 자판은 컴퓨터 키보드 자판과는 다르게 하나의 키에 여러 개의 문자가 할당될 수 있습니다. 키 하나에 여러 문자가 할당된 경우, 동일한 키를 연속해서 빠르게 누르면 할당된 순서대로 문자가 바뀝니다.
# 예를 들어, 1번 키에 "A", "B", "C" 순서대로 문자가 할당되어 있다면 1번 키를 한 번 누르면 "A", 두 번 누르면 "B", 세 번 누르면 "C"가 되는 식입니다.
# 같은 규칙을 적용해 아무렇게나 만든 휴대폰 자판이 있습니다. 이 휴대폰 자판은 키의 개수가 1개부터 최대 100개까지 있을 수 있으며, 특정 키를 눌렀을 때 입력되는 문자들도 무작위로 배열되어 있습니다. 또, 같은 문자가 자판 전체에 여러 번 할당된 경우도 있고, 키 하나에 같은 문자가 여러 번 할당된 경우도 있습니다. 심지어 아예 할당되지 않은 경우도 있습니다. 따라서 몇몇 문자열은 작성할 수 없을 수도 있습니다.
# 이 휴대폰 자판을 이용해 특정 문자열을 작성할 때, 키를 최소 몇 번 눌러야 그 문자열을 작성할 수 있는지 알아보고자 합니다.
# 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열배열 keymap과 입력하려는 문자열들이 담긴 문자열 배열 targets가 주어질 때, 각 문자열을 작성하기 위해 키를 최소 몇 번씩 눌러야 하는지 순서대로 배열에 담아 return 하는 solution 함수를 완성해 주세요.
# 단, 목표 문자열을 작성할 수 없을 때는 -1을 저장합니다.
# 제한사항
# 1 ≤ keymap의 길이 ≤ 100
# 1 ≤ keymap의 원소의 길이 ≤ 100
# keymap[i]는 i + 1번 키를 눌렀을 때 순서대로 바뀌는 문자를 의미합니다.
# 예를 들어 keymap[0] = "ABACD" 인 경우 1번 키를 한 번 누르면 A, 두 번 누르면 B, 세 번 누르면 A 가 됩니다.
# keymap의 원소의 길이는 서로 다를 수 있습니다.
# keymap의 원소는 알파벳 대문자로만 이루어져 있습니다.
# 1 ≤ targets의 길이 ≤ 100
# 1 ≤ targets의 원소의 길이 ≤ 100
# targets의 원소는 알파벳 대문자로만 이루어져 있습니다.

# 키맵에서 입력해야 할 문자가 어느 배열에 몇번째에 있는 지 파악하고 최소 입력수를 골라 세면 되지 않을까?

keymap = ["AGZ", "BSSS"]
targets = ["ASA", "BGZ"]

answer = []
# 타겟들 각각 살펴보기
for target in targets:
    # 하나의 타겟을 입력하는 횟수
    check = 0
    # 타겟의 글자별로 확인하기
    for a in target:
        # 글자가 키맵에서 어디 있는지 확인하기
        key_check = []
        for k in keymap:
            if a in k:
                key_check.append(k.index(a))
            else:
                # 키맵에 존재하지 않을 경우, 큰 수를 입력해 작은 인덱스 값을 얻게 하기.
                key_check.append(101)
        # 키맵 어디에도 글자가 없다면 -1
        if all(i == 101 for i in key_check):
            check = -1
            break
        # 있다면 작은 값 더해주기
        else:
            check += min(key_check)+1

    answer.append(check)

print(answer)


# 최종 함수
def solution(keymap, targets):
    answer = []
    for target in targets:
        check = 0
        for a in target:
            key_check = []
            for k in keymap:
                if a in k:
                    key_check.append(k.index(a))
                else:
                    key_check.append(101)
            if all(i == 101 for i in key_check):
                check = -1
                break
            else:
                check += min(key_check)+1

        answer.append(check)
    return answer


# 삼중 for문으로 구성되어 있어서 조금 빠르게 할 수 없나 고민하다가 keymap같은 경우는 딕셔너리로 인덱스 값을 정리해 놓으면 좋을 것 같다는 생각이 들었다.
keymap = ["AGZ", "BSSS"]
targets = ["ASA", "BGZ"]

# keymap 딕셔너리에 알파벳과 최소 인덱션 값 정리하기
keys = {}
for k in keymap:
    for i, w in enumerate(k):
        if w in keys:
            keys[w] = min(i+1, keys[w])
        else:
            keys[w] = i+1

# 타겟 입력 횟수 확인하기
push_num = []
for target in targets:
    push = 0
    for t in target:
        if t in keys:
            push += keys[t]
        else:
            push = -1
            break
    push_num.append(push)


# 최최종 함수
# 삼중 반복문을 해제해 주니 속도가 확실히 빨라졌다.
def solution(keymap, targets):
    keys = {}
    for k in keymap:
        for i, w in enumerate(k):
            if w in keys:
                keys[w] = min(i+1, keys[w])
            else:
                keys[w] = i+1
    answer = []
    for target in targets:
        push = 0
        for t in target:
            if t in keys:
                push += keys[t]
            else:
                push = -1
                break
        answer.append(push)
    return answer
