#1
# n = int(input("정수를 입력하세요: "))
# num = []

# for i in range(n+1):
#     num.append(n)
#     n -= 1
#     if(n<1):
#          break
# num.reverse()
# num = list(range(n+1))
# num.pop(0)
# print(num)

# i=0
# while i<5:
#     i+=1
#     print(i)
# print("끝")

# num = 0
# while num < 10:
#     num += 1
#     if (num % 2) != 1:
#         continue
#     print(num)

#1
# n = int(input("정수를 입력하세요: "))
# sum = 0

# for i in range(n+1):
#     sum += i

# print(sum)

# n = int(input("정수를 입력하세요: "))
# sum_1 = 0
# sum_2 = 0

# for i in range(n+1):
#    sum_1 += i
#    if i % 2 == 1:
#           sum_2 += i

# print(sum_1)
# print(sum_2)

# n = int(input("정수를 입력하세요: "))

# for i in range(n, 0, -1):
#     print(i,end=" ")
# print("발사!") 

# n = int(input("몇 단?: "))

# for i in range(1, 10):
#     print(f"{n} * {i} = {n*i} ")

# a = [1, 2, 3, 4, 5]
# a3 = []
# a4 = []

# a3 = [i * 3 for i in a]
# print("a3 =", a3)

# a4 = [i * 3 for i in a if i % 2 == 0]
# print("a4 =", a4)

# for y in range(3):
#     for x in range(2):
#         print(f"y:{y}, x:{x}")
#     print("")

# for i in range(2, 10):
#     print(f"{i}단")
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j} ")
#     print("\n")

print('*** 자리배치도 ***')
customer = int(input('고객수 입력: '))
row = int(input('좌석행 수 입력: '))

if customer % row == 0:
    column = customer // row
else:
    column = (customer // row) + 1
# print(row)

for i in range(0, row):
  for j in range(1, column + 1):
    seat = i * column + j
    if seat > customer:
      break
    print(seat, end=" ")
  print()