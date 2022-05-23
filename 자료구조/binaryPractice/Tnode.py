class tnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __eq__(self,other):
        return self.data == other.data