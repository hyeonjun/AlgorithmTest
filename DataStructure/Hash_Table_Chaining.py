# 개방 해쉬(Open Hashing) 기법 중 하나.
# 해쉬 테이블 저장 공간 외의 공간을 활용하는 기법
# 충돌이 일어나면, 리스트를 잉효아여 데이터 추가로 뒤에 연결시켜 저장
# 뒤에 연결시키는 것으로 Chaining 기법이라 함
hash_table = [0] * 8

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for i in range(len(hash_table[hash_address])):
            if hash_table[hash_address][i][0] == index_key:
                hash_table[hash_address][i][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for i in range(len(hash_table[hash_address])):
            if hash_table[hash_address][i][0] == index_key:
                return hash_table[hash_address][i][1]
        return None
    else:
        return None

print (hash('Dave') % 8) # 0
print (hash('Dd') % 8) # 1
print (hash('Data') % 8) # 5

save_data('Dd', '1201023010')
save_data('Data', '3301023010')
save_data('Dave', '3929139493')
print(read_data('Dd'))
print(read_data('Data'))
print(read_data('Dave'))

print(hash_table)
"""
[[[-3102527239189243712, '3929139493']], 
 [[-1683329283695540631, '1201023010']], 
 0, 
 0, 
 0,
 [[-8411239324333639627, '3301023010']], 
 0, 
 0]
"""