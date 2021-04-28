def solution(new_id):
    import re
    new_id = re.sub('[^\w\-\_\.]', '', new_id.lower())
    new_id = re.sub('\.+', '.', new_id)
    new_id = re.sub('^\.|\.$', '', new_id)
    new_id = "a" if len(new_id) == 0 else re.sub('\.$', '', new_id[:15])
    new_id = new_id if len(new_id) > 2 else new_id + new_id[-1] * (3 - len(new_id))
    return new_id

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
# print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))