# https://school.programmers.co.kr/learn/courses/30/lessons/42885?language=python3
# 구명보트
# 문제 설명
# 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
# 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.
# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
# 제한사항
# 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
# 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

# people 리스트를 오름차순으로 정리한 후 limt에 맞춰 태워보내면 되지 않을까
people = [40, 40, 40, 70, 70]
limit = 100
# 몸무게 적은 순으로 정리
people.sort()
boat = []
count = 1
for p in people:
    boat.append(p)
    print(boat)
    if sum(boat) > limit:
        boat = boat[-1:]
        count += 1
    if sum(boat) == limit:
        boat.clear()
        count += 1

# 놓친게 있었다. 한번에 최대 2명씩 밖에 탈 수 없다. 이 점 유의해서 다시 문제를 풀어보겠다.
# 정렬을 한 다음, 두개씩 짝지어 계산을 하면 되지 않을까?
# 몸무게 적은 순으로 정리
people.sort()
boat = []
count = 1
for i in range(1, len(people), 2):
    if sum(people[i], people[i-1]) > limit:
        count += 2
    else:
        count += 1

# 몇문제가 실패했다. 어차피 두명씩만 태워야 한다면 작은 몸무게와 큰 몸무게를 하나씩 태워야 잘 태울수 있을것 같다.
# 30, 70 몸무게를 가진 사람이 두명씩 있다면 위와 같이 했을 땐 [30,30],[70],[70] 이렇게 태울 수 있지만 큰사람과 적은 사람을 태우면 [30,70],[30,70] 이렇게 태울수 있다.
# 그러면 정렬 후 첫 사람과 끝사람이 탈 수 있게 해보겠다.
# 몸무게 적은 순으로 정리
people.sort()
count = 0
# 태울 앞사람과 뒷사람
start = 0
end = len(people)-1
# 앞사람 인덱스가 end를 넘지 않을 동안 반복
while start <= end:
    # 구명보트 띄우기
    count += 1
    # 몇명 탈 수 있는 지 판별
    # 두사람이 탔을 때 limit을 초과하지 않는다면 두사람 다 태우기
    if people[start]+people[end] <= limit:
        start += 1
        end -= 1
    # 초과한다면 끝사람만 태우기
    else:
        end -= 1


# 최종함수
def solution(people, limit):
    people.sort()
    count = 0
    start = 0
    end = len(people)-1
    while start <= end:
        count += 1
        if people[start]+people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
    return count
