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
    print(f"{result:.3f}"+"%")
