# https://www.acmicpc.net/problem/10871
# X보다 작은 수
# 문제
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.\
# 출력
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

N, X = map(int, input().split())
a = list(map(int, input().split()))
a_list = []
for i in a:
    if X > i:
        a_list.append(i)
print(' '.join(map(str, a_list)))
# join은 ''를 원소 사이사이에 넣고 리스트를 문자열로 바꿔준다. 문자열로 바꾸기 때문에 리스트 원소들은 문자여야한다.

# 프린트문의 end=''는 프린트문이 끝나는 부분에 ''를 넣어준다. 기본값은 end='\n'
# 예) print(1,2,end='end') -> 1 2end(그리고개행입력이안되어있어서개행이안된다.)
# sep=''은 여러개의 값을 출력할 때 값들 사이에 들어간다. 기본값은 공백으로 sep=' '
# 예) print(1,2,sep='') -> 12 (공백을 안주었기 때문에 값이 붙어서 나온다)


# ----------------------------------
# https://www.acmicpc.net/problem/10818
# 최소, 최대
# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

N = int(input())
num_list = list(map(int, input().split()))

min_num = min(num_list)
max_num = max(num_list)

print(min_num, max_num)


# ----------------------------------
# https://www.acmicpc.net/problem/2562
# 최댓값
# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

num_list = list(map(int, input()))
max_num = max(num_list)
max_index = num_list.index(max_num)

print(max_num, max_index+1, sep='\n')

# 틀렸다 뭔가 받는 방법에서 잘못된것 같은데 일렬로 입력된 값들은 어떻게 받아야하지? 하나하나 받아서 리스트에 넣어야하나?
num_list = []
# 아홉번째 줄까지 한줄에 하나의 자연수가 입력된다.
for i in range(9):
    num_list.append(int(input()))
# 리스트로 만든다음 처음과 같이 찾아주겠다.
max_num = max(num_list)
max_index = num_list.index(max_num)
print(max_num, max_index+1, sep='\n')


# ----------------------------------
# https://www.acmicpc.net/problem/10810
# 공넣기
# 문제
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다. 가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다
# 도현이는 앞으로 M번 공을 넣으려고 한다. 도현이는 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다. 만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다. 공을 넣을 바구니는 연속되어 있어야 한다.
# 공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다. 각 방법은 세 정수 i j k로 이루어져 있으며, i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다. 예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다. (1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)
# 도현이는 입력으로 주어진 순서대로 공을 넣는다.
# 출력
# 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다. 공이 들어있지 않은 바구니는 0을 출력한다.

# 바구니 개수 = N
# 공 번호 = 1 ~ N
# 공을 넣는 횟수 = M
# i~j번 바구니에 k번 공을 넣자

# 바구니들에 담긴 번호들을 리스트로 만들어서 바꾸면 어떨까
N, M = map(int, input().split())
bucket = [0 for i in range(N)]  # 아무것도 안담겨있으므로 0으로 바구니를 만들어준다

# M만큼 공을 넣는 방법이 주어지므로 M번만큼 인풋을 받고 방법에 맞춰 바구니에 담아준다
for a in range(M):
    i, j, k = map(int, input().split())
    for ball in range(i, j+1):
        bucket[ball] = k

print(' '.join(map(str, bucket)))

# 인덱스에러/ 잠시만 index는 0부터고 i는 1부터 시작한다. 잘 생각해보자 그럼 넣고싶은데 넣으려면 1을 빼줘야한다.
# i가 1일때 0번째에 있는 바구니에 공이 들어갈 수 있도록!
for a in range(M):
    i, j, k = map(int, input().split())
    for ball in range(i-1, j):
        bucket[ball] = k

print(' '.join(map(str, bucket)))


# ----------------------------------
# https://www.acmicpc.net/problem/10813
# 공 바꾸기
# 문제
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.
# 도현이는 앞으로 M번 공을 바꾸려고 한다. 도현이는 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환한다.
# 공을 어떻게 바꿀지가 주어졌을 때, M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다. 각 방법은 두 정수 i j로 이루어져 있으며, i번 바구니와 j번 바구니에 들어있는 공을 교환한다는 뜻이다. (1 ≤ i ≤ j ≤ N)
# 도현이는 입력으로 주어진 순서대로 공을 교환한다.
# 출력
# 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.

