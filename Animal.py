"""
Animal 클래스를 만들어서
    이름과 나이를 속성으로 갖고
    speak 메서드를 추가해 주세요
    
Dog 클래스, Cat 클래스를 각각 Animal 상속을 받아 만듭니다
    speak 메서드를 각각의 클래스에 맞게 
    상상력을 발휘해 구현해 보세요
---
    룰 : 10분 동안 명세만 보고 구현 고민하기.
    막힌다면 5분 동안 복습, 타이핑은 no.
    다시 고민 반복.
"""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print(f"{self.name} sound here!")
    
class Dog(Animal):
    def __init__(self, name, age, omnivorous="whatever"):
        super().__init__(name, age)
        # 개는 잡식성을 가집니다
        self.omnivourous = omnivorous
        
    def speak(self):
        super().speak()
        print(f"Hi! I'm {self.name}, {self.age}years old, and I wanna eat {self.omnivourous}.")
        
        
class Cat(Animal):
    def __init__(self, name, age, carnivorous="prefer meat"):
        super().__init__(name, age)
        # 고양이는 육식성을 가집니다
        self.carnivorous = carnivorous

    def speak(self):
        super().speak()
        print(f"Hi! I'm {self.name}, {self.age}years old, and I wanna eat {self.carnivorous}.")

# Dummy data for testing
my_dog = Dog("Buddy", 3, "meat and vegetables")
my_dog.speak()  # prints "Buddy sound here! Hi! I'm a Buddy, 3years old, and I wanna eat meat and vegetables."

my_cat = Cat("Master", 5, "mice and fish")
my_cat.speak()  # prints "Master sound here! Hi! I'm a Master, 5years old, and I wanna eat mice and fish."
