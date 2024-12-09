# a = dict()
# a = set()

# class b:
#     pass

# bb1 = b()
# bb2 = b()
# bb3 = b()

# class Movie:
#     title1 = "BossBaby"
#     title2 = "BossFather"

# movie1 = Movie()
# movie2 = Movie()

# print(movie1.title1)
# print(movie2.title2)

# Movie.title1 = "test1"
# Movie.title2 = "test2"
# print(movie1.title1)
# print(movie2.title2)

# class Movie:
#     name = ''

#     def print_msg(msg):
#         print(msg)

#     def modify(self, movie):
#         self.name = movie
    
#     def print_name(self):
#         print(self.name)

# movie1 = Movie()
# movie2 = Movie()

# Movie.print_msg('프린트하기')
# movie1.modify("name1")
# movie2.modify("name2")

# print(movie1.name)
# movie1.print_name()
# print(movie2.name)
# movie2.print_name()
# print(movie2.name)

# class Movie:
#     def __init__(self):
#         print("Hello, I'm Movie Class")

# moive = Movie()

# class Movie():
#     count = 0
    
#     # def __init__(self, title = "범죄도시3", audience = 300):
#     def __init__(self, title, audience):
#         self.title = title
#         self.audience = audience

# movie1 = Movie("범죄도시1", 100)
# movie2 = Movie("범죄도시2", 200)

# print(movie1.title, movie1.audience)
# print(movie2.title, movie2.audience)

# # movie3 = Movie(movie1)
# # print(movie3.title, movie3.audience)

# class Movie:
#     count = 0
    
#     def __init__(self, title, audience):
#         self.title = title
#         self.audience = audience
#         Movie.count += 1

# movie1 = Movie("범죄도시1", 100)
# print(Movie.count)
# movie2 = Movie("범죄도시2", 200)
# print(Movie.count)

# print(movie1.count)
# print(movie2.count)
# print(Movie.count)

# class Movie:
#     count = 0
    
#     def __init__(self, title, audience):
#         self.__title = title
#         self._audience = audience
#         Movie.count += 1
    
#     def get_title(self):
#         return self.__title
    
#     def set_title(self, title):
#         self.__title = title

#     def get_audience(self):
#         return self._audience

#     def set_audience(self, audience):
#         self._audience = audience

# movie1 = Movie("범죄도시", 100)
# print(movie1.get_title())
# movie1.__title = "오징어 게임"
# print(movie1.__title )
# movie1.set_title("타이타닉")
# print(movie1.get_title())

# class MyAdd:
#     __a = 1
#     __b = 2

#     def sum(self):
#         return self.__a + self.__b

#     def a_change(self, n):
#         self.__a = n

#     #######메소드 구현
    

# a = MyAdd()
# print(a.sum()) # 3
# # a 값 3으로 변경 
# a.a_change(3)
# print(a.sum()) # 5

class Health:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100

    def get_name(self):
        return self.__name
    
    def set_hp(self, hp):
        if hp < 0:
            hp = 0
        elif hp > 100:
            hp = 100
        self.__hp = hp

    def get_hp(self):
        return "hp: " + str(self.__hp)
    
    def exercise(self, hours):
        self.set_hp(self.__hp + hours)
        print(f"{hours}시간 운동하다.")

    def drink(self, cups):
        self.set_hp(self.__hp - cups)
        print(f"술을 {cups}잔 마시다.")

p1 = Health("나몸짱")
p1.set_hp(100)
p1.exercise(5)
p1.drink(2)
print(f"{p1.get_name()} - {p1.get_hp()}")

p2 = Health("나약해")
p2.set_hp(10)
p2.exercise(1)
p2.drink(12)
print(f"{p2.get_name()} - {p2.get_hp()}")

