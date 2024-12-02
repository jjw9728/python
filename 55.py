# #1
# n = int(input("정수를 입력하세요: "))

# num = list(range(n+1))
# num.pop(0)
# print(num)

#2
# vending_machine = ["게토레이", "레쓰비", "생수", "이프로"]
# want = input("마시고 싶은 음료? ")

# if want in vending_machine:
#     print(f"{want} 드릴게요")
# else:
#     print(f"{want}는 지금 없네요")

#3
vending_machine = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "이프로", "이프로"]
print("남은 음료수 :", vending_machine)

choice = input("사용자 종류를 입력하세요\n1.소비자\n2.주인\n")

if choice == "1":
        want = input("마시고 싶은 음료? ")
        if want in vending_machine:
            print(f"{want} 드릴게요")
            vending_machine.remove(want)
            print("남은 음료수 :", vending_machine)
        else:
            print(f"{want}는 지금 없네요")
elif choice == "2":
        manage = input("할 일 선택\n1.추가\n2.삭제\n")
        if manage == "1":
            add = input("추가할 음료수?: ")
            vending_machine.append(add)
            vending_machine.sort()
            print("추가 완료")
            print("남은 음료수 :", vending_machine)
        elif manage == "2":
            remove = input("삭제할 음료수?: ")
            if remove in vending_machine: 
                vending_machine.remove(remove)
                vending_machine.sort()
                print("삭제 완료")
                print("남은 음료수 :", vending_machine)
            else:
                print("이미 없음")
        else:
            print("해당사항 없음") 
else:
     print("잘못된 값")


    