from bisect import *
n, m = map(int, raw_input().split())
dp = [10**10] * 5050
for i in xrange(n):
    k, a = raw_input().split()
    k = int(k)
    dp[bisect_right(dp, k)] = k
print n - bisect_left(dp, 10**10)