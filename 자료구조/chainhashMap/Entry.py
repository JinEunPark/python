class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return str("key: %s , value: %d"%(self.key, self.value))