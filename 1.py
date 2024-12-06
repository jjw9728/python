# def pr_str(txt, count=1):
#     for i in range(count):
#         print(txt)

# pr_str("Hello", 3)
# print()
# pr_str("Hello")
# print()
# # pr_str()    

# def calc_avg(*numbers):
#     # print(type(numbers))
#     print(numbers)
#     return sum(numbers)/len(numbers)

# print(calc_avg(1,2))
# print(calc_avg(1,2,3,4,5))

# def a():
#     return 1,2

# print(a())

# def introduce(**me):
#     print(type(me))
#     for key, value in me.items():
#         print(f"{key}: {value}")
#     for i in me:
#         print(f"{i}")
        
# introduce(name = "Jaewon", age = "28", city = "Gwang-Yang")

# list = [2,3,4,1,4]
# list.sort()
# print("list", list)
# list2 = [2,3,4,5,6]
# print("sorted(list2)", sorted(list2))
# print("list2", list2)

# print(eval("1+2*2"))
 
# print("%.0f"%4.5444)
# print("%.1f"%4.5444)
# print("%.2f"%4.5444)
# print("%.3f"%4.5444)

# def hello():
#     global cnt
#     cnt += 1
#     if cnt<4:
#         print("Hello")
#         hello()

# cnt = 0
# hello()

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)

# print(fact(10))

# def fib(n):
#     arr = [0]*(n+1)
#     arr[1] = 1
#     for i in range(2,n+1):
#         arr[i] = arr[i-1] + arr[i-2]
#     return arr[n]

memory = {1: 1, 2: 1}

def fib(n):
    if n in memory:
        number = memory[n]
    else:
        number = fib(n-1) + fib(n-2)
        memory[n] = number
    return number
    
    
print(fib(100))
# a = int(input("수입력?: "))
# print("피보나치 수: ", end = " ")
# for i in range(a):
#     print(fib(i+1), end=" ")