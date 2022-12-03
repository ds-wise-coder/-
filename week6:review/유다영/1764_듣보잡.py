# 듣지 못한 사람
# 보지 못한 사람
# 두개의 배열에서 중복된 원소=듣보잡
# 배열에서 중복된 원소 여부 찾을때 이용-> set

n, m = map(int, input().split())
no_hear_set = set()

for i in range(n):
    no_hear_set.add(input())

no_see_set = set()
for i in range(m):
    no_see_set.add(input())

result = sorted(list(no_hear_set & no_see_set))  # 교집합(중복되는 원소)->사전 순 정렬

print(len(result))
for i in result:
    print(i)
