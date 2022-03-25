class Arraylist:
    def __init__(self):
        self.list = []

    def insert(self, pos, item):
        self.list[pos] = item

    def delelte(self, pos):
        return self.list.append(pos)

    def isEmpty(self):
        if len(self.list) == 0:
            return True

    def getEntry(self, pos):
        return self.list[pos]

    def size(self):
        return len(self.list)

    def clear(self):
        self.list.clear(self)

    def find(self, item):
        return self.list.index(item)

    def replace(self, pos, item):
        self.list.pop(pos)
        self.list.insert(pos,item)


    def sort(self, bool):
        if bool == True:
            self.list.sort(reverse=True)
        elif bool == False:
            self.list.sort(reverse=False)

    def merge(self, listA):
        self.list.extend(listA)

    def append(self, item):
        self.list.append(item)

    def __str__(self):
        return "Arratlist" + str(self.list)


def lineEditor():
    list = Arraylist()
    list.list = ["0" for i in range(10)]
    command = 'a'

    while command != 'q':
        command = input("실행할 명령을 입력하세요. i.라인삽입, d 라인삭제, r 라인변경, p 현재 내용 출력, l 파일 입력, s 파일 출력")

        if command == 'i':
            index = int(input("행번호를 입력하세요"))
            string = input("문자열을 입력하세요")
            list.insert(index, string)
        elif command == 'd':
            index = int(input("삭제할 행 번호"))
        elif command == 'r':
            index = int(input("대체할 행 번호"))
            string = input("대신 들어갈 문자열")
            list.replace(index, string)

        elif command == 'p':

            for i, string in enumerate(list.list):# list 객체 안의 list 를 돌려야해 진은아.
                print(i, string)


        elif command == 'l':
            infile = open("/Users/bagjin-eun/Desktop/무제.txt", "r")  # 읽기 모드를 사용해서 파일을 열었음
            lines = infile.read()  # 파일의 라인 전체를 읽어온다.
            lines = lines.split("\n")#" \n"을 기준으로 한줄 씩 잘라서 스트링 타입 리스트를 생성햇다.
            for line in lines:
                list.append(line.strip("\n"))  # 문장 끝에 존재하는 \n기호 삭제 후의 문자열 arraylist 객체에 삽입함.
            infile.close()


        elif command == 's':
            outfile = open("/Users/bagjin-eun/Desktop/무제.txt", "w")
            for i in range(list.size()):
                outfile.write(list.getEntry(i) + "\n")  # list 안에 들어있는 문자열을 전부 outflie에 삽입.
            outfile.close()

        elif command == 'q':
            print("파일을 종료합니다.")
            second_command = input("작성중인 문서를 저장하시겠습니까? Y/N")

            if second_command in 'Yy':

                outfile = open("/Users/bagjin-eun/Desktop/무제.txt", "w")

                for i in range(list.size()):
                    outfile.write(list.getEntry(i)+"\n")
                outfile.close()
                break;
            else:
                break;
lineEditor()