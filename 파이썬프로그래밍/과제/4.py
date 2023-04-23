# 4
bankName = input("은행이름을 입력하세요")
way = input("입급 수단을 방법을 입력하세요")
money_check = input(" 입금하실 돈을 입력하세요")

if bankName == "파이" and (way == "card" or way == "bankbook") and (money_check == "money"):
    print("입급 가능")
else:
    print("입급불가능")
