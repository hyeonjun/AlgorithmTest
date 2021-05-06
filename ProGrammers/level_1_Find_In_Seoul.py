def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 "+str(i)+"에 있다"
    return None
print(solution(["KKK","QQQ","Kim"]))

def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

print(solution(["KKK","QQQ","Kim"]))