def solution(N, P, Q):
    prime_list = []
    for i in range(2, N//2+1):
        isPrime = True
        for j in prime_list:
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            prime_list.append(i)

    semi_prime = [0] * (N+1)
    for i in range(len(prime_list)):
        for j in range(i,len(prime_list)):
            data = prime_list[i] * prime_list[j]
            if data <= N:
                semi_prime[data] = 1
            else:
                break

    count = [0] * (N+1)
    for i in range(1,len(semi_prime)):
        if i == 1:
            count[i] = semi_prime[i]
        else:
            count[i] = count[i-1] + semi_prime[i]

    # scope = list(zip(P, Q)) # 66% 시간복잡도
    # result = []
    # for p, q in scope:
    #     c = 0
    #     for i in semi_prime[p-1:q]:
    #         if i == 1:
    #             c+=1
    #     result.append(c)

    result = []
    for i in range(len(P)): # 0 1 2
        result.append(count[Q[i]] - count[P[i]-1])
    return result

print(solution(26, [1,4,16], [26,10,20]))