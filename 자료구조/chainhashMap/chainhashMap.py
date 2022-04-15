from Entry import Entry
from node import Node


class chainMap:
    def __init__(self, M):
        self.M = M
        self.list = [None] * M
        # 생성자에게서 맵의 크기를 전달받음

    def hashFn(self, key: str):
        sum = 0  # string 타입의 키값을 받는다
        for i in range(len(key)):
            sum += ord(key[i])  # 아스키 코드값을 전부 더하고 배열의 크기로 나누 나머지를 해쉬어드레스로 사용
        hashAddress = sum % self.M
        return hashAddress

    def insert(self, key, value):
        index = self.hashFn(key)
        self.list[index] = Node(Entry(key, value), self.list[index])
        # 현재 list[index]에 저장되어있는 node를 링크필에 연결하는 node를 생성하고 이 노드를 가리키는 list[index] 를 새로 만듦
        # 가장 처음에 삽이비되는 node의 링크는 None이 삽입된다. 그 이유는 맨처음에 None으로 리스트를 초기화 했기 때문이다
        # 따라서 serach 메소드를 사용할 때도 whlie none을 사용할 수 있다.

    def search(self, key):
        index = self.hashFn(key)
        node = self.list[index]
        while node is not None:
            if node.data.key == key:
                return node.data.value
            node = node.link
        return None

    def delete(self, key):
        index = self.hashFn(key)
        node = self.list[index]
        before = None
        while node is not None:
            if node.data.key == key:
                if before == None:
                    self.list[index] = self.list[index].link
                    # 첫번째 항목 삭제
                    return
                else:
                    before.link = node.link  # 두번째 항목부터 삭제연산
                before = node
                node = node.link

    def display(self):
        for i in range(len(self.list)):
            if self.list[i] is not None:
                print("list[%d]" %i, end=" ")
                node = self.list[i]
                while node is not None:
                    print(node.data, end=" ->")
                    node = node.link
                print(None)


c = chainMap(10)
c.insert("qkrwlsdms", 1)
c.insert("qkrwlsdms", 2)
c.insert("qkrwlsdms", 3)
print(c.list[0].data.value)
print(c.list[0].link.data.value)
print(c.list[0].link.link.data.value)
print(c.search("qkrwlsdms"))
c.display()