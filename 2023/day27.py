# https://school.programmers.co.kr/learn/courses/30/lessons/140108
# 문자열 나누기
# 문제 설명
# 문자열 s가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.
# 먼저 첫 글자를 읽습니다. 이 글자를 x라고 합시다.
# 이제 이 문자열을 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다. 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
# s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다. 남은 부분이 없다면 종료합니다.
# 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료합니다.
# 문자열 s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 분해한 문자열의 개수를 return 하는 함수 solution을 완성하세요.
# 제한사항
# 1 ≤ s의 길이 ≤ 10,000
# s는 영어 소문자로만 이루어져 있습니다.

# 비교할 첫글자 x를 등록 -> 다음 글자와 비교 -> x와 x가 아닌 다른 글자들이 나온 횟수 계산 -> 같아지면 cnt +1 및 첫글자 재등록(이미 계산된 문자 삭제) -> 반복 -> 남은 부분이 없다면 종료

s = "abracadabra"
# 분해한 문자열 개수
cnt = 0
for i in range(len(s)):
    # x의 개수
    cnt_x = 0
    # x가 아닌 글자의 개수
    cnt_y = 0
    # 문자열 읽기
    for i in range(len(s)):
        # 첫글자 x
        x = s[0]
        # 다음 글자와 비교하기
        if x == s[i]:
            cnt_x += 1
        else:
            cnt_y += 1
        if cnt_x == cnt_y:
            cnt += 1
            s = s[i+1:]
            break
    if cnt_x != cnt_y:
        cnt += 1
        break


def solution(s):
    cnt = 0
    for i in range(len(s)):
        cnt_x = 0
        cnt_y = 0
        for i in range(len(s)):
            x = s[0]
            if x == s[i]:
                cnt_x += 1
            else:
                cnt_y += 1
            if cnt_x == cnt_y:
                cnt += 1
                s = s[i+1:]
                break
        if cnt_x != cnt_y:
            cnt += 1
            break
    return cnt

# 이중반복문을 사용하는데 반복문을 사용하지 않고도 풀 수 있는 지 고민해봐야겠다.


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/70128
# 내적
# 문제 설명
# 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.
# 이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)
# 제한사항
# a, b의 길이는 1 이상 1,000 이하입니다.
# a, b의 모든 수는 -1,000 이상 1,000 이하입니다.

# 길이는 같으니 길이만큼 for문을 돌려서 더해나가면 되지 않을까?
a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]

answer = 0
for i in range(len(a)):
    answer += a[i]*b[i]

# 이 외의 답변들을 확인하니 zip을 이용하여 원소 두개를 뽑아 곱한 후 합을 구하면 한줄 정리가 된다. 세상엔 똑똑한 사람이 많다..
