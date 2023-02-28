import sys
input = sys.stdin.readline

N = input().strip()
len_N = len(N)
half_N = N[:(len_N + 1) // 2]

# 9 or 99 or 999 or 9999 ... 이런 경우라면?
if N == "9" * len_N:
    print(int(N) + 2)
elif len_N == 1:
    print(int(N) + 1)
# 만약 숫자의 길이가 홀수인 경우
elif len_N % 2 != 0:
    temp = half_N + half_N[-2::-1]
    if int(temp) > int(N):
        print(temp)
    else:
        temp = str(int(half_N) + 1)
        temp = temp[:] + temp[-2::-1]
        print(temp)
# 만약 숫자의 길이가 짝수인 경우
else:
    temp = half_N + half_N[::-1]
    if int(temp) > int(N):
        print(temp)
    else:
        temp = str(int(half_N) + 1)
        temp = temp[:] + temp[::-1]
        print(temp)