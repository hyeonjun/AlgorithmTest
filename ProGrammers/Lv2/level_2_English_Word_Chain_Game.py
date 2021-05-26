def solution(n, words):
    N = len(words)
    used = [words.pop(0)]
    while words:
        word = words.pop(0)
        last_used = used[-1]
        if word in used or last_used[-1] != word[0]:
            break
        else:
            used.append(word)
    return [(len(used))%n+1, (len(used))//n+1] if len(used) != N else [0,0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])) # [3,3]
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])) # [0,0]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])) # [1,3]