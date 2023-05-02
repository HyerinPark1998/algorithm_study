# https://school.programmers.co.kr/learn/courses/30/lessons/12954
# 문제 설명
# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
# 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
# 제한 조건
# x는 -10000000 이상, 10000000 이하인 정수입니다.
# n은 1000 이하인 자연수입니다.
x = -4
n = 2
# range(x시작점,n*x끝점+1,x차이)
# .append()
list_a = []
for i in range(1, n+1):
    list_a.append(x*i)

print(list_a)


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/12948
# 핸드폰 번호 가리기
# 문제 설명
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
# 제한 조건
# phone_number는 길이 4 이상, 20이하인 문자열입니다.


phone_number = '01033331234'
phone = list(phone_number)
# phone_number ="027778888"
for i in range(len(phone_number)-4):
    phone[i] = "*"
phone_number = ''.join(phone)

print(phone_number)

# .replace(a,b)
