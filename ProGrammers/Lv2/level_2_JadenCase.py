def solution(s):
    return " ".join([i.capitalize() for i in s.split(' ')]) # capitalize() 단어별로 앞글자만 대문자화 해줌

print(solution("3people unFollowed me")) # 	"3people Unfollowed Me"
print(solution("for the last week")) # 	"For The Last Week"
