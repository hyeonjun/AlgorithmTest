def solution(m, musicinfos):
    import re
    answer = []
    p = re.compile('([A-Z])(\#)?')
    m = [x + y for x, y in p.findall(m)]

    for i in musicinfos:
        data = i.split(',')
        name = data[2]
        time = (int(data[1].split(':')[0]) - int(data[0].split(':')[0])) * 60 + (
                    int(data[1].split(':')[1]) - int(data[0].split(':')[1]))
        scale = [x + y for x, y in p.findall(data[3])]
        scale = [scale[i % len(scale)] for i in range(time)]

        for i in range(len(scale)):
            if m == scale[i:i + len(m)]:
                answer.append([name, time])
                break

    return sorted(answer, reverse=True, key=lambda x: x[1])[0][0] if answer else "(None)"