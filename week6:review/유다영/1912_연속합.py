# n개의 정수로 이루어진 임의의 수열
# 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합

n = int(input())
numbers=list(map(int, input().split()))

dp =[0]*n
dp[0]=numbers[0] # 첫번째 값은 수열의 첫번째 값 대입

if max(numbers)<0: # 가장 큰 값이 음수라면==음수뿐인 수열
    print(max(numbers))
else: # 음수, 양수 섞인 수열
    for i in range(1, n):
        if dp[i-1]+numbers[i]>0:
            dp[i]=dp[i-1]+numbers[i]
    print(max(dp))