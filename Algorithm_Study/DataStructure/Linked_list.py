class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = data
    def add(self, data):
        if self.head == '' : self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    def delete(self, data):
        if self.head == '':
            print("첫 번째 노드가 없습니다.")
            return
        if self.head.data == data:
            tmp = self.head
            self.head = self.head.next
            del tmp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    tmp = node.next
                    node.next = node.next.next
                    del tmp
                else:
                    node = node.next

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.data
        return print("해당 데이터를 가진 노드가 존재하지 않습니다.")

# 테스트
node_mgmt = NodeMgmt(0)
for data in range(1, 10):
    node_mgmt.add(data)

node = node_mgmt.search_node(4)
print (node.data)

node_mgmt.delete(4)
node_mgmt.desc()
node_mgmt.search_node(4)