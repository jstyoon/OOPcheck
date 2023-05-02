"""
circle 클래스를 만들고
    get_area 메서드를 갖게 해주세요.
    
Circle과 Rectangle 클래스를 만들때 circle를 상속받아주세요
    Circle은 radius(반지름) 속성을 가지게
    Rectangle(직사각형)은 length와 width(폭) 속성을 가지게
    get_area 메서드는 각각에 맞게 구현해주세요
---
    룰 : 10분 동안 명세만 보고 구현 고민하기.
    막힌다면 5분 동안 복습, 타이핑은 no.
    다시 고민 반복.
"""
class circle:
    def get_area(self):
        pass  # 추상적인 메서드입니다. 하위 클래스에 구현됩니다.

class Circle(circle):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        # 원의 면적 = πr2 = 원주율 * 반지름
        # 참고 Python: Calculate area of a circle 
        # https://www.w3resource.com/python-exercises/python-basic-exercise-4.php
        π = 3.14 # 가독성을 위해 변수 선언 (3.14 = float형)
        return π * self.radius ** 2  # πr2
    
class Rectangle(circle):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def get_area(self):
        # 길이 * 폭 = 사각형 면적
        return self.length * self.width


# Dummy data for testing
my_circle = Circle(5)
print(my_circle.get_area())  # 78.5

my_circle = Rectangle(10, 20)
print(my_circle.get_area())  # 200
