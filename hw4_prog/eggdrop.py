import sys
sys.setrecursionlimit(100000)

if __name__ == "__main__":
    with open("input.txt","r") as f:
        contents = f.readline()
        index = contents.find(",")
        N = int(contents[0:index])
        K = int(contents[index+1:-1])
        f.close()
    ################################################
    # dp = [[0 for x in range(K+1)] for x in range(N+1)]
    # for i in range(1, K+1):
    #     dp[1][i] = 0
    #     dp[0][i] = 0
    # for j in range(1,N+1):
    #     dp[j][1] = j-1
    # for j in range(2, K+1):
    #     for i in range(2, N+1):
    #         dp[i][j] = 65535
    #         for x in range(1, i+1):
    #             if j == 2:
    #                 ans = 1 + max(dp[x][j-1],  dp[i-x][j])
    #             else:
    #                 ans = 1 + max(dp[x-1][j-1],  dp[i-x+1][j])
    #             if ans < dp[i][j]:
    #                 dp[i][j] = ans
    ################################################
    # for j in range(2, K+1):
    #     for i in range(2, N+1):
    #         dp[i][j] = 65535
    #         lo, hi = 1, i
    #         while lo+1 < hi:
    #             x = int((lo+hi)/2)
    #             if j == 2:
    #                 t1 = dp[x][j-1]
    #                 t2 = dp[i-x][j]
    #                 if t1 < t2:
    #                         lo = x
    #                 elif t1 > t2:
    #                         hi = x
    #                 else:
    #                         lo = hi = x
    #             else:
    #                 t1 = dp[x-1][j-1]
    #                 t2 = dp[i-x][j]
    #                 if t1 < t2:
    #                         lo = x
    #                 elif t1 > t2:
    #                         hi = x
    #                 else:
    #                         lo = hi = x
    #         if j == 2:
    #             ans = 1 + min(max(dp[x][j-1], dp[i-x][j]) for x in (lo, hi))    
    #         else: 
    #             1 + min(max(dp[x-1][j-1], dp[i-x][j])for x in (lo, hi))
    #         dp[i][j] = ans
    #################################################
    dp = [0 for x in range(N+1)]
    for j in range(1,N+1):
        dp[j]= j-1
    flag = 0
    if N == 1:
        flag = 1
    if K == 2 and flag == 0:
        dp2 = [0]
        dp2.append(0)
        for n in range(2,N+1):
            dp2.append(65536)
            for x in range(1,n+1):
                ans = 1 + max(dp[x], dp2[n-x])
                if ans < dp2[n]:
                    dp2[n] = ans
        dp = dp2
        flag = 1
    if flag == 0:
        for k in range(2, K+1):
            # Now, we will develop dp2[i] = dp(k, i)
            dp2 = [0]
            x = 1
            for n in range(1, N+1):
                # Let's find dp2[n] = dp(k, n)
                # Increase our optimal x while we can make our answer better.
                # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
                # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
                if k > 2:
                    while x < n and max(dp[x-1], dp2[n-x]) > \
                                    max(dp[x], dp2[n-x-1]):
                        x += 1

                    # The final answer happens at this x.
                    dp2.append(1 + max(dp[x-1], dp2[n-x]))
                else:
                    while x < n and max(dp[x], dp2[n-x]) > \
                                    max(dp[x+1], dp2[n-x-1]):
                        x += 1
                    dp2.append(1 + max(dp[x-1], dp2[n-x]))
            dp = dp2
    print(dp[-1])
    with open("output.txt","w") as f:
        f.write(str(dp[-1]))
        f.close()



    
