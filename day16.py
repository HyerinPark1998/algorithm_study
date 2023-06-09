# ----------------------------------
# https://www.acmicpc.net/problem/2444
# 별 찍기 -7
# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

N = int(input())

# 별 개수 규칙
1+2*0, 1+2*1, 1+2*2, 1+2*3

# 한줄 한줄 별 찍기

# 점점 늘어나는 구간
for i in range(N):
    print(' '*(N-(i+1)), '*'*(1+2*i), ' '*(N-(i+1)), sep='')
# 다시 줄어드는 구간
for i in range(N-1, 0, -1):
    print(' '*(N-(i)), '*'*(2*i-1), ' '*(N-(i)), sep='')

# 출력 형식이 잘못되었다고 한다... 한번에 프린트가 되어야하나? 뭘까?
# 생각해보니 우선 별이 출력된 뒤에는 빈공간이 딱히 필요하지 않은 것 같아 빼주었다.
for i in range(N):
    print(' '*(N-(i+1)), '*'*(1+2*i), sep='')
for i in range(N-1, 0, -1):
    print(' '*(N-(i)), '*'*(2*i-1), sep='')
# 혹시나 하고 돌렸는데 왜... 됐지? 끝에 빈칸이 출력되서 출력형식이 잘못되었던 걸까...


# ----------------------------------
# https://www.acmicpc.net/problem/10812
# 바구니 순서 바꾸기
# 문제
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 순서대로 적혀져 있다. 바구니는 일렬로 놓여져 있고, 가장 왼쪽 바구니를 1번째 바구니, 그 다음 바구니를 2번째 바구니, ..., 가장 오른쪽 바구니를 N번째 바구니라고 부른다.
# 도현이는 앞으로 M번 바구니의 순서를 회전시키려고 만들려고 한다. 도현이는 바구니의 순서를 회전시킬 때, 순서를 회전시킬 범위를 정하고, 그 범위 안에서 기준이 될 바구니를 선택한다.
# 도현이가 선택한 바구니의 범위가 begin, end이고, 기준이 되는 바구니를 mid라고 했을 때, begin, begin+1, ..., mid-1, mid, mid+1, ..., end-1, end 순서로 되어있는 바구니의 순서를 mid, mid+1, ..., end-1, end, begin, begin+1, ..., mid-1로 바꾸게 된다.
# 바구니의 순서를 어떻게 회전시킬지 주어졌을 때, M번 바구니의 순서를 회전시킨 다음, 바구니에 적혀있는 번호를 가장 왼쪽 바구니부터 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에는 바구니의 순서를 바꾸는 만드는 방법이 주어진다. 방법은 i, j, k로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 회전시키는데, 그 때 기준 바구니는 k번째 바구니라는 뜻이다. (1 ≤ i ≤ k ≤ j ≤ N)
# 도현이는 입력으로 주어진 순서대로 바구니의 순서를 회전시킨다.
# 출력
# 모든 순서를 회전시킨 다음에, 가장 왼쪽에 있는 바구니부터 바구니에 적혀있는 순서를 공백으로 구분해 출력한다.

# 바구니 총 개수: N
# 바구니의 순서가 회전되는 횟수 : M
# 바구니의 순서는 mid를 기준으로 쪼개져 mid 앞부분이 맨 뒤로 향한다.

N, M = map(int, input().split())

# 바구니 늘어놓기
# 리스트로 바구니를 만들어야할까 스트링으로 만들어야할까
# 쪼개야하니까 스트링이면 좀 더 쉬울것 같기도 하고.
# 음 스트링으로 만들어서 인덱싱한 다음에 둘이 순서를 바꿔서 이어붙이면 되지 않을까?

a = ''.join([str(i) for i in range(1, N+1)])


# M만큼 바구니의 순서를 바꾸는 방법 입력받기
for n in range(M):
    i, j, k = map(int, input().split())
    # i부터 j전까지, j부터 k까지 쪼개기
    # 쪼갠 후 위치 바꿔서 붙이기
    a = a[:i]+a[k:j+1]+a[i:k]+a[j:]

