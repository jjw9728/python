# add = lambda x, y : x + y
# print(type(add))
# print(add(1,2))

# def add2(x, y):
#     return x+y

# print(add2(1,2))

# print("콜백 함수")
# def call_3(func):
#     for i in range(3):
#         func()

# def hello():
#     print("hello!")

# print(call_3(hello))
# print()
# print(call_3(lambda : print("hello!")))

# def download(startedCallback, endedCallback):
#     startedCallback()
#     endedCallback()

# download(lambda:print("시작"),lambda:print("완료"))

# list(map(int, ['1','2','3']))
# result = map(lambda x : 3 * x, [1,2,3,4])
# print(list(result))

# li = [-5, 1, 2, -11, 76]

# print(list(filter(lambda x:x>=3, map(lambda x:2*x, li))))

# value = list(filter(lambda x:x>0, li))
# print(value)

# 람다식 예제 

# def solution(arr):
#     answer = []
#     for i in answer:
#         if answer[i]>=50:
#             if answer[i] % 2 == 0:
#                 answer[i] = answer[i]/2
#         else:
#             if answer[i] % 2 == 1:
#                 answer[i] = answer[i]*2
#     return answer

# print(solution([1, 2, 3, 100, 99, 98]))

def solution(my_string, letter):
    answer = []
    for i in range(len(my_string)):
            if letter not in my_string:
                  answer.append(letter)
       
               
        
    return str(answer)

print(solution("aksajasgb", "a"))