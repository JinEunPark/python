def sortGapInsertion(list, first, last, gap):

    for i in range(first+gap, last+1 , gap):
        key = list[i]#첫번째 키값은 첫번째요소 + gap 위치에 있는 요소
        j = i - gap# 키값보다 gap 만큼 뒤에 있는 요소로 설정
        while j >= first and list[j] > key:#first보다 크고 키값보다 클때까지
            list[j + gap] = list[j]#위 조건을 만족하면 둘이 처음에는 키값자리에 복사되고 이후에는 교환이 일어난 자리에 gap차이만큼 작은 위치에서 교환
            j -= gap# gap 만큼 작인 인덱스를 선택해서 설정
        list[j + gap] = key#위에 while문에서 조건을 만족하지 않아서 끝났기 때문에 다시 gap만큼 더해준 자리에


def shell_sort(list):
    n = len(list)
    gap = n // 2  # 리스트의 길이의 절반을 gap으로 설정

    while gap > 0:
        
        if (gap % 2) == 0: gap += 1  # 만일 간격이 짝수라면 1을 더해서 홀수로 만든다.
        for i in range(gap):
            sortGapInsertion(list, i, n - 1, gap)# 1.list 2.first비교를 시작하는 첫번째 요소 3.리스트의 마지막인덱스 전달
        print(' gap=', gap, list)
        gap = gap // 2#gap을 정수나눗셈을 실행해서 비교 간격을 반으로 줄인다.
