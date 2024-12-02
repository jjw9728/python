# month = 12
# day = 2
# print("오늘은 %d월 %d일 입니다." % (month, day))

# print("Hello".upper())
# print("Hello".lower())

# friends = "고찬국 김다운 김민창"
# a = friends.split()
# print(a)

# sentence = "{0}월 {1}일".format(12, 2)
# print(sentence)

# b = "      111 222         "
# print(b.strip())
# print(b.split())
# print(b.lstrip())
# print(b.rstrip())

# a = "Hello, Python"
# print(a.replace("Python", "C#"))

# a = input("세자리 자연수를 입력하세요.")
# b = input("세자리 자연수를 입력하세요.")

# first = b[2:]
# second = b[1:2]
# third = b[0:1]

# answer_1 = int(a) * int(first)
# answer_2 = int(a) * int(second)
# answer_3 = int(a) * int(third)
# answer_4 = int(a) * int(b)

# print(answer_1, answer_2, answer_3, answer_4, sep="\n")

# print(1==2)
# print(1!=2)

# cart = ["계란", "마늘", "콩나물", "커피"]
# print("두부" in cart)
# print("커피" in cart)

# if 1<3:
#     print("True")

# a = int(input())

# if (a%2)==1:
#     print("odd")
# if (a%2)==0:
#     print("even")

# a = int(input())

# if a==100:
#     print("만점")
# else:
#     if a>=90:
#         print("A")
#     elif a>=80:
#         print("B")
#     elif a>=70:
#         print("C")
#     elif a>=60:
#         print("D")
#     else:
#         print("E")
# 
ages = int(input("나이를 숫자로 입력해주세요: "))
if ages<0:
     ages = int(input("입력한 나이가 0보다 작습니다. 나이를 다시 숫자로 입력해주세요: "))
cost = input("결제 방법을 입력해주세요. ('카드' 또는 '현금' 만 입력): ") 
if (cost!='카드') and (cost!='현금'):
     cost = input("입력한 결제방법이 존재하지않습니다. 다시 입력해주세요: ")
          
if ages<8:
    money = '무료'
    
elif ages<14:
    money = 450
elif ages<20:
    if cost == '카드':
         money = 720
    else:
         money = 1000
elif ages<75:
    if cost == '카드':
         money = 1200
    else:
         money = '1300'
else:
     money = '무료'
     
print(f"{ages}세의 {cost} 요금은 {money} 입니다.")        
    