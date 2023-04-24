hp = 999
answer = 0

if hp // 5:  # hp가 5로 나누어진다면 장군개미 공격 가능
    answer += hp//5
    hp = hp % 5
    if hp // 3:  # hp가 3으로 나누어진다면 장군개미 공격 가능
        answer += hp//3
        hp = hp % 3
        if hp < 3:
            answer += hp
    else:
        answer += hp
elif hp // 3:
    answer += hp//3
    hp = hp % 3
    if hp < 3:
        answer += hp
else:
    answer += hp


print(answer, hp)
