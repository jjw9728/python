# d = [
#     [3, 1],
#     [3, 2],
#     [3, 3],
#     [3, 4],
#     [3, 5],
#     [3, 6],
#     [3, 7],
#     [3, 8],
#     [3, 9],
# ]

# for i in range(1, 10):
#     print(f"{d[i-1][0]} * {i} = {d[i-1][0]*i}")

# for x, y in d:
#     print(f"{x} * {y} = {x*y}")

# def f(x):
#     value = x**2 + 2*x + 1
#     return value

# print(f(3))   

# def say_hello():
#     print("Hello!")
#     print("Hello!")
#     print("Hello!")

# say_hello()

# x = 10

# def fnc():
#     x= 20
#     print(x)

# fnc()
# print(x)

# def fnc2():
#     print(x)

# fnc2()

# def fnc3(x):
#     print(x)

# fnc3(3)

# def fnc(x, y):
#     if x == y:
#         val = x * y
#     else:
#         val = x + y

#     return val

# a, b = map(int, input("숫자 두개 입력: ").split())
# a = int(input("숫자 1 입력: "))
# b = int(input("숫자 2 입력: "))

# print(fnc(a,b))

# def fnc(x, y):
#     if (x*y) >= 20000:
#         val = x * y
#     else:
#         val = x * y + 2500

#     return val

# a = int(input("상품 금액 입력: "))
# b = int(input("상품 수량 입력: "))
# print(f"총 가격: {fnc(a,b)}")

# def fnc(a):
#     a2 = [i * 3 for i in a]
#     return a2

# v = [1,2,3,4,5]
# v2 = fnc(v)
# print(v2)

# def sum_mul(a, b):
#     sum = a + b
#     mul = a * b
    
#     return sum, mul 

# s, m = sum_mul(2, 3)
# print(s, m)

def check_machine(x):
     print("남은 음료수 :", x)

def is_drink(x, y):
     return y in x

def add_drink(x, y):
     x.append(y)
     x.sort()

def remove_drink(x, y):
     x.remove(y)

vending_machine = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "이프로", "이프로"]
check_machine(vending_machine)

choice = input("사용자 종류를 입력하세요\n1.소비자\n2.주인\n")

if choice == "1" or choice == "소비자":
        want = input("마시고 싶은 음료? ")
        if is_drink(vending_machine, want):
            print(f"{want} 드릴게요")
            remove_drink(vending_machine, want)
            check_machine(vending_machine)
        else:
            print(f"{want}는 지금 없네요")
elif choice == "2" or choice == "주인":
        manage = input("할 일 선택\n1.추가\n2.삭제\n")
        if manage == "1" or manage == "추가":
            add = input("추가할 음료수?: ")
            add_drink(vending_machine, add)
            print("추가 완료")
            check_machine(vending_machine)
        elif manage == "2" or manage == "삭제":
            remove = input("삭제할 음료수?: ")
            if is_drink(vending_machine, remove): 
                remove_drink(vending_machine, remove)
                print("삭제 완료")
                check_machine(vending_machine)
            else:
                print("이미 없음")
        else:
            print("해당사항 없음") 

else:
     print("잘못된 값")
