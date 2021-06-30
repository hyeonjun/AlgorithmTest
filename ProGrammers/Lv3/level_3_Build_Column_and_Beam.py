# build_frame = [x, y, a, b]
# x,y는 기둥, 보를 설치 또는 삭제할 좌표(가로, 세로)
# a는 구조물 종류, 0은 기둥 1은 보
# b는 0은 삭제, 1은 설치

# 조건
# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위 또는 다른 기둥 위에 있어야함
# 보는 한쪽 끝 부분 기둥 위에 있거나, 양쪽 끝부분이 다른 보와 동시에 연결

# 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제
def available(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥
            if y != 0 and (x, y-1, 0) not in answer and (x-1, y, 1) not in answer and (x, y, 1) not in answer:
                return False
        else: # 보
            if (x, y-1, 0) not in answer and (x+1, y-1, 0) not in answer and \
                    not ((x-1, y, 1) in answer and (x+1, y, 1) in answer):
                return False
    return True


def solution(n, build_frame):
    answer = set()

    for x, y, a, b in build_frame:
        item = (x, y, a)
        if b:  # 1이면 설치
            answer.add(item)
            if not available(answer):
                answer.remove(item)
        elif b == 0 and item in answer:
            answer.remove(item)
            if not available(answer):
                answer.add(item)
    return sorted(map(list, answer))

# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))