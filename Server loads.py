
processes=[1,2,3,4,5]
max_load = sum(processes)
total = max_load // 2
dp = [[0 for i in processes] for j in range(total)]
for i in range(1, total + 1):
    if i >= processes[0]:
        dp[i - 1][0] = processes[0]
for idx, item in enumerate(processes):
    for w in range(2, total + 1):
        if w - 1 < item:
            dp[w - 1][idx] = dp[w - 1][idx - 1]
        else:
            dp[w - 1][idx] = max(dp[w - 1][idx - 1], dp[w - item - 1][idx - 1] + item)

best = dp[total - 1][len(processes) - 1]