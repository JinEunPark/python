class bnode:
    def __init__(self, key, value):
        self.key = key#key 값을 파라미터로 전달 받는다.
        self.value = value#value를 파라민터로 전달 받는다.
        self.left = None#생성할시에는 공백으로 링크를 체운다.
        self.right = None