def solution(strs, t):
    n = len(t)
    dp = [float('inf') for _ in range(n+1)]
    dp[0] = 0
    for i in range(1, n+1):
        for k in range(1, 6):
            s = 0 if i-k < 0 else i-k
            if t[s:i] in strs:
                dp[i] = min(dp[i], dp[s]+1)
    return dp[-1] if dp[-1] != float('inf') else -1

print(solution(["ab", "na", "n", "a", "bn"], "nabnabn")) # 4
print(solution(["ba", "na", "n", "a"], "banana")) # 3
print(solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple")) # 2
print(solution(["ba", "an", "nan", "ban", "n"], "banana")) # -1
"""
ba -> ba 1 bana 2 o ban 2 baa x
na -> na 1 o nan 2 naa x
n -> n 1 na 2
a -> a 1

app -> app 1 o appap x appp x appl 2 appe x appple x apppp x
ap -> ap 1 app  apl ape apple appp
p -> p 1 pl 2 pe x pple 2 ppp x
l -> l 1 le 2 lple x lpp x
e -> e 1 eple x epp x
ple -> ple 1 o plepp x
pp -> pp 1
"""