N = int(input())
count = 0

for i in range(N):
    word = input()
    checking = []
    breaker = False
    # 문자를 for문으로 돌리고 그 전 문자와 같다면 넘어가고 다르다면 이미 나왔던 알파벳인지 확인하자.
    for k in range(len(word)):
        if k == 0:
            checking.append(word[0])
        elif word[k-1] == word[k]:
            pass
        else:
            if word[k] in checking:
                breaker = True
                break
            else:
                checking.append(word[k])
    if breaker == False:
        count += 1
print(count)
