n = int(input())
numbers = list(map(str, input().split()))
# 리스트의 각 원소가 1000000000보다 작거나 같은 음이 아닌 정수.
# 파이썬의 문자형 숫자 정렬의 경우 숫자의 크기순이 아닌 숫자의 순서로 정렬된다.
# 그래서 모든 리스트의 각 원소를 최대값의 길이 이상으로 맞추고 정렬시키면
# 숫자 순서대로 정렬되므로 가장 큰 수를 뽑아낼 수 있다.
numbers = sorted(numbers, reverse=True, key=lambda x : x*(11-len(x)) if len(x) < 10 else x)
print(str(int(''.join(numbers))))

