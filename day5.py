# 백준
import sys
# 구구단

n = input()
for i in range(1,10):
    print(f'{n} * {i} = {n*i}')



# A+B-3
# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

T = int(input())
for i in range(1, T+1):
    A, B = map(int, input().split())
    print(A+B)



# 합
# 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
# 출력
# 1부터 n까지 합을 출력한다.

n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)



# 영수증
# 문제
# 준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다.
# 정말 멋졌다. 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다!
# 준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.
# 영수증에 적힌,
# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액
# 을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.
# 입력
# 첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
# 이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.
# 출력
# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 일치하지 않는다면 No를 출력한다.

X = int(input())
N = int(input())
total = 0
for i in range(N):
    a,b = map(int,input().split())
    c = a*b
    total += c
if total == X:
    print('Yes')
else:
    print('No')

# 코딩은 체육과목 입니다
# 문제
# 요약) 혜아가 면접에서 코드를 작성하였다. 코드를 본 면접관은 다음 질문을 했다.
# "만약. 입출력이 N바이트 크기의 정수라면 프로그램을 어덯게 구현해야 할까요?"
# long int는 4바이트 정수까지 저장할 수 있는 자료형이고 long long int는 8바이트 정수까지 저장할 수 있는 정수 자료형이라고 적혀있었다.
# 혜아는 int 앞에 long을 하나씩 더 붙일 때마다 4바이트씩 저장할 수 있는 공간이 늘어나는 것이라고 생각했다.
# 혜아가 N바이트 정수까지 저장할 수 있다고 생각해서 칠판에 쓴 정수 자료형의 이름은 무엇일까?
# 입력
# 첫 번째 줄에는 문제의 정수 N이 주어진다(4=<N=<1000; N은 4의 배수)
# 출력
# 혜아가 N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.

# N이 4의 몇배수인지 확인 한 후 그 수만큼 long을 붙여주자
N = int(input())
a = N//4
for i in range(a):
    print('long', end=' ')
print('int')



# 빠른 A+B
# input 대신 sys.stdin.readline을 사용하여 빠르게 입력받기
# 단, 입력 후 엔터가 사용되므로 rstrip()을 함께 사용하기(문자열 자체를 변수에 저장하고 싶을 때)

T = int(sys.stdin.readline())
for i in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)

