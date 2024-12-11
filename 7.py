# import calendar

# calendar.prcal(2024)
# calendar.prmonth(2024, 12)
# print(calendar.weekday(2024, 12, 8))
# print(calendar.prweek(2024, 12, 8))

# import calendar
# import datetime

# days = ["월", "화", "수", "목", "금", "토", "일"]

# weekday = datetime.date.today().weekday()
# print(weekday)
# print("오늘은" + days[weekday] + "요일")

# the_day = datetime.date(2024, 12, 25).weekday()
# print(the_day)
# print("크리스마스는 " + days[the_day] + "요일")

# import calendar
# import datetime

# def get_weekday(yyyy, mm, dd):
#     days = ["월", "화", "수", "목", "금", "토", "일"]
#     idx = datetime.date(yyyy, mm, dd).weekday()
#     print(f"{yyyy}년 {mm}월 {dd}일 {days[idx]}요일")

# get_weekday(1960, 12, 18)

# import time
# start = time.time()
# time.sleep(2)
# finish = time.time()
# print(finish-start)

# print(time.localtime())
# time_str = time.localtime()
# print(time_str.tm_year)

# print(time.ctime(start))
# print(time.ctime(finish))

# year = round(time.time()/(365*24*60*60))
# day = round(time.time()/(24*60*60))

# print(year)
# print(day)

# import time

# def check_time(n, m):
#     start = time.time()
#     for i in range(n):
#         print(i)
#         time.sleep(m)

#     end = time.time()
#     delay_time = end - start
#     print(f"수행시간 : {delay_time}초")

# # def a():
# #     for i in range(10):
# #         print(i)
# #         time.sleep(1)

# # def b():
# #     for i in range(10):
# #         print(i)
# #         time.sleep(0.5)

# check_time(5, 0.5)

import random
import time

word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
        'grape', 'garlic', 'onion', 'potato']

n = 1

input("[타자 게임] 준비되면 엔터! ")
start = time.time()

while n < 11:
    print("문제 ", n)
    question = random.choice(word)
    print(question)
    user = input()
    if question == user:
        print("통과!! ")
        n += 1
    else:
        print("오타! 다시 도전! ")

end = time.time()
et = end - start
print(f"타자 시간: {et: .2f}초")