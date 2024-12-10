# import calc_module

# print(calc_module.add(2,3))
# print(calc_module.sub(2,3))
# print(calc_module.mul(2,3))
# print(calc_module.div(2,3))

# from calc_module import add
# print(add(2,3))

# import calc_module as cm

# print(cm.add(2,3))
# print(cm.sub(2,3))
# print(cm.mul(2,3))
# print(cm.div(2,3))

# import math

# print(math.floor(3.141592))
# print(math.ceil(3.141592))
# print(math.sqrt(9))
# print(math.fabs(-3.141592))
# print(math.factorial(3))

# from math import floor, ceil

# print(floor(3.141592))
# print(ceil(3.141592))

# import random

# print(random.randint(1,5))
# print(random.uniform(1,5))
# print(random.random())
# print(random.randrange(1,5))
# print(random.randrange(1,5,2))

# import random

# num = random.randint(1, 100)
# min_val = 1
# max_val = 100

# global cnt
# cnt = 0

# while True:
#     try:
#         guess = int(input("숫자입력(%d ~ %d): " % (min_val, max_val)))
#         cnt += 1

#         if cnt > 10:
#             print("횟수 초과!!")
#             break

#         if guess < 0 or guess > 100 :
#             print("입력 범위를 초과했어요.")

#         elif num == guess:
#             print("정답이에요!!")
#             print(f"정답: {num}")
#             score = 110-(cnt*10)
#             print(f"점수({cnt}회): {score}")
             

#         elif num > guess:
#             print("랜덤수보다 작아요.")
#             min_val = guess

#         else:
#             print("랜덤수보다 커요.")
#             max_val = guess        
   
#     except ValueError:
#         print("숫자만 입력 가능합니다.")

# import random
# val = []
# num = random.randint(1, 45)
    
# for i in range(True):
#     a = len[val]
#     print(a)
#     if a > 5:
#         break    
#     if num not in val: 
#         val.append(num)       
#     else:
#         num = random.randint(1, 45)
        
# print(a)
# val.sort()
# print(val)

# import random

# lotto = []
# count = 0

# while True: 
#     if count > 5:
#         break 
#     num = random.randint(1, 45)
#     if num not in lotto: 
#         lotto.append(num)
#         count += 1

# lotto.sort()
# print(lotto)

# import datetime
# now = datetime.time.today()
# print(now)
# # now = datetime.datetime.today()
# # print(now)
# # print(now.year, now.month)
# # print(now.month)

# print(f"{now.hour}시 {now.minute}분 {now.second}초")

import datetime
print("지금까지 몇 일?")
first_day = datetime.date(1998, 9, 24)
print(first_day)

today = datetime.date.today()
print(today)

passed_time = today - first_day
print(passed_time.days)

print(f"태어난지 {passed_time.days}일 됬습니다.")