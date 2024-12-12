# from modules.mylib import food

# print(food.name)
# food.cook()
# food.eat()

# from modules.mylib.food import name, cook, eat, mukbang

# print(name)
# cook()
# eat()

# import jw.calc_module
# print(jw.calc_module.add(1, 2))

# import jw.calc_module as jw
# print(jw.add(1, 2))

# f = open("./test.txt","w")
# f.write("Hello World!!\n")
# f.close()

# # f2 = open("./test.txt","r")
# # print(f2.read())
# # f2.close()

# f3 = open("./test.txt","a")
# f3.write("Hello World!!_data_add\n")
# f3.close()

# f2 = open("./test.txt","r")
# print(f2.readline(), end = "")
# print(f2.readline(), end = "")
# f2.close()

# f = open("./test2.txt","w")
# f.write("Hello World!!\n안녕\n반가워\n난, 코딩온이야")
# f.close()

# f4 = open("./test.txt")
# print(f4.readlines())
# f4.close()

# f4 = open("./test2.txt","r")
# print(f4.read())

# f4.seek(0)
# print(f4.tell())

# context = f4.readlines()
# print(context)

# f4.close()

# f5 = open("test.txt", "r+")
# str = f5.read()
# print(f5.tell())
# f5.seek(str.find('5'))
# print(f5.write("8"))
# f5.close()

# with open('./with_as.txt', 'w') as f1:
#     f1.write("Hello~\n")
#     f1.write("안녕\n")
#     num = '1KB는 %dB이다' % 1024
#     f1.write(num)

# with open('./with_as.txt', 'r') as f2:
#     data = f2.read()
#     print(data)

# import random
# import time

# with open("./word.txt", "w") as f:
#     word = ["sky", "earth", "moon", "flower", "tree", 
#             "strawberry", "grape", "garlic", "onion", "potato"]
    
#     for i in word:
#         f.writ(i + " ")

# with open("./word.txt", "r") as f:
#     word = f.read().split()

# n = 1

# input("[타자 게임] 준비되면 엔터!")
# start = time.time()

# while n < 11:
#     try:
#         print("문제", n)
#         question = random.choice(word)
#         print(question)
#         user = input()

#         if question == user:
#             print("통과!!")
#             n += 1
#         else:
#             print("오타!! 다시 도전")
        
#    end = time.time()
#    print(f"게임 소요시간 : {end-start:.2f}초")

#    except:
#     print("")

# import random
# import time
# with open("word.txt", 'w') as f:
#     word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
#             'grape', 'garlic', 'onion', 'potato']
#     for i in word:
#         f.write(i + ' ')
# with open("word.txt", 'r') as f:
#     word = f.read().split()
#     # word = random.choice(data)
#     print(word)
# n = 1
# input("[타자 게임] 준비되면 엔터! ")
# start = time.time()
# while n < 11:
#     print("문제 ", n)
#     question = random.choice(word)
#     print(question)
#     user = input()
#     if question == user:
#         print("통과!! ")
#         n += 1
#     else:
#         print("오타! 다시 도전! ")
# end = time.time()
# et = end - start
# print(f"타자 시간: {et: .2f}초")
# import os

# if os.path.exists("/io.txt"):
#     with open("./io.txt", "a") as f:
#         while True:
#             text = input("저장할 내용을 입력해 주세요(종료-z) : ")
#             if text == "z" or text =="Z":
#                 break
#             f.write(text)
#             f.write("\n")   

# else:
#     with open("./io.txt", "w") as f:
#         while True:
#             text = input("저장할 내용을 입력해 주세요(종료-z) : ")
#             if text == "z" or text =="Z":
#                 break
#             f.write(text)
#             f.write("\n")   


# import random
# import time
# with open("word.txt", 'w') as f:
#     word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
#             'grape', 'garlic', 'onion', 'potato']
#     for i in word:
#         f.write(i + ' ')

# with open("word.txt", 'r') as f:
#     word = f.read().split()
#     # word = random.choice(data)
#     print(word)
# import random
# import time
# with open(".input.txt", 'w') as f:
#     while True:
#         word = input("저장할 내용 입력(종료-z)")
#         if word == 'z' or word == 'Z':
#             break
#         f.write(word + ' ')

# with open(".input.txt", 'r') as f:
#     word = f.read().split()

# n = 1

# input("[타자 게임] 준비되면 엔터! ")
# start = time.time()
# while n < 11:
#     print("문제 ", n)
#     question = random.choice(word)
#     print(question)
#     user = input()
#     if question == user:
#         print("통과!! ")
#         n += 1
#     else:
#         print("오타! 다시 도전! ")
# end = time.time()
# et = end - start
# print(f"타자 시간: {et: .2f}초")


        

# with open("./customer.txt", 'r') as f:
#     answer = f.read().split()

# name_00 = input("이름 입력 : ")

# with open("./customer.txt", 'r') as f:
#     str = f.read()
    
#     if name_00 in str:
#         password = int(input("비밀번호 입력 : "))  
        
#         f.seek(str.find(name_00))
#         a=f.readline()
#         print(a)
#     #     a = f.readline().split()
#     #     secret = a[1]
        
#     #     if int(secret)==int(password):
#     #         print("성공")
#     #     else:
#     #         print("실패")
#     # else:
#     #     print("사용자 정보 없음")  

import os
dictUser = {}

# with open("./customer.txt", 'w') as f:
#     for i in range(3):
#         name = input("이름 입력 : ")
#         password = input("비밀번호 입력 : ")
#         f.write(name + ' ' + password + '\n')

with open("customer.txt", 'r') as f:
    for line in f:
        n, p = line.split()
        dictUser[n] = p

print(dictUser)

# for i in range(100) :
name = str(input("이름을 입력하세요: "))
pw = input("비밀번호를 입력하세요: ")

if pw == dictUser.get(name):
    print("로그인 성공!")
    phone = input("전화번호를 입력하세요: ")
    
    
    if os.path.exists("member1.txt"):
        with open("member1.txt", 'r') as f1:
            lines = f1.readlines()
            filtered_lines = [line for line in lines if name not in line]
            # print(filtered_lines)
          
        with open("member1.txt", 'w') as f1:
            f1.writelines(filtered_lines)
            f1.write(name + ' ' + phone + '\n')  
            f1.close()

    else:
        with open("member1.txt", 'w') as f1:
            f1.write(name + ' ' + phone + '\n')  
            f1.close()

else:
    print("로그인 실패!") 
  

        
        

