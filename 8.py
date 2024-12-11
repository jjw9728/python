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

f = open("./test.txt","w")
f.write("Hello World!!\n")
f.close()

# f2 = open("./test.txt","r")
# print(f2.read())
# f2.close()

f3 = open("./test.txt","a")
f3.write("Hello World!!_data_add\n")
f3.close()

f2 = open("./test.txt","r")
print(f2.readline(), end = "")
print(f2.readline(), end = "")
f2.close()
