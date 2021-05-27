class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.data = data

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next # 마지막 노드까지 감
            new = Node(data) # 추가할 노드
            node.next = new # 마지막 노드의 다음 주소에 추가 노드 지정
            new.prev = node
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    def search_from_head(self, data):
        if self.head == None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False
    def search_from_tail(self, data):
        if self.head == None:
            return False
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False
    def insert_before(self, data, before_data): # ex) 1.5, 2
        if self.head == None:
            self.head = Node(data) # 노드가 없으면 새로운 노드 만듬
            return True
        else:
            node = self.tail # 끝 노드 지정
            while node.data != before_data: # 이전으로 넘어가면서 위치 찾음
                node = node.prev
                if node == None:
                    return False
            new = Node(data) # 추가할 노드 생성
            before_new = node.prev # 이전 노드 지정 // 2의 이전 1
            before_new.next = new # 이전 노드의 다음 주소를 새로운 노드 // 1의 다음 주소를 1.5로 지정
            new.prev = before_new # 새로운 노드의 이전 주소를 이전 노드로 지정 // 1.5의 이전 주소를 1로 지정
            new.next = node # 새로운 노드의 다음 주소 지정 // 1.5의 다음 주소 2로 지정
            node.prev = new # 노드의 이전 주소를 새로운 노드로 지정 // 2의 이전 주소 1.5
            return True
    def insert_after(self, data, after_data):
        if self.head == Node:
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != after_data:
                node = node.next
                if node == None:
                    return False
            new = Node(data)
            after_new = node.next
            new.next = after_new
            new.prev = node
            node.next = new
            if new.next == None:
                self.tail = new
            return True

double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
double_linked_list.desc()

print()

node_3 = double_linked_list.search_from_tail(3)
print(node_3.data)

print()

double_linked_list.insert_before(1.5, 2)
double_linked_list.desc()

print()

node_3 = double_linked_list.search_from_tail(1.5)
print(node_3.data)

print()
double_linked_list.insert_after(8.5, 8)
double_linked_list.desc()