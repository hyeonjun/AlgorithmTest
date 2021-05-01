# 폐쇄 해쉬(Close Hashing) 기법 중 하나.
# 해쉬 테이블 저장 공안 안에서 충돌 문제를 해결하는 기법
# 충돌이 일어나면, 해당 hash address의 다음 address부터 맨 처음
# 나오는 빈 공간에 저장하는 기법
# - 저장 공간 활용도를 높이기 위한 기법
hash_table = [0] * 8

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for i in range(hash_address, len(hash_table)):
            if hash_table[i] == 0:
                hash_table[i] = [index_key, value]
                return
            elif hash_table[i][0] == index_key:
                hash_table[i][1] = value
                return
    else:
        hash_table[hash_address] = [index_key,value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for i in range(hash_address, len(hash_table)):
            if hash_table[i] == 0:
                return None
            elif hash_table[i][0] == index_key:
                return hash_table[i][1]
    else:
        return None

print (hash('dk') % 8)
print (hash('da') % 8)
print (hash('dc') % 8)

save_data('dk', '01200123123')
save_data('da', '3333333333')
print(read_data('dc')) # None
save_data('dc', '111111111')
print(read_data('dc')) # 111111111

print(hash_table)
# [0,
#  0,
#  0,
#  0,
#  0,
#  0,
#  [2095437034436907190, '111111111'],
#  [1188993361022051855, '01200123123']]