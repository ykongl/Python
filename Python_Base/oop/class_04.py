
# 练习
class Dog:
    def __init__(self,name,gender,age,height):
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height

    def jiao(self):
        print(self.name,"在叫")

    def run(self):
        print(self.name,"在跑")


d1 = Dog('爆米花', '男', 8, '0.63m')
#
print(d1.name,d1.age,d1.height,d1.gender)
d1.jiao()
d1.run()