# class Supermarket:
#     count = 0
    
#     def __init__(self, location, name, product, customer):
#         self.__location = location
#         self.__name = name
#         self.__product = product
#         self.__customer = customer
#         Supermarket.count += 1

#     def print_location(self):
#         print(f"위치 : {self.__location}")

#     def change_category(self, change):
#         self.__product = change

#     def show_list(self):
#         print(f"파는물건 : {self.__product}")
    
#     def enter_customer(self):
#         self.__customer += 1

#     def show_info(self):
#         print(f"가게이름 : {self.__name}, 위치 : {self.__location}, 파는물건 : {self.__product}, 손님 수 : {self.__customer}")

#     def show_supermarket_count(self):
#         print(f"인스턴스 수 : {Supermarket.count}")

# x = Supermarket("응암", "미소분식", "오징어덮밥, 동태찌개, 순두부찌개, 뚝배기우동", 4)
# x.print_location()
# x.change_category("오징어덮밥, 동태찌개, 순두부찌개, 뚝배기우동, 제육덮밥")
# x.show_list()
# x.enter_customer()
# x.show_info()
# x.show_supermarket_count()

# class Country:
#     def __init__(self):
#         self.name = "나라이름"
#         self.population = "인구"
#         self.capital = "수도"
    
#     def show(self):
#         print("국가 클래스의 메소드입니다.")

# class Korea(Country):
#     def __init__(self, name):
#         self.name = name
    
#     def show_name(self):
#         print("국가 이름은 :", self.name)

# country = Korea("대한민국")
# country.show()
# print(country.name)
# country.show_name()

# class Country:
#     def __init__(self):
#         self.name = "나라이름"
#         self.population = "인구"
#         self.capital = "수도"
    
#     def show_detail(self):
#         print("국가 클래스의 메소드입니다.")

# class Korea(Country):
#     def __init__(self, name, population, capital):
#         self.name = name
#         self.population = population
#         self.capital = capital
    
#     def show_detail(self):
#         print(f"국가 이름은 {self.name}, 인구는 {self.population}명, 수도는 {self.capital} 입니다.")

# country = Korea("대한민국","5천만","서울")
# country.show_detail()

# class Calculator():
#     def __init__(self):
#         self.value = 100

#     def sub(self, value):
#         self.value -= value
#         return self.value

# class over_Cal(Calculator):
#     def sub(self, value):
#         self.value -= value
#         if self.value < 0:
#             self.value = 0
      
#         return self.value
        
# cal = over_Cal()
# print(cal.sub(20))
# print(cal.sub(90))
# print(cal.value)

class Calculator():
    def __init__(self):
        self.value = 100

    def sub(self, val):
        self.value -= val
    
    def sub(self):
        self.value -= 10

    def sub(self, val1, val2):
        self.value = val1 - val2

a = Calculator()
print(a.sub())
print(a.sub(50))
print(a.sub(100, 30))
