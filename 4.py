# class Health:
#     def __init__(self, name):
#         self.__name = name
#         self.__hp = 100

#     def get_name(self):
#         return self.__name
    
#     def set_hp(self, hp):
#         if hp < 0:
#             hp = 0
#         elif hp > 100:
#             hp = 100
#         self.__hp = hp

#     def get_hp(self):
#         return "hp: " + str(self.__hp)
    
#     def exercise(self, hours):
#         self.set_hp(self.__hp + hours)
#         print(f"{hours}시간 운동하다.")

#     def drink(self, cups):
#         self.set_hp(self.__hp - cups)
#         print(f"술을 {cups}잔 마시다.")

# p1 = Health("나몸짱")
# p1.set_hp(100)
# p1.exercise(5)
# p1.drink(2)
# print(f"{p1.get_name()} - {p1.get_hp()}")

# p2 = Health("나약해")
# p2.set_hp(10)
# p2.exercise(1)
# p2.drink(12)
# print(f"{p2.get_name()} - {p2.get_hp()}")

# class cal:
#     def __init__(self, a, b):
#         self.__a = a
#         self.__b = b               

#     def add(self):
#         return self.__a + self.__b

#     def sub(self):
#         return self.__a - self.__b

#     def mul(self):
#         return self.__a * self.__b

#     def div(self):     
#         try: 
#             return self.__a / self.__b
#         except ZeroDivisionError:
#             return "error"
       

# result = cal(4, 3)
# print(result.add())
# print(result.sub())
# print(result.mul())
# print(result.div())

class Employee:
    serial_num = 1000

    def __init__(self, name):
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name

    def __str__(self):
        return f"사번 : {self.id}, 이름 : {self.name}"
    
e1 = Employee("최사원")
print(e1)
e2 = Employee("안사원")
print(e2)
e3 = Employee("한사원")
print(e3)

employee = [
    Employee("구름"),
    Employee("별"),
    Employee("행성"),
    Employee("달")    
]

for i in employee:
    print(i) 
