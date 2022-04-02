from lineEditor import Editor


class lineEditor2(Editor):
    def lineEditor2(self):
        super.__init__()

    def lineEditor(self):
        while command != 'q':
            command = input("실행할 명령을 입력하세요. i.라인삽입, d 라인삭제, r 라인변경, p 현재 내용 출력, l 파일 입력, s 파일 출력, f 문자열 찾기")

            if command == 'i':
                index = int(input("행번호를 입력하세요"))
                string = input("문자열을 입력하세요")
                list.insert(index, string)


            elif command == 'd':
                index = int(input("삭제할 행 번호"))
                listsub = [s for s in range(index,len(self.list))]
                self.list.pop(index)
                self.list.extend(listsub)


            elif command == 'r':
                index = int(input("대체할 행 번호"))
                string = input("대신 들어갈 문자열")
                list.replace(index, string)


            elif command == 'f':
                findline = input("찾을 문자열을 입력하세요")
                while i < len(self.list):
                    for e in range(len(self.list)):
                        if findline == self.list[e]:
                            print(self.list.index(findline),self.list[self.list.index(findline)])


            elif command == 'p':

                for i, string in enumerate(list.list):  # list 객체 안의 list 를 돌려야해 진은아.
                    print(i, string)


            elif command == 'l':
                filename = input("파일이름을 입력하세요")
                infile = open(filename, "r")  # 읽기 모드를 사용해서 파일을 열었음
                lines = infile.read()  # 파일의 라인 전체를 읽어온다.
                lines = lines.split("\n")  # " \n"을 기준으로 한줄 씩 잘라서 스트링 타입 리스트를 생성햇다.
                for line in lines:
                    list.append(line.strip("\n"))  # 문장 끝에 존재하는 \n기호 삭제 후의 문자열 arraylist 객체에 삽입함.
                infile.close()


            elif command == 's':
                filename = input("파일 이름을 입력하세요")
                outfile = open(filename, "w", encoding="UTF8")
                for i in range(list.size()):
                    outfile.write(list.getEntry(i) + "\n")  # list 안에 들어있는 문자열을 전부 outflie에 삽입.
                outfile.close()

            elif command == 'q':
                print("파일을 종료합니다.")
                second_command = input("작성중인 문서를 저장하시겠습니까? Y/N")

                if second_command in 'Yy':

                    outfile = open("/Users/bagjin-eun/Desktop/무제.txt", "w")

                    for i in range(list.size()):
                        outfile.write(list.getEntry(i) + "\n")
                    outfile.close()
                    break;
                else:
                    break;
