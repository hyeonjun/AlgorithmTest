# hash()는 실행할 때마다 값이 달라질 수 있다.
# 그래서 SHA 알고리즘을 사용
# SHA는 어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로,
# 해쉬 함수로 유용하게 활용가능
import hashlib
hash_table = [0] * 8

def get_key(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)

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


hash_object = hashlib.sha256()
hash_object.update('Dd'.encode())
hex_dig = hash_object.hexdigest()
print (int(hex_dig, 16))  # 41288454500577170759602173815427620867758960932057963992518085078120395201641
print (int(hex_dig, 16) % 8) # 1

save_data('Dd', '1201023010')
save_data('Data', '3301023010')
save_data('Dave', '3929139493')
print(read_data('Dd'))
print(read_data('Data'))
print(read_data('Dave'))

print(hash_table)
"""
[[[93522153357889875539564776448390291898091266846706709766185292547775466951976, '3301023010'], [58168926492874022204843410240616221587430711422315320988033179720499944676464, '3929139493']], 
 [[41288454500577170759602173815427620867758960932057963992518085078120395201641, '1201023010']], 
 0, 
 0, 
 0, 
 0, 
 0, 
 0]
"""