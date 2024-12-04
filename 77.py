# t1 = (10, 20, 30)
# print(type(t1))
# print(t1)
# print(t1[0])

# del t1
# t2 = (10)
# t2 = (10,)
# t2 = 10, 20
# print(type(t2))

# set1 = {1, 2, 3, 3}
# set2 = set([1, 2, 3, 3])
# print(set1)
# print(set2)

# set2.add(4)
# print(set2)

# while len(set2) > 0:
#     a = set2.pop()
#     print(a)

# l1 = [1,2,3,4]
# while len(l1) > 0:
#     a = l1.pop()
#     print(a)

# set3 = set("apple")
# print(set3)

# name = ["1", "2", "3", "2"]
# name_del = []

# for i in name:
#     if i not in name_del:
#         name_del.append(i)

# print(name_del)

# a = {}
# print(type(a))
# b = {1}
# print(type(b))
# c = dict()
# print(type(c))
# c = {1: 'a', 'b':'b'}
# print(c)
# c[2] = 'c'
# c['c'] = 2
# print(c)
# del c[2]
# del c['b']
# print(c)
# # print(c[2])
# print(c.get(2))
# print(c.keys())
# print(c.values())

# for i in c.keys():
#     print(i, c.get(i))

# for i in c.values():
#     # print(i, c.get(i))

# dic = {
#     "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
#     "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
#     "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
# }


# print("★ 컴퓨터 사전 ★")
# word = input("검색할 단어를 입력하세요: ")
# if word in dic:
#     print(f'{word}: {dic[word]}')
# else:
#     print("정의된 단어가 없습니다.")

# a, b = map(int, input().split())

# a_str = set()
# for i in range(a):
#     a_str.add(input())

# count = 0
# for i in range(b):
#     str = input()
#     if str in a_str:
#         count += 1

# print(count)

# students = {"Alice": 85, "Bob": 90, "Charlie": 95}
# print(students)
# students["David"] = 80
# print(students)
# students["Alice"] = 88
# print(students)
# del(students["Bob"])
# print(students)
# for student in students.keys():
#     print(student, students[student])

d = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(d)
print(d[0][0])
print(d[1][1])
d.append([70, 80])
print(d)

d[0][0] = 90
d[0][1] = 100
print(d)

# d[1].pop(0)
# d[1].pop(-1)
# print(d)
print(len(d))
print(len(d[0]))

for i in range(0, len(d)):
    for j in range(0, len(d[i])):
        print(d[i][j], end = ' ')
    print()

for x,y in d:
    print(x, y)
