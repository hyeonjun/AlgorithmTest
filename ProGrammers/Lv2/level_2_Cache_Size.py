def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cache = []
    for i in cities:
        city = i.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)
            answer += 5
        cache.append(city)

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 50
print(solution(3, 	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) # 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])) # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 25