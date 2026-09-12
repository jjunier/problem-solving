def solution(arr):
    nums = list(map(int, arr[::2]))
    ops = arr[1::2]
    n = len(nums)

    max_dp = [[-float('inf')] * n for _ in range(n)]
    min_dp = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        max_dp[i][i] = nums[i]
        min_dp[i][i] = nums[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            for k in range(i, j):
                op = ops[k]

                if op == '+':
                    max_val = max_dp[i][k] + max_dp[k + 1][j]
                    min_val = min_dp[i][k] + min_dp[k + 1][j]
                else:
                    max_val = max_dp[i][k] - min_dp[k + 1][j]
                    min_val = min_dp[i][k] - max_dp[k + 1][j]

                max_dp[i][j] = max(max_dp[i][j], max_val)
                min_dp[i][j] = min(min_dp[i][j], min_val)

    return max_dp[0][n - 1]