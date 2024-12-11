# import sys

# # print(sys.argv)

# args = sys.argv[1:]
# # print(args)

# if len(args) <= 2 or len(args) >= 4:
#     # val = "error"
#     # break
#     sys.exit(0) 
# if sys.argv[1] == "mul":
#     val = int(sys.argv[2]) * int(sys.argv[3])
# elif sys.argv[1] == "add":
#     val = int(sys.argv[2]) + int(sys.argv[3])

# print(val)

# import os

# os.chdir("C:\\Users\\MSI\\anaconda3\\python")    

# dir = os.popen("git status")

# print(dir.read())
# print(os.listdir())

import random
import time

word = ["sky", "earth", "moon", "flower", "tree", "apple",
        "grape", "garlic", "onion", "potato"]

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
print(f"타자 시간: {et}초")
