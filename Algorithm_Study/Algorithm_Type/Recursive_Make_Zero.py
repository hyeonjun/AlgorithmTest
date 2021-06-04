def solution(n):
    import copy
    def recursive(arr, n):
        if len(arr) == n:
            operators_list.append(copy.deepcopy(arr))
            return
        arr.append(' ')
        recursive(arr, n)
        arr.pop()

        arr.append('+')
        recursive(arr, n)
        arr.pop()

        arr.append('-')
        recursive(arr, n)
        arr.pop()

    operators_list = []
    recursive([], n-1)
    num_list = [i for i in range(1, n+1)]
    answer = []
    for op in operators_list:
        exp = ""
        for i in range(n-1):
            exp += str(num_list[i]) + op[i]
        exp += str(num_list[-1])
        if eval(exp.replace(" ","")) == 0:
            answer.append(exp)
    return answer

print(solution(3))
print(solution(7))

def solution(n):
    from itertools import product
    oper = ['+', '-', ' ']
    oper_list = []
    answer = []
    for i in product(oper,repeat=n-1):
        oper_list.append(i)
    num_list = [i for i in range(1, n+1)]
    for op in oper_list:
        exp = ""
        for i in range(n-1):
            exp += str(num_list[i]) + op[i]
        exp+=str(num_list[-1])

        if eval(exp.replace(" ", "")) == 0:
            answer.append(exp)
    return answer

print(solution(3))
print(solution(7))