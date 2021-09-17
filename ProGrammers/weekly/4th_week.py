def solution(table, languages, preference):
    answer = []
    new_pre = {i:j for i, j in zip(languages, preference)}
    scores = [5, 4, 3, 2, 1]
    for i in table:
        data = i.split(' ')
        job = data[0]
        lang = data[1:]
        score = 0
        for j in range(len(lang)):
            if lang[j] in new_pre:
                score += new_pre[lang[j]] * scores[j]
        answer.append([score, job])
    answer.sort(key = lambda x:(-x[0], x[1]))
    return answer[0][1]

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
print(solution(table, ["PYTHON", "C++", "SQL"], [7, 5, 5])) # "HARDWARE
tabel = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
print(solution(table, ["JAVA", "JAVASCRIPT"], [7, 5])) # PORTAL