# 연속된 수의 합
# 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다.
# 두 정수 num과 total이 주어집니다. 연속된 수 num개를 더한 값이 total이 될 때,
# 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

# 제한사항
# 1 ≤ num ≤ 100
# 0 ≤ total ≤ 1000
# num개의 연속된 수를 더하여 total이 될 수 없는 테스트 케이스는 없습니다.

# 연속된 수가 홀수라면 나누었을 때 몫을 기준으로 결과값을 갖게 된다...
# 짝수라면..? 짝수라면 어떻게 값이 정해질까

# 우선 num이 홀수 일 때
num = 5
total = 15
answer = []

center = total//num
start = center - num//2
for i in range(start, start+num):
    answer.append(i)

# 짝수일때..는..우선 결과값이 짝수니까 홀수는 센터가 있었다면 짝수는 왼쪽 오른쪽으로 나눠보자
num = 4
total = 14
answer = []

left = total//num
start = left - (num//2-1) #왼쪽에 left가 포함되어 있으니까 한개 빼주기
for i in range(start, start+num):
    answer.append(i)

# 최종함수
def solution(num,total):
    answer = []
    if num%2 == 0:
        left = total // num
        start = left - (num // 2 - 1)
        for i in range(start, start + num):
            answer.append(i)
    else:
        center = total // num
        start = center - num // 2
        for i in range(start, start + num):
            answer.append(i)
    return answer


# -------------------------------------------
# 로그인 성공?
# 머쓱이는 프로그래머스에 로그인하려고 합니다. 머쓱이가 입력한 아이디와 패스워드가 담긴 배열 id_pw와 회원들의 정보가 담긴 2차원 배열 db가 주어질 때,
# 다음과 같이 로그인 성공, 실패에 따른 메시지를 return하도록 solution 함수를 완성해주세요.
# 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.
# 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.

# 제한사항
# 회원들의 아이디는 문자열입니다.
# 회원들의 아이디는 알파벳 소문자와 숫자로만 이루어져 있습니다.
# 회원들의 패스워드는 숫자로 구성된 문자열입니다.
# 회원들의 비밀번호는 같을 수 있지만 아이디는 같을 수 없습니다.
# id_pw의 길이는 2입니다.
# id_pw와 db의 원소는 [아이디, 패스워드] 형태입니다.
# 1 ≤ 아이디의 길이 ≤ 15
# 1 ≤ 비밀번호의 길이 ≤ 6
# 1 ≤ db의 길이 ≤ 10
# db의 원소의 길이는 2입니다.

# 먼저 db에서 입력된 아이디 값이 있는 지 확인
id_pw = ["meosseugi", "1234"]
db = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]

# for a in db:
#     if a[0] == id_pw[0]:
#         pass
# else: # for문이 중간에 빠져나오지 않고 끝까지 실행 됐을 경우 실행된다.
#     pass

# 아이디가 있다면 비밀번호 확인하기
for a in db:
    if a[0] == id_pw[0]:
        if a[1] == id_pw[1]:
            print('login')
        else:
            print('wrong pw')
else:
    print('fail')

# 최종함수
def solution(id_pw, db):
    answer = ''
    for a in db:
        if a[0] == id_pw[0]:
            if a[1] == id_pw[1]:
                answer = 'login'
                return answer
            else:
                answer = 'wrong pw'
                return answer
    else:
        answer = 'fail'
        return answer






