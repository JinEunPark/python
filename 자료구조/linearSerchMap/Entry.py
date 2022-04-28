class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("(value: {} key: {})".format(self.key, self.value))
