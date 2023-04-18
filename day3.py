# 추억 점수
# 문제 설명
# 사진들을 보며 추억에 젖어 있던 루는 사진별로 추억 점수를 매길려고 합니다.
# 사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값이 해당 사진의 추억 점수가 됩니다.
# 예를 들어 사진 속 인물의 이름이 ["may", "kein", "kain"]이고 각 인물의 그리움 점수가
# [5점, 10점, 1점]일 때 해당 사진의 추억 점수는 16(5 + 10 + 1)점이 됩니다.
# 다른 사진 속 인물의 이름이 ["kali", "mari", "don", "tony"]이고
# ["kali", "mari", "don"]의 그리움 점수가 각각 [11점, 1점, 55점]]이고,
# "tony"는 그리움 점수가 없을 때, 이 사진의 추억 점수는 3명의 그리움 점수를 합한 67(11 + 1 + 55)점입니다.
# 그리워하는 사람의 이름을 담은 문자열 배열 name, 각 사람별 그리움 점수를 담은 정수 배열 yearning,
# 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo가 매개변수로 주어질 때,
# 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return하는 solution 함수를 완성해주세요.

# 제한 사항
# 포토 안에 있는 사진 속의 누가 들어있는지 파악하기
# 그 사람에 대응하는 그리움 점수를 각각 찾아서 더하는 거죠
# 우선 한 리스트에 넣고 포토에 있는 모든 사진들을 다 찾았으면
# 추억 점수들을 담은 리스트를 반환한다.

# 포토라는 리스트를 루프를 돌면서(반복문) 각 리스트의 요소들을 체크하고(in? 인덱스 사용?)
# 요소들에 해당하는 그리움 점수를 yearning 정수 배열에서 찾는다.(인덱스?)
# 그리움 점수들을 합산해야하는데 어떻게 합산하지. 한데 모아서 합산한다.
# 합산한 추억점수를 새로운 리스트에 넣는다.
# 포토에 있는 리스트들을 다 돌고 추억점수 계산이 다끝나고 리스트에 다 담겨있으면 반환.
name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

answer = []
dic = dict(zip(name,yearning))

# 포토 리스트 돌기
for a in photo:
    sum_list = 0
    # a=안쪽 리스트가 나오겠지?
    # 사진 한장의 리스트가 있으면 이제 그 안에 든 사람을 파악해야할텐데...
    # name in 안쪽리스트를 사용하면 되려나,,?
    for person in a:
        # 네임안에 펄슨이 있으면 어떡하지.
        # 펄슨에 해당하는 점수를 가져와야해. 어떻게?
        # 딕셔너리 제조?
        # 인덱스 활용? 흠냐리
        if person in name:
            sum_list += dic[person]

    answer.append(sum_list)

print(answer)

# 최종함수
def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name,yearning))

    for a in photo:
        sum_list = 0
        for person in a:
            if person in name:
                sum_list += dic[person]

        answer.append(sum_list)
    return answer



