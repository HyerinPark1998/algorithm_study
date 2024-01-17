# https://school.programmers.co.kr/learn/courses/30/lessons/134240
# 푸드 파이트 대회
# 문제 설명
# 수웅이는 매달 주어진 음식을 빨리 먹는 푸드 파이트 대회를 개최합니다. 이 대회에서 선수들은 1대 1로 대결하며, 매 대결마다 음식의 종류와 양이 바뀝니다. 대결은 준비된 음식들을 일렬로 배치한 뒤, 한 선수는 제일 왼쪽에 있는 음식부터 오른쪽으로, 다른 선수는 제일 오른쪽에 있는 음식부터 왼쪽으로 순서대로 먹는 방식으로 진행됩니다. 중앙에는 물을 배치하고, 물을 먼저 먹는 선수가 승리하게 됩니다.
# 이때, 대회의 공정성을 위해 두 선수가 먹는 음식의 종류와 양이 같아야 하며, 음식을 먹는 순서도 같아야 합니다. 또한, 이번 대회부터는 칼로리가 낮은 음식을 먼저 먹을 수 있게 배치하여 선수들이 음식을 더 잘 먹을 수 있게 하려고 합니다. 이번 대회를 위해 수웅이는 음식을 주문했는데, 대회의 조건을 고려하지 않고 음식을 주문하여 몇 개의 음식은 대회에 사용하지 못하게 되었습니다.
# 예를 들어, 3가지의 음식이 준비되어 있으며, 칼로리가 적은 순서대로 1번 음식을 3개, 2번 음식을 4개, 3번 음식을 6개 준비했으며, 물을 편의상 0번 음식이라고 칭한다면, 두 선수는 1번 음식 1개, 2번 음식 2개, 3번 음식 3개씩을 먹게 되므로 음식의 배치는 "1223330333221"이 됩니다. 따라서 1번 음식 1개는 대회에 사용하지 못합니다.
# 수웅이가 준비한 음식의 양을 칼로리가 적은 순서대로 나타내는 정수 배열 food가 주어졌을 때, 대회를 위한 음식의 배치를 나타내는 문자열을 return 하는 solution 함수를 완성해주세요.

# 제한사항
# 2 ≤ food의 길이 ≤ 9
# 1 ≤ food의 각 원소 ≤ 1,000
# food에는 칼로리가 적은 순서대로 음식의 양이 담겨 있습니다.
# food[i]는 i번 음식의 수입니다.
# food[0]은 수웅이가 준비한 물의 양이며, 항상 1입니다.
# 정답의 길이가 3 이상인 경우만 입력으로 주어집니다.

# food = 구매한 음식 개수, 0번은 물이며 항상 1.

# 각 음식별로 짝수로 몇번 먹을 수 있는 지 파악
# 물을 기준으로 대칭으로 나열

food = [1, 7, 1, 2]

# 딕셔너리로 몇번 음식을 한 선수당 몇개 먹을 수 있는지 정리한다음 대칭으로 반환하면 되지 않을까?
# 0번은 고정값이므로 제외
menu = {}
for i in range(1, len(food)):
    # 한사람이 먹을 양을 파악
    menu[i] = food[i]//2

# 생각해보니 딕셔너리를 굳이 안해도 될 것 같다.
# 한명분의 음식을 나열한 뒤 물을 기준으로 대칭으로 붙여주면 될것 같다.
result = ""
for i in range(1, len(food)):
    result += str(i)*(food[i]//2)

# 물 기준으로 대칭 만들기
result = result + "0" + result[::-1]
print(result)


# 최종 함수
def solution(food):
    result = ""
    for i in range(1, len(food)):
        result += str(i)*(food[i]//2)
    return result + "0" + result[::-1]


# ----------------------------------
# https://school.programmers.co.kr/learn/courses/30/lessons/161989
# 덧칠하기
# 문제 설명
# 어느 학교에 페인트가 칠해진 길이가 n미터인 벽이 있습니다. 벽에 동아리 · 학회 홍보나 회사 채용 공고 포스터 등을 게시하기 위해 테이프로 붙였다가 철거할 때 떼는 일이 많고 그 과정에서 페인트가 벗겨지곤 합니다. 페인트가 벗겨진 벽이 보기 흉해져 학교는 벽에 페인트를 덧칠하기로 했습니다.
# 넓은 벽 전체에 페인트를 새로 칠하는 대신, 구역을 나누어 일부만 페인트를 새로 칠 함으로써 예산을 아끼려 합니다. 이를 위해 벽을 1미터 길이의 구역 n개로 나누고, 각 구역에 왼쪽부터 순서대로 1번부터 n번까지 번호를 붙였습니다. 그리고 페인트를 다시 칠해야 할 구역들을 정했습니다.
# 벽에 페인트를 칠하는 롤러의 길이는 m미터이고, 롤러로 벽에 페인트를 한 번 칠하는 규칙은 다음과 같습니다.
# 롤러가 벽에서 벗어나면 안 됩니다.
# 구역의 일부분만 포함되도록 칠하면 안 됩니다.
# 즉, 롤러의 좌우측 끝을 구역의 경계선 혹은 벽의 좌우측 끝부분에 맞춘 후 롤러를 위아래로 움직이면서 벽을 칠합니다. 현재 페인트를 칠하는 구역들을 완전히 칠한 후 벽에서 롤러를 떼며, 이를 벽을 한 번 칠했다고 정의합니다.
# 한 구역에 페인트를 여러 번 칠해도 되고 다시 칠해야 할 구역이 아닌 곳에 페인트를 칠해도 되지만 다시 칠하기로 정한 구역은 적어도 한 번 페인트칠을 해야 합니다. 예산을 아끼기 위해 다시 칠할 구역을 정했듯 마찬가지로 롤러로 페인트칠을 하는 횟수를 최소화하려고 합니다.
# 정수 n, m과 다시 페인트를 칠하기로 정한 구역들의 번호가 담긴 정수 배열 section이 매개변수로 주어질 때 롤러로 페인트칠해야 하는 최소 횟수를 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 1 ≤ m ≤ n ≤ 100,000
# 1 ≤ section의 길이 ≤ n
# 1 ≤ section의 원소 ≤ n
# section의 원소는 페인트를 다시 칠해야 하는 구역의 번호입니다.
# section에서 같은 원소가 두 번 이상 나타나지 않습니다.
# section의 원소는 오름차순으로 정렬되어 있습니다.

# 벽의 크기를 원소가 0인 리스트로 나타내고 칠해야하는 구역을 1로 나타낸다.
# 롤러의 크기만큼 앞에서부터 칠해나가며 이때 칠해진 벽은 0으로 표시한다.
# 그렇게 덧칠한 횟수를 파악하면 되지 않을까?

n = 8
m = 4
section = [2, 3, 6]

# for문으로 배열 만들기
wall = [0 for i in range(n)]

# 칠해야하는 구역 1로 표시하기
for i in section:
    wall[i-1] = 1

# 덧칠 횟수
check = 0
# 롤러 크기만큼 앞에서부터 칠하기
for i, n in enumerate(wall):
    if n:
        wall[i:i+m] = [0 for i in range(m)]
        check += 1


# 최종 함수
def solution(n, m, section):
    wall = [0 for i in range(n)]
    for i in section:
        wall[i-1] = 1
    check = 0
    for i, n in enumerate(wall):
        if n:
            wall[i:i+m] = [0 for i in range(m)]
            check += 1
    return check
