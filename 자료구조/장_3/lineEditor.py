from list import list


class lineEditor:
    def __init__(self):
        self.list = list()

    def operation(self):
        while True:
            command = input('명령을 입력하세요 i - insert, d - delete, r - replace, p - print, l- readfile, q - quit')
            if command == 'i':
                pos = int(input("삽입할 위치를 입력하세요"))
                string = input("삽입할 내용을 입력하세요")
                self.list.insert(pos, string)

            if command == 'd':
                pos = int(input("삭제할 위치를 입력하세요"))
                print(self.list.list.delete(pos), "삭제됩니다")

            if command == 'r':
                pos = int(input("변경할 위치를 입력하세요"))
                data = input("변경할 내용을 입력하세요")
                self.list[pos] = data
            if command == 'p':
                for i in range(self.list.size()):
                    print("%d 번째 행: " % (i + 1), self.list.list[i])
            if command == 'l':
                filename = input("파일의 경로와 이름을 입력하세요")
                file = open(filename)
                lines = file.readlines()
                for line in lines:
                    self.append(line)

                file.close()

            if command == 'q':
                print("quit program")
                break


lineeditor = lineEditor()
lineeditor.operation()
