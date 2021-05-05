class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched == False:
            return False

        # case 1
        # self.current_node가 삭제할 Node
        # self.parent는 삭제할 Node의 Parent Node인 상태
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            # del self.current_node

        # case 2
        # 삭제할 Node가 하나의 leaf Node를 가지고
        # leaf 노드가 왼쪽에만 있을 때
        elif self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        # leaf 노드가 오른쪽에만 있을 때
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # case 3
        # 삭제할 Node가 leaf Node를 두 개 가지고 있을 때
        # 방법 1: 삭제할 Node의 오른쪽 자식 중, 가장 작은(왼쪽 끝) 값을 삭제할 Node의 Parent Node가 가리키도록 한다.
        # 방법 2: 삭제할 Node의 왼쪽 자식 중, 가장 큰(오른쪽 끝) 값을 삭제할 Node의 Parent Node가 가리키도록 한다
        # 방법 1 구현
        # 방법 1의 두 가지 경우의 수
        # 1. 삭제할 Node의 왼쪽 끝 Node로 갔을 때 이 Node가 leaf Node를 가지고 있지 않을 때
        # 2. 삭제할 Node의 왼쪽 끝 Node로 갔을 때 이 Node가 오른쪽 leaf Node를 가지고 있을 때
        elif self.current_node.left != None and self.current_node.right != None:
            # 삭제할 Node가 Parent Node 왼쪽에 있을 때
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != Node: # 가장 작은 값 찾음
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            # 삭제할 Node가 Parent Node 오른쪽에 있을 때
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != Node:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
        return True

# Test
# 0 ~ 999 숫자 중에서 임의로 100개를 추출
from random import randint
bst_nums = set()
while len(bst_nums) <= 100:
    bst_nums.add(randint(0, 999))

# 위 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

# 검색 기능 확인
for num in bst_nums:
    if binary_tree.search(num) == False:
        print("search False", num)

# 입력한 100개의 숫자 중 10개의 숫자 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[randint(0, 99)])

# 선택한 10개의 숫자 삭제 기능 확인
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print("delete failed", del_num)



# head = Node(1)
# BST = NodeMgmt(head)
# BST.insert(2)
# BST.insert(4)
# BST.insert(3)
# BST.insert(0)
# BST.insert(8)
# print(BST.search(0), BST.search(-1))


