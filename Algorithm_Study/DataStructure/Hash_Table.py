hash_table = [0] * 8

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_function(get_key(data)) # 인덱스 번호
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave', '3')
save_data('Andy', '1')
print(read_data('Dave')) # 3
print(hash_table) # [0, 0, 0, 0, '3', 0, '1', 0]


