"""
자동차 클래스를 만들어주세요.
    모델, 색, 현재 속도를 속성으로 갖고
    속도를 올려주는 accelerate 메서드
    속도를 낮춰주는 brake 메서드
    현재 속도를 리턴하는 get_speed 메서드를 추가해 주세요
---
    룰 : 10분 동안 명세만 보고 구현 고민하기.
    막힌다면 5분 동안 복습, 타이핑은 no.
    다시 고민 반복.
"""
# 자동차 클래스
class Car:
    # 모델, 색, 현재 속도를 속성으로
    def __init__(self, model, color, current_speed=0):
        self.model = model
        self.color = color
        self.current_speed = current_speed
    
    # 속도를 올려주는 acclerate method
    def accelerate(self, increase_speed):
        # self.current_speed = self.current_speed + increase_speed
        self.current_speed += increase_speed
        
    # 속도를 낮춰주는 brake method    
    def brake(self, decrease_speed):
        # self.current_speed = self.current_speed - decrease_speed
        self.current_speed -= decrease_speed
        # 현재속도에서 감소속도를 뺀 값이 0보다 크다면
        if self.current_speed - decrease_speed >= 0: 
            # (현재속도 값)은 (현재속도에서 감소속도를 뺀 값)과 같다
            self.current_speed -= decrease_speed
        else:
            # 더 이상 감소할 수 없는 속도 0일 경우
            self.current_speed = 0 
            
    # 현재 속도를 리턴하는 get_speed method
    def get_speed(self):
        return self.current_speed
    
# Dummy data for testing (get_speed method)
my_car = Car("Kia", "blue")
print(my_car.get_speed())  # 0

my_car.accelerate(20)
print(my_car.get_speed())  # 20

my_car.brake(5)
print(my_car.get_speed())  # 15