# 바구니 개수 = N
# 바구니 번호 = 1 ~ N
# 바구니 안에는 바구니 번호와 같은 번호의 공
# 공을 바꾸는 횟수 = M
# i번 , j번 2개의 바구니에 들어 있는 공 바꾸기

N, M = map(int, input().split())
bucket = [i for i in range(1, N+1)]

for a in range(M):
    i, j = map(int, input().split())
    ball = bucket[i-1]
    bucket[i-1] = bucket[j-1]
    bucket[j-1] = ball

print(' '.join(map(str, bucket)))

# 변수를 선언하지 않고 바꿀 수 있는 방법은 없을까? 검색검색
# 오호 for문에서 위에서부터 차례대로 코드가 실행되므로 나는 변수를 선언해서 변경되지 않은 값을 넣을 수 있게 해주었다.
# 하지만 이걸 한줄에서 실행해버리면 변수를 선언하지 않아도 한번에 바뀌므로 변경되지 않은 값을 바꿀 수 있다.
for a in range(M):
    i, j = map(int, input().split())
    bucket[i-1], bucket[j-1] = bucket[j-1], bucket[i-1]
# A,B = 5, 7 이 가능!


# ----------------------------------
# https://www.acmicpc.net/problem/5597
# 과제안내신분
# 문제
# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.
# 입력
# 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.
# 출력
# 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.

# 학생 수는 30명인데 28명만 과제를 제출했다 제출 안 한 학생을 순서대로 출력하자
student = [i for i in range(1, 31)]

for i in range(28):
    ok = int(input())
    student.remove(ok)

print(*student, sep='\n')


# ----------------------------------
# https://www.acmicpc.net/problem/3052
# 나머지
# 문제
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.
# 출력
# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

# 입력받은 수를 42로 나눈 나머지를 구한다음 중복 없이 숫자 세기
namerge = set()
for i in range(10):
    a = int(input())
    namerge.add(a % 42)

print(len(namerge))


# ----------------------------------
# https://www.acmicpc.net/problem/10811
# 바구니 뒤집기
# 문제
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 순서대로 적혀져 있다. 바구니는 일렬로 놓여져 있고, 가장 왼쪽 바구니를 1번째 바구니, 그 다음 바구니를 2번째 바구니, ..., 가장 오른쪽 바구니를 N번째 바구니라고 부른다.
# 도현이는 앞으로 M번 바구니의 순서를 역순으로 만들려고 한다. 도현이는 한 번 순서를 역순으로 바꿀 때, 순서를 역순으로 만들 범위를 정하고, 그 범위에 들어있는 바구니의 순서를 역순으로 만든다.
# 바구니의 순서를 어떻게 바꿀지 주어졌을 때, M번 바구니의 순서를 역순으로 만든 다음, 바구니에 적혀있는 번호를 가장 왼쪽 바구니부터 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법이 주어진다. 방법은 i j로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만든다는 뜻이다. (1 ≤ i ≤ j ≤ N)
# 도현이는 입력으로 주어진 순서대로 바구니의 순서를 바꾼다.
# 출력
# 모든 순서를 바꾼 다음에, 가장 왼쪽에 있는 바구니부터 바구니에 적혀있는 순서를 공백으로 구분해 출력한다.

# 바구니 개수 = N
# 바구니 번호 = 1 ~ N
# 바구니의 순서를 바꾸는 횟수 = M
# i번 ~ j번 바구니의 순서를 역순으로 만들기
N, M = map(int, input().split())
bucket = [i for i in range(1, N+1)]

for i in range(M):
    i, j = map(int, input().split())
    # 바구니를 뒤집어야한다.. 원하는 구간을 자르고 그걸 뒤집어주면 원하는 구간은 역순이된다.
    bucket[i-1:j][::-1]
    # 원하는 구간을 뒤집었는데 그럼 나머지 구간은 어떻게 붙여줄까
    # 해당이 안되는 구간을 잘라 앞 뒤로 붙여주자
    bucket = bucket[:i-1]+bucket[i-1:j][::-1]+bucket[j:]

print(' '.join(map(str, bucket)))