# 흠 생각해보니까 문자열이면 두글자 숫자를 구분하지 못한다. 리스트로 바꿀 방법을 고민해보자.
# 그리고 위의 코드를 실행시켰을 때 숫자가 불어난다. 이것도 고쳐야겠다.
# 우선 N만큼 바구니 만들기
buckets = [num for num in range(1, N+1)]

# 바구니가 줄세워 졌으면 다시 순서를 바꿔보자.
# 순서를 바꿀 때 mid기준 앞부분을 뒤로 넣어주면 되는거였다.
for n in range(M):
    i, j, k = map(int, input().split())
    buckets = buckets[:i]+buckets[k:j+1]+buckets[i:k]+buckets[j:]

# 음 이게 바꿔주면서 살짝 인덱스 값에 혼란이 있어서 수정을 거쳐주었다.
for n in range(M):
    i, j, k = map(int, input().split())
    # 바구니는 총 네구역으로 나눠진다.
    # 1~(i-1), i~(k-1), k~j, (j+1)~N -> 1~(i-1), k~j, i~(k-1), (j+1)~N
    buckets = buckets[:i-1]+buckets[k-1:j]+buckets[i-1:k-1]+buckets[j:]

# 최종함수
N, M = map(int, input().split())
buckets = [num for num in range(1, N+1)]
for n in range(M):
    i, j, k = map(int, input().split())
    buckets = buckets[:i-1]+buckets[k-1:j]+buckets[i-1:k-1]+buckets[j:]
print(' '.join(map(str, buckets)))


# ----------------------------------
# https://www.acmicpc.net/problem/10988
# 팰린드롬인지 확인하기
# 문제
# 알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다.
# level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.
# 입력
# 첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.
# 출력
# 첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

# 주어진 단어를 거꾸로 배열한 다음 처음의 받은 값과 비교해본다.
a = input()
b = a[::-1]
if a == b:
    print(1)
else:
    print(0)


# ----------------------------------
# https://www.acmicpc.net/problem/1157
# 단어 공부
# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 대소문자 구분이 없다고 하나 출력이 대문자이니 단어를 대문자로 모두 바꿔준 다음에 카운트해주자
word = input().upper()

# 변환 후에 각 글자들을 카운트 해주자
count = {}
for i in word:
    if count[i]:
        count[i] += 1
    else:
        count[i] = 1

# 카운트 한 글자들을 정렬한 후 가장 큰 값을 가져오자
count_sort = sorted(count.items(), key=lambda x: x[1], reverse=True)
# 가장 많이 사용된 알파벳이 여러 개 존재하는지 확인 후 결과값 출력
if count_sort[0][1] == count_sort[1][1]:
    print('?')
else:
    print(count_sort[0][0])

# 코드를 돌려보니 인덱스에러가 발생하였는데 한글자인 경우의 상황을 정의해 주지 않았다.
# 한글자일때는 그 글자가 출력되도록 조건문을 추가해주겠다.
if len(word) == 1:
    print(word)

# 최종함수
word = input().upper()
if len(word) == 1:
    print(word)
else:
    count = {}
    for i in word:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    count_sort = sorted(count.items(), key=lambda x: x[1], reverse=True)
    if count_sort[0][1] == count_sort[1][1]:
        print('?')
    else:
        print(count_sort[0][0])


# ----------------------------------
# https://www.acmicpc.net/problem/4344
# 평균은 넘겠지
# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# 테스트 케이스 개수
C = int(input())

# 케이스마다 입력 받기
for i in range(C):
    students = list(map(int, input().split()))
    # 케이스마다 평균 구하기
    avg = (sum(students)-students[0])/students[0]
    # 평균을 넘는 학생 수 구하기
    count = 0
    for a in range(1, students[0]+1):
        if students[a] > avg:
            count += 1
    # 평균을 넘는 학생들의 비율 구하기
    result = count/students[0]*100
    # 반올림하여 소수점 셋째 자리까지 출력
    print(round(result, 3)+'%')